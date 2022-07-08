import ledpanel

#dictionaries can be used to map one thing to another. instead of just numbers, you can use whatever you like
phone_book = {"bobert" : 8634143093 , "hoebert" : 1234567890 , "sam" : 4}

ledpanel.ScrollPanelRGB(str(phone_book["hoebert"]) , 0,129,32,1)

#you can use a loop to check everything in the phone book like so
for name in phone_book.keys():
    ledpanel.ScrollPanelRGB(str(phone_book[name]) , 10,129,132,1)