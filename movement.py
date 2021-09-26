import constants
import pygame
from main import BORDER


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - constants.VEL > 0:  # LEFT
        yellow.x -= constants.VEL
    if (
        keys_pressed[pygame.K_d]
        and yellow.x + constants.VEL + yellow.width - 12 < BORDER.x
    ):  # RIGHT
        yellow.x += constants.VEL
    if keys_pressed[pygame.K_w] and yellow.y - constants.VEL > 0:  # UP
        yellow.y -= constants.VEL
    if (
        keys_pressed[pygame.K_s]
        and yellow.y + constants.VEL + yellow.height < constants.HEIGHT - 12
    ):  # DOWN
        yellow.y += constants.VEL


def red_handle_movement(keys_pressed, red):
    if (
        keys_pressed[pygame.K_LEFT] and red.x - constants.VEL > BORDER.x + BORDER.width
    ):  # LEFT
        red.x -= constants.VEL
    if (
        keys_pressed[pygame.K_RIGHT]
        and red.x + constants.VEL + red.width - 12 < constants.WIDTH
    ):  # RIGHT
        red.x += constants.VEL
    if keys_pressed[pygame.K_UP] and red.y - constants.VEL > 0:  # UP
        red.y -= constants.VEL
    if (
        keys_pressed[pygame.K_DOWN]
        and red.y + constants.VEL + red.height < constants.HEIGHT - 12
    ):  # DOWN
        red.y += constants.VEL
