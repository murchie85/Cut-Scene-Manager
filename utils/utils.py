def drawBlinkingText(SCREEN,myfont, text,x,y, colour=(0, 128, 0),blinkFraction=0.5,fast=False):
    """ Center means giving the far x point """
    textsurface = myfont.render(text, True, colour)
    tw = textsurface.get_rect().width
    th = textsurface.get_rect().height

    if(not fast):
        if time.time() % 1 > blinkFraction:
            SCREEN.blit(textsurface,(x,y))
    else:
        if time.time() % 0.5 > 0.25:
            SCREEN.blit(textsurface,(x,y))

    return(tw,th)



class countDownTimer():
    def __init__(self):
        self.counter = None

    def countDownReal(self,count,game):
        if(self.counter==None): self.counter = count

        self.counter-=game.dt/1000
        if(self.counter<1):
            self.counter= None
            return(True,self.counter)

        return(False,self.counter)





# LOOPS THRU IMAGE REEL

class imageAnimateAdvanced():
    def __init__(self,imageFrames,changeDuration):
        self.frameTimer      = stopTimer()
        self.changeDuration  = changeDuration
        self.changeCount     = 0

        self.currentFrame    = 0
        self.imageFrames     = imageFrames
        self.reelComplete    = False

    def reset(self):
        self.currentFrame    = 0
        self.reelComplete    = False
        self.changeCount     = 0

    def animate(self,gui,trackedName,blitPos,game,rotation=None,centerOfRotation=(0.5,0.5),repeat=True,skipBlit=False):
        # TIMER THAT ITERATES THROUGH A FRAME EACH GIVEN INTERVAL
        changeFrame = self.frameTimer.stopWatch(self.changeDuration,trackedName, str(self.changeCount) + trackedName, game,silence=True)
        
        if(changeFrame):
            self.changeCount +=1
            self.currentFrame +=1
            if(self.currentFrame>=len(self.imageFrames)):
                if(repeat==False):
                    self.currentFrame = len(self.imageFrames)-1
                else:
                    self.currentFrame = 0
                self.reelComplete = True
            else:
                # LATE ADDITION MIGHT NEED ROLLED BACK
                self.reelComplete = False
        if(skipBlit):
            return(self.reelComplete,{})

        if(rotation==None): rotation = 0
        rotation = wrapAngle(rotation)

        # GET ORIGINAL AND ROTATED LEN AND WIDTH
        rotated_image = pygame.transform.rotate(self.imageFrames[self.currentFrame], rotation)
        rotatedWidth,rotatedHeight     = rotated_image.get_width(),rotated_image.get_height()
        imgW,imgH = self.imageFrames[self.currentFrame].get_width(), self.imageFrames[self.currentFrame].get_height()

        # GET MUTATED COORDINATES
        blitx,blity         = blitPos[0]+centerOfRotation[0]*(imgW-rotatedWidth),blitPos[1]+centerOfRotation[1]*(imgH-rotatedHeight)
        gui.screen.blit(rotated_image, (blitx,blity))



        # GET MUTATED COORDINATES
        midTopX,midTopY     = (blitPos[0]+0.5*imgW + imgW * 0.5*math.cos(wrapAngle(rotation+90)*math.pi/180),blitPos[1]+0.5*imgH  -imgH*0.5*math.sin(wrapAngle(rotation+90)*math.pi/180))
        # HORIZONTAL OFFSET OF MIDTOP
        offx = 30 * math.cos(math.radians(360-rotation))
        offy = 30 * math.sin(math.radians(360-rotation))
        rightTopX, rightTopY = midTopX + offx, midTopY + offy
        leftTopX, leftTopY   = midTopX - offx, midTopY - offy

        centerX,centerY   = (blitPos[0]+0.5*imgW + rotatedWidth*0.01*math.cos(wrapAngle(rotation+90)*math.pi/180),blitPos[1]+0.5*imgH -rotatedHeight*0.01*math.sin(wrapAngle(rotation+90)*math.pi/180))

        smallOx,smallOy = 20 * math.cos(math.radians(360-rotation)), 20 * math.sin(math.radians(360-rotation))
        centerRx,CenterRy = centerX + smallOx, centerY + smallOy
        centerLx,CenterLy = centerX - smallOx, centerY - smallOy

        behindX,behindY   = (blitPos[0]+0.5*imgW - imgW*1.3*math.cos(wrapAngle(rotation+90)*math.pi/180),blitPos[1]+0.5*imgH +imgH*1.3*math.sin(wrapAngle(rotation+90)*math.pi/180))
        

        #pygame.draw.circle(gui.screen, (220,100,100), (blitPos[0],blitPos[1]), 10, 0)


        return(self.reelComplete,{'center':(centerX,centerY ), 'centerL':(centerLx,CenterLy ),'centerR':(centerRx,CenterRy ), 'midTop':(midTopX,midTopY),'leftTop':(leftTopX, leftTopY),'rightTop':(rightTopX, rightTopY),'behind':(behindX,behindY) , 'rotatedDims': (rotatedWidth,rotatedHeight)})



    def animateNoRotation(self,gui,trackedName,blitPos,game,repeat=True):
        # TIMER THAT ITERATES THROUGH A FRAME EACH GIVEN INTERVAL
        changeFrame = self.frameTimer.stopWatch(self.changeDuration,trackedName, str(self.changeCount) + trackedName, game,silence=True)
        
        if(changeFrame):
            self.changeCount +=1
            self.currentFrame +=1
            if(self.currentFrame>=len(self.imageFrames)):
                if(repeat==False):
                    self.currentFrame = len(self.imageFrames)-1
                else:
                    self.currentFrame = 0
                self.reelComplete = True
            else:
                # LATE ADDITION MIGHT NEED ROLLED BACK
                self.reelComplete = False


        # GET ORIGINAL AND ROTATED LEN AND WIDTH
        imgW,imgH = self.imageFrames[self.currentFrame].get_width(), self.imageFrames[self.currentFrame].get_height()
        gui.screen.blit(self.imageFrames[self.currentFrame], (blitPos[0],blitPos[1]))

        return(self.reelComplete)


    def animateLowCompute(self,gui,trackedName,blitPos,game,repeat=True,rotation=None,skipBlit=False):
        # TIMER THAT ITERATES THROUGH A FRAME EACH GIVEN INTERVAL
        changeFrame = self.frameTimer.stopWatch(self.changeDuration,trackedName, str(self.changeCount) + trackedName, game,silence=True)
        
        if(changeFrame):
            self.changeCount +=1
            self.currentFrame +=1
            if(self.currentFrame>=len(self.imageFrames)):
                if(repeat==False):
                    self.currentFrame = len(self.imageFrames)-1
                else:
                    self.currentFrame = 0
                self.reelComplete = True
            else:
                # LATE ADDITION MIGHT NEED ROLLED BACK
                self.reelComplete = False

        # SKIP BLIT
        if(skipBlit):
            return(self.reelComplete)

        if(rotation==None): rotation = 0
        rotation = wrapAngle(rotation)

        # GET ORIGINAL AND ROTATED LEN AND WIDTH
        rotated_image = pygame.transform.rotate(self.imageFrames[self.currentFrame], rotation)
        rotatedWidth,rotatedHeight     = rotated_image.get_width(),rotated_image.get_height()
        imgW,imgH = self.imageFrames[self.currentFrame].get_width(), self.imageFrames[self.currentFrame].get_height()

        # GET MUTATED COORDINATES
        blitx,blity         = blitPos[0]+0.5*(imgW-rotatedWidth),blitPos[1]+0.5*(imgH-rotatedHeight)
        gui.screen.blit(rotated_image, (blitx,blity))


        # GET ORIGINAL AND ROTATED LEN AND WIDTH
        imgW,imgH = self.imageFrames[self.currentFrame].get_width(), self.imageFrames[self.currentFrame].get_height()

        return(self.reelComplete)






class gui():
    def __init__(self,screen,width,height,IMAGEASSETPATH='notset'):
        self.clicked         = False
        self.rightClicked    = False
        self.pressed         = False
        self.KEYDOWN         = False
        self.scrollUp        = False
        self.scrollDown      = False
        self.input           = None # Assigned during main

        self.screen          = screen
        self.x               = 0
        self.y               = 0
        self.w               = width
        self.h               = height
        self.mx              = 0 
        self.my              = 0 

        self.basePath        = IMAGEASSETPATH



        self.camX            = 0
        self.camY            = 0
        self.camW            = 1500
        self.camH            = 850
        self.camdx, self.camdy      = 0,0

        # ------------------------------ 
        #     CLASSES
        # ------------------------------

        self.smsDialogue            = None # UPDATED IN SETUP
        self.smsScrollDialogue      = None # UPDATED IN SETUP



        # ------------------------------ 
        #     COLOURS
        # ------------------------------
        self.white              = (255,255,255)
        self.green              = (0,255,0)
        self.black              = (0,0,0)
        self.blue               = (176,224,230)

        #self.guiTheme           = guiTheme # SET AS 'main' for now
        #c = returnColourScheme(guiTheme)
        self.colourA                              = c['a']
        self.colourB                              = c['b']
        self.colourC                              = c['c']
        self.colourD                              = c['d']
        self.bgColour                             = (175,175,175)
        self.innerBGColour                        = (119,121,118)
        self.bannerColour                         = (14,0,135)
        self.bannerTextColour                     = self.white





        # ------------------------------ 
        #     SPECIAL EFFECTS
        # ------------------------------

        # ----------FADE

        self.fadeInState    = None
        self.fadeOutState   = None
        self.resetFadeIn    = True
        self.resetFadeOut   = True
        self.fadeAlphaIndex = 100    # used on fade in, goes down to 0
        self.alphaI         = 0      # used on fade out (goes up to 255)
        self.fadeSurface    = pygame.Surface((self.w,self.h))

        self.contortMapDelay     = 0.4                # BUFF
        self.contortMapTimer     = stopTimer()
        self.contortMapCount     = 0



        self.boxOutState  = None
        self.boxInit      = False
        self.boxFill      = 0
        self.boxComplete  = False


        self.menuBG            = None
        self.hideExitButton    = False

