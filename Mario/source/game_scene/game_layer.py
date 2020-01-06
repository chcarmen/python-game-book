from cocos.layer import ScrollableLayer
from cocos.director import director
from cocos.batch import BatchNode
from cocos.collision_model import CollisionManagerGrid
from cocos.actions import Delay, CallFunc, JumpBy

from common.stats import stats
from common.sound import Sound
from .mario import Mario
from .enemy import *
from .prop import *
from .cliff import Cliff
from .coin import Coin
from .flag import *
from .brick import PopupBrick, BrokenBrick


class GameLayer(ScrollableLayer):
    def __init__(self, *args):
        super().__init__()

        self.hud = args[0]
        self.obstacle_map = args[1]
        self.objects_map = args[2]
        self.tileset = args[3]

        self.create_mario()
        self.create_cliff()
        self.create_flag()

        self.enemies = BatchNode()
        self.add(self.enemies)
        self.enemy_objs = self.objects_map.match(label="enemy")
        self.exist_enemy_index = []

        width, height = director.get_window_size()
        self.cm = CollisionManagerGrid(0, width, 0, height, 20, 20)

        stats.reset_current_game()

        Sound.play("mario")

    def on_enter(self):
        super().on_enter()
        self.schedule(self.update)

    def on_exit(self):
        super().on_exit()
        self.unschedule(self.update)

    def create_mario(self):
        obj = self.objects_map.match(label="start point")[0]
        self.mario = Mario(obj.position, self.obstacle_map)
        self.add(self.mario, z=50)

    def create_cliff(self):
        self.cliffs = BatchNode()
        self.add(self.cliffs)

        for i, _ in enumerate(self.obstacle_map.cells):
            if not self.obstacle_map.cells[i][0].tile:
                self.cliffs.add(Cliff(self.obstacle_map.cells[i][0].center, self.obstacle_map))

    def create_flag(self):
        obj = self.objects_map.match(label="flag")[0]
        self.flag = Flag(obj.position)
        self.add(self.flag)

    def find_new_enemies(self):
        for obj in self.enemy_objs:
            if self.obstacle_map.is_visible(obj) and \
                    obj["index"] not in self.exist_enemy_index:
                yield obj

    def create_enemies(self):
        for obj in self.find_new_enemies():
            if obj.name == "Goomba":
                self.enemies.add(Goomba(obj.position, self.obstacle_map))
            elif obj.name == "Koopa":
                self.enemies.add(Koopa(obj.position, self.obstacle_map))

            self.exist_enemy_index.append(obj["index"])

    def update(self, dt):
        self.mario.update_(dt)
        self.create_enemies()
        self.handle_collide()
        self.update_timer(dt)

    def handle_collide(self):
        self.collide_with_obstacle()
        self.collide_with_objects()

    def collide_with_obstacle(self):
        if not self.mario.collide_cells:
            return

        cell = self.mario.collide_cells.popleft()
        label = cell.get("label")

        if label == "normal brick":
            if self.mario.state == Mario.SMALL:
                Sound.play("bump")
                self.popup_brick("normal", cell)
            else:
                Sound.play("brick_smash")
                self.smash_brick(cell)
        elif label == "unknown brick":
            self.popup_brick("unknown", cell)

            objs = self.objects_map.get_in_region(cell.left, cell.bottom, cell.right, cell.top)
            if objs:
                Sound.play("powerup_appears")
                # normally, only 1 object collide with cell
                self.collide_unknown_brick_with_obj(objs[0])
            else:
                Sound.play("coin")
                self.collide_unknown_brick_without_obj(cell)
        elif label == "flagpole":
            self.world_complete()

    def popup_brick(self, name, cell):
        self.obstacle_map.set_cell_opacity(cell.i, cell.j, 0)
        self.add(PopupBrick(name, cell.center))

        def recover_opacity():
            self.obstacle_map.set_cell_opacity(cell.i, cell.j, 255)
            self.obstacle_map.set_cell_color(cell.i, cell.j, (255, 255, 255))

        self.do(Delay(0.2) + CallFunc(recover_opacity))

        if name == "unknown":
            # change cell image to "bumped brick"
            cell.tile = self.tileset[1]
            self.obstacle_map.set_dirty()

    def smash_brick(self, cell):
        cell.tile = None
        self.obstacle_map.set_dirty()

        self.add(BrokenBrick(cell.midtop))

    def collide_unknown_brick_with_obj(self, obj):
        if obj.name == "Normal mushroom":
            self.add(NormalMushroom(obj.position, self.obstacle_map))
        elif obj.name == "Life mushroom":
            self.add(LifeMushroom(obj.position, self.obstacle_map))
        elif obj.name == "Reward":
            if self.mario.state == Mario.SMALL:
                self.add(NormalMushroom(obj.position, self.obstacle_map))
            elif self.mario.state == Mario.BIG:
                self.add(FireFlower(obj.position, self.obstacle_map))
            elif self.mario.state == Mario.FIRE:
                self.add(FireFlower(obj.position, self.obstacle_map))

    def collide_unknown_brick_without_obj(self, cell):
        self.add(Coin(cell.midtop))
        stats.coins += 1
        stats.score += 200

    def collide_with_objects(self):
        self.cm.xmin = self.obstacle_map.view_x
        self.cm.xmax = self.obstacle_map.view_x + self.obstacle_map.view_w

        self.cm.clear()

        for _, enemy in self.enemies.children:
            if enemy.active:
                self.cm.add(enemy)

        for _, cliff in self.cliffs.children:
            self.cm.add(cliff)

        for _, node in self.children:
            if isinstance(node, Mushroom) or isinstance(node, FireFlower):
                self.cm.add(node)

        for obj in self.cm.iter_colliding(self.mario):
            if isinstance(obj, Enemy):
                self.collide_enemy(obj)
            elif isinstance(obj, Cliff):
                self.collide_cliff()
                break
            else:
                self.collide_prop(obj)

    def collide_enemy(self, obj):
        if self.mario.collide_bottom_obj(obj):
            Sound.play("stomp")
            stats.score += 100
            obj.die()
            self.mario.do(JumpBy((0, 0), 16, 1, 0.3))
        else:
            if self.mario.state == Mario.SMALL:
                self.game_over("enemy")
            elif self.mario.state == Mario.BIG:
                self.mario.state = Mario.SMALL
            elif self.mario.state == Mario.FIRE:
                self.mario.state = Mario.BIG

            self.enemies.remove(obj)

    def collide_cliff(self):
        self.game_over("cliff")

    def collide_prop(self, obj):
        Sound.play("powerup")

        if isinstance(obj, NormalMushroom):
            stats.score += 1000
            if self.mario.state == Mario.SMALL:
                self.mario.state = Mario.BIG
        elif isinstance(obj, LifeMushroom):
            stats.life += 1
        elif isinstance(obj, FireFlower):
            stats.score += 1000
            if self.mario.state == Mario.BIG:
                self.mario.state = Mario.FIRE
            elif self.mario.state == Mario.FIRE:
                # do something else
                pass

        self.remove(obj)

    def enter_info_scene(self, world_complete=False):
        from info_scene.info_scene import InfoScene
        director.replace(InfoScene(self.hud, world_complete))

    def game_over(self, reason):
        stats.life -= 1

        Sound.stop("mario")
        if stats.life > 0:
            Sound.play("death")
        else:
            Sound.play("game_over")

        # change current layer z-order, make it the top
        self.parent.remove(self)
        self.parent.add(self, z=3)

        self.unschedule(self.update)

        if reason == "enemy" or reason == "timeout":
            self.mario.die()
            self.do(Delay(1) + CallFunc(self.enter_info_scene))
        elif reason == "cliff":
            self.enter_info_scene()
        else:
            pass

    def world_complete(self):
        stats.update_score_flagpole_height(self.mario.y)

        Sound.stop("mario")
        Sound.play("flagpole")

        self.unschedule(self.update)

        end_point_pos_x = 0
        castle_flag_pos = 0, 0

        for obj in self.objects_map.objects:
            if obj.name == "End point":
                end_point_pos_x = obj.x
            elif obj.name == "Castle flag":
                castle_flag_pos = obj.position

        self.flag.lower()
        self.mario.raise_flag(end_point_pos_x)

        self.do(Delay(5) + CallFunc(lambda: self.add(CastleFlag(castle_flag_pos))) +
                Delay(5) + CallFunc(self.enter_info_scene, True))

    def update_timer(self, dt):
        stats.update_timer(dt)

        if stats.time == 100:
            Sound.stop("mario")
            Sound.play("out_of_time")
            self.do(Delay(2) + CallFunc(Sound.play, "mario"))

        if stats.time <= 0:
            self.game_over("timeout")
