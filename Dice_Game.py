import random
min = 1
max = 6

Roll_Dice = "Yes"

while Roll_Dice == "Yes" or Roll_Dice == "Y":
	print ("Rolling the dice")
	print ("The Value is:")
	print (random.randint(min,max))
	print (random.randint(min,max))
	break

Roll_Dice = input("Do you want to roll the dice again?")