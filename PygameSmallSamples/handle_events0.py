import sys

import pygame
from pygame.locals import *


MY_EVENT1 = USEREVENT + 1
MY_EVENT2 = USEREVENT + 2


def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 300))
    pygame.display.set_caption("Event Handling0")

    type_font = pygame.font.SysFont(None, 48)
    dict_font = pygame.font.SysFont(None, 26)

    additional_info = ""
    buttons = ["left", "middle", "right", "wheel up", "wheel down"]
    times = 0

    pygame.key.set_repeat(1, 50)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                times += 1
                additional_info = " ".join([pygame.key.name(event.key), "key is pressed", str(times)])
                if event.key == K_q:
                    sys.exit()
                elif event.key == K_SPACE:
                    my_event = pygame.event.Event(MY_EVENT1, attri1="attribute1", attri2="my attribute2")
                    pygame.event.post(my_event)
                elif event.key == K_e:
                    pygame.time.set_timer(MY_EVENT2, 2000)
                elif event.key == K_d:
                    pygame.time.set_timer(MY_EVENT2, 0)
            elif event.type == KEYUP:
                times = 0
                additional_info = " ".join([pygame.key.name(event.key), "key is released"])
            elif event.type == MOUSEMOTION:
                additional_info = ""
            elif event.type == MOUSEBUTTONDOWN:
                additional_info = buttons[event.button-1].join(["mouse ", " button is pressed"])
            elif event.type == MOUSEBUTTONUP:
                additional_info = buttons[event.button-1].join(["mouse ", " button is released"])
            elif event.type == MY_EVENT1:
                additional_info = "my event1 is received"
            elif event.type == MY_EVENT2:
                additional_info = "my event2 is received"

            # text 0: type
            type_text = pygame.event.event_name(event.type)
            type = type_font.render(type_text, True, (255, 0, 0))

            # text 1: dict
            dict_text = str(event.dict)
            attributes = dict_font.render(dict_text, True, (0, 0, 255))

            # text 2: additional
            additional = dict_font.render(additional_info, True, (0, 0, 0))

            screen.fill((255, 255, 255))
            screen.blit(type, (20, 50))
            screen.blit(attributes, (20, 100))
            screen.blit(additional, (20, 200))
            pygame.display.flip()


if __name__ == "__main__":
    main()
