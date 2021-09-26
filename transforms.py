import pygame


def rotate(object, angle):
    return pygame.transform.rotate(object, angle)


def scale(object, width, height):
    return pygame.transform.scale(object, (width, height))
