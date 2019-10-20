# stone_paper_scissors
print("..stone...")
print("...paper...")
print("...scissors...")

player1 = input("(enter Player 1's choice): ")
print("***NO CHEATING!\n\n" * 20)
player2 = input("(enter Player 2's choice): ")

print("SHOOT!")

if player1 == "stone" and player2 == "scissors":
	print("player1 wins!")
elif player1 == "stone" and player2 == "paper":
	print("player2 wins!")
elif player1 == "paper" and player2 == "stone":
	print("player1 wins!")
elif player1 == "paper" and player2 == "scissors":
	print("player2 wins!")
elif player1 == "scissors" and player2 == "stone":
	print("player2 wins!")
elif player1 == "scissors" and player2 == "paper":
	print("player1 wins!")
elif player1 == player2:
	print("It's a tie!")
else:
	print("something went wrong")
