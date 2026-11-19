import os
import pygame
import classes
from classes import (Player, Background, ButtonCreation, PenaltyTaker, draw_textbox, handle_textbox_event)

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Final Penalty Shootout")
clock = pygame.time.Clock()
newPlayer = Player(classes.currentUserName, 0, None)

# Backgrounds
mainMenuBG = Background("Images/main_menu.jpg", 1000, 600)
penaltyBG = Background("Images/penalty_background.jpg", 1000, 600)
customisationMenuBG = Background("Images/custMenu.jpg", 1000, 600)
newGameMenuBG = Background("Images/celebration.jpg", 1000, 600)

# Celebration Images
scoredImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Images", "scoredImage.jpg")
scoredBG = pygame.image.load(scoredImagePath).convert_alpha()
scoredBG = pygame.transform.scale(scoredBG, (1000, 600))

missedImagePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Images", "missImage.jpg")
missedBG = pygame.image.load(missedImagePath).convert_alpha()
missedBG = pygame.transform.scale(missedBG, (1000, 600))

# Ball image
ball_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Images", "ball.png")
ballImage = pygame.image.load(ball_path).convert_alpha()
ballImage = pygame.transform.scale(ballImage, (35, 35))

# Main menu title
titleFont = pygame.font.Font("freesansbold.ttf", 70)
titleMessage = titleFont.render("Final Penalty Shootout", True, (255, 215, 60), (168, 33, 32))
titleRect = titleMessage.get_rect(center=(500, 45))

mainMenuFont = pygame.font.Font("freesansbold.ttf", 40)
mainMenuMessage = mainMenuFont.render("Main Menu", True, (64, 170, 157), (168, 33, 32))
mainMenuRect = mainMenuMessage.get_rect(center=(500, 110))

# Other screen titles
creditsFont = pygame.font.Font("freesansbold.ttf", 50)
creditsTitle = creditsFont.render("Credits", True, (235, 235, 235), (18, 18, 22))
creditsTitleRect = creditsTitle.get_rect(center=(500, 45))

messageFont = pygame.font.Font("freesansbold.ttf", 20)
creditsMessage1 = messageFont.render("made by THE big J, Jahmai of course. big up Ms Lassami!", True, (255, 255, 255), (120, 0, 35),)
credits1Rect = creditsMessage1.get_rect(center=(500, 300))

customisationFont = pygame.font.Font("freesansbold.ttf", 60)
customisationTitle = customisationFont.render("Customisation", True, (235, 235, 235), (11, 73, 127))
customisationTitleRect = customisationTitle.get_rect(center=(500, 45))

welcomeFont = pygame.font.Font("freesansbold.ttf", 45)

# Buttons
newGameButton = ButtonCreation(400, 200, 200, 50, "   New Game", (255, 195, 0), (0, 128, 128))
loadGameButton = ButtonCreation(400, 255, 200, 50, "   Load Game", (255, 195, 0), (0, 128, 128))

customisationButton = ButtonCreation(
    400, 310, 200, 50, "Customisation", (255, 195, 0), (0, 128, 128)
)
instructionsButton = ButtonCreation(
    400, 365, 200, 50, "  Instructions", (255, 195, 0), (0, 128, 128)
)
viewScoresButton = ButtonCreation(
    400, 420, 200, 50, "  View Scores", (255, 195, 0), (0, 128, 128)
)
settingsButton = ButtonCreation(
    400, 475, 200, 50, "     Settings", (255, 195, 0), (0, 128, 128)
)
quitButton = ButtonCreation(
    800, 500, 100, 50, "  Quit", (10, 26, 47), (212, 162, 0)
)
backtoMainMenuButton = ButtonCreation(
    600, 525, 300, 50, "Back to Main Menu", (10, 26, 47), (212, 162, 0)
)
custbacktoMainMenuButton = ButtonCreation(
    370, 525, 260, 50, "Back to Main Menu", (10, 26, 47), (212, 162, 0)
)
creditsButton = ButtonCreation(
    100, 500, 120, 50, "Credits", (10, 26, 47), (212, 162, 0)
)

team1CustomButton = ButtonCreation(
    100, 110, 200, 40, "Team 1", (104, 178, 17), (47, 159, 221)
)
team2CustomButton = ButtonCreation(
    700, 110, 200, 40, "Team 2", (104, 178, 17), (47, 159, 221)
)
team3CustomButton = ButtonCreation(
    100, 320, 200, 40, "Team 3", (104, 178, 17), (47, 159, 221)
)
team4CustomButton = ButtonCreation(
    700, 320, 200, 40, "Team 4", (104, 178, 17), (47, 159, 221)
)

penaltyTakerGameButton = ButtonCreation(
    400, 300, 200, 50, "Start Game", (255, 195, 0), (0, 128, 128)
)

goalkeeperGameButton = ButtonCreation(
    400, 300, 200, 50, "Start Game", (255, 195, 0), (0, 128, 128)
)

penaltyTaker = PenaltyTaker(0, "")


def clicked(button, event):
    #returns True when left mouse button clicked
    return (
        event.type == pygame.MOUSEBUTTONDOWN
        and event.button == 1
        and button.rect.collidepoint(event.pos)
    )


# Drawing functions

def draw_main_menu():
    mainMenuBG.render(screen)
    screen.blit(titleMessage, titleRect)
    screen.blit(mainMenuMessage, mainMenuRect)

    newGameButton.draw(screen)
    loadGameButton.draw(screen)
    customisationButton.draw(screen)
    instructionsButton.draw(screen)
    viewScoresButton.draw(screen)
    settingsButton.draw(screen)
    quitButton.draw(screen)
    creditsButton.draw(screen)
    draw_textbox(screen)


def draw_new_gamePENALTYTAKER():
    # screen.fill((18, 70, 45))
    newGameMenuBG.render(screen)

    welcomeMessage = welcomeFont.render(
        f"Welcome {classes.currentUserName}, you play for {newPlayer.selectedTeam}",
        True,
        (235, 235, 235),
        (11, 73, 127),
    )
    welcomeRect = welcomeMessage.get_rect(center=(500, 100))
    screen.blit(welcomeMessage, welcomeRect)

    penaltyTakerGameButton.draw(screen)
    backtoMainMenuButton.draw(screen)


def draw_penalty_shootout():
    penaltyBG.render(screen)
    penaltyTaker.updateBall()

    ballRect = ballImage.get_rect(
        center=(penaltyTaker.ballX, penaltyTaker.ballY)
    )
    screen.blit(ballImage, ballRect)


def draw_customisation():
    # screen.fill((11, 73, 127))
    customisationMenuBG.render(screen)
    
    screen.blit(customisationTitle, customisationTitleRect)

    team1CustomButton.draw(screen)
    team2CustomButton.draw(screen)
    team3CustomButton.draw(screen)
    team4CustomButton.draw(screen)
    custbacktoMainMenuButton.draw(screen)


def draw_settings():
    screen.fill((18, 70, 45))
    backtoMainMenuButton.draw(screen)


def draw_instructions():
    screen.fill((18, 70, 45))
    backtoMainMenuButton.draw(screen)


def draw_view_scores():
    screen.fill((18, 70, 45))
    backtoMainMenuButton.draw(screen)


def draw_credits():
    screen.fill((18, 18, 22))
    screen.blit(creditsTitle, creditsTitleRect)
    screen.blit(creditsMessage1, credits1Rect)
    backtoMainMenuButton.draw(screen)


def draw_current_screen():
    if current_screen == "main_menu":
        draw_main_menu()
    elif current_screen == "create_new_game":
        draw_new_gamePENALTYTAKER()
    elif current_screen == "penalty_shootout":
        draw_penalty_shootout()
    elif current_screen == "customisation":
        draw_customisation()
    elif current_screen == "settings":
        draw_settings()
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "view_scores":
        draw_view_scores()
    elif current_screen == "credits":
        draw_credits()


running = True
current_screen = "main_menu"

while running:
    for event in pygame.event.get():
        handle_textbox_event(event)

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if current_screen == "main_menu":
                if clicked(newGameButton, event):
                    current_screen = "create_new_game"
                elif clicked(loadGameButton, event):
                    print("Loading Previous Slot....")
                elif clicked(customisationButton, event):
                    current_screen = "customisation"
                elif clicked(instructionsButton, event):
                    current_screen = "instructions"
                elif clicked(viewScoresButton, event):
                    current_screen = "view_scores"
                elif clicked(settingsButton, event):
                    current_screen = "settings"
                elif clicked(creditsButton, event):
                    current_screen = "credits"
                elif clicked(quitButton, event):
                    running = False

            elif current_screen == "create_new_game":
                if clicked(penaltyTakerGameButton, event):
                    current_screen = "penalty_shootout"
                elif clicked(backtoMainMenuButton, event):
                    current_screen = "main_menu"

            elif current_screen == "penalty_shootout":
                if penaltyTaker.ballMoving == False:
                    selectedShot = penaltyTaker.selectShot(event.pos)
                    if selectedShot != None:
                        print("Player selected:", selectedShot)
                        if selectedShot == "Middle Centre":
                            scoredBG.blit(screen)


            elif current_screen == "customisation":
                if clicked(custbacktoMainMenuButton, event):
                    current_screen = "main_menu"

                elif clicked(team1CustomButton, event):
                    print("Team 1 has been chosen!")
                    newPlayer.setSelectedTeam("Team 1")

                elif clicked(team2CustomButton, event):
                    print("Team 2 has been chosen!")
                    newPlayer.setSelectedTeam("Team 2")

                elif clicked(team3CustomButton, event):
                    print("Team 3 has been chosen!")
                    newPlayer.setSelectedTeam("Team 3")

                elif clicked(team4CustomButton, event):
                    print("Team 4 has been chosen!")
                    newPlayer.setSelectedTeam("Team 4")

            elif current_screen in (
                "settings",
                "instructions",
                "view_scores",
                "credits",
            ):
                if clicked(backtoMainMenuButton, event):
                    current_screen = "main_menu"

    draw_current_screen()
    pygame.display.update()
    clock.tick(120)

pygame.quit()

#if player scores, image pops up, time limiot