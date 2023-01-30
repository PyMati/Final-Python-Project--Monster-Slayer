"""Player class module."""
import pygame
from config import *


class Hero(pygame.sprite.Sprite):
    """Player class."""
    def __init__(self, pos):
        super(Hero, self).__init__()
        # Position.
        self.posx = pos[0]
        self.posy = pos[1]

        # Rectangle and image settings.
        self.image = IDLE_SPRITE_SCALED
        self.rect = IDLE_SPRITE.get_rect()
        self.rect.x = self.posx
        self.rect.y = self.posy + 25
        self.rect.height = 116
        self.side = "r"
        self.is_moving = False
        self.is_attacking = False

        # Game player setting.
        self.speed = PLAYER_SPEED
        self.hp = START_PLAYER_HP
        self.dmg = PLAYER_DMG
        self.gold = START_GOLD
        self.collected_gold = self.gold
        self.armor = 0

        # Animation trackers.
        self.attack_index = 0
        self.run_index = 0
        self.lcounter = 0
        self.rcounter = 0
        self.attcounter = 0
        self.dmg_getter_counter = 0

    def reset_player_state(self):
        """Resets player actions to false in order to get idle animation."""
        self.is_moving = False
        self.is_attacking = False

    def reset_anim_index(self):
        """Function that always reset animation queqe."""
        self.attack_index = 0
        self.run_index = 0

    def return_idle_anim(self):
        if not self.is_moving and not self.is_attacking:
            self.reset_anim_index()
            if self.side == "r":
                self.image = IDLE_SPRITE_SCALED
            else:
                self.image = IDLE_SPRITE_FLIPPED

    def attack(self):
        """Function that creates attack animation."""
        if not self.is_moving:
            self.attcounter += 1
            if self.attcounter > 4:
                self.attack_index += 1
                self.attcounter = 0
            if self.attack_index >= 8:
                self.attack_index = 0
            if self.side == "r":
                self.image = ATTACK_1[self.attack_index]
            else:
                self.image = ATTACK_1_FLIPPED[self.attack_index]
            self.is_attacking = True

    def move_left(self):
        """Function that creates attack moving animation and
            moves hero lefts."""
        if not self.is_attacking:
            if self.run_index >= 9:
                self.run_index = 0
            if self.lcounter > 8:
                self.lcounter = 0
                self.run_index += 1
            if self.side == "r":
                self.side = "l"
                self.posx -= IMAGE_LENGTH
            self.posx -= self.speed
            self.rect.x -= self.speed
            self.image = RUN_FLIPPED[self.run_index]
            self.is_moving = True
            self.lcounter += 1

    def move_right(self):
        """Function that creates attack moving animation and
            moves hero rights."""
        if not self.is_attacking:
            if self.run_index >= 9:
                self.run_index = 0
            if self.lcounter > 8:
                self.lcounter = 0
                self.run_index += 1
            if self.side == "l":
                self.side = "r"
                self.posx += IMAGE_LENGTH
            self.posx += self.speed
            self.rect.x += self.speed
            self.image = RUN[self.run_index]
            self.is_moving = True
            self.lcounter += 1

    def get_dmg(self, monster_dmg):
        """Deals damage to the player."""
        self.dmg_getter_counter += 1
        if self.dmg_getter_counter > 8:
            self.dmg_getter_counter = 0
            if self.armor > 0:
                self.armor = self.armor - monster_dmg
                if self.armor < 0:
                    self.armor = 0
            else:
                self.hp -= monster_dmg
