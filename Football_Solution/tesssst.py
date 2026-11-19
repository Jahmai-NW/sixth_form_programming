# --- Libraries --- #

# Import pygame
import pygame

# INITialize pygame


pygame.init() 
# --- Window & Cursor --- #

# Open a WINDOW of size [500, 300]
window=pygame.display.set_mode([500,300]) 

# SET_VISIBLE of cursor to False
pygame.mouse.set_visible(False) 
# Set the variable cursor_size to 10
cursor_size=10


#### ---- MAIN LOOP ---- ####
running=True 
# Create a variable called running with value True
while running: 

# Loop while running



    # --- Event Loop --- #

    # Create an EVENT LOOP
    for event in pygame.event.get(): 

        # Check for the QUIT event
        if event.type==pygame.QUIT: 
            running=False 

            # Set running to False
            # ---> TEST AFTER THIS LINE <--- #



        # --- The cursor increases size while clicking --- #

        # Check if the event TYPE is MOUSEBUTTONDOWN

        if event.type==pygame.MOUSEBUTTONDOWN: 
            cursor_size=20
            # Set cursor_size to 20
            # ---> TEST AFTER THIS LINE <--- #


        # Otherwise if the event TYPE is MOUSEBUTTONUP
        elif event.type==pygame.MOUSEBUTTONUP: 
            cursor_size=10
        
 


    # GET_POSition of mouse and store it in x, y
    x,y=pygame.mouse.get_pos() 
    # ---> TEST AFTER THIS LINE <--- #



    # --- Draw --- #

    # FILL the window with WHITE
    window.fill((215,158,222)) 


    # Draw a CIRCLE of any COLOR at position (x, y)
    # with cursor_size
    pygame.draw.circle(window,(255,255,255),(x,y),cursor_size,10) 


    # FLIP the display
    pygame.display.flip() 
    # ---> TEST AFTER THIS LINE <--- #