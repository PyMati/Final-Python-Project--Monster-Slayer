"""Main game screen module."""
from config import *
import pygame
import sys
import random
from monster import Monster, Death
from config import *
import random
from end import endgame
import connector


monsters_number = 2


def game(player_character):
    """Main game function."""
    global monsters_number
    pygame.init()
    # Loop tracker and animation indexes trackers.
    game_loop = True
    go_home = False
    is_dead = False
    pygame.display.set_caption('Game - Monster Slayer')

    # Player initialization.
    player = player_character

    # Monster initialization.
    monster_list = pygame.sprite.Group()
    monster_control_x_right = 40
    monster_control_x_left = 40
    for _ in range(monsters_number):
        pos = random.choice(STARTING_POINTS)
        if pos < 0:
            pos -= monster_control_x_left
            monster_control_x_left += 80
        elif pos > 1000:
            pos += monster_control_x_right
            monster_control_x_right += 80
        new_monster = random.choice(MONSTERS_LVL_1)
        monster_list.add(Monster(pos,
                                 new_monster[0], new_monster[1],
                                 new_monster[2], new_monster[3],
                                 new_monster[4], new_monster[5]))
    monsters_number *= 2

    death_places = pygame.sprite.Group()
    # Sound effects.
    sound = random.choice(GAME_MUSIC)
    sound.set_volume(SOUND_VOLUME)
    sound.play()

    # Screen settings.
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode(GAME_WINDOW_SIZE)
    screen_rect = screen.get_rect()
    background = GAME_BACKGROUND
    background_clouds = GAME_BACKGROUND_CLOUDS
    att_stat = FONT.render(f"Attack: {player.dmg}", True, BLACK)
    ENV_OBJECTS = [background_clouds, background]
    for envsprite in ENV_OBJECTS:
        screen.blit(envsprite, screen_rect.topleft)
    pygame.display.flip()

    def draw_env():
        """Function that draw environemt."""
        # Text reinitialization.
        monsters_left = FONT.render(f"Monsters left: {len(monster_list)}",
                                    True,
                                    BLACK)
        gold_stat = FONT.render(f"Gold: {player.collected_gold}",
                                True,
                                BLACK)
        hp_stat = FONT.render(f"Health: {player.hp}",
                              True,
                              BLACK)
        armor_stat = FONT.render(f"Armor: {player.armor}", True, BLACK)
        screen.fill((0, 0, 0))
        for envsprite in ENV_OBJECTS:
            screen.blit(envsprite, screen_rect.topleft)
        if go_home:
            message = FONT.render("""You will come back to village in 3 seconds.""",
                                  True,
                                  BLACK)
            screen.blit(message, (screen_rect.centerx - 350,
                                  screen_rect.centery))
        screen.blit(gold_stat, (screen_rect[0] + 10, screen_rect[1] + 10))
        screen.blit(hp_stat, (screen_rect[0] + 10, screen_rect[1] + 60))
        screen.blit(armor_stat, (screen_rect[0] + 10, screen_rect[1] + 110))
        screen.blit(att_stat, (screen_rect[0] + 10, screen_rect[1] + 160))
        screen.blit(monsters_left, (screen_rect[0] + 10, screen_rect[1] + 210))
        if not is_dead:
            screen.blit(player.image, (player.posx, player.posy))
        # pygame.draw.rect(screen, (0, 0, 0), player.rect, 2)

    def draw_monsters():
        """Function that draws all enemies on the screen."""
        for monster in monster_list:
            monster.move_monster(player.rect.x)
            monster.check_sprite(player.rect.x)
            monster.update_rect()
            monster.animate(player.rect.x)
            screen.blit(monster.image, (monster.posx, monster.posy))
        for death in death_places:
            screen.blit(death.sprite, (death.posx, death.posy))

    def player_is_hit():
        """Checks if the player gets hit from the monster."""
        for monster in monster_list:
            if monster.rect.colliderect(player.rect):
                player.get_dmg(monster.monster_dmg)

    def screen_border_collision():
        """Checks if the player is not trying to leave game arena."""
        if player.rect.x >= 930 and player.side == "r":
            player.speed = 0
        elif player.rect.x <= 10 and player.side == "l":
            player.speed = 0
        else:
            player.speed = PLAYER_SPEED

    def player_attack_rect():
        """
        Scans the space in front of player and
        search for enemies to deal dmg.
        """
        if player.is_attacking:
            if player.side == "r":
                attack_space = pygame.draw.rect(screen,
                                                BLACK,
                                                pygame.Rect(
                                                    player.rect.x + 50,
                                                    player.rect.y,
                                                    140,
                                                    100), 1)
            else:
                attack_space = pygame.draw.rect(screen,
                                                BLACK,
                                                pygame.Rect(
                                                    player.rect.x - 130,
                                                    player.rect.y,
                                                    140,
                                                    100), 1)
            for monster in monster_list:
                monster_rect = pygame.draw.rect(screen, BLACK, monster.rect, 2)
                if monster_rect.colliderect(attack_space):
                    monster.get_dmg(player.dmg)
                    if monster.hp <= 0:
                        monster.kill()
                        death_places.add(Death(MONSTER_DEATH,
                                               monster.rect.x,
                                               monster.rect.y,
                                               monster.image.get_width()))
                        player.collected_gold += monster.gold_value
                    break

    # Main game loop.
    while game_loop:
        # Checking if the player is still alive.
        if not is_dead:
            if player.hp <= 0:
                is_dead = True
                player.kill()
                death_places.add(Death(MONSTER_DEATH,
                                       player.rect.x,
                                       player.rect.y,
                                       100))
                # endgame(True, player.collected_gold)
                # break
        if is_dead and len(death_places) == 0:
            monsters_number = 2
            endgame(True, player.collected_gold)
            break
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Player controls.
        player.reset_player_state()
        # Go left.
        if keys[pygame.K_a]:
            player.move_left()
        # Go right
        if keys[pygame.K_d]:
            player.move_right()
        # Attack
        if keys[pygame.K_p]:
            player.attack()
        # Check state of the player.
        player.return_idle_anim()

        draw_env()
        draw_monsters()
        screen_border_collision()
        player_is_hit()
        for death in death_places:
            death.play_animation()
        pygame.display.flip()
        player_attack_rect()
        if not go_home:
            if len(monster_list) <= 0:
                go_home = True
        else:
            pygame.mixer.stop()
            pygame.time.wait(3000)
            connector.return_to_village(player)
            break
        fps.tick(MAX_FPS)
