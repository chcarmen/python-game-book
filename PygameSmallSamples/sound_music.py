import sys

import pygame


sound1 = None
sound2 = None
sound3 = None


class Button(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(name+".png").convert_alpha()
        self.rect = self.image.get_rect()

        if name == "button0":
            self.rect.topleft = (60, 50)
        elif name == "button1":
            self.rect.topleft = (60, 100)
        elif name == "button2":
            self.rect.topleft = (60, 150)
        elif name == "button3":
            self.rect.topleft = (60, 200)
        elif name == "button4":
            self.rect.topleft = (280, 50)
        elif name == "button5":
            self.rect.topleft = (280, 100)
        elif name == "button6":
            self.rect.topleft = (280, 150)

    def update(self, pos):
        if self.rect.collidepoint(pos):
            if self.name == "button0":
                pygame.mixer.music.play(-1)
            elif self.name == "button1":
                pygame.mixer.music.pause()
            elif self.name == "button2":
                pygame.mixer.music.unpause()
            elif self.name == "button3":
                pygame.mixer.music.stop()
            elif self.name == "button4":
                sound1.play()
            elif self.name == "button5":
                sound2.play()
            elif self.name == "button6":
                sound3.play()


def main():
    pygame.init()

    screen = pygame.display.set_mode((500, 300))
    pygame.display.set_caption("Sound and Music")

    buttons_name = ["button0", "button1", "button2", "button3",
                    "button4", "button5", "button6"]

    buttons = pygame.sprite.Group()
    for name in buttons_name:
        buttons.add(Button(name))

    global sound1, sound2, sound3
    sound1 = pygame.mixer.Sound("win.wav")
    sound2 = pygame.mixer.Sound("rock.wav")
    sound3 = pygame.mixer.Sound("tap.wav")

    pygame.mixer.music.load("carmen.mp3")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button != 1:
                    continue

                buttons.update(event.pos)

        screen.fill((255, 255, 255))
        buttons.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
