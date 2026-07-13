while True:
    if newSFX != currentSFX: # if the newSFX pointer is not equal to the currentSFX pointer
        newSFX = currentSFX # currentSFX pointer is set to newSFX pointer
    endif

    if newVolume != currentVolume: # if the newVolume pointer is not equal to currrentVolume pointer
        newVolume = currentVolume # currentVolume pointer set to newVolume pointer
    endif   

    if newBrightness != currentBrightness: # if newBrightness pointer is not equal to currentBrightness pointer
        newBrightness = currentBrightness # currentBrightness pointer set to newBrightness pointer
    endif

    if saveprogress.getpressed(): # if button linked to saveprogress is clicked, SaveSlotDisplay() function will run
        SaveSlotDisplay()
    endif

    if backToMenu.getpressed(): # if button linked to backToMenu is clicked, backToMenu() function will run
        MainMenu()
    endif

    
    