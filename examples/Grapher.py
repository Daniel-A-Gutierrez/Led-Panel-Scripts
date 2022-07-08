import math
import ledpanel
import time

#draw coordinate axes
ledpanel.LightUpRow(15,(255,255,255))
ledpanel.LightUpColumn(15 , (255,255,255))


#will graph a function from -2 to 2
def graph ( f, color = (255,0,0) ):
    for i in range(32):
        x = float(i - 15)/8
        y = (f(x)*8) + 15
        ledpanel.SetPixel(i,y,color[0],color[1],color[2])
        time.sleep(.05)

#now you can just pass a function and optionally a color to graph and see what it makes!
def sin2x(x):
    return math.sin(2*x)

graph( sin2x )
time.sleep(2)