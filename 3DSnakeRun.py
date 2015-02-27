
import random
from Tkinter import *
from Animation import Animation
from Cloud import MyCloud
from Grid import MyGrid
from Snake import Snake
from Food import Food
from MiniMap import MiniMap
import pygame
from Menu import Menu

# focus point = (400,300)

class Play (Animation):
    play = False
    option = False
    score = False
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.skycolor = 'cyan'
        # set up the mixer
        freq = 44100     # audio CD quality
        bitsize = -16    # unsigned 16 bit
        channels = 1     # 1 is mono, 2 is stereo
        buffer = 1024    # number of samples (experiment to get right sound)
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.load("Media/Kirby.mp3")
        pygame.mixer.music.play(-1)
               
    def init(self):
        #create a game of 5*5
        gameSize = 5
        class Struct: pass
        self.image = Struct()
        self.image.heart = PhotoImage(file="Media/heart.gif").subsample(30,30)
        self.image.life = PhotoImage(file="Media/heart.gif").subsample(35,35)
        self.image.clock = PhotoImage(file = 'Media/clock.gif').subsample(4,4).zoom(2,2)
        self.image.apple = PhotoImage(file = 'Media/apple.gif').subsample(6,6)
        self.image.capsule = PhotoImage(file = 'Media/capsule.gif').subsample(3,3)
        self.image.BigSnake = PhotoImage(file = 'Media/BigSnake.gif').subsample(2,2)
        self.grid = MyGrid(self.canvas,self.width,self.height,gameSize, self.image)
        self.food = Food(self.grid)
        self.timerFiredCount = 0
        self.snake = Snake(self.grid, self.food)
        Snake.gameOver = False
        self.food.placeFood()
        self.food.placeFood()
        self.food.placeFood()
        self.food.placeFood()
        self.food.placeFood()
        self.food.placeFood()
        self.food.placeFood()
        MyCloud.cloudList = []
        MyCloud(self.canvas)
        MyCloud(self.canvas)
        MyCloud(self.canvas)
        MyCloud(self.canvas)
        MyCloud(self.canvas)
        self.miniMap = MiniMap(self.canvas,self.grid, self.food, self.snake,
                               self.width, self.height)
        self.menu = Menu(self.canvas,self.width, self.height,self.food)

    def init2(self):
        #create a game of 5*5
        gameSize = 5
        self.grid = MyGrid(self.canvas,self.width,self.height,gameSize, self.image)
        self.food = Food(self.grid)
        self.timerFiredCount = 0
        self.snake = Snake(self.grid, self.food)
        Snake.gameOver = False
        self.food.placeFood()
        self.food.placeFood()
        self.food.placeFood()
        self.food.placeFood()
        self.food.placeFood()
        self.food.placeFood()
        self.food.placeFood()
        self.miniMap = MiniMap(self.canvas,self.grid, self.food, self.snake,
                               self.width, self.height)
        self.menu = Menu(self.canvas,self.width, self.height,self.food)
        
            
    def timerFired(self):
        if(Snake.gameOver ==False and Play.play == True):
            self.timerFiredCount += 1
            MyCloud.grow()
            if (self.timerFiredCount % 150 == 0):
                Snake.statusSpeed = Snake.gameSpeed
            if(self.timerFiredCount % Snake.statusSpeed ==0 ):
                self.snake.snakeMove()
            if(Snake.restart):
                self.init2()
                Snake.restart = False
        else:
            MyCloud.grow()

    def keyPressed(self,event):
        if(Play.option == True):
            if(event.keysym == 'Left'):
                if(Snake.gameSpeed>1):
                    Snake.gameSpeed -=1
                    Snake.statusSpeed = Snake.gameSpeed
            if(event.keysym == 'Right'):
                if(Snake.gameSpeed<20):
                    Snake.gameSpeed +=1
                    Snake.statusSpeed = Snake.gameSpeed
                
        if(Snake.gameOver == False):
            if(event.keysym == 'Left'):
                self.snake.turnLeft()
            if(event.keysym == 'Right'):
                self.snake.turnRight()
            if(event.char =='s'):
                Play.start = True
                
    def mousePressed(self,event):
        x = event.x
        y = event.y
        if(self.menu.isBack(x,y)):
            Play.play = False
            Play.option = False
            Play.score = False
        elif( self.menu.isQuit(x,y)):
            Snake.gameOver = True
            pygame.mixer.quit()
            Animation.root.quit()
        elif( self.menu.isScore(x,y)):
            Play.score = True
        elif( self.menu.isOption(x,y)):
              Play.option = True
        elif ( self.menu.isPlay(x,y)):
            Play.play = True
            self.init2()
            Snake.life = 3
            Snake.score = 0
    
    def redrawAll(self):
        if(Play.play):
            self.displaySky()
            self.displayCloud()
            self.displayGrid()
            '''
            self.displaySnake()
            '''
            self.diaplayMap()
            self.displayStatus()
            self.displayGameOver()
            self.menu.displayBack()
        elif(Play.score):
            self.menu.displayStatistic()
            self.menu.displayBack()
        elif(Play.option):
            self.menu.displayOption()
            self.menu.displayBack()
        else:
            self.displayMenu()
        
    def displaySky(self):
        self.canvas.create_rectangle(0,0,self.width,
                                     self.height,fill = self.skycolor,
                                     width = 0)
        
    def displayCloud(self):
        MyCloud.drawCloud()
        
    def displayGrid(self):
        self.grid.drawGrid(self.snake)

    def diaplayMap(self):
        self.miniMap.draw()

    def displayStatus(self):
        self.canvas.create_text(20, self.height/10,anchor = W,
                                text = 'Life :  ',
                                 font="Helvetica 18 bold")
        self.canvas.create_text(self.width/2, self.height/10,
                                text = 'Score:   %000d'%Snake.score,
                                font="Helvetica 18 bold")
        for i in xrange (Snake.life):
            width = self.image.life.width()
            self.canvas.create_image(self.width/7+width*i,
                                     self.height/10,image = self.image.life)
    def displayGameOver(self):
        if(Snake.gameOver):
            self.canvas.create_text(self.width/2, self.height/2,
                                    text = 'Game  Over', fill = 'red',
                                    font="Helvetica 30 bold")

    def displayMenu(self):
        self.displaySky()
        self.displayCloud()
        self.canvas.create_image(self.width/5, self.height*4/6.0,
                                 image = self.image.BigSnake)
        self.canvas.create_text(self.width/2+self.width/4,self.height/3,
                                text = ' SNAKE! ', fill = 'red',
                                font = "Helvetica 50 bold")
        self.menu.displayWelcome()

    def run(self):
        width = self.width
        height = self.height
        super(Play, self).run(width, height)
        
Play(800,600).run()
#create an 800* 600 display
