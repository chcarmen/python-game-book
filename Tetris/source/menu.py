from cocos.director import director
from cocos.layer import MultiplexLayer
from cocos.menu import *
from cocos.scene import Scene
from cocos.scenes.transitions import ZoomTransition
from pyglet.app import exit

from background import BackgroundLayer
from game import create_game_scene
from settings import Settings
from sound import Sound
from sprites import SpritesLayer


class MainMenu(Menu):
    def __init__(self):
        super().__init__("TETRIS")

        self.font_title["font_name"] = "DJB Letter Game Tiles"
        self.font_title["font_size"] = 72
        self.font_title["color"] = (176, 48, 96, 255)
        self.font_title["bold"] = True

        self.font_item["font_name"] = "Kristen ITC"
        self.font_item["font_size"] = 32
        self.font_item["color"] = (160, 160, 160, 255)

        self.font_item_selected["font_name"] = "Kristen ITC"
        self.font_item_selected["font_size"] = 46
        self.font_item_selected["color"] = (128, 128, 128, 255)

        self.menu_valign = TOP
        self.menu_halign = RIGHT

        items = []

        items.append(MenuItem("Play", self.on_play))
        items.append(MenuItem("Option", self.on_option))
        items.append(MenuItem("Quit", self.on_quit))

        self.create_menu(items, shake(), shake_back())

        self.select_sound = Sound.button_sound

    def on_play(self):
        game_scene = create_game_scene()
        director.push(ZoomTransition(game_scene))

    def on_option(self):
        self.parent.switch_to(1)

    def on_quit(self):
        exit()


class OptionMenu(Menu):
    def __init__(self):
        super().__init__("TETRIS")

        self.font_title["font_name"] = "DJB Letter Game Tiles"
        self.font_title["font_size"] = 72
        self.font_title["color"] = (176, 48, 96, 255)
        self.font_title["bold"] = True

        self.font_item["font_name"] = "Kristen ITC"
        self.font_item["font_size"] = 32
        self.font_item["color"] = (160, 160, 160, 255)

        self.font_item_selected["font_name"] = "Kristen ITC"
        self.font_item_selected["font_size"] = 46
        self.font_item_selected["color"] = (128, 128, 128, 255)

        self.menu_valign = TOP
        self.menu_halign = RIGHT

        items = []

        self.level = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        items.append(MultipleMenuItem("Level: ", self.on_level, self.level, Settings.input_level-1))
        items.append(ToggleMenuItem("Music: ", self.on_music, Settings.input_music))
        items.append(ToggleMenuItem("Sound: ", self.on_sound, Settings.input_sound))
        items.append(MenuItem("Back", self.on_back))

        self.create_menu(items, shake(), shake_back())

        self.select_sound = Sound.button_sound

    def on_level(self, idx):
        Settings.input_level = int(self.level[idx])

    def on_music(self, value):
        Settings.input_music = value

    def on_sound(self, value):
        Settings.input_sound = value

    def on_back(self):
        self.parent.switch_to(0)


def create_menu_scene():
    scene = Scene()
    scene.add(BackgroundLayer(), z=0)
    scene.add(SpritesLayer(), z=1)
    scene.add(MultiplexLayer(MainMenu(), OptionMenu()), z=2)
    return scene
