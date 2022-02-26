# progrem for dice_roll
#function cretae random numbers 1 to 6
import random
def number():
	num=random.randint(1, 6)
	return(num)

print("Welcome Dice Game")
while(True):
	print ("Do you want roll the dice ?")
	try:
		value= int(input("enter 1 for roll dice, 2 for exit"))
		if (value==1):
			print(number())
		elif (value==2):
			break
		else:
			print("wrong input")
	except:
		print("Please enter valid inputs")

