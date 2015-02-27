from Snake import Snake
from Food import Food

class MyGrid(object):
    
    def __init__(self,canvas,width,height, size, image):
        self.canvas = canvas
        # empty = 0 , food = str, snake >0
        # food : time, drug, life, apple
        self.emptyColor = 'gray'
        self.gridSize = size
        self.width = width
        self.height = height
        self.ratio = 0.8
        self.startRowSize = 90
        self.startColSize = 200
        self.grid = self.createGrid()
        self.image = image
        
    def createGrid(self):
        size = self.gridSize
        grid=[]
        for index in xrange(6):
            grid.append( [[0]*size for i in xrange(size)])
        return grid
        
    def drawGrid(self,snake):
        location = snake.hLocation
        direction = snake.dire
        if(direction[0] == 1): # south
            self.faceSouth(location,direction)
        elif(direction[0] == -1): # north
            self.faceNorth(location,direction)
        elif(direction[1] ==1): # east
            self.faceEast(location,direction)
        elif(direction[1] == -1): # west
            self.faceWest(location,direction)

    def faceEast(self,location,direction):
        rows = self.gridSize - location[1] # show yourself
        colsL = location[0]
        colsR = self.gridSize - location[0]-1
        R = location[0]
        C = location[1]
        for row in xrange(rows):
            self.drawPolygon(self.getCurrentCol(row),
                             self.getColor(R,C+row))
            for coll in xrange(colsL):
                self.drawPolygon(self.getPointOnLeft(row,coll),
                                self.getColor(R-1-coll,C+row))
            for colr in xrange(colsR):
                self.drawPolygon(self.getPointOnRight(row,colr),
                                self.getColor(R+1+colr,C+row))

    def faceWest(self,location,direction):
        rows = location[1]+1 #show yourself
        colsL = self.gridSize - location[0]-1
        colsR = location[0]
        R = location[0]
        C = location[1]
        for row in xrange(rows):
            self.drawPolygon(self.getCurrentCol(row),
                             self.getColor(R,C-row))
            for coll in xrange(colsL):
                self.drawPolygon(self.getPointOnLeft(row,coll),
                                self.getColor(R+1+coll,C-row))
            for colr in xrange(colsR):
                self.drawPolygon(self.getPointOnRight(row,colr),
                                self.getColor(R-1-colr,C-row))

    def faceNorth(self,location,direction):
        rows = location[0] +1 # show yourself
        colsL = location[1]
        colsR = self.gridSize - location[1]-1
        R = location[0]
        C = location[1]
        for row in xrange(rows):
            self.drawPolygon(self.getCurrentCol(row),
                             self.getColor(R-row,C))
            for coll in xrange(colsL):
                self.drawPolygon(self.getPointOnLeft(row,coll),
                                self.getColor(R-row,C - coll - 1))
            for colr in xrange(colsR):
                self.drawPolygon(self.getPointOnRight(row,colr),
                                self.getColor(R-row,C + colr + 1))

    def faceSouth(self,location,direction):
        rows = self.gridSize - location[0] # show yourself
        colsL = self.gridSize - location[1]-1
        colsR = location[1]
        R = location[0]
        C = location[1]
        for row in xrange(rows):
            self.drawPolygon(self.getCurrentCol(row),
                             self.getColor(R+row,C))
            for coll in xrange(colsL):
                self.drawPolygon(self.getPointOnLeft(row,coll),
                                self.getColor(R+row,C + coll + 1))
            for colr in xrange(colsR):
                self.drawPolygon(self.getPointOnRight(row,colr),
                                self.getColor(R+row,C - colr - 1))
        
    def getColor(self, row,col):
        item = self.grid[Snake.surface][row][col]
        if( isinstance (item, str)):
            if ( item == 'a'):
                return 'yellow'
            elif(item == 'l'):
                return 'white'
            elif(item == 't'):
                return 'orange'
            elif(item == 'd'):
                return 'black'
        elif ( item ==0):
            return self.emptyColor
        elif ( item == Snake.length):
            return 'red'
        elif( item >0):
            return 'green'
            
    def getCurrentCol(self, row):
        y0 = y1 = self.height - self.getRowSize(row)
        y3 = y2 = self.height - self.getRowSize(row+1)
        x0 = self.width/2 - self.getColSize(row)
        x1 = self.width/2 + self.getColSize(row)
        x2 = self.width/2 + self.getColSize(row+1)
        x3 = self.width/2 - self.getColSize(row+1)
        return (x0,y0,x1,y1,x2,y2,x3,y3) 
        
    def getPointOnLeft(self, row,coll):
        y0 = y1 = self.height - self.getRowSize(row)
        y3 = y2 = self.height - self.getRowSize(row+1)
        x1 = self.width/2- (coll*2+1)*self.getColSize(row)
        x0 = self.width/2- ((coll+1)*2+1)*self.getColSize(row)
        x2 = self.width/2- (coll*2+1)*self.getColSize(row+1)
        x3 = self.width/2- ((coll+1)*2+1)*self.getColSize(row+1)
        return (x0,y0,x1,y1,x2,y2,x3,y3)
        
    def getPointOnRight(self,row,colr):
        y0 = y1 = self.height - self.getRowSize(row)
        y3 = y2 = self.height - self.getRowSize(row+1)
        x0 = self.width/2+ (colr*2+1)*self.getColSize(row)
        x1 = self.width/2+ ((colr+1)*2+1)*self.getColSize(row)
        x3 = self.width/2+ (colr*2+1)*self.getColSize(row+1)
        x2 = self.width/2+ ((colr+1)*2+1)*self.getColSize(row+1)
        return (x0,y0,x1,y1,x2,y2,x3,y3)
    
    def getColSize(self,row): # get one piece of the col
        start = self.startColSize /2
        height = self.height -  self.getRowSize(row)
        return start * height / float(self.height)
        
    def getRowSize(self,row):
        Sum = 0
        for r in xrange(row):
            Sum += self.startRowSize* (self.ratio**r)
        return Sum 

    #use polygon
    def drawPolygon(self, points, color):
        (x0,y0,x1,y1,x2,y2,x3,y3) = points
        offset = 5
        x = (x1+x0)/2 # find middle
        y = (y1+y2)/2

        if ( color  =='red'):
            self.canvas.create_polygon(x0,y0,x1,y1,x2,y2,x3,y3,
                                         outline = 'black',width = 1,
                                         fill = 'red')
        elif(color  =='green'):
            self.canvas.create_polygon(x0,y0,x1,y1,x2,y2,x3,y3,
                                         outline = 'black',width = 1,
                                         fill = 'green')
        else:
            self.canvas.create_polygon(x0,y0,x1,y1,x2,y2,x3,y3,
                                             outline = 'black',width = 1,
                                             fill = self.emptyColor)
        if color =='yellow':
            self.canvas.create_image(x,y-offset, image = self.image.apple)
        elif color =='black':
            self.canvas.create_image(x,y-offset, image = self.image.capsule)
        elif color =='white':
            self.canvas.create_image(x,y-offset, image = self.image.heart)
        elif color =='orange':
            self.canvas.create_image(x,y-offset, image = self.image.clock)
            
