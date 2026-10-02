import pygame

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


class ButtonCreation():
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
        self.font = pygame.font.Font('freesansbold.ttf', 25)

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




    # --- TEXTBOX STATE ---
textbox_rect = pygame.Rect(100, 100, 200, 32)
textbox_active = False
textbox_text = ""
textbox_color_inactive = pygame.Color('lightskyblue3')
textbox_color_active = pygame.Color('dodgerblue2')
textbox_color = textbox_color_inactive

def handle_textbox_event(event):
    global textbox_active, textbox_text, textbox_color

    if event.type == pygame.MOUSEBUTTONDOWN:
        if textbox_rect.collidepoint(event.pos):
            textbox_active = True
        else:
            textbox_active = False
        textbox_color = textbox_color_active if textbox_active else textbox_color_inactive

    if event.type == pygame.KEYDOWN and textbox_active:
        if event.key == pygame.K_RETURN:
            global currentUserName
            currentUserName = ""
            
            print(textbox_text)
            currentUserName = textbox_text
            textbox_text = ""
              
        elif event.key == pygame.K_BACKSPACE:
            textbox_text = textbox_text[:-1]
        else:
            textbox_text += event.unicode


def draw_textbox(screen):
    font = pygame.font.Font(None, 32)
    # Render text
    txt_surface = font.render(textbox_text, True, textbox_color)

    # Resize box if needed
    textbox_rect.w = max(200, txt_surface.get_width() + 10)

    # Draw text + box
    screen.blit(txt_surface, (textbox_rect.x + 5, textbox_rect.y + 5))
    pygame.draw.rect(screen, textbox_color, textbox_rect, 2)
