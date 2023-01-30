"""Monster class module."""
import pygame
from config import *


class Monster(pygame.sprite.Sprite):
    """Monster class."""
    def __init__(self, pos, image, image_flipped, monster_gold_value,
                 monster_dmg, monster_hp, monster_speed):
        super(Monster, self).__init__()
        # Position.
        self.posx = pos
        self.posy = 800 - image[0].get_height()
        self.hp = monster_hp
        self.speed = monster_speed
        # Rectangle and image settings.
        self.image = image[0]
        self.not_flipped = image
        self.flipped = image_flipped
        self.rect = self.image.get_rect()

        # Monster settings.
        self.gold_value = monster_gold_value
        self.monster_dmg = monster_dmg

        # Animation trackers and counters.
        self.anim_counter = 0
        self.anim_index = 0
        self.dmg_counter = 0

    def move_monster(self, player_posx):
        """Move monster towards the player."""
        if player_posx < self.posx:
            self.posx -= self.speed
        elif player_posx > self.posx:
            self.posx += self.speed
        else:
            pass

    def check_sprite(self, player_posx):
        """Flips sprite depedning on monster position on x axis."""
        if self.posx > player_posx:
            self.image = self.flipped[0]
        else:
            self.image = self.not_flipped[0]

    def animate(self, player_posx):
        """Animates sprite of the monster."""
        self.anim_counter += 1
        if self.anim_counter >= 8:
            self.anim_counter = 0
            self.anim_index += 1
        if self.anim_index >= len(self.not_flipped):
            self.anim_index = 0
        if self.posx > player_posx:
            self.image = self.flipped[self.anim_index]
        else:
            self.image = self.not_flipped[self.anim_index]

    def update_rect(self):
        """Updates the rectangle of the monster."""
        self.rect.x = self.posx
        self.rect.y = self.posy

    def get_dmg(self, player_dmg):
        """Deals dmg to the monster."""
        self.dmg_counter += 1
        if self.dmg_counter >= 7:
            self.dmg_counter = 0
            self.hp -= player_dmg


class Death(pygame.sprite.Sprite):
    """Death animation."""
    def __init__(self, anim_sprites, posx, posy, scale):
        super(Death, self).__init__()
        # Animation settings.
        self.animation_counter = 0
        self.animation_index = 0
        self.anim_sprites = anim_sprites
        # Sprite settings.
        self.alpha_colour = (16, 30, 41)
        self.scale = scale
        self.sprite = self.anim_sprites[0]
        self.sprite = self.anim_sprites[self.animation_index]
        self.sprite = pygame.transform.scale(self.sprite, (self.scale,
                                                           self.scale))
        self.sprite.set_colorkey(self.alpha_colour)

        # Position.
        self.posx = posx
        self.posy = posy

    def play_animation(self):
        """Plays animation of death of the monster."""
        self.animation_counter += 1
        if self.animation_counter >= 6:
            self.sprite = self.anim_sprites[self.animation_index]
            self.sprite = pygame.transform.scale(self.sprite, (self.scale,
                                                               self.scale))
            self.sprite.set_colorkey(self.alpha_colour)
            self.animation_index += 1
        if self.animation_index >= len(self.anim_sprites) - 1:
            self.kill()
