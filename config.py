"""File with configuration settings."""
import pygame


pygame.init()
# Font settings.
FONT = pygame.font.Font('font/PixelFraktur.ttf', 36)
ENDGAMEFONT = pygame.font.Font('font/PixelFraktur.ttf', 72)

# Colours.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen and tickrate settings.
MENU_WINDOW_SIZE = (800, 800)
GAME_WINDOW_SIZE = (1000, 800)
MAX_FPS = 60

# Player settings.
START_PLAYER_HP = 100
START_GOLD = 100
PLAYER_SPEED = 8
PLAYER_DMG = 3
# Sound and music settings.
SOUND_VOLUME = 0.05
MENU_THEME = pygame.mixer.Sound("sounds/menu/theme.mp3")
GAME_MUSIC = [
    pygame.mixer.Sound("sounds/game/themes/gaming8bit.mp3"),
    pygame.mixer.Sound("sounds/game/themes/ladyofthe80.mp3"),
    pygame.mixer.Sound("sounds/game/themes/neongaming.mp3"),
    pygame.mixer.Sound("sounds/game/themes/nightcity.mp3"),
    pygame.mixer.Sound("sounds/game/themes/strangerthings.mp3"),
]
DEATH_MUSIC = pygame.mixer.Sound("sounds/game/death.mp3")
# Menu sprites.
ALPHA_COLOUR = (16, 30, 41)
TITLE_TEXT = pygame.image.load("menusprites/EntryInfo.png")
TITLE_TEXT = pygame.transform.scale(TITLE_TEXT, (750, 75))
TITLE_TEXT_POS = (25, 50)
START_TEXT = pygame.image.load("menusprites/Start.png")
START_TEXT_POS = (200, 300)
START_RECT_POS = (385, 325)
QUIT_TEXT = pygame.image.load("menusprites/Quit.png")
QUIT_TEXT_POS = (250, 500)
QUIT_RECT_POS = (382, 522)
BACKGROUND = pygame.image.load("menusprites/background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, (956, 800))
STARTING_POINTS = [-20, 1020, -30, 1030]
# Game sprites.
GAME_BACKGROUND = pygame.image.load("envsprites/BGFront.png")
GAME_BACKGROUND = pygame.transform.scale(GAME_BACKGROUND, (1000, 800))
GAME_BACKGROUND_CLOUDS = pygame.image.load("envsprites/CloudsBack.png")
GAME_BACKGROUND_CLOUDS = pygame.transform.scale(GAME_BACKGROUND_CLOUDS,
                                                (1000, 800))
VILLAGE_BACKGROUND = pygame.image.load("envsprites/Background.png")
VILLAGE_BACKGROUND = pygame.transform.scale(VILLAGE_BACKGROUND, (1000, 800))
# Main hero sprites.
IMAGE_LENGTH = 141
IDLE_SPRITE = pygame.image.load("charactersprites/iddle/f0.png")
IDLE_SPRITE_SCALED = pygame.transform.scale(IDLE_SPRITE, (201, 141))
IDLE_SPRITE_FLIPPED = pygame.transform.flip(IDLE_SPRITE_SCALED, -1, 0)

ATTACK_1 = []
ATTACK_1_FLIPPED = []
for i in range(1, 10):
    sprite = pygame.image.load(f"charactersprites/attack1/f{i}.png")
    sprite = pygame.transform.scale(sprite, (201, 141))
    ATTACK_1.append(sprite)
    sprite = pygame.transform.flip(sprite, -1, 0)
    ATTACK_1_FLIPPED.append(sprite)

RUN = []
RUN_FLIPPED = []
for i in range(0, 10):
    sprite = pygame.image.load(f"charactersprites/run/f{i}.png")
    sprite = pygame.transform.scale(sprite, (201, 141))
    RUN.append(sprite)
    sprite = pygame.transform.flip(sprite, -1, 0)
    RUN_FLIPPED.append(sprite)

DEATH = pygame.image.load("charactersprites/death/f0.png")
DEATH_SCALED = pygame.transform.scale(DEATH, (268, 188))
# Monster sprites and number.
MONSTER_DEATH = []
for i in range(64, 96):
    sprite = pygame.image.load(f"effects/MagicBarrier_64x{i}.png")
    sprite = pygame.transform.scale(sprite, (64, 64))
    sprite.set_colorkey(ALPHA_COLOUR)
    MONSTER_DEATH.append(sprite)
ORC_SPRITES = []
ORC_SPRITES_FLIPPED = []
for i in range(0, 4):
    sprite = pygame.image.load(f"monstersprites/orc/f{i}.png")
    sprite = pygame.transform.scale(sprite, (64, 64))
    ORC_SPRITES.append(sprite)
    sprite = pygame.transform.flip(sprite, -1, 0)
    ORC_SPRITES_FLIPPED.append(sprite)
ORC_JUGGERNOUT = []
ORC_JUGGERNOUT_FLIPPED = []
for i in range(0, 8):
    sprite = pygame.image.load(f"monstersprites/juggernout/f{i}.png")
    sprite = pygame.transform.scale(sprite, (128, 128))
    ORC_JUGGERNOUT.append(sprite)
    sprite = pygame.transform.flip(sprite, -1, 0)
    ORC_JUGGERNOUT_FLIPPED.append(sprite)
TANK_MONSTER = []
TANK_MONSTER_FLIPPED = []
for i in range(1, 9):
    sprite = pygame.image.load(f"monstersprites/tank_monster/f{i}.png")
    sprite = pygame.transform.scale(sprite, (256, 256))
    TANK_MONSTER.append(sprite)
    sprite = pygame.transform.flip(sprite, -1, 0)
    TANK_MONSTER_FLIPPED.append(sprite)
HIGH_DMG_MONSTER = []
HIGH_DMG_MONSTER_FLIPPED = []
for i in range(1, 9):
    sprite = pygame.image.load(f"monstersprites/high_dmg_monster/f{i}.png")
    sprite = pygame.transform.scale(sprite, (128, 128))
    HIGH_DMG_MONSTER.append(sprite)
    sprite = pygame.transform.flip(sprite, -1, 0)
    HIGH_DMG_MONSTER_FLIPPED.append(sprite)
FAST_MONSTER = []
FAST_MONSTER_FLIPPED = []
for i in range(1, 5):
    sprite = pygame.image.load(f"monstersprites/fast_monster/f{i}.png")
    sprite = pygame.transform.scale(sprite, (64, 64))
    FAST_MONSTER.append(sprite)
    sprite = pygame.transform.flip(sprite, -1, 0)
    FAST_MONSTER_FLIPPED.append(sprite)
MONSTERS_LVL_1 = [
    (ORC_SPRITES, ORC_SPRITES_FLIPPED, 5, 5, 5, 3),
    (ORC_JUGGERNOUT, ORC_JUGGERNOUT_FLIPPED, 50, 20, 20, 2),
    (TANK_MONSTER, TANK_MONSTER_FLIPPED, 100, 40, 40, 1),
    (HIGH_DMG_MONSTER, HIGH_DMG_MONSTER_FLIPPED, 75, 30, 25, 0.5),
    (FAST_MONSTER, FAST_MONSTER_FLIPPED, 20, 2, 3, 10)
]
# Npc sprites.
BLUE_NPC = []
RED_NPC = []
MAGENTA_NPC = []
for i in range(0, 5):
    sprite = pygame.image.load(f"charactersprites/NPC's/Blue/f{i}.png")
    sprite = pygame.transform.scale(sprite, (200, 200))
    BLUE_NPC.append(sprite)
    sprite = pygame.image.load(f"charactersprites/NPC's/Red/f{i}.png")
    sprite = pygame.transform.scale(sprite, (200, 200))
    RED_NPC.append(sprite)
    sprite = pygame.image.load(f"charactersprites/NPC's/Magenta/f{i}.png")
    sprite = pygame.transform.scale(sprite, (200, 200))
    MAGENTA_NPC.append(sprite)
