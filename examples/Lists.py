import ledpanel
# you can make a 'list' of stuff , and refer to it by its place in the list (0, 1, 2 or 3)
my_stuff = ["apple", "rainbow", "fireball", "russia"]

ledpanel.ScrollPanelRGB(my_stuff[0],255,255,255,1) #print the 0th thing in the list
ledpanel.ScrollPanelRGB(my_stuff[1],255,255,255,1) #print the 1th thing in the list
ledpanel.ScrollPanelRGB(my_stuff[2],255,255,255,1) #etc
ledpanel.ScrollPanelRGB(my_stuff[3],255,255,255,1)

#instead of doing it manually, usually you should use a loop
for i in range(len(my_stuff)):
    ledpanel.ScrollPanelRGB(my_stuff[i],255,255,255,1)

#or if you dont need to modify the list it can become even simpler
for thing in my_stuff:
    ledpanel.ScrollPanelRGB(thing,255,255,255,1)
