import pygame, random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Penalty Shootout")
clock = pygame.time.Clock()

WHITE, BLACK = (255, 255, 255), (0, 0, 0)
FONT = pygame.font.Font(None, 48)

ball = pygame.Rect(WIDTH//2 - 15, HEIGHT - 60, 30, 30)
goal = pygame.Rect(WIDTH//2 - 100, 50, 200, 20)
score = 0

def show_text(text, y):
    txt = FONT.render(text, True, BLACK)
    rect = txt.get_rect(center=(WIDTH//2, y))
    screen.blit(txt, rect)

running = True
shooting = False
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            shooting = True

if shooting:
    ball.y -= 10
    if ball.colliderect(goal):
        score += 1
        ball.y = HEIGHT - 60
        shooting = False
    elif ball.y < 0:
        ball.y = HEIGHT - 60
        shooting = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, goal)
    pygame.draw.ellipse(screen, BLACK, ball)
    show_text(f"Score: {score}", HEIGHT - 30)
    show_text("Press SPACE to Shoot", HEIGHT//2)
    pygame.display.flip()

pygame.quit()