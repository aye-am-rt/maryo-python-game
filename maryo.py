
#Import modules

import pygame, random, sys
from pygame.locals import *
pygame.init()

#intialising variables for ease
#here windows height and width we firat set because it is going to be our canvas or everything, it will be black by default.

window_height=600 
window_width=1200

blue = (0,0,255)                                  #these are RGB colour intensity numbers.
black = (0,0,0)
white = (255, 255, 255)

fps = 25                                          #this is for moving speed of rects fireball and dragon will move with this speed,increased it at each level
level = 0                                         #initially level we set to zero
addnewflamerate = 20

#defining the required function
#best idea is making a class of dragon, mario, flames it will be like user defined data type so can change what properties and functions to have. 


#----------------------------------------------------------------------------------------------------------------------------------------------------------------

class dragon:

    global firerect, imagerect, Canvas               #declairation of global variable for dragon class so ,this can be used anywhere in program for dragon class.
    up = False
    down = True                                      #by this dragon will go down initially when its object is creatd. not now
    velocity = 20
    
    def __init__(self):                              #here defined the constructor for class which will be called automatically when the class object is created.
        self.image = load_image('dragon.png')        #all the images should present in same folder.to be able to load.
        self.imagerect = self.image.get_rect()       #by this we get the image as rectangle properties
        self.imagerect.right = window_width          #dragon image should be in last of window thats why right cordinate is set to windows_width.
        self.imagerect.top = window_height/2         #and height is total window height/2 ,means middle right point.

    def update(self):                                #ths is to update dragons conditions 

#had very problems finding this so understand it correctly and remember this         

        if (self.imagerect.top < cactusrect.bottom):     #this is to limit the movements of dragon. 
            self.up = False                              #as soon as dragon image crosses the cactus which is on top it should start go down.
            self.down = True

        if (self.imagerect.bottom > firerect.top):      #as soon as dragon crosses the fires this means its bottom >firerect.top it should go up.
            self.up = True
            self.down = False
            
        if (self.down):
            self.imagerect.bottom += self.velocity         #velocity of going down means the bottom of dragon image should increase by that velocity

        if (self.up):
            self.imagerect.top -= self.velocity            #velocity of going up   means the now top of dragon image should decrease by that velocity
#blit is used to overlap one image rectangle over other. syntax== canvas.blit(surface,surface_rect)
        Canvas.blit(self.image, self.imagerect)   #now we are displaying the self.image and its rect on the top of the canvas(w*h=1200*600) 

    def return_height(self):

        h = self.imagerect.top              #this funtion to return top cordinte of image rect or say height.
        return h


#new class for Flames
#-------------------------------------------------------------------------------------------------------------------------


class flames:
    flamespeed = 20                  #defined flame speed with which it will move toward mariyo from dragon. 

    def __init__(self):                        #constructer
        self.image = load_image('fireball.png')       #loading fire ball image which is big in size so we have to reduce it using pygame.transform.scale method.
        self.imagerect = self.image.get_rect()       #getting image rect form.
        self.height = Dragon.return_height() + 20       #initial flame height. down to dragon +20 
        self.surface = pygame.transform.scale(self.image, (20,20))
        self.imagerect = pygame.Rect(window_width - 106, self.height, 20, 20)  #now set the flame image finally with its initial positon and size.

    def update(self):
            self.imagerect.left -= self.flamespeed       #updating for image of flame,means it will move towars left with that flamespeed.

    def collision(self):                          # a  function collision which returns true when flame hit the left most part of canvas.
        if self.imagerect.left == 0:            # this means end ,when flame reaches to zero.
            return True
        else:
            return False




#new class for maryo and its functions and variable also with update rule
#---------------------------------------------------------------------------------------------------------------------------------------------

class maryo:
    global moveup, movedown, gravity, cactusrect, firerect        # global variables of class maryo they can be used by anyon in class maryo
    speed = 10
    downspeed = 20

    def __init__(self):                                          #construcer of class maryo
        self.image = load_image('maryo.png')                     # loading image of maryo from folder by self.image=load_image('maryo.png')
        self.imagerect = self.image.get_rect()
        self.imagerect.topleft = (50,window_height/2)            # initialy puttin maryo at X=50(little away from left border) and height= middle of canvas
        self.score = 0                                           #remember doing initial score =0 otherwise gettin error when try to set/call score

    def update(self):

#moveup and movedown is there to get when keys of up and dowm are pressed respectivly.
#if arrow up key is pressed and maryo was not touching cactus it means below cactus its y cordinate should decrese that is maryo will go up
        
        if (moveup and (self.imagerect.top > cactusrect.bottom)):                                          #was not working difficult hint grvity problem.
            self.imagerect.top -= self.speed
            self.score += 1                                                                                 #tackeled by trying all possible options.

#if arrow down key is pressed and maryo was not touching flames it means above fire rect its y cordinate should increase that is maryo will can go down             

        if (movedown and (self.imagerect.bottom < firerect.top)):
            self.imagerect.bottom += self.downspeed
            self.score += 1

#this condotion is putting so maryo is constantly falling   if you dont press any key or up arrow key 
            
        if (gravity and (self.imagerect.bottom < firerect.top)): 
            self.imagerect.bottom += self.speed                  #into maryo bottom cordinate speed should add up to get it towards flames. and gravity is on.



def terminate():        #to end the program
    pygame.quit()
    sys.exit()




def waitforkey():
    while True :                                        #to wait for user to start
        for event in pygame.event.get():               #pygame.event.get() can acccept two types of things one is pygame.QUIT or any KEYDOWN OR KEYUP EVENT.
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:     #to terminate if the user presses the escape key
                if event.key == pygame.K_ESCAPE:
                    terminate()
                return
            
            


def flamehitsmario(playerrect, flames):      #to check if flame has hit mario or not
    for f in flame_list:                               # if any  condition true which is  in flames list 
        if playerrect.colliderect(f.imagerect):
            return True
        return False




def drawtext(text, font, surface, x, y):        #to display text on the screen
    textobj = font.render(text, 1, white) #font representation is done by rendering syntax== pygame.font.render(text,analytics(its a boolean value bool=0 or 1),color) 
    textrect = textobj.get_rect()               #getting text rect 
    textrect.topleft = (x,y)                    #representing its cordinate which are given by x,y .that will be its topleft corner     
    surface.blit(textobj, textrect)             #represent the text rect on the canvas using blit (surface object,surface rect)






def check_level(score):                                    #the function to chek score and change level on every 250 points                             
    global window_height, level, cactusrect, firerect      




# on each level movement area will decrease and cactus and flame width will increase

    if score in range(0,250):                           
        firerect.top = window_height - 50     #initially fire top shuld be window height-50 it means just in last and covering it.
        cactusrect.bottom = 50                #initially at level 1 cactus bottom will bw at 50 upper side of canavas          
        level = 1


    elif score in range(250, 500):            #on each level fire will move up by -50 pixels
        firerect.top = window_height - 100     #on each level cactus will come down +50 pixels
        cactusrect.bottom = 100
        level = 2


    elif score in range(500,750):
        level = 3
        firerect.top = window_height-150
        cactusrect.bottom = 150


    elif score in range(750,1000):
        level = 4
        firerect.top = window_height - 200
        cactusrect.bottom = 200

def load_image(imagename):
    return pygame.image.load(imagename)

#main loop    
#--------------------------------------------------------------------------------------------------------------------------------------------------

#end of functions, begin to start the main code
#now clock cheching for how much time it has taken.


mainClock = pygame.time.Clock()                                   #This will be main time loop of code  also used to run music from start  
Canvas = pygame.display.set_mode((window_width,window_height))    #displaying the canvas initially 
pygame.display.set_caption('SAVE THE MARYO GAME')                  #setting the caption of whole window                 

#setting up font and sounds and images

font = pygame.font.SysFont(None, 48)                       # getting font object  using syntax pygame.font.SysFont(Name,size,bold,italics) 
scorefont = pygame.font.SysFont(None, 30)       #this is fornt for displaying score they both will be used in function mentioned above draw text(text,font,surface,x,y)


#loading fire image and cactus image then getting their rect.

fireimage = load_image('fire_bricks.png')
firerect = fireimage.get_rect()

cactusimage = load_image('cactus_bricks.png')
cactusrect = cactusimage.get_rect()

#this is starting image which will say press any key to start the game


startimage = load_image('start.png')
startimagerect = startimage.get_rect()
startimagerect.centerx = window_width/2         #starter image centerX and centerY will be full canvas mid points as window_widht/2,window_heigh/2
startimagerect.centery = window_height/2


#now get the image for when game ends either by pressing escape or maryo dying by flames or cactus

endimage = load_image('end.png')
endimagerect = startimage.get_rect()
endimagerect.centerx = window_width/2
endimagerect.centery = window_height/2

#now load the music which playes all the time and when game ends.
#pygame.mixer.Sound('string format file name with extension')

pygame.mixer.music.load('mario_theme.wav')
#putting this gameover into variable when maryo dies.
gameover = pygame.mixer.Sound('mario_dies.wav')  #this synatax is just for loading the sound file pygame.mixer.Sound('file name')





#getting to the start screen

drawtext('Mario', font, Canvas,(window_width/3), (window_height/3))     #writing the text at w/3,h/3
Canvas.blit(startimage, startimagerect)                                 #displaying the start iamge on surface of canvas 

pygame.display.update()        #one time update the whole dispaly it will put the image and text on specified positions      
waitforkey()                    #now we wait for the key function defined above if we press escape key or pygame.QUIT it will keep waiting coz condition while:True.








#start for the main code

topscore = 0
Dragon = dragon()     #Dragon object is created so constuctor will be initiated automatically daragon image will be loaded at specified positions




while True:         # this is infinite loop running untill maryo dies or esc pressed

    flame_list = []
    player = maryo()         #creating  maryo object player which will instantiste constuctor.
    moveup = movedown = gravity = False             #initilly moveing up,down ,gravity all ==0;
    flameaddcounter = 0                             #this was added on suggestion how many flames will go at a time and ito the list.

    gameover.stop()             #when maryo dies that sound will stop playing      
    pygame.mixer.music.play(-1,0.0)  #this is for playing the music arguments (number of loops, when to start) -1 is give to run for nfinite loop time this is whre
                                     #main clock is used the music will start playing at time 0.0    

    while True:     #the main game loop
        
        for event in pygame.event.get():                 #if you choose to quit intially pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:                   #if any key is pressed down on keyboard which  the waitforkey() funtion will be waiting for
                
                if event.key == K_UP:
                    movedown = False
                    moveup = True                      #as long as you keep pressing the arrowup key you will move up and gravity  will not work (falase) 
                    gravity = False

                if event.key == K_DOWN:              #as ong as you keep pressing the arrow down key you will go down and aslso gravity ==false 
                    movedown = True
                    moveup = False
                    gravity = False

            if event.type == KEYUP:               #at the moment when you relesaed the key 

                if event.key == K_UP:              #if that was the arrow up key released moving up will become false and gravity willl start pulling you down 
                    moveup = False
                    gravity = True
                if event.key == K_DOWN:   #if that was the arrow down key released moving down by key will become false and gravity willl start pulling you down 
                    movedown = False
                    gravity = True
                    
                if event.key == K_ESCAPE:   # if any time esc key was released it will quit the game as defined in that terminate function
                    terminate()

        flameaddcounter += 1
        check_level(player.score)              #to check level of player by its score defined up.
        
        if flameaddcounter == addnewflamerate:     #each time flame add counter equals new flame rate counter will be changed to zero       

            flameaddcounter = 0
            newflame = flames()                    #newFlame object is created of class flames its constructer
            flame_list.append(newflame)             #this object will be added in flame list 

#flame list conatins all the flame object that are on the screen at any time.        
        
        for f in flame_list:                   
            flames.update(f)                 #updating flames present on the screen at a time

        for f in flame_list:                  #when flame is present in list and on the screen 
            if f.imagerect.left <= 0:           #as soon as flame image reaches across the canvas (means f.imagerect.left<=0) remove it from the list
                flame_list.remove(f)

        player.update()         #updating the player maryo  and dragon
        Dragon.update()
        
#canvas intially will be black. all the other image will be displayed upon it by canvas.blit(surface,surface_rect) method
        Canvas.fill(black)
        Canvas.blit(fireimage, firerect)      #fire image on bottom
        Canvas.blit(cactusimage, cactusrect)   #cactus image on top
        Canvas.blit(player.image, player.imagerect)    #player image put on canvas surface 
        Canvas.blit(Dragon.image, Dragon.imagerect)    #Dragon image put on canvas
        
#this is calling  draw_text(text,font,surface,x,y) function  score,topscore,level all will be in one string)
        drawtext('Score : %s | Top score : %s | Level : %s' %(player.score, topscore, level), scorefont, Canvas, 350, cactusrect.bottom + 10)




#three way of geting out of loop or game over is
#                  1.maryo hits  top
#                  2. or bottom
#                  3. or flames hit maryo
                  

#untill f is in flames list  putting it on canvas f.surface,f.imagerect;        
        for f in flame_list:
            Canvas.blit(f.surface, f.imagerect)         
#if flames hit maryo checking it by if flame.rect < playerimage.rect it means x cordinate touches that function will return true.
        if flamehitsmario(player.imagerect, flame_list):
            if player.score > topscore:
                topscore = player.score               #changing top score if curren score is gretar when maryo dies
            break
        
        if ((player.imagerect.top <= cactusrect.bottom) or (player.imagerect.bottom >= firerect.top)): #when maryo touches top or bottom
            if player.score > topscore:
                topscore = player.score        #also top scaore changes and inner for  loop should break here
            break

        pygame.display.update()          #updating the display 

        mainClock.tick(fps)           #main clock is incresing 25 fps #it also important to update 
    
    pygame.mixer.music.stop()           #stop playing music at end 
    gameover.play()         
    Canvas.blit(endimage, endimagerect)         # display end image on canvas 
    pygame.display.update()           #update the display
    waitforkey()                    #wait for key clled either you press esc or any othrt key which starts the game again
        
    

#---------------------------------------------  #END OF PROGRAM------------   3 WEEKS 4 DAYS  ------------   JUNE 2017  ----------------------------------------------------
         
               
                                                     
                    
            
        

    
