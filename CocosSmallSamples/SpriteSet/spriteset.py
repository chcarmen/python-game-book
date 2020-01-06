from cocos.director import director
from cocos.scene import Scene
from cocos.layer import ColorLayer
from cocos.sprite import Sprite

from pyglet import resource, image


class MyLayer(ColorLayer):
    def __init__(self):
        super().__init__(255, 255, 255, 255)
        sprite_set = resource.image("spriteset.png")
        image_grid = image.ImageGrid(sprite_set, 6, 10)

        image0 = image_grid[54]
        self.add(Sprite(image0, (200, 150)))

        image1 = image_grid[(5, 4)].get_transform(flip_y=True)
        self.add(Sprite(image1, (300, 150)))


if __name__ == "__main__":
    director.init(caption="SpriteSet", width=500, height=300)
    director.run(Scene(MyLayer()))
