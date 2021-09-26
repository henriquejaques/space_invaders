import pygame
import os
import random

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
FPS = 60
VEL = 3
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
BORDER_WIDTH = 10
YELLOW_SPACESHIP_INIT_POSITION_X = random.randrange(
    20, WIDTH // 2 - BORDER_WIDTH // 2 - 20
)
YELLOW_SPACESHIP_INIT_POSITION_Y = random.randrange(20, HEIGHT - 20)
RED_SPACESHIP_INIT_POSITION_X = random.randrange(
    WIDTH // 2 + BORDER_WIDTH // 2 + 20, WIDTH - 20
)
RED_SPACESHIP_INIT_POSITION_Y = random.randrange(20, HEIGHT - 20)
HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Grenade+1.ogg"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Gun+Silencer.ogg"))
