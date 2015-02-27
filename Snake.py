import random
import os

class Snake (object):
    gameSpeed = 10
    life = 3
    score = 0
    surface = 0
    priorSurface = None
    gameOver = None
    restart = False
    statusSpeed = gameSpeed
    length = 1
    
    def __init__(self, grid , food):
        self.grid = grid
        self.food = food
        self.length = 1
        Snake.length = self.length
        self.hLocation = [random.randint(0,grid.gridSize-1),random.randint(0,grid.gridSize-1)]
        self.dire = [1,0]
        # [row,col]
        self.surface = Snake.surface = random.randint(0,5)
        self.grid.grid[self.surface][self.hLocation[0]][self.hLocation[1]] = 1
        Snake.gameOver = False

    def snakeMove(self):
        self.hLocation = [self.hLocation[0]+self.dire[0],
                        self.hLocation[1]+self.dire[1]]
        loc = self.hLocation
        if( self.offBound()):
            self.wrap()
            if( self.isOver()):
                Snake.gameOver = True
                self.record()
                return
            newloc = self.hLocation
            if( self.food.hasFood(newloc)):
                self.eatFood()
                self.food.placeFood()
            else:
                self.grid.grid[self.surface][newloc[0]][newloc[1]] = self.length +1
                self.removeTail()
                
        elif(self.isOver()):
            self.record()
            Snake.gameOver = True
        elif( self.food.hasFood(self.hLocation)):
            self.eatFood()
            self.food.placeFood()
        else:
            self.grid.grid[self.surface][loc[0]][loc[1]] = self.length +1
            self.removeTail()
            
    def record(self):
        content = self.food.readFile(self.food.filename)
        num = eval(content)
        if(Snake.score > num):
            content = 'int(%d)'% Snake.score
            self.food.writeFile(self.food.filename,content)

    def isOver(self):
        item = self.grid.grid[self.surface][self.hLocation[0]][self.hLocation[1]]
        if ( isinstance(item,int) and item>0):
            if( Snake.life<=1):
                Snake.life -=1
                return True
            else:
                Snake.life-=1
                Snake.restart = True
                return False
        else: return False

    def offBound(self):
        loc = self.hLocation
        if (loc[0]<0 or loc[0]>=self.grid.gridSize or
            loc[1]<0 or loc[1]>=self.grid.gridSize):
            return True
        else: return False
        
    def wrap(self):
        location, direction = self.makeTurn() # change surface direction location
        Snake.surface = self.surface
        self.hLocation = location
        self.dire = direction

    def makeTurn(self):
        N = [-1,0] # north
        S = [1,0] # south
        E = [0,1] # east
        W = [0,-1] # west
        if(self.surface==0):
            return self.turnFrom0(N,S,E,W)
        elif(self.surface ==1):
            return self.turnFrom1(N,S,E,W)
        elif(self.surface ==2):
            return self.turnFrom2(N,S,E,W)
        elif(self.surface ==3):
            return self.turnFrom3(N,S,E,W)
        elif(self.surface ==4):
            return self.turnFrom4(N,S,E,W)
        elif(self.surface ==5):
            return self.turnFrom5(N,S,E,W)

    def turnFrom0(self,N,S,E,W):
        Snake.priorSurface = 0
        if(self.dire[0] == 1):
            self.surface = 3
            location = [self.hLocation[0]%self.grid.gridSize,self.hLocation[1]]
            return location, S
        elif(self.dire[0] == -1):
            self.surface = 1
            location = [self.hLocation[0]%self.grid.gridSize,self.hLocation[1]]
            return location, N
        elif(self.dire[1] ==1):
            self.surface = 5
            location = [self.grid.gridSize-1,self.hLocation[0]]
            return location, N
        elif(self.dire[1] == -1):
            self.surface = 4
            location = [self.grid.gridSize-1, self.grid.gridSize -1 - self.hLocation[0]]
            return location, N

    def turnFrom1(self,N,S,E,W):
        Snake.priorSurface = 1
        if(self.dire[0] == 1):
            self.surface = 0
            location = [self.hLocation[0]%self.grid.gridSize,self.hLocation[1]]
            return location, S
        elif(self.dire[0] == -1):
            self.surface = 2
            location = [self.hLocation[0]%self.grid.gridSize,self.hLocation[1]]
            return location, N
        elif(self.dire[1] ==1):
            self.surface = 5
            location = [self.hLocation[0],self.hLocation[1]%self.grid.gridSize]
            return location, E
        elif(self.dire[1] == -1):
            self.surface = 4
            location = [self.hLocation[0],self.hLocation[1]%self.grid.gridSize]
            return location, W

    def turnFrom2(self,N,S,E,W):
        Snake.priorSurface = 2
        if(self.dire[0] == 1):
            self.surface = 1
            location = [self.hLocation[0]%self.grid.gridSize,self.hLocation[1]]
            return location, S
        elif(self.dire[0] == -1):
            self.surface = 3
            location = [self.hLocation[0]%self.grid.gridSize,self.hLocation[1]]
            return location, N
        elif(self.dire[1] ==1):
            self.surface = 5
            location = [0,self.grid.gridSize -1-self.hLocation[0]]
            return location, S
        elif(self.dire[1] == -1):
            self.surface = 4
            location = [0,self.hLocation[0]]
            return location, S

    def turnFrom3(self,N,S,E,W):
        Snake.priorSurface = 3
        if(self.dire[0] == 1):
            self.surface = 2
            location = [self.hLocation[0]%self.grid.gridSize,self.hLocation[1]]
            return location, S
        elif(self.dire[0] == -1):
            self.surface = 0
            location = [self.hLocation[0]%self.grid.gridSize,self.hLocation[1]]
            return location, N
        elif(self.dire[1] ==1):
            self.surface = 5
            location = [self.grid.gridSize-self.hLocation[0]-1,self.grid.gridSize-1]
            return location, W
        elif(self.dire[1] == -1):
            self.surface = 4
            location = [self.grid.gridSize-self.hLocation[0]-1,0]
            return location, E

    def turnFrom4(self,N,S,E,W):
        Snake.priorSurface = 4
        if(self.dire[0] == 1):
            self.surface = 0
            location = [self.grid.gridSize -1-self.hLocation[1],0]
            return location, E
        elif(self.dire[0] == -1):
            self.surface = 2
            location = [self.hLocation[1],0]
            return location, E
        elif(self.dire[1] ==1):
            self.surface = 1
            location = [self.hLocation[0],0]
            return location, E
        elif(self.dire[1] == -1):
            self.surface = 3
            location = [self.grid.gridSize-self.hLocation[0]-1,0]
            return location, E

    def turnFrom5(self,N,S,E,W):
        Snake.priorSurface = 5
        if(self.dire[0] == 1):
            self.surface = 0
            location = [self.hLocation[1],self.grid.gridSize-1]
            return location, W
        elif(self.dire[0] == -1):
            self.surface = 2
            location = [self.grid.gridSize -1-self.hLocation[1],self.grid.gridSize-1]
            return location, W
        elif(self.dire[1] ==1):
            self.surface = 3
            location = [self.grid.gridSize-self.hLocation[0]-1,self.grid.gridSize-1]
            return location, W
        elif(self.dire[1] == -1):
            self.surface = 1
            location = [self.hLocation[0],self.grid.gridSize-1]
            return location, W
        
    def eatFood(self):
        loc = self.hLocation
        item = self.grid.grid[self.surface][loc[0]][loc[1]]
        if( item == 'a'):
            Snake.score +=10
        elif( item =='l'):
            if Snake.life<4:
                Snake.life +=1
            Snake.score +=10
        elif( item == 'd'):
            Snake.statusSpeed = Snake.gameSpeed /4.0
            Snake.score +=10
        elif ( item == 't'):
            Snake.statusSpeed = Snake.gameSpeed*2.0
            Snake.score +=10
        self.grid.grid[self.surface][loc[0]][loc[1]] = self.length +1
        self.length += 1
        Snake.length = self.length

    def removeTail(self):
        for surface in xrange(len(self.grid.grid)):
            for row in xrange(len(self.grid.grid[surface])):
                for col in xrange(len(self.grid.grid[surface][0])):
                    num = self.grid.grid[surface][row][col]
                    if(isinstance(num,int) and num>0):
                        self.grid.grid[surface][row][col] -= 1
            
    def turnLeft(self):
        if(self.dire[0] !=0):
            temp = self.dire[0] 
            self.dire[0] = 0
            self.dire[1] = temp
        else:
            temp = self.dire[1] *(-1)
            self.dire[1] = 0
            self.dire[0] = temp

    def turnRight(self):
        if(self.dire[0] !=0):
            temp = self.dire[0] *(-1)
            self.dire[0] = 0
            self.dire[1] = temp
        else:
            temp = self.dire[1] 
            self.dire[1] = 0
            self.dire[0] = temp
