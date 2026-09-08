import pygame

pygame.init() #initiates pygame module
screen = pygame.display.set_mode((1000, 600)) #establishes the size of the screen to be displayed

pygame.display.set_caption("Final Penalty Shootout") #establishes the text to be displayed as the caption of the screen

clock = pygame.time.Clock() #creates a clock object which keeps track of time
running = True #running set to true


titlePanel = pygame.Surface((200, 600)) #creates a new surface object with the specified size (200, 600) which can be used to draw on and display on the screen
font = pygame.font.Font('freesansbold.ttf', 50) #creates a font object with the specified font file and size
titleMessage = font.render("Final Penalty Shootout", True, 	(18, 70, 45), (255, 215, 60)) #creates a text message to be displayed on the screen, with the text "Final Penalty Shootout", in colour (18, 70, 45) with a background colour of (255, 215, 60)
titleRect = titleMessage.get_rect() #this gets the rectangular area of the title message
titleRect.center = (400, 50) #coordinates of the center of the title message

mainMenuPanel = pygame.Surface((400, 300)) #creates a new surface object with the specified size (400, 300) which can be used to draw on and display on the screen
font = pygame.font.Font('freesansbold.ttf', 32) #creates a font object with the specified font file and size
mainMenuMessage = font.render("Main Menu", True, (0, 255, 0), (255, 255, 255)) #creates a text message to be displayed on the screen, with the text "Main Menu", in green colour (0, 255, 0) with a background colour of blue (0, 0, 128)
mainMenuRect = mainMenuMessage.get_rect() #this gets the rectangular area of the main menu message
mainMenuRect.center = (400, 150) #coordinates of the center of the main menu message

settingsPanel = pygame.Surface((400, 200)) #creates a new surface object with the specified size (400, 200) which can be used to draw on and display on the screen
font = pygame.font.Font('freesansbold.ttf', 32) #creates a font object with the specified font file and size
settingsMessage = font.render("Settings", True, (0, 255, 0), (255, 255, 255)) #creates a text message to be displayed on the screen, with the text "Settings", in green colour (0, 255, 0) with a background colour of blue (0, 0, 128)
settingsRect = settingsMessage.get_rect() #this gets the rectangular area of the settings message
settingsRect.center = (400, 300) #coordinates of the center of the settings message


while running: #as long as running is true
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #running is changed to False, meaning this loop stops

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((18, 70, 45)) #fills the screen with a color (18, 70, 45) which is a shade of green (may be changed to a different color later)

<<<<<<< HEAD
    screen.blit(titleMessage, titleRect)
    screen.blit(mainMenuMessage, mainMenuRect)
=======
    # screen.blit(titleMessage, titleRect)
>>>>>>> 5f220477e1400c4396539d8ba6b3bda7a384f482

    # flip() the display to put your work on screen
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000


pygame.quit()