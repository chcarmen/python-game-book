from cocos.director import director
from cocos.scene import Scene
from cocos.layer import ColorLayer
from cocos.sprite import Sprite

from pyglet import image, resource


class MyLayer(ColorLayer):
    def __init__(self):
        super().__init__(255, 255, 255, 255)

        # method 1
        anim1 = resource.animation('dinosaur.gif', flip_x=True)
        self.sprite1 = Sprite(anim1, (150, 250))
        self.add(self.sprite1)
        anim2 = image.load_animation("dinosaur.gif")
        self.sprite2 = Sprite(anim2, (350, 250))
        self.add(self.sprite2)

        # method 2
        sprite_set = image.load("spriteset.png")
        image_grid = image.ImageGrid(sprite_set, 2, 5)
        frame_seq1 = image_grid[5:8]
        anim3 = image.Animation.from_image_sequence(frame_seq1, 0.1)
        anim3_flip = anim3.get_transform(flip_x=True)
        self.sprite3 = Sprite(anim3_flip, (150, 100))
        self.add(self.sprite3)

        # method 3
        self.sprite4 = Sprite(frame_seq1[0], (350, 100))
        self.add(self.sprite4)
        self.schedule(self.update, frame_seq1)
        self.elapsed = 0
        self.frame_idx = 0

    def update(self, dt, seq):
        self.elapsed += dt
        if self.elapsed >= 0.1:
            self.elapsed = 0
            self.frame_idx = (self.frame_idx + 1) % 3
            self.sprite4.image = seq[self.frame_idx]


if __name__ == "__main__":
    director.init(caption="Animation", width=500, height=300)
    director.run(Scene(MyLayer()))
