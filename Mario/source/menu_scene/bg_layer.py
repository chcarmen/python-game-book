from cocos.layer import Layer
from pyglet.gl import *

from common.image import Image


class BackgroundLayer(Layer):
    def __init__(self):
        super().__init__()

        self.img = Image.background

    def draw(self):
        glPushMatrix()
        self.transform()
        self.img.blit(0, 0)
        glPopMatrix()
