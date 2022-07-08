from ledpanel import *
import time
for i in range(0, 32, 2):
    LightUpRow(i, green)
    time.sleep(0.2)
for i in range(0, 32, 2):
    LightUpColumn(i, blue)
    time.sleep(0.2)
