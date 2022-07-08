import ledpanel
import time

#simple
for i in range(32):
    ledpanel.LightUpColumn(i,ledpanel.green)
    time.sleep(.05)

#the loop contents are indented. Stuff afterward is not indented
ledpanel.ClearPanel()

#count up from 1 to 32 (starts at 1, ends at 31)
for i in range(1,32): 
    ledpanel.LightUpColumn(i, ledpanel.blue) #light up a column
    ledpanel.LightUpColumn(i-1, (0,0,0)) #black out the old one
    time.sleep(.05)

#count down from 31 to 0
for i in range(31,0,-1): 
    ledpanel.LightUpColumn(i, ledpanel.blue)
    ledpanel.LightUpColumn(i+1 , ledpanel.blue)
    time.sleep(.05)

#loops can go indefinitely
usertxt = input("Type 'exit' or ctrl+c to exit")
while(usertxt != "exit"):
    ledpanel.PrintPanelRGB(usertxt)
    time.sleep(1)

