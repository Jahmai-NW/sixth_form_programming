import pygame

pygame.init()

SCREEN_SIZE = (640, 480)
SCALE = 8
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Goalkeeper Sprite")

# Draw at the sprite's native pixel size.
sprite = pygame.Surface((32, 32), pygame.SRCALPHA)

# Colors
skin = (233, 173, 120)
hair = (56, 37, 31)
green = (22, 131, 74)
green_light = (32, 168, 93)
yellow = (243, 213, 41)
blue = (38, 60, 112)
dark = (48, 32, 29)

def pixel_rect(x, y, width, height, color):
    pygame.draw.rect(sprite, color, (x, y, width, height))

# Hair and face
pixel_rect(12, 4, 8, 3, hair)
pixel_rect(11, 6, 2, 3, hair)
pixel_rect(13, 7, 7, 6, skin)
pixel_rect(18, 9, 1, 1, dark)

# Arms and gloves
pixel_rect(8, 13, 3, 3, green)
pixel_rect(5, 11, 4, 3, skin)
pixel_rect(2, 9, 4, 4, yellow)
pixel_rect(21, 13, 3, 3, green)
pixel_rect(23, 11, 4, 3, skin)
pixel_rect(26, 9, 4, 4, yellow)

# Jersey
pixel_rect(11, 13, 10, 7, green)
pixel_rect(14, 13, 4, 7, green_light)
pixel_rect(15, 14, 2, 2, yellow)

# Shorts and legs
pixel_rect(11, 20, 10, 4, blue)
pixel_rect(12, 24, 3, 4, skin)
pixel_rect(18, 24, 3, 4, skin)
pixel_rect(10, 28, 6, 2, dark)
pixel_rect(17, 28, 6, 2, dark)

# Scale up without blurring the pixel art.
big_sprite = pygame.transform.scale(sprite, (32 * SCALE, 32 * SCALE))
sprite_rect = big_sprite.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((70, 150, 80))
    screen.blit(big_sprite, sprite_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()