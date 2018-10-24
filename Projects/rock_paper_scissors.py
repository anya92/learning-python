from random import randint

print("rock.......")
print("paper......")
print("scissors...")

player = input("(Enter your choice): ").lower()
random_number = randint(0, 2)

if random_number == 0:
  computer = 'rock'
elif random_number == 1:
  computer = 'paper'
else:
  computer = 'scissors'

print(f"The computer plays: {computer}")

if player == computer:
  print("It's a tie.")
elif player == 'rock':
  if computer == 'paper':
    print("Computer wins.")
  else:
    print("You win!") 
elif player == 'paper':
  if computer == 'rock':
    print("You win!")
  else:
    print("Computer wins.")
elif player == 'scissors':
  if computer == 'rock':
    print("Computer wins.")
  else:
    print("You win!")
else:
  print("Please enter a valid value.")
