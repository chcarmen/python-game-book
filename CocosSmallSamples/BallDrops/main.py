from collections import defaultdict

from cocos.director import director
from cocos.scene import Scene
from cocos.tiles import load
from cocos.layer import ScrollingManager, ScrollableLayer
from cocos.sprite import Sprite

from actor import Actor


class GameLayer(ScrollableLayer):
    is_event_handler = True

    def __init__(self, *args):
        super().__init__()
        self.obstacle_layer = args[0]
        self.objects = args[1]
        self.tileset = args[2]

        # create actor
        start_obj = self.objects.match(label="start")[0]
        self.actor = Actor(start_obj.position, self.obstacle_layer)
        self.add(self.actor)

        # create boat
        boat_obj = self.objects.match(label="boat")[0]
        self.boat = Sprite("boat.png")
        self.boat.position = boat_obj.position
        self.add(self.boat)

        self.pressed = defaultdict(int)
        self.schedule(self.update)

    def on_enter(self):
        super().on_enter()
        self.scroller = self.parent

    def on_key_press(self, k, _):
        self.pressed[k] = 1

    def on_key_release(self, k, _):
        self.pressed[k] = 0

    def on_mouse_press(self, x, y, buttons, modifiers):
        world_x, world_y = self.scroller.screen_to_world(x, y)
        cell = self.obstacle_layer.get_at_pixel(world_x, world_y)
        cell.tile = self.tileset[46]
        self.obstacle_layer.set_dirty()

    def update(self, dt):
        self.actor.update_position(dt, self.pressed)


if __name__ == "__main__":
    director.init(caption="Ball Drops", width=320, height=416)

    map = load("map.tmx")
    background_layer = map["background"]
    obstacle_layer = map["obstacle"]
    objects = map["objects"]
    tileset = map["tileset"]

    scroller = ScrollingManager()
    scroller.add(background_layer, z=0)
    scroller.add(obstacle_layer, z=1)
    scroller.add(GameLayer(obstacle_layer, objects, tileset), z=2)

    scene = Scene()
    scene.add(scroller)
    director.run(scene)
