import pyglet


class Settings:
    pyglet.resource.path.append("../res/image")
    pyglet.resource.reindex()

    try:
        pyglet.font.add_directory("../res/font")
    except Exception as e:
        print(e)

    # pre-defined parameters
    ROW = 20
    COLUMN = 10
    SQUARE_SIZE = 29

    # level: total 10 levels
    # speed: the real speed is 1/speed, which means, move down 1 square per xx seconds
    # lines: the lower limit lines
    # score: score for one line
    LEVEL_INFO = [{"level": 1, "speed": 1.0, "lines": 0, "score": 10},
                  {"level": 2, "speed": 0.9, "lines": 10, "score": 20},
                  {"level": 3, "speed": 0.8, "lines": 20, "score": 30},
                  {"level": 4, "speed": 0.7, "lines": 30, "score": 40},
                  {"level": 5, "speed": 0.6, "lines": 40, "score": 50},
                  {"level": 6, "speed": 0.5, "lines": 50, "score": 60},
                  {"level": 7, "speed": 0.4, "lines": 60, "score": 70},
                  {"level": 8, "speed": 0.3, "lines": 70, "score": 80},
                  {"level": 9, "speed": 0.2, "lines": 80, "score": 90},
                  {"level": 10, "speed": 0.1, "lines": 90, "score": 100}]

    # black is phony color, not used
    COLORS = ["black", "blue", "green", "magenta", "orange", "pink", "violet", "yellow"]

    COLOR_BLACK, COLOR_BLUE, COLOR_GREEN, COLOR_MAGENTA, COLOR_ORANGE, COLOR_PINK, COLOR_VIOLET, COLOR_YELLOW \
        = range(len(COLORS))

    try:
        IMAGES = [pyglet.resource.image(color.join(["block_", ".png"])) for color in COLORS]
    except pyglet.resource.ResourceNotFoundException:
        raise SystemExit("cannot find block image!")

    # user input parameters
    input_level = 1
    input_music = True
    input_sound = True
