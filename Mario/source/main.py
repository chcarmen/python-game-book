import pyglet_ffmpeg2

import pyglet
from cocos.director import director

from menu_scene.menu_scene import MenuScene


def run_game():
    try:
        pyglet.font.add_directory("../res/font")
    except Exception as e:
        print(e)

    director.init(resizable=True, vsync=False, width=800, height=600, caption="Super Mario Bros")
    director.run(MenuScene())


if __name__ == "__main__":
    run_game()
