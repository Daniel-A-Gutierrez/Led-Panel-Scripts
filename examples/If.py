import ledpanel
import time

#a value that is either True or False is called a boolean
toggle= True

#a while loop can run as long as some boolean value given to it is true.
#this one will run forever, unless you stop it! 
print("Type ctrl+c to exit this loop")
while(True):

    #an if statement checks if some boolean is 'true' , and runs some code if it is
    if(toggle):
        ledpanel.Fill(128,128,128)
    else: 
        #it runs the else if the boolean was false. 
        ledpanel.Fill(0,0,0)
    toggle = not toggle
    time.sleep(.5)