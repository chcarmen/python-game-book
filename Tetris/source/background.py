import pyglet
from cocos.layer import Layer
from pyglet.gl import *


class BackgroundLayer(Layer):
    def __init__(self):
        super().__init__()

        try:
            self.img = pyglet.resource.image("background.png")
        except pyglet.resource.ResourceNotFoundException:
            raise SystemExit("cannot find background image!")

    def draw(self):
        glPushMatrix()
        self.transform()
        self.img.blit(0, 0)
        glPopMatrix()
