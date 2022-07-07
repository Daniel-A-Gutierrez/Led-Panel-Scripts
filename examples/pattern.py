from samples.rgb import *
from samples.samplebase import SampleBase
for i in range(0, 32, 2):
        lightUpRow(i, green)
        time.sleep(0.2)
for i in range(0, 32, 2):
        lightUpColumn(i, blue)
        time.sleep(0.2)
