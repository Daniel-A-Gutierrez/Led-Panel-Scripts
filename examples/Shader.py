#shaders are also called 'gpu programs'. Gpu stands for graphics processing unit. 
#Theyre how your computer draws pretty much all the graphics you see,
#from text to minecraft. 

#the basic idea of a shader is some function that takes in information,
#doesnt change any global state, and returns a color.

import time
#import ledpanel
import numpy as np

frameCount = 0


def Run():
    screen = np.zeros((32,32,3),dtype=np.uint8)
    while(True):
        ClearScreen(screen)
        time.sleep(.016)
        for x in range(32):
            for y in range(32):
                screen[y][x] = Rainbow(y,x)
        break
        ledpanel.DrawArray(screen)
    #print(screen)

def ClearScreen(arr):
    arr[::] = 0 

def Circle(row,col):
    u = (row-16)/32 #row now goes from -1 to 1 instead of 0 to 32
    v = (col-16)/32
    size = .25
    if( np.sqrt(u*u+v*v) <= size ):
        return (1,1,1)
    else:
        return (0,0,0)

def Wave(row,col):
    u = (row-16)/32
    v = (col-16)/32
    thickness = .2
    curve = np.sin(u + frameCount/120)
    if(np.abs(curve-v) < thickness):
        return (0,255,0)
    else:
        return (0,0,0)

#rainbows are complicated so the next 2 functions below are just to help this one out
def Rainbow(row,col):
    u = (row-16)/32
    v = (col-16)/32

    #set up the colors for the corners
    TL = np.array([0,255,0])
    TR = np.array([255,0,255])
    BL = np.array([0,0,255])
    BR = np.array([255,255,255])

    coords = np.array([  [-1,1], [1,1], [1,-1], [-1,-1] ])
    p = np.array((u,v))
    
    #we are in the top left
    if(row<col):
        w = getWeights( p, coords[0], coords[1], coords[2] )
        return TL*w[0] + TR*w[1] + BL*w[2]
    #we are in the bottom right
    else:
        w = getWeights( p, coords[1], coords[2], coords[3] )
        return TR*w[0] + BL*w[1] + BR*w[2]
    

def fsign ( p1,  p2,  p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

#if you want to learn more about this : https://www.youtube.com/watch?v=HYAgJN3x4GA
def getWeights( pt , v1, v2 , v3):
    d1 = fsign(pt, v1, v2)
    d2 = fsign(pt, v2, v3)
    d3 = fsign(pt, v3, v1)
    d4 = fsign(v1,v2,v3)
    return [ d2/ d4 , d3/d4 , d1/d4]


Run()