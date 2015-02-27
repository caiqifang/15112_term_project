import random
import math

class MyCloud(object):
    cloudList = []
    canvas = None
    # the size of cloud = length, which should less than 60 pix
    
    def __init__(self,canvas):
        MyCloud.canvas = canvas
        self.createCloud()
        MyCloud.cloudList.append(self)
        
    def createCloud(self):
        self.cx = random.randint(350,430)
        self.cy = random.randint(150,250)
        if( self.cx >400):
            self.dir = random.randint(0,90)
        else: self.dir = random.randint(90,180)
        
        self.length = random.randint(0,20)
        self.rate = random.randint(3,5)
    
    def offScreen(self):
        if ( self.cx - self.length) > 600:
            return True
        elif ( self.cy + self.length) < 0:
            return True
        elif ( self.cx + 5*self.length) < 0:
            return True
        elif ( self.cy - 2*self.length ) > 400:
            return True
        elif (self.length > 50 ):
            return True
        else:
            return False    
    
    @classmethod
    def grow(cls):
        for cloud in MyCloud.cloudList:
            cloud.cx += cloud.rate*math.cos((float(cloud.dir)/180)* math.pi)
            cloud.cy -= cloud.rate*math.sin((float(cloud.dir)/180)* math.pi)
            cloud.length += 0.5
            if( cloud.offScreen()):
                MyCloud.cloudList.remove(cloud)
                MyCloud(MyCloud.canvas)
                
                
    @classmethod
    def drawCloud(cls):
        for c in MyCloud.cloudList:
            cx = c.cx
            cy = c.cy
            length = c.length
            
            c.canvas.create_oval(cx-length, cy - length,
                                    cx+length, cy + length, fill = 'white',
                                    width = 0)
            c.canvas.create_oval(cx, cy - 2*length,
                                    cx+2*length, cy, fill = 'white',
                                    width = 0)
            c.canvas.create_oval(cx+length, cy - 3*length/2,
                                    cx+3*length, cy + length/2, fill = 'white',
                                    width = 0)
            c.canvas.create_oval(cx+2*length, cy - 4*length/3,
                                    cx+4*length, cy + 2*length/3, fill = 'white',
                                    width = 0)
            c.canvas.create_oval(cx, cy - length,
                                    cx+3*length, cy + length, fill = 'white',
                                    width = 0)
            c.canvas.create_oval(cx+3*length, cy - length,
                                    cx+5*length, cy + length/3, fill = 'white',
                                    width = 0)