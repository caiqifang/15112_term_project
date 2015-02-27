import math
from Snake import Snake

class MiniMap (object):

    def __init__(self,canvas,grid,food,snake,width,height):
        self.grid = grid
        self.food = food
        self.snake = snake
        self.canvas = canvas
        self.width = width
        self.height = height
        self.mapSize = 200
        self.lineLength = 80
        self.margin = 25
        self.topAngle = 25
        self.segment = self.lineLength / self.grid.gridSize

    def draw(self):
        self.drawBackground()
        self.drawTop()
        self.drawLeft()
        self.drawRight()
        self.paintTop()
        self.paintLeft()
        self.paintRight()
        # surfaces filled with yellow, snake = green, item = blue,
        # snake head = red

    def drawBackground(self):
        self.canvas.create_rectangle(self.width-self.mapSize,0,self.width,
                                     self.mapSize,
                                     fill = 'yellow', width = 2)

    def drawTop(self):
        startPoint  = (self.width-self.mapSize + self.mapSize/2, self.margin)
        cos = math.cos(float(self.topAngle)/180 * math.pi)
        sin = math.sin(float(self.topAngle)/180*math.pi)
        for i in xrange(self.grid.gridSize+1):
            self.canvas.create_line(startPoint[0]-i*self.segment*cos,
                                    startPoint[1]+i*self.segment*sin,
                        startPoint[0]-i*self.segment*cos+self.lineLength*cos,
                        startPoint[1]+i*self.segment*sin+self.lineLength*sin,
                                    width =1)
            self.canvas.create_line(startPoint[0]+i*self.segment*cos,
                                    startPoint[1]+i*self.segment*sin,
                        startPoint[0]+i*self.segment*cos-self.lineLength*cos,
                        startPoint[1]+i*self.segment*sin+self.lineLength*sin,
                                    width =1)

    def drawLeft(self):
        startPoint  = (self.width-self.mapSize + self.mapSize/2, self.margin)
        cos = math.cos(float(self.topAngle)/180 * math.pi)
        sin = math.sin(float(self.topAngle)/180*math.pi)
        startPoint =(startPoint[0]-self.lineLength*cos,
                     startPoint[1]+self.lineLength*sin)
        for i in xrange(self.grid.gridSize+1):
            self.canvas.create_line(startPoint[0]+i*self.segment*cos,
                                    startPoint[1]+i*self.segment*sin,
                        startPoint[0]+i*self.segment*cos,
                        startPoint[1]+i*self.segment*sin + self.lineLength,
                                    width =1)
            self.canvas.create_line(startPoint[0],
                                    startPoint[1]+i*self.segment,
                        startPoint[0]+self.lineLength*cos,
                        startPoint[1]+i*self.segment+self.lineLength*sin,
                                    width =1)
            
    def drawRight(self):
        startPoint  = (self.width-self.mapSize + self.mapSize/2, self.margin)
        cos = math.cos(float(self.topAngle)/180 * math.pi)
        sin = math.sin(float(self.topAngle)/180*math.pi)
        startPoint =(startPoint[0]+self.lineLength*cos,
                     startPoint[1]+self.lineLength*sin)
        for i in xrange(self.grid.gridSize+1):
            self.canvas.create_line(startPoint[0]-i*self.segment*cos,
                                    startPoint[1]+i*self.segment*sin,
                        startPoint[0]-i*self.segment*cos,
                        startPoint[1]+i*self.segment*sin + self.lineLength,
                                    width =1)
            self.canvas.create_line(startPoint[0],
                                    startPoint[1]+i*self.segment,
                        startPoint[0]-self.lineLength*cos,
                        startPoint[1]+i*self.segment+self.lineLength*sin,
                                    width =1)

    def paintTop(self):
        if(self.snake.surface == 1 or
           self.snake.surface == 4 or
           self.snake.surface == 0):
            grid = self.grid.grid[1]
            for row in xrange(len(grid)):
                for col in xrange(len(grid[0])):
                    item = grid[row][col]
                    if isinstance(item,str):
                       self.colorTop(row,col,'blue')
                    elif(grid[row][col] ==self.snake.length):
                        self.colorTop(row,col,'red')
                    elif( grid[row][col]>0):
                       self.colorTop(row,col,'green')
        else:
            grid2 = self.grid.grid[3]
            for row in xrange(len(grid2)):
                for col in xrange(len(grid2[0])):
                    item = grid2[row][col]
                    if isinstance(item,str):
                       self.colorTop(col,self.grid.gridSize -row-1,'blue')
                    elif(grid2[row][col] ==self.snake.length):
                        self.colorTop(col,self.grid.gridSize -row-1,'red')
                    elif( grid2[row][col]>0):
                       self.colorTop(col,self.grid.gridSize-row-1,'green')

    def colorTop(self,row,col,color):
        startPoint  = (self.width-self.mapSize + self.mapSize/2, self.margin)
        cos = math.cos(float(self.topAngle)/180 * math.pi)
        sin = math.sin(float(self.topAngle)/180*math.pi)
        startPoint =(startPoint[0]-self.lineLength*cos,
             startPoint[1]+self.lineLength*sin)
        startPoint = (startPoint[0] + row*self.segment*cos,
                      startPoint[1] + row*self.segment*sin)
        nextPoint = (startPoint[0]+self.segment*cos,
                     startPoint[1]+self.segment*sin)
        self.canvas.create_oval(startPoint[0]+self.segment/2*cos+col*self.segment*cos,
                                startPoint[1]-self.segment/2*sin-col*self.segment*sin,
                                nextPoint[0]+self.segment/2*cos+col*self.segment*cos,
                                nextPoint[1]-self.segment/2*sin-col*self.segment*sin,
                                   fill = color)
    def paintRight(self):
        if(self.snake.surface == 1 or
           self.snake.surface == 4 or
           self.snake.surface == 0):
            grid = self.grid.grid[0]
            for row in xrange(len(grid)):
                for col in xrange(len(grid[0])):
                    item = grid[row][col]
                    if isinstance(item,str):
                       self.colorRight(row,col,'blue')
                    elif(grid[row][col] ==self.snake.length):
                        self.colorRight(row,col,'red')
                    elif( grid[row][col]>0):
                       self.colorRight(row,col,'green')
        else:
            grid2 = self.grid.grid[5]
            for row in xrange(len(grid2)):
                for col in xrange(len(grid2[0])):
                    item = grid2[row][col]
                    if isinstance(item,str):
                       self.colorRight(self.grid.gridSize-col-1,row,'blue')
                    elif(grid2[row][col] ==self.snake.length):
                        self.colorRight(self.grid.gridSize-col-1,row,'red')
                    elif( grid2[row][col]>0):
                       self.colorRight(self.grid.gridSize - col-1,row,'green')

    def colorRight(self,row,col,color):
        startPoint  = (self.width-self.mapSize + self.mapSize/2, self.margin)
        cos = math.cos(float(self.topAngle)/180 * math.pi)
        sin = math.sin(float(self.topAngle)/180*math.pi)
        startPoint =(startPoint[0],
             startPoint[1]+2*self.lineLength*sin)
        startPoint = (startPoint[0]+col*self.segment*cos,
                      startPoint[1]-col*self.segment*sin)
        nextPoint = (startPoint[0]+self.segment*cos,
                     startPoint[1]-self.segment*sin)
        self.canvas.create_oval(startPoint[0],
                                startPoint[1]+self.segment/2+row*self.segment,
                                nextPoint[0],
                                nextPoint[1]+self.segment/2+row*self.segment,
                                   fill = color)
        
    def paintLeft(self):
        if(self.snake.surface == 1 or
           self.snake.surface == 4 or
           self.snake.surface == 0):
            grid = self.grid.grid[4]
            for row in xrange(len(grid)):
                for col in xrange(len(grid[0])):
                    item = grid[row][col]
                    if isinstance(item,str):
                       self.colorLeft(row,col,'blue')
                    elif(grid[row][col] ==self.snake.length):
                        self.colorLeft(row,col,'red')
                    elif( grid[row][col]>0):
                       self.colorLeft(row,col,'green')
        else:
            grid2 = self.grid.grid[2]
            for row in xrange(len(grid2)):
                for col in xrange(len(grid2[0])):
                    item = grid2[row][col]
                    if isinstance(item,str):
                       self.colorLeft(col,self.grid.gridSize-1-row,'blue')
                    elif(grid2[row][col] ==self.snake.length):
                        self.colorLeft(col,self.grid.gridSize -1-row,'red')
                    elif( grid2[row][col]>0):
                       self.colorLeft(col,self.grid.gridSize-1-row,'green')

    def colorLeft(self,row,col,color):
        startPoint  = (self.width-self.mapSize + self.mapSize/2, self.margin)
        cos = math.cos(float(self.topAngle)/180 * math.pi)
        sin = math.sin(float(self.topAngle)/180*math.pi)
        startPoint =(startPoint[0]-self.lineLength*cos,
             startPoint[1]+self.lineLength*sin)
        startPoint = (startPoint[0] + row*self.segment*cos,
                      startPoint[1] + row*self.segment*sin+ self.segment/2)
        nextPoint = (startPoint[0]+self.segment*cos,
                     startPoint[1]+self.segment*sin)
        col = self.grid.gridSize - col-1
        self.canvas.create_oval(startPoint[0],
                                startPoint[1]+col*self.segment,
                                nextPoint[0],
                                nextPoint[1]+col*self.segment,
                                   fill = color)
