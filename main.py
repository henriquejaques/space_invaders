import pygame
import os
import transforms
import constants
import movement
import projectiles


WIN = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Space Invaders")
BORDER = pygame.Rect(
    constants.WIDTH // 2 - (constants.BORDER_WIDTH // 2),
    0,
    constants.BORDER_WIDTH,
    constants.HEIGHT,
)

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

SPACE = transforms.scale(
    pygame.image.load(os.path.join("Assets", "space.png")),
    constants.WIDTH,
    constants.HEIGHT,
)


YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png")
)
YELLOW_SPACESHIP = transforms.scale(
    YELLOW_SPACESHIP_IMAGE, constants.SPACESHIP_WIDTH, constants.SPACESHIP_HEIGHT
)
YELLOW_SPACESHIP = transforms.rotate(YELLOW_SPACESHIP, 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = transforms.scale(
    RED_SPACESHIP_IMAGE, constants.SPACESHIP_WIDTH, constants.SPACESHIP_HEIGHT
)
RED_SPACESHIP = transforms.rotate(RED_SPACESHIP, 270)


def draw_window(red, yellow, yellow_bullets, red_bullets, yellow_health, red_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, constants.BLACK, BORDER)
    yellow_health_text = constants.HEALTH_FONT.render(
        f"Health: {yellow_health}", 1, constants.WHITE
    )
    red_health_text = constants.HEALTH_FONT.render(
        f"Health: {red_health}", 1, constants.WHITE
    )
    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(red_health_text, (constants.WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, constants.YELLOW, bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WIN, constants.RED, bullet)
    pygame.display.update()


def main():
    yellow = pygame.Rect(
        300, 100, constants.SPACESHIP_WIDTH, constants.SPACESHIP_HEIGHT
    )
    red = pygame.Rect(700, 100, constants.SPACESHIP_WIDTH, constants.SPACESHIP_HEIGHT)
    red_bullets = []
    yellow_bullets = []
    yellow_health = 10
    red_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(constants.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if (
                    event.key == pygame.K_LCTRL
                    and len(yellow_bullets) < constants.MAX_BULLETS
                ):
                    bullet = pygame.Rect(
                        yellow.x + yellow.width,
                        yellow.y + yellow.height // 2 - 2,
                        10,
                        5,
                    )
                    yellow_bullets.append(bullet)

                if (
                    event.key == pygame.K_RCTRL
                    and len(red_bullets) < constants.MAX_BULLETS
                ):
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)

            if event.type == YELLOW_HIT:
                yellow_health -= 1
            if event.type == RED_HIT:
                red_health -= 1

        winner_text = ""
        if yellow_health <= 0:
            winner_text = "Red Wins!"
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        if winner_text != "":
            pass  # SOMEONE WON

        keys_pressed = pygame.key.get_pressed()
        movement.yellow_handle_movement(keys_pressed, yellow)
        movement.red_handle_movement(keys_pressed, red)
        projectiles.handle_bullets(
            yellow_bullets, red_bullets, yellow, red, YELLOW_HIT, RED_HIT
        )
        draw_window(red, yellow, yellow_bullets, red_bullets, yellow_health, red_health)

    pygame.quit()


if __name__ == "__main__":
    main()
