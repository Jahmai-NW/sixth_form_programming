import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Penalty Shootout")
clock = pygame.time.Clock()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 500 * dt
    if keys[pygame.K_s]:
        player_pos.y += 500 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 500 * dt
    if keys[pygame.K_d]:
        player_pos.x += 500 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000



class Player():
    #private username
    #private HighScore

    def __init__(self, theUsername, theHighScore):
        self.username = theUsername
        self.highScore = theHighScore

    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username

    def setHighScore(self, highScore):
        self.highScore = highScore

    def getHighScore(self):
        return self.highScore







class PenaltyTaker():
    #private background
    #private totalScore
    #private shotDirection

    def __init__(self, theTotalScore, theShotDirection):
        self.totalScore = theTotalScore
        self.shotDirection = theShotDirection

    def getTotalScore(self, totalScore):
        self.totalScore = totalScore

    def setTotalScore(self):
        return self.totalScore

    def setShotDirection(self, shotDirection):
        self.shotDirection = theShotDirection

    def getShotDirection(self):
        return self.shotDirection


class Goalkeeper():
    #private background
    #private totalScore
    #private diveDirection

    def __init__(self, theTotalScore, theDiveDirection):
        self.totalScore = theTotalScore
        self.theDiveDirection = theDiveDirection


class MainGame():
    #private buttons (to track placement of buttons on the screen)
    #private background
    #private totalScore
    #private 
    None


class Button():
    #private text
    #private x
    #private y
    #private width
    #private height
    None




class MainMenuPanel():
    #private buttons
    #private background
    None


class SettingsPanel():
    #private buttons
    #private background
    None


class CustomisationPanel():
    #private buttons
    #private background
    None


class InstructionsPanel():
    #private buttons
    #private background
    None


class ViewScorePanel():
    #private buttons
    #private background
    None



pygame.quit()
quit()