import pygame #imports the pygame module
import sys #imports the sys module
from classes import * #imports all classes from the classes.py file

pygame.init() #initiates pygame module
screen = pygame.display.set_mode((1000, 600)) #establishes the size of the screen to be displayed

pygame.display.set_caption("Final Penalty Shootout") #establishes the text to be displayed as the caption of the screen

clock = pygame.time.Clock() #creates a clock object which keeps track of time
running = True #running set to true



titlePanel = pygame.Surface((500, 600)) #creates a new surface object with the specified size (500, 600) which can be used to draw on and display on the screen
font = pygame.font.Font('freesansbold.ttf', 50) #creates a font object with the specified font file and size
titleMessage = font.render("Final Penalty Shootout", True, 	(18, 70, 45), (255, 215, 60)) #creates a text message to be displayed on the screen, with the text "Final Penalty Shootout", in colour (18, 70, 45) with a background colour of (255, 215, 60)
titleRect = titleMessage.get_rect() #this gets the rectangular area of the title message
titleRect.center = (500, 45) #coordinates of the center of the title message

mainMenuPanel = pygame.Surface((500, 400)) #creates a new surface object with the specified size (500, 400) which can be used to draw on and display on the screen
font = pygame.font.Font('freesansbold.ttf', 35) #creates a font object with the specified font file and size
mainMenuMessage = font.render("Main Menu", True, (0, 255, 0), (10, 26, 47)) #creates a text message to be displayed on the screen, with the text "Main Menu", 
mainMenuRect = mainMenuMessage.get_rect() #this gets the rectangular area of the main menu message
mainMenuRect.center = (500, 110) #coordinates of the center of the main menu message


newGameButton = ButtonCreation(400, 200, 200, 50, "   New Game", (255, 195, 0), (0, 128, 128)) #creates a new button object with the specified position (500, 300), size (400, 200), text "New Game", colour (0, 255, 0) and hover colour (0, 128, 128)

loadGameButton = ButtonCreation(400, 255, 200, 50, "   Load Game", (255, 195, 0), (0, 128, 128))

customisationButton = ButtonCreation(400, 310, 200, 50, "Customisation", (255, 195, 0), (0, 128, 128))

instructionsButton = ButtonCreation(400, 365, 200, 50, "  Instructions", (255, 195, 0), (0, 128, 128))

viewScoresButton = ButtonCreation(400, 420, 200, 50, "  View Scores", (255, 195, 0), (0, 128, 128))

settingsButton = ButtonCreation(400, 475, 200, 50, "     Settings", (255, 195, 0), (0, 128, 128))

quitButton = ButtonCreation(800, 500, 100, 50, "  Quit", (10, 26, 47), (212, 162, 0))

#############################################################################

def settingsScreen():
    screen.fill((18, 70, 45))

def customisationScreen():
    while True:

        screen.fill((18, 70, 45))
        pygame.display.update()

def instructionsScreen():
    screen.fill((18, 70, 45))
    pygame.display.update()


################################################################################




while running: #as long as running is true
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #running is changed to False, meaning this loop stops


        if newGameButton.is_clicked():
            print("New Game button clicked!")

        if loadGameButton.is_clicked():
            print("Loading Previous Slot....")

        if customisationButton.is_clicked():
            print("Choose a team!")
            # customisationScreen()

        if instructionsButton.is_clicked():
            print("Instructions instructions...")
            # instructionsScreen()

        if viewScoresButton.is_clicked():
            print("Change whatever you want!")
            # viewScoresScreen()

        if settingsButton.is_clicked():
            print("Settings!")
            # settingsScreen()

        if quitButton.is_clicked():
            running = False

    # fill the screen with a color to wipe away anything from last frame
        screen.fill((199, 0, 57)) #fills the screen with a color
    
    mouse_pos = pygame.mouse.get_pos()  # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse_click = pygame.mouse.get_pressed()[0]

    screen.blit(titleMessage, titleRect)
    screen.blit(mainMenuMessage, mainMenuRect)

    newGameButton.draw(screen)
    loadGameButton.draw(screen)
    customisationButton.draw(screen)
    instructionsButton.draw(screen)
    viewScoresButton.draw(screen)
    settingsButton.draw(screen)
    quitButton.draw(screen)


    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000


pygame.quit()