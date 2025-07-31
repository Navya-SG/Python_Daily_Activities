import random
val = random.randint(1,100)
while True:
	guess = int(input("Guess the number"))
	if guess < val:
		print("Too low")
	elif guess > val:
		print("Too high")
	else:
		print("Correct!")
		break