
import pygame
from utils._utils import drawBlinkingText,countDownTimer,scrollingDilaogue,imageAnimateAdvanced,scrollingDialogueSimple

#  LOADS ONLY THE INCOMING NOTIFICATION, AND CANVAS


class cutScene():
	def __init__(self,gui):
		self.state          = None
		self.themes         = {'ally': (49,105,213) , 'enemy': (150,20,20), 'neutral':(0,200,0)}
		self.theme          = self.themes['ally']
		self.orientation    = 'topCenter'
		self.orientationSet = False 

		# TOP CENTER ORIENTATION DEFAULT DIMENSIONS
		self.x            = 0.25*gui.w
		self.y            = 1
		self.w 		      = 0.5*gui.w
		self.h 		      = 0.26 *gui.h
		#  MESSAGE X,Y FOR INCOMING ALERT
		self.incomingX    = self.x + 0.3*self.w
		self.incomingY    = self.y + 0.45*self.h
		# WHERE THE LEFT PICTURE IS SHOWN
		self.imageLeftX = self.x + 0.05*self.w
		self.imageY     = self.y + 10

		# OPENING SFX 
		self.openingTimer = countDownTimer()
		self.msgFlashtime = 3







		# STATE 
		self.pannelOpen     = False
		self.openingMessage = False
		self.wOpening       = 0
		self.hOpening       = 0


		# TEXT 
		#self.dialogue       = scrollingDilaogue(gui,self.x,self.y,self.w,self.h,self.theme)
		self.dialogue       = scrollingDialogueSimple()
		self.backColour     = (0,0,0)

		# LEFT SIDE
		self.textX          = self.x + 0.4*self.w
		self.textY          = self.y + 0.11* self.h
		self.textW  		= 0.5*self.w
		self.textH          = 0.6*self.h


		# CODEC MASK
		self.codec             = imageAnimateAdvanced(gui.allyCodec,0.3)
		self.enemyCodec        = imageAnimateAdvanced(gui.enemyCodec,0.3)
		self.transMaskAlpha   = 100
		self.transMask        = pygame.Surface((220,195))


		#REINFORCEMENTS  

		self.notifyReinforcements = False 
		self.reinforcementTimer = countDownTimer()
		self.reinforcmentTime   = 4
		self.rx            = 0.3*gui.w
		self.ry            = 0.03*gui.h
		self.rw 		   = 0.4*gui.w
		self.rh 		   = 0.1 *gui.h
		self.rxText        = self.rx + 0.15*self.rw
		self.ryText        = self.ry + 0.35*self.rh

		
	#----------------------------------------
	# OPENS DIALOGUE WINDOW, 
	#----------------------------------------
	def runCutScene(self,gui,game,scene='ally',underlay=True,orientation='topCenter'):

		# --------OPENING SFX
		self.theme = self.themes[scene]

		# -------GET DIMENSIONS
		if(self.orientationSet==False):
			self.orientation = orientation
			self.getOrientationDimensions(gui)
			self.orientationSet = True



		# -----------EXPAND PANNEL TO OPEN UP

		if(self.pannelOpen==False and self.openingMessage==False):
			pygame.draw.rect(gui.screen, (0,0,0), [self.x,self.y,self.wOpening,self.hOpening])
			pygame.draw.rect(gui.screen, self.theme, [self.x,self.y,self.wOpening,self.hOpening],3)
			if(self.wOpening<= self.w): self.wOpening += self.w/25
			if(self.hOpening<= self.h): self.hOpening += self.h/25

			if(self.wOpening>= self.w and self.hOpening>=self.h):
				self.openingMessage=True
		
		# -----------FTL REQUEST MESSAGE

		elif(self.pannelOpen==False and self.openingMessage):
			pygame.draw.rect(gui.screen, (0,0,0), [self.x,self.y,self.w,self.h])
			pygame.draw.rect(gui.screen, self.theme, [self.x,self.y,self.w,self.h],4)
			drawBlinkingText(gui.screen,gui.font, 'FTL Message Request',self.incomingX,self.incomingY, colour=(self.theme),blinkFraction=0.5)
			complete,timeRemaining = self.openingTimer.countDownReal(self.msgFlashtime,game)
			if(complete):
				self.pannelOpen           = True # opening animation complete
				self.openingTimer.counter = None # reset


		else:
			# ---------- DRAW CANVAS ONLY 
			pygame.draw.rect(gui.screen, (0,0,0), [self.x,self.y,self.w,self.h])
			pygame.draw.rect(gui.screen, self.theme, [self.x,self.y,self.w,self.h],3)
			if(scene=='ally'):
				gui.screen.blit(gui.allyUnderlay, (self.imageLeftX,self.imageY))


	#----------------------------------------
	# IMAGE MASK, CODEC AND BORDER
	#----------------------------------------


	def runRHSCutScene(self,gui,game,scene='ally',underlay=True,orientation='topRight'):

		# --------OPENING SFX
		self.theme = self.themes[scene]

		# -------GET DIMENSIONS
		if(self.orientationSet==False):
			self.orientation = orientation
			self.getOrientationDimensions(gui)
			self.orientationSet = True

		# -----------EXPAND PANNEL TO OPEN UP

		if(self.pannelOpen==False and self.openingMessage==False):
			pygame.draw.rect(gui.screen, self.backColour, [self.x,self.y,self.wOpening,self.hOpening])
			pygame.draw.rect(gui.screen, self.theme, [self.x,self.y,self.wOpening,self.hOpening],3)
			if(self.wOpening<= self.w): self.wOpening += self.w/25
			if(self.hOpening<= self.h): self.hOpening += self.h/25

			if(self.wOpening>= self.w and self.hOpening>=self.h):
				self.openingMessage=True
		
		# -----------FTL REQUEST MESSAGE

		elif(self.pannelOpen==False and self.openingMessage):
			pygame.draw.rect(gui.screen, self.backColour, [self.x,self.y,self.w,self.h])
			pygame.draw.rect(gui.screen, self.theme, [self.x,self.y,self.w,self.h],4)
			drawBlinkingText(gui.screen,gui.font, 'FTL Message Request',self.incomingX,self.incomingY, colour=(self.theme),blinkFraction=0.5)
			complete,timeRemaining = self.openingTimer.countDownReal(self.msgFlashtime,game)
			if(complete):
				self.pannelOpen           = True # opening animation complete
				self.openingTimer.counter = None # reset


		else:
			# ---------- DRAW CANVAS ONLY 
			pygame.draw.rect(gui.screen, self.backColour, [self.x,self.y,self.w,self.h])
			pygame.draw.rect(gui.screen, self.theme, [self.x,self.y,self.w,self.h],3)
			if(scene=='ally'):
				gui.screen.blit(gui.allyUnderlay, (self.imageLeftX,self.imageY))


	def drawMask(self,gui,game,overlay=True,codec=True,border=None,mask='ally'):
		

		# --------OVERLAY 

		if(overlay):
			self.transMask.set_alpha(self.transMaskAlpha)
			self.transMask.fill((0,0,150))
			gui.screen.blit(self.transMask, (self.imageLeftX,self.imageY))

		# --------CODEC ANIMATION

		if(codec):
			if(mask=='ally'):
				self.codec.animate(gui,'character mask',[self.imageLeftX,self.imageY],game)
			elif(mask=='enemy'):
				self.enemyCodec.animate(gui,'enemy mask',[self.imageLeftX,self.imageY],game)

		#--------BLIT BORDER 

		if(border!=None):
			if(border=='ally'):
				gui.screen.blit(gui.allyBorder, (self.imageLeftX,self.imageY))
			elif(border=='enemy'):
				gui.screen.blit(gui.enemyBorder, (self.imageLeftX,self.imageY))


	def specialNotification(self,gui,game):
		if(self.pannelOpen==False):
			if(self.notifyReinforcements):
				pygame.draw.rect(gui.screen, (0,0,0), [self.rx,self.ry,self.rw,self.rh])
				pygame.draw.rect(gui.screen, self.theme, [self.rx,self.ry,self.rw,self.rh],4)
				drawBlinkingText(gui.screen,gui.font, 'ReInfocements have Arrived',self.rxText,self.ryText, colour=(self.theme),blinkFraction=0.5)
				complete,timeRemaining = self.reinforcementTimer.countDownReal(self.reinforcmentTime,game)
				if(complete):
					self.notifyReinforcements = False
					self.reinforcementTimer.counter = None # reset


	def getOrientationDimensions(self,gui):
		if(self.orientation=='topCenter'):
			# TOP CENTER ORIENTATION DEFAULT DIMENSIONS
			self.x            = 0.25*gui.w
			self.y            = 1
			self.w 		      = 0.5*gui.w
			self.h 		      = 0.26 *gui.h
			#  MESSAGE X,Y FOR INCOMING ALERT
			self.incomingX    = self.x + 0.3*self.w
			self.incomingY    = self.y + 0.45*self.h
			# WHERE THE LEFT PICTURE IS SHOWN
			self.imageLeftX = self.x + 0.05*self.w
			self.imageY     = self.y + 10

			self.textX          = self.x + 0.4*self.w
			self.textY          = self.y + 0.11* self.h
			self.textW  		= 0.5*self.w
			self.textH          = 0.6*self.h
			self.backColour     = (0,0,0)


		if(self.orientation=='topRight'):
			self.x            = 0.84*gui.w
			self.y            = 0.26 *gui.h
			self.w 		      = 0.15*gui.w
			self.h 		      = 0.19 *gui.h
			self.incomingX    = self.x + 0.3*self.w
			self.incomingY    = self.y + 0.45*self.h
			
			self.imageLeftX   = self.x
			self.imageY       = 10
			self.msgFlashtime = 1


			self.textX          = self.x + 0.06*self.w
			self.textW  		= 0.85*self.w
			self.textY          = self.y + 0.07* self.h
			self.textH          = 0.6*self.h

			self.backColour     = (34,45,65)



	def reset(self):
		self.pannelOpen     = False
		self.orientationSet = False
