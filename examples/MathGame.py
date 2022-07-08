from ledpanel import *
import random
score = 0
questions = 5
for i in range(questions):
	num1 = random.randint(0, 9)
	num2 = random.randint(0, 9)
	PrintPanelRGB(" " + str(num1) + "+" + str(num2) + "=", 0,0,255, "middle")
	x = int(input("Answer: "))
	ClearPanel()
	PrintPanelRGB("  " + str(x) + "?", 0,0,255, "middle")
	time.sleep(1)
	if (x == num1 + num2):
		ScrollPanelRGB("Correct!", 0,255,0, 1, "middle")
		score = score + 1
	else:
		ScrollPanelRGB("Incorrect!", 255,0,0, 1, "middle")
if(score > 3):
	ScrollPanelRGB("Congratulations! You scored " + str(score) + "/" + str(questions), 0,255,0, 1, "middle")
else:
	ScrollPanelRGB("Better Luck Next Time... You sored " + str(score) + "/" + str(questions), 255,0,0, 1, "middle") 
