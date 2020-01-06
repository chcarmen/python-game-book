import pyglet_ffmpeg2

from cocos.director import director

import menu


def run_game():
    director.init(resizable=True, width=800, height=600, caption="Tetris")
    director.run(menu.create_menu_scene())


if __name__ == "__main__":
    run_game()
