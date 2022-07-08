import ledpanel
import time 
#data in python can be a few different types.

#text is called a 'string'. we denote it with quotes
mytext = "banana boat"
ledpanel.PrintPanelRGB(mytext)
#you can make a string out of other things by using str(other thing)

#integers are whole numbers, you can do math with them
x = 5
y = 3 + x*x
ledpanel.PrintPanelRGB(str(x))

#floats are numbers with decimals. 
z = 5.5 * 3.14159
ledpanel.PrintPanelRGB(str(z), 33)

#booleans are true or false values. They can control what code runs using if statements!
b = False
if( not b ):
    ledpanel.Fill(55,244,19)
    time.sleep(1)
    ledpanel.ClearPanel()

if( b ):
    ledpanel.Fill(99,44,99)
    time.sleep(1)
    ledpanel.ClearPanel()

#these are just some of the basic types in python , you can make your own new types out of these!