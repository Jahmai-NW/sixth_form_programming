import pygame
import os

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

    # Ball starting position
        self.ballX = 500 # Initial x-coordinate of the ball
        self.ballY = 540 # Initial y-coordinate of the ball

        # Ball destination
        self.targetX = 500 # Initial x-coordinate of the target destination
        self.targetY = 500 # Initial y-coordinate of the target destination

        self.ballMoving = False # Flag to indicate if the ball is moving

        # shooting zones represented as rectangles on the screen
        self.shotZones = {
            "Top Left": pygame.Rect(350, 150, 100, 100),
            "Top Centre": pygame.Rect(450, 150, 100, 100),
            "Top Right": pygame.Rect(550, 150, 100, 100),

            "Middle Left": pygame.Rect(350, 250, 100, 100),
            "Middle Centre": pygame.Rect(450, 250, 100, 100),
            "Middle Right": pygame.Rect(550, 250, 100, 100),

            "Bottom Left": pygame.Rect(350, 350, 100, 100),
            "Bottom Centre": pygame.Rect(450, 350, 100, 100),
            "Bottom Right": pygame.Rect(550, 350, 100, 100)
        }

    def setTotalScore(self, totalScore):
        self.totalScore = totalScore

    def getTotalScore(self):
        return self.totalScore

    def setShotDirection(self, shotDirection):
        self.shotDirection = shotDirection

    def getShotDirection(self):
        return self.shotDirection

    def selectShot(self, mousePosition): #function to select the shot direction based on the mouse position

        for zone, rectangle in self.shotZones.items(): #for every zone and rectangle in the shotZones dictionary, check if the mouse position is within the rectangle

            if rectangle.collidepoint(mousePosition): #if the mouse position is within the rectangle, set the shot direction to the zone and set the target position to the center of the rectangle

                self.shotDirection = zone #set the shot direction to the zone

                self.targetX = rectangle.centerx #set the target position to the center of the rectangle
                self.targetY = rectangle.centery #set the target position to the center of the rectangle

                self.ballMoving = True #set the ball moving flag to True, showing that the ball is moving towards the target position

                return zone #returns the zone that was selected based on the mouse position

        return None #returns None if no zone was selected

    def updateBall(self):

        if self.ballMoving:

            speed = 5

            if self.ballX < self.targetX:
                self.ballX = min(self.ballX + speed, self.targetX)

            elif self.ballX > self.targetX:
                self.ballX = max(self.ballX - speed, self.targetX)

            if self.ballY < self.targetY:
                self.ballY = min(self.ballY + speed, self.targetY)

            elif self.ballY > self.targetY:
                self.ballY = max(self.ballY - speed, self.targetY)

            if self.ballX == self.targetX and self.ballY == self.targetY:
                self.ballMoving = False


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
            pygame.draw.rect(screen, self.hover_colour, self.rect, width=5)
        else:
            pygame.draw.rect(screen, self.colour, self.rect, width=5)

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
currentUserName = ""
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
        textbox_color = textbox_color_active if textbox_active else textbox_color_inactive #textbox colour is determined if text_box is active or not

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


class Background:

    def __init__(self, image_file, world_width, world_height):

        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),image_file)
        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image, (world_width, world_height))
        self.rect = self.image.get_rect(topleft=(0, 0))

    #

    def render(self, screen):
        screen.blit(self.image, (0,0))