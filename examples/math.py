from samples.rgb import *
import random
score = 0
questions = 5
for i in range(questions):
	num1 = random.randint(0, 9)
	num2 = random.randint(0, 9)
	printPanel(" " + str(num1) + "+" + str(num2) + "=", blue, middle)
	x = int(input("Answer: "))
	clearPanel()
	printPanel("  " + str(x) + "?", blue, middle)
	time.sleep(1)
	if (x == num1 + num2):
		scrollPanel("Correct!", green, 1, middle)
		score = score + 1
	else:
		scrollPanel("Incorrect!", red, 1, middle)
if(score > 3):
	scrollPanel("Congratulations! You scored " + str(score) + "/" + str(questions), green, 1, middle)
else:
	scrollPanel("Better Luck Next Time... You sored " + str(score) + "/" + str(questions), red, 1, middle) 
