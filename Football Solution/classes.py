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
        self.shotDirection = shotDirection

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
    #private colour
    #private hoverColour

    def __init__(self, x, y, width, height, text, colour, hover_colour):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text 
        self.colour = colour
        self.hover_colour = hover_colour
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_colour, self.rect)
        else:
            pygame.draw.rect(screen, self.colour, self.rect)

        text_surf = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surf, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]
        return self.rect.collidepoint(mouse_pos) and mouse_click

    




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
