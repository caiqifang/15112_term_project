# Animation.py

import random
from Tkinter import *

###########################################
# Animation class
###########################################

class Animation(object):
    root = None
    # Override these methods when creating your own animation
    def mousePressed(self, event): pass
    def keyPressed(self, event): pass
    def timerFired(self): pass
    def init(self): pass
    def redrawAll(self): pass
    
    # Call app.run(width,height) to get your app started
    def run(self, width=300, height=300):
        # create the root and the canvas
        root = Tk()
        self.width = width
        self.height = height
        self.timerFiredDelay =30 # milliseconds
        self.canvas = Canvas(root, width=width, height=height)
        self.canvas.pack()
        root.resizable(width=0, height=0)
        Animation.root = root
        # set up events
        def redrawAllWrapper():
            self.canvas.delete(ALL)
            self.redrawAll()
        def mousePressedWrapper(event):
            self.mousePressed(event)
            redrawAllWrapper()
        def keyPressedWrapper(event):
            self.keyPressed(event)
            redrawAllWrapper()
        root.bind("<Button-1>", mousePressedWrapper)
        root.bind("<Key>", keyPressedWrapper)
        # set up timerFired events
        def timerFiredWrapper():
            self.timerFired()
            redrawAllWrapper()
            # pause, then call timerFired again
            self.canvas.after(self.timerFiredDelay, timerFiredWrapper)
        # init and get timerFired running
        self.init()
        timerFiredWrapper()
        # and launch the app
        root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)
