
import pygame
import time
import math
import random
import json
import os, sys
from utils.utils import gui

#--------------SETUP--------------------

width, height  = 1500 ,850                 # Can be adjusted
FPS            = 90                        # Frame rate

pygame.init()
pygame.display.set_caption("My Cool Game")
clock          = pygame.time.Clock()
nextFrame      = pygame.time.get_ticks()
monitorSize    = [pygame.display.Info().current_w,pygame.display.Info().current_h]
screen         = pygame.display.set_mode((width,height),pygame.DOUBLEBUF)
ASSETPATH      = 'assets/'

#--------------SETTING A GUI OBJECT--------------------

gui                   = gui(screen,width,height,guiTheme, ASSETPATH=ASSETPATH)
gui.font              = pygame.font.Font(ASSETPATH + '/Orbitron-Regular.ttf', 25)
gui.claireTalking     = imageAnimateAdvanced(talkFrames,0.2)
gui.clareSmiling      = imageAnimateAdvanced(gui.claireSmileFrames,0.2)


gui.allyCodec         = loadImageFiles('allyCodec1.png',ASSETPATH + 'mask/')
gui.enemyCodec        = loadImageFiles('enemyCodec1.png',ASSETPATH + 'mask/')
gui.allyBorder        = pygame.image.load(ASSETPATH + 'mask/maskAlly.png')
gui.enemyBorder       = pygame.image.load(ASSETPATH + 'mask/maskEnemy.png')

gui.allyUnderlay      = pygame.image.load(ASSETPATH + 'mask/allyUnderlay.png')
gui.enemyUnderlay     = pygame.image.load(ASSETPATH + 'mask/enemyUnderlay.png')








# -----ALL VARIABLES & CLASSES IMPORTED FROM SETUP


while game.running:

	# -------------NEXT CYCLE 

    game.itercount                +=1                          # INCREMENT LOOP COUNT
    gui.resetMouseInputs()
    gui.screen.fill((0, 0, 0))                                 # DRAW BLACK BG
    user_input.returnedKey =''
    gui.mx, gui.my = pygame.mouse.get_pos()

    

    # -------------PROCESS STANDARD INPUT EVENTS

    for event in pygame.event.get():
        pos            = pygame.mouse.get_pos()
        if event.type == pygame.QUIT: game.running = False

        if pygame.mouse.get_pressed()[0]:
            gui.pressed = True

        
        if(event.type==pygame.MOUSEBUTTONUP):
            gui.pressed = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if(event.button==1):
                gui.clicked  = True
            if(event.button==3):
                gui.rightClicked = True
            
            if(event.button==4):
                gui.scrollUp  = True
            if(event.button==5):
                gui.scrollDown = True
                
        
        gui.input              = user_input.getButtonInputs(event)

    gui.mx, gui.my             = pygame.mouse.get_pos()        # GET MOUSE POS

    
    # -----------MANAGE EVENTS EXAMPLE



	if(game.scene=='claire'):
		game.pauseGame = True

		# OPEN WINDOW
		game.cutScene.runCutScene(gui,game,scene='ally',underlay=True)


		# ANIMATE ONCE WINDOW OPEN
		if(game.cutScene.pannelOpen):
			gui.claireTalking.animateNoRotation(gui,'claireTalking',[game.cutScene.imageLeftX,game.cutScene.imageY],game)
			game.cutScene.drawMask(gui,game,overlay=False,border='ally',codec=True)
			finished = game.cutScene.dialogue.drawScrollingDialogue(gui,game,game.cutScene.textW,game.cutScene.textH,gui.smallishFont, "Welcome to training rookie, time to learn the ropes. You have a number of air, land and sea targets. Get going, good luck. Remember you will go into automatic lockon mode which changes your button inputs, press y to toggle lockon on and off.", textStartingPos=(game.cutScene.textX ,game.cutScene.textY),colour=(255,255,255),closeOutDelay=True)
			if(finished):
				game.scene    ='gameUnderway'
				game.pauseGame = False
				game.cutScene.reset()



    # Flip the display
    pygame.display.flip() 
    
    # TICK

    game.dt           = clock.tick(game.FPS)     # GET TIME INCREMENT
    game.elapsed     += game.dt/1000        # UPDATE TIME ELAPSED
    continue



pygame.quit()   # END GAME WHEN LOOP EXITS










