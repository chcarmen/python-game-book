from collections import defaultdict

from cocos.director import director
from cocos.scene import Scene
from cocos.layer import ColorLayer
from cocos.collision_model import CollisionManagerGrid

from actor import Mouse, Cat


class MainLayer(ColorLayer):
    is_event_handler = True

    def __init__(self):
        super().__init__(220, 220, 220, 255)

        for i in range(5):
            mouse = Mouse((24, 300 * (6-i-1)/6))
            self.add(mouse)

        self.cat = Cat((468, 32))
        self.add(self.cat)

        self.pressed = defaultdict(int)
        self.schedule(self.update)

        self.cm = CollisionManagerGrid(0, 500, 0, 300, 48*1.25, 48*1.25)

        # case 1
        '''
        for _, node in self.children:
            if isinstance(node, Mouse):
                self.cm.add(node)
        '''

    def on_key_press(self, k, _):
        self.pressed[k] = 1

    def on_key_release(self, k, _):
        self.pressed[k] = 0

    def update(self, dt):
        self.cat.move(self.pressed)
        self.collide()

    def collide(self):
        # case 2
        self.cm.clear()

        for _, node in self.children:
            self.cm.add(node)

        for mouse in self.cm.objs_colliding(self.cat):
            #self.cm.remove_tricky(mouse) # case 1
            self.remove(mouse)


if __name__ == "__main__":
    director.init(caption='CatMouse', width=500, height=300)
    main_layer = MainLayer()
    main_scene = Scene()
    main_scene.add(main_layer)
    director.run(main_scene)
