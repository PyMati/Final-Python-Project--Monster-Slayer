"""Village game scene."""
import pygame
from config import *
import sys
import connector


heal_price = 25
armor_price = 50
dmg_price = 100


def return_to_village(player_character):
    """Village scene."""
    global dmg_price
    # Scene settings.
    pygame.init()
    village_loop = True
    player = player_character
    animationcounter = 0
    animation_index = 0

    # Screen settings.
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode(GAME_WINDOW_SIZE)
    screen.fill(WHITE)
    pygame.display.set_caption('Village - Monster Slayer')
    screen_rect = screen.get_rect()
    rects_coordinates = [(100, 500), (450, 500), (800, 500)]

    def screen_border_collision():
        """Checks if the player is not trying to leave game arena."""
        if player.rect.x >= 930 and player.side == "r":
            player.speed = 0
        elif player.rect.x <= 10 and player.side == "l":
            player.speed = 0
        else:
            player.speed = PLAYER_SPEED

    def draw_env():
        """Function that draw environemt."""
        # Text reinitialization.
        npc_list = []
        seller = 0
        for coordinates in rects_coordinates:
            npc = pygame.draw.rect(screen, BLACK,
                                   pygame.Rect(coordinates[0] - 15,
                                               coordinates[1] + 100, 100, 100),
                                   1)
            npc_list.append(npc)
        for npc in npc_list:
            seller = check_shop(npc_list)
        screen.blit(player.image, (player.posx, player.posy))
        screen.fill(WHITE)
        screen.blit(VILLAGE_BACKGROUND, screen_rect.topleft)
        gold_stat = FONT.render(f"Gold: {player.collected_gold}", True, BLACK)
        hp_stat = FONT.render(f"Health: {player.hp}", True, BLACK)
        armor_stat = FONT.render(f"Armor: {player.armor}", True, BLACK)
        att_stat = FONT.render(f"Attack: {player.dmg}", True, BLACK)
        msg = "Click space in order to comeback on battlefield!"
        message = FONT.render(msg, True, BLACK)
        screen.blit(message, (screen_rect.centerx - 375,
                              screen_rect.centery))
        screen.blit(BLUE_NPC[animation_index], (100, 500))
        screen.blit(RED_NPC[animation_index], (450, 500))
        screen.blit(MAGENTA_NPC[animation_index], (800, 500))
        screen.blit(gold_stat, (screen_rect[0] + 10, screen_rect[1] + 10))
        screen.blit(hp_stat, (screen_rect[0] + 10, screen_rect[1] + 60))
        screen.blit(armor_stat, (screen_rect[0] + 10, screen_rect[1] + 110))
        screen.blit(att_stat, (screen_rect[0] + 10, screen_rect[1] + 160))
        screen.blit(player.image, (player.posx, player.posy))
        check_seller(seller)
        pygame.display.flip()

    def check_shop(npc_list):
        """Check if player is nearby seller."""
        index = 0
        for npc in npc_list:
            if player.rect.colliderect(npc):
                # Blue
                if index == 0:
                    return 0
                # Magenta
                elif index == 1:
                    return 1
                # Red
                elif index == 2:
                    return 2
                else:
                    return 3
            index += 1

    def check_seller(seller):
        """Shows seller message."""
        global dmg_price, heal_price, armor_price
        if seller == 2:
            price_and_item = FONT.render(f"Buy +1 attack dmg for {dmg_price} gold",
                                         True,
                                         BLACK)
            screen.blit(price_and_item, (400, 100))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        if player.collected_gold >= dmg_price:
                            player.collected_gold = (player.collected_gold
                                                     - dmg_price)
                            dmg_price += 100
                            player.dmg += 1
        if seller == 1:
            price_and_item = FONT.render(f"Buy +10 health for {heal_price} gold",
                                         True,
                                         BLACK)
            screen.blit(price_and_item, (400, 100))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        if (player.collected_gold >=
                                heal_price and player.hp < 100):
                            player.collected_gold = (player.collected_gold
                                                     - heal_price)
                            player.hp += 10
                            heal_price += 5
                            if player.hp > 100:
                                player.hp = 100
        if seller == 0:
            price_and_item = FONT.render(f"Buy +10 armor for {armor_price} gold", True, BLACK)
            screen.blit(price_and_item, (400, 100))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        if player.collected_gold >= armor_price:
                            player.collected_gold = (player.collected_gold
                                                     - armor_price)
                            player.armor += 10
                            armor_price += 10

    # Main game loop.
    while village_loop:
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
        if keys[pygame.K_SPACE]:
            pygame.mixer.stop()
            pygame.time.wait(3000)
            connector.run_game_again(player)
            break
        # Check state of the player.
        player.return_idle_anim()

        # Animating NPC's.
        animationcounter += 1
        if animationcounter >= 20:
            animationcounter = 0
            animation_index += 1
            if animation_index >= 5:
                animation_index = 0

        draw_env()
        screen_border_collision()
        fps.tick(MAX_FPS)
