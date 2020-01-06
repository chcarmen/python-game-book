import pygame


class Image:
    pygame.init()
    pygame.display.set_mode((480, 852))

    heros_name = ["hero1", "hero2", "hero_blowup_n1", "hero_blowup_n2", "hero_blowup_n3", "hero_blowup_n4"]
    small_enemies_name = ["enemy1", "enemy1_down1", "enemy1_down2", "enemy1_down3", "enemy1_down4"]
    mid_enemies_name = ["enemy2", "enemy2_hit", "enemy2_down1", "enemy2_down2", "enemy2_down3", "enemy2_down4"]
    big_enemies_name = ["enemy3_n1", "enemy3_n2", "enemy3_hit", "enemy3_down1", "enemy3_down2", "enemy3_down3",
                        "enemy3_down4", "enemy3_down5", "enemy3_down6"]

    pause_resume_name = ["game_pause_nor", "game_pause_pressed", "game_resume_nor", "game_resume_pressed"]

    try:
        background = pygame.image.load("../res/image/background.png").convert()
        bullet = pygame.image.load("../res/image/bullet1.png").convert_alpha()
        heros = [pygame.image.load(image.join(["../res/image/", ".png"])).convert_alpha() for image in heros_name]
        small_enemies = [pygame.image.load(image.join(["../res/image/", ".png"])).convert_alpha() for image in small_enemies_name]
        mid_enemies = [pygame.image.load(image.join(["../res/image/", ".png"])).convert_alpha() for image in mid_enemies_name]
        big_enemies = [pygame.image.load(image.join(["../res/image/", ".png"])).convert_alpha() for image in big_enemies_name]
        logo = pygame.image.load("../res/image/logo.png").convert_alpha()
        pause_resume = [pygame.image.load(image.join(["../res/image/", ".png"])).convert_alpha() for image in pause_resume_name]
    except pygame.error:
        raise SystemExit(pygame.get_error())
