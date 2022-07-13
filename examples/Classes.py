#a class is a template for a structure called an object
#an object has both data , and functions. Heres an example of a class for a bouncy ball

import numpy as np
import ledpanel
import time 


#first we name it
class Ball:

    #init is used automatically to make a ball object from this template
    def __init__(self,row,col,size):
        self.row=row
        self.col=col
        self.size=size
        self.color = [0,0,255]
        self.position = np.array([row,col] , dtype=np.float64)
        self.vel = np.array([3.14159,1.618033], dtype=np.float64)
        self.sprite = np.array( [[self.color]*self.size]*self.size )
    
    #functions like update and draw live inside of the new object
    def update(self,t):
        #this will move the ball and make it bounce on the edges of the panel
        self.position += self.vel * t 
        if( self.position[0] + self.size/2 > 32 and self.vel[0] > 0):
            self.vel[0] = -self.vel[0]
        if( self.position[0] - self.size/2 < 0 and self.vel[0] < 0):
            self.vel[0] = -self.vel[0]
        if( self.position[1] +self.size/2 > 32 and self.vel[1] > 0):
            self.vel[1] = -self.vel[1]
        if( self.position[1] - self.size/2 < 0 and self.vel[1] < 0):
            self.vel[1] = -self.vel[1]
        self.row=np.floor(self.position[0])
        self.col=np.floor(self.position[1])
    
    def draw(self):
        ledpanel.DrawArray( self.row, self.col, self.sprite )

#now we can make an object from the Ball template, and call it ball (lowercase). 
#self is made up so we only have to tell it the row, column, and size, like we asked for in __init__
ball = Ball(16,16,4)
while(True):
    ledpanel.ClearPanel()
    time.sleep(.0333)
    #you can call an objects methods like so
    ball.update(.0333)
    ball.draw()
    break