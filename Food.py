from Snake import Snake
import random
import os

class Food(object):
    
    def __init__(self, grid):
        self.grid = grid
        self.filename='Media/score.txt'
        
    def hasFood(self,location):
        if isinstance(self.grid.grid[Snake.surface][location[0]][location[1]],
                      str):
            return True
        else: return False

    def placeFood(self):
            row = random.randint(0,self.grid.gridSize-1)
            col = random.randint(0,self.grid.gridSize-1)
            surface = random.randint(0,5)
            while(self.grid.grid[surface][row][col]  != 0):
                row = random.randint(0,self.grid.gridSize-1)
                col = random.randint(0,self.grid.gridSize-1)
                surface = random.randint(0,5)
            self.grid.grid[surface][row][col] = self.randomFood()

    def randomFood(self):
        num = random.randint(0,100)
        if ( num <10):
            return 'd'
        elif(num <20):
            return 't'
        elif(num < 25):
            return 'l'
        else: return 'a'

    # the readFile and writeFIle come from class note
    def readFile(self,filename, mode="rt"):
        # rt stands for "read text"
        fin = contents = None
        try:
            fin = open(filename, mode)
            contents = fin.read()
        finally:
            if (fin != None): fin.close()
        return contents

    def writeFile(self,filename, contents, mode="wt"):
        # wt stands for "write text"
        fout = None
        try:
            fout = open(filename, mode)
            fout.write(contents)
        finally:
            if (fout != None): fout.close()
        return True
