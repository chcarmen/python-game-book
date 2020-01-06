from cocos.scene import Scene
from cocos.director import director

from common.stats import stats
from game_scene.game_scene import GameScene
from .info_layer import InfoLayer


class InfoScene(Scene):
    def __init__(self, hud, world_complete=False):
        super().__init__()

        self.hud = hud
        self.world_complete = world_complete
        self.life = stats.life

        self.add(InfoLayer(self.world_complete), z=0)
        self.add(self.hud, z=10)

        self.elapsed = 0

    def on_enter(self):
        super().on_enter()
        self.schedule(self.transition)

    def on_exit(self):
        super().on_exit()
        self.unschedule(self.transition)

    def transition(self, dt):
        self.elapsed += dt

        if self.elapsed > 3.0:
            if self.life <= 0 or self.world_complete:
                director.pop()
            else:
                director.replace(GameScene(self.hud))
