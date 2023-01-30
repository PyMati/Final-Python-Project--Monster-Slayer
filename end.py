"""End game screen module."""
import pygame
import sys
from config import *
import main


pygame.init()


def endgame(death, gold):
    """Function that shows the end screen."""
    if death:

        pygame.display.set_caption('End - Village Deffender')
        # Sound settings.
        pygame.mixer.stop()
        sound = DEATH_MUSIC
        sound.set_volume(SOUND_VOLUME)
        sound.play()

        # Screen settings.
        fps = pygame.time.Clock()
        screen = pygame.display.set_mode(GAME_WINDOW_SIZE)
        screen_rect = screen.get_rect()

        # Messages settings.
        msg = ENDGAMEFONT.render("You died!", True, RED)
        score_msg = FONT.render(f"You managed to collect {gold} gold,",
                                True,
                                RED)
        score_msg_cont = FONT.render(f"though it didn't help you much. . .",
                                     True,
                                     RED)

        restart_msg = FONT.render("Clicl R to reset game.", True, RED)

        # Main loop.
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main.main()
                        pygame.mixer.stop()
                        break

            screen.blit(msg, (screen_rect.center[0] - 160,
                              screen_rect.center[1] - 300))
            screen.blit(DEATH_SCALED, (screen_rect.center[0] - 80,
                                       screen_rect.center[1] - 300))
            screen.blit(score_msg, (250, screen_rect.center[1] - 75))
            screen.blit(score_msg_cont, (250, screen_rect.center[1] - 25))
            screen.blit(restart_msg, (screen_rect.center[0] - 180, 450))
            pygame.display.flip()
            fps.tick(MAX_FPS)
