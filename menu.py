"""Start menu game screen module."""
import pygame
from config import *
import sys


pygame.init()


def menu():
    """Menu function."""
    menu_loop = True
    pygame.display.set_caption('Menu - Monster Slayer')
    # Screen settings.
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode(MENU_WINDOW_SIZE)

    screen_rect = screen.get_rect()
    background_rect = BACKGROUND.get_rect()
    background_rect.center = screen_rect.center
    start_text_rect = START_TEXT.get_rect()
    start_text_rect.center = START_RECT_POS
    quit_text_rect = QUIT_TEXT.get_rect()
    quit_text_rect.center = QUIT_RECT_POS

    screen.blit(BACKGROUND, background_rect.topleft)
    screen.blit(TITLE_TEXT, TITLE_TEXT_POS)
    screen.blit(START_TEXT, START_TEXT_POS)
    screen.blit(QUIT_TEXT, QUIT_TEXT_POS)
    pygame.display.flip()
    menu_elements = [start_text_rect, quit_text_rect]

    # Sound functions.
    sound = MENU_THEME

    def play_theme():
        sound.set_volume(SOUND_VOLUME)
        sound.play()

    def stop_theme():
        pygame.mixer.pause()

    # Main loop.
    while menu_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for element in menu_elements:
                    if element.collidepoint(mouse_pos):
                        if element == quit_text_rect:
                            sys.exit()
                        if element == start_text_rect:
                            menu_loop = False
                            stop_theme()

        play_theme()

        screen.blit(BACKGROUND, background_rect.topleft)
        screen.blit(TITLE_TEXT, TITLE_TEXT_POS)
        screen.blit(START_TEXT, START_TEXT_POS)
        screen.blit(QUIT_TEXT, QUIT_TEXT_POS)
        pygame.display.flip()
        fps.tick(MAX_FPS)
