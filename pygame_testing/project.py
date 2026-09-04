import pygame

# pygame.init()
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Penalty Shootout")
# clock = pygame.time.Clock()




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
    #private diveButton
    #private diveDirection


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



class SettingsPanel():
    #private buttons
    #private background


class CustomisationPanel():
    #private buttons
    #private background

class InstructionsPanel():
    #private buttons
    #private background


class ViewScorePanel():
    #private buttons
    #private background



pygame.quit()