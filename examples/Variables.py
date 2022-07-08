import ledpanel
import time
x = 5
y = 4
ledpanel.SetPixel(x,y,255,255,255)
time.sleep(1)
words = input("What wisdom does the frog of the lake offer?\n")
ledpanel.PrintPanelRGB(words,0,255,0)
