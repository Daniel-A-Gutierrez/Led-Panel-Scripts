from io import StringIO
import sys
import time
import argparse
import os
import numpy as np
import PIL.Image
#sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))
from .rgbmatrix import RGBMatrix, RGBMatrixOptions ,graphics


middle="middle"
bottom="bottom"
top="top"
class Panel(object):
    def __init__(self, *args, **kwargs):
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument("-r", "--led-rows", action="store", help="Display rows. 16 for 16x32, 32 for 32x32. Default: 32", default=32, type=int)
        self.parser.add_argument("--led-cols", action="store", help="Panel columns. Typically 32 or 64. (Default: 32)", default=32, type=int)
        self.parser.add_argument("-c", "--led-chain", action="store", help="Daisy-chained boards. Default: 1.", default=1, type=int)
        self.parser.add_argument("-P", "--led-parallel", action="store", help="For Plus-models or RPi2: parallel chains. 1..3. Default: 1", default=1, type=int)
        self.parser.add_argument("-p", "--led-pwm-bits", action="store", help="Bits used for PWM. Something between 1..11. Default: 11", default=11, type=int)
        self.parser.add_argument("-b", "--led-brightness", action="store", help="Sets brightness level. Default: 100. Range: 1..100", default=100, type=int)
        self.parser.add_argument("-m", "--led-gpio-mapping", help="Hardware Mapping: regular, adafruit-hat, adafruit-hat-pwm" , choices=['regular', 'adafruit-hat', 'adafruit-hat-pwm'], type=str)
        self.parser.add_argument("--led-scan-mode", action="store", help="Progressive or interlaced scan. 0 Progressive, 1 Interlaced (default)", default=1, choices=range(2), type=int)
        self.parser.add_argument("--led-pwm-lsb-nanoseconds", action="store", help="Base time-unit for the on-time in the lowest significant bit in nanoseconds. Default: 130", default=130, type=int)
        self.parser.add_argument("--led-show-refresh", action="store_true", help="Shows the current refresh rate of the LED panel")
        self.parser.add_argument("--led-slowdown-gpio", action="store", help="Slow down writing to GPIO. Range: 1..100. Default: 1", choices=range(3), type=int)
        self.parser.add_argument("--led-no-hardware-pulse", action="store", help="Don't use hardware pin-pulse generation")
        self.parser.add_argument("--led-rgb-sequence", action="store", help="Switch if your matrix has led colors swapped. Default: RGB", default="RGB", type=str)
        self.parser.add_argument("--led-pixel-mapper", action="store", help="Apply pixel mappers. e.g \"Rotate:90\"", default="", type=str)
        self.parser.add_argument("--led-row-addr-type", action="store", help="0 = default; 1=AB-addressed panels;2=row direct", default=0, type=int, choices=[0,1,2])
        self.parser.add_argument("--led-multiplexing", action="store", help="Multiplexing type: 0=direct; 1=strip; 2=checker; 3=spiral; 4=ZStripe; 5=ZnMirrorZStripe; 6=coreman; 7=Kaler2Scan; 8=ZStripeUneven (Default: 0)", default=0, type=int)

    def usleep(self, value):
        time.sleep(value / 1000000.0)

    def run(self):
        print("Running")

    def process(self):
        self.args = self.parser.parse_args()

        options = RGBMatrixOptions()

        if self.args.led_gpio_mapping != None:
            options.hardware_mapping = self.args.led_gpio_mapping
            options.rows = self.args.led_rows
            options.cols = self.args.led_cols
            options.chain_length = self.args.led_chain
            options.parallel = self.args.led_parallel
            options.row_address_type = self.args.led_row_addr_type
            options.multiplexing = self.args.led_multiplexing
            options.pwm_bits = self.args.led_pwm_bits
            options.brightness = self.args.led_brightness
            options.pwm_lsb_nanoseconds = self.args.led_pwm_lsb_nanoseconds
            options.led_rgb_sequence = self.args.led_rgb_sequence
            options.pixel_mapper_config = self.args.led_pixel_mapper
        if self.args.led_show_refresh:
          options.show_refresh_rate = 1

        if self.args.led_slowdown_gpio != None:
            options.gpio_slowdown = self.args.led_slowdown_gpio
        if self.args.led_no_hardware_pulse:
          options.disable_hardware_pulsing = True

        self.matrix = RGBMatrix(options = options)

        try:
            # Start loop
            print("Press CTRL-C to stop sample")
            self.run()
        except KeyboardInterrupt:
            print("Exiting\n")
            sys.exit(0)

        return True
#options = RGBMatrixOptions()
#options.hardware_mapping = 'adafruit-hat'
canvas = RGBMatrix()

def ClearPanel():
    canvas.Fill(0,0,0) 

def SetPixel(row,col,r,g,b):
    canvas.SetPixel(row,col,r,g,b)


def DrawArray(row_offset,col_offset,pixels):
    '''
    Pass a numpy array of uint8 as an RGB image to draw it on the panel efficiently
    the panel is 32x32 so it would expect the array to be of size 96x96 
    '''
    img = PIL.Image.fromarray(pixels.astype('uint8'), 'RGB')
    canvas.SetImage(img, row_offset, col_offset)

def DrawImage(row_offset,col_offset,image):
    canvas.SetImage( image, row_offset, col_offset)

green = tuple((0,255,0))
red = tuple((255,0,0))
blue = tuple((0,0,255))
purple  = tuple((80,0,80))
orange = tuple((255,165,0))
yellow = tuple((255,255,0)) 
aqua = tuple((0,255,255))
lime = tuple((128,255,0))
indigo = tuple((75,0,130))
violet = tuple((238,130,238))
pink = tuple((255,20,147))

def LightUpRow(rowNumber, color):
    r, g, b = color
    for x in range (0,32):
        canvas.SetPixel(x, rowNumber, r, g, b)

def LightUpColumn(columnNumber, color):
    r, g, b = color
    for x in range (0,32):
        canvas.SetPixel(columnNumber, x, r, g, b)

def PrintPanelRGB (text, redValue=255, greenValue=0, blueValue=0, position="middle"):
        if position=="top":
                 loc=8
        if position=="middle":
                 loc=17
        if position=="bottom":
                 loc=26
        font = graphics.Font()
        font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x10.bdf")
        old = sys.stdout
        io = StringIO()
        sys.stdout = io
        print(text)
        sys.stdout = old
        text = io.getvalue().rstrip()
        color = graphics.Color(redValue,greenValue,blueValue)
        len = graphics.DrawText(canvas, font,0, loc, color, text)

def ScrollPanelRGB(text, redValue, greenValue, blueValue, timesPassed=5,position="middle"):
        font = graphics.Font()
        font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x10.bdf")
        old = sys.stdout
        io = StringIO()
        sys.stdout = io
        print(text)
        sys.stdout = old
        test = io.getvalue().rstrip()
        color = graphics.Color(redValue, greenValue, blueValue)
        pos = 0
        x = 0
        loc = 0
        clearfunc = ClearTop()
        if position=="top":
            loc=8
        elif position=="middle":
            loc=19
            clearfunc=ClearMiddle()
        elif position=="bottom":
            loc=30
            clearfunc = ClearBottom()
        while (x<timesPassed):
            clearfunc()
            len = graphics.DrawText(canvas, font, pos, loc, color, test)
            pos -= 1
            if (pos + len < 0):
                pos = 32
                x += 1
            time.sleep(0.05)

def ClearTop():
    for x in range (0,32):   
        for y in range (0,11):
            canvas.SetPixel(x, y, 0, 0, 0)

def ClearMiddle():
    for x in range (0,32):   
        for y in range (11,22):
            canvas.SetPixel(x, y, 0, 0, 0)

def ClearBottom():
    for x in range (0,32):   
        for y in range (22,32):
            canvas.SetPixel(x, y, 0, 0, 0)