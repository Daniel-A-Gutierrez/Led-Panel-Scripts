import ledpanel
import time
#parameter names (r=128 instead of just '128') are provided 
#for clarity and are not strictly necessary

ledpanel.Fill(r=28,g=90,b=55) 

time.sleep(1)#wait for 1 second

ledpanel.ClearPanel()

ledpanel.LightUpColumn(columnNumber=3, color = (129,33,51))

ledpanel.LightUpRow(rowNumber=3 , color=(99,81,31))

ledpanel.PrintPanelRGB(text="Stuff", redValue=51, greenValue=151, blueValue=51)

ledpanel.ScrollPanelRGB("more stuff",255,255,255,1)

ledpanel.SetPixel(row=16,col=16,r=180,g=180,b=33)

time.sleep(5)


##Advanced##

import numpy as np
from PIL import Image

#draw a numpy array of pixels to the led panel 
square = np.array([
    [[255,0,0] , [0,255,0]],
    [[0,0,255] , [255,0,0]]],
    dtype=np.uint8)
ledpanel.DrawArray(row_offset=10,col_offset=10,pixels=square)
time.sleep(3) 

#convert the array to an image first for better performance
squareImg = Image.fromarray(square.astype('uint8'), mode="RGB")
ledpanel.DrawImage(24,24,squareImg)

#scale the image
biggerSquareImg = squareImg.resize((6,6))
ledpanel.DrawImage(0,0,biggerSquareImg)

#rotate the image
for i in range(720):
    ledpanel.DrawImage(15,15,biggerSquareImg.rotate(i))
    time.sleep(.01)

time.sleep(1)