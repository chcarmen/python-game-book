from common.image import Image
from .actor import Actor


class Cliff(Actor):
    def __init__(self, pos, _):
        super().__init__(Image.cliff, pos, _)
