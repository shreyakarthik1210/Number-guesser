import random
topNum = int(input("Please type the maximum number you would like to have in the game: "))
number = random.randint(1,topNum)
while True:
	userInput = input("Please type in your guess for the random number: ")
	if int(userInput) == number:
		print("You got the right number!")
		break;
	elif int(userInput) > number:
		print("The number is lower.")
	else:
		print("The number is higher.")