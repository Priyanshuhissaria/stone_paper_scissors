from random import randint
print("stone...")
print("Paper...")
print("Scissors...")

player = input("Player, make your move: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
	computer = "stone"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"

print(f"Computer plays {computer}" )

if player == computer:
	print("It's a tie!")
elif player == "stone":
	if computer == "scissors":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "paper":
	if computer == "stone":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	else:
		print("computer wins!")	
else:
	print("Please enter a valid move!")
