import pygame

pygame.init() #initiates pygame module
screen = pygame.display.set_mode((1000, 600)) #establishes the size of the screen to be displayed

pygame.display.set_caption("Penalty Shootout") #establishes the text to be displayed as the caption of the screen

clock = pygame.time.Clock() #creates a clock object which keeps track of time
running = True #running set to true


titlePanel = pygame.display.set_mode((200, 100))
font = pygame.font.Font('freesansbold.ttf', 32)
titleMessage = font.render("Final Penalty Shootout", True, (0, 255, 0), (0, 0, 128))
titleRect = titleMessage.get_rect()
titleRect.center = (400, 300)




while running: #as long as running is true
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #running is changed to False, meaning this loop stops

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # screen.blit(titleMessage, titleRect)

    # flip() the display to put your work on screen
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000


pygame.quit()