import os
from Snake import Snake
from Food import Food
from Cloud import MyCloud

class Menu(object):
# quit, option, play, highest score

    def __init__(self,canvas,width, height,food):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.margin = 50
        self.food = food

    def displayWelcome(self):
        #1
        self.canvas.create_rectangle(self.width/2+self.margin,
                                     self.height/2 + self.margin,
                                     self.width/2+self.width/4-self.margin/2,
                                     self.height/2+self.height/4-self.margin/2,
                                     width = 2, fill = 'gray')
        #2
        self.canvas.create_rectangle(self.width/2+self.width/4+self.margin/2,
                             self.height/2 + self.margin,
                             self.width-self.margin,
                             self.height/2+self.height/4-self.margin/2,
                             width = 2, fill = 'gray')
        #3
        self.canvas.create_rectangle(self.width/2+self.margin,
                     self.height/2 +self.height/4+ self.margin/2,
                     self.width/2+self.width/4-self.margin/2,
                     self.height - self.margin,
                     width = 2, fill = 'gray')
        #4
        self.canvas.create_rectangle(self.width/2+self.width/4+self.margin/2,
             self.height/2 + self.height/4+self.margin/2,
             self.width - self.margin,
             self.height- self.margin,
             width = 2, fill = 'gray')

        self.displayLetter()

    def displayLetter(self):

        self.canvas.create_text((self.width+self.margin +self.width/4-self.margin/2)/2,
                                (self.height + self.margin+self.height/4-self.margin/2)/2,
                                text = 'PLAY', font = 'Calibri 20 bold')
        self.canvas.create_text((self.width/2+self.width/4+self.width-self.margin/2)/2,
                                (self.height+ self.margin/2+self.height/4)/2,
                                text = 'SCORE', font = 'Calibri 20 bold')
        self.canvas.create_text((self.width+self.margin/2+self.width/4)/2,
                                (self.height/2 +self.height/4+self.height - self.margin/2)/2,
                                text = 'OPTION', font = 'Calibri 20 bold')
        self.canvas.create_text((self.width/2+self.width/4+self.width - self.margin/2)/2,
                                (self.height/2 + self.height/4+self.height- self.margin/2)/2,
                                text = 'QUIT',font = 'Calibri 20 bold')

    def displayStatistic(self):
        self.displaySky()
        MyCloud.drawCloud()
        content = self.food.readFile(self.food.filename)
        self.canvas.create_text(self.width/2,self.height/3,
                                text = ' HIGHEST SCORE ! ',
                                font = 'Calibri 45 bold')
        self.canvas.create_text(self.width/2,self.height/2,
                                text = eval(content) ,font = 'Calibri 35 bold')
        

    def displayOption(self):
        self.displaySky()
        MyCloud.drawCloud()
        self.canvas.create_text(self.width/2, self.height/4,
                                 text = ' USE ARROW KEY TO ADJUST DIFFICULTY ',
                                 font = 'Calibri 30 bold', fill = 'red')
        self.canvas.create_text(self.width/2, self.height/3,
                         text = ' <- HARD        EASY -> ',
                         font = 'Calibri 30 bold', fill = 'red')
        self.canvas.create_text(self.width/2, self.height/2,
                                 text = ' Game Speed :   %000d'%Snake.gameSpeed,
                                font = 'Calibri 30 bold')
        self.canvas.create_text(self.width/2, self.height/2+self.height/5,
                         text = 'IN GAME',
                         font = 'Calibri 30 bold', fill = 'black')
        self.canvas.create_text(self.width/2, self.height/2+self.height/3,
                         text = ' <- LEFT    ARROW KEY TO PLAY    RIGHT -> ',
                         font = 'Calibri 30 bold', fill = 'black')

    def displaySky(self):
        self.canvas.create_rectangle(0,0,self.width,
                                     self.height,fill = 'cyan',
                                     width = 0)
    
    def isPlay(self,x,y):
        if ( x>self.width/2+self.margin and
             x <self.width/2+self.width/4-self.margin/2
             and y>self.height/2 + self.margin and
             y<self.height/2+self.height/4-self.margin/2):
            return True
        else: return False

    def isOption(self,x,y):
        if ( x>self.width/2+self.margin and
             x<self.width/2+self.width/4-self.margin/2
             and y >self.height/2 +self.height/4+ self.margin/2
             and y < self.height - self.margin):
            return True
        else: return False

    def isScore(self,x,y):
        if(x>self.width/2+self.width/4+self.margin/2
           and x< self.width-self.margin and
           y>self.height/2 + self.margin and
           y<self.height/2+self.height/4-self.margin/2):
            return True
        else: return False

    def isQuit(self,x,y):
        if(x>self.width/2+self.width/4+self.margin/2 and
           x<self.width - self.margin and
           y>self.height/2 + self.height/4+self.margin/2 and
           y<self.height- self.margin):
            return True
        else: return False

    def displayBack(self):
        self.canvas.create_rectangle( self.width - 60, 230,self.width ,260,
                                      fill = 'gray', width = 2)
        self.canvas.create_text(self.width-30, 245,
                                text = 'BACK', font = 'Calibri 20 bold')
        
    def isBack(self,x,y):
        if(x>self.width-60 and x<self.width and
           y>230 and y<260):
            return True
        else: return False
