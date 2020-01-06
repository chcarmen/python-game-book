from cocos.director import director
from cocos.scene import Scene

from listener import Listener


if __name__ == "__main__":

    director.init(resizable=True)
    main_scene = Scene(Listener())
    director.run(main_scene)
