from random import randint

player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score:
    print("*" * 50)
    print(f"Your score: {player_wins} Computer score: {computer_wins}")
    print("rock.......")
    print("paper......")
    print("scissors...")

    player = input("(Enter your choice): ").lower()
    if player == 'quit' or player == 'q':
        break

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
            computer_wins += 1
        else:
            print("You win!")
            player_wins += 1
    elif player == 'paper':
        if computer == 'rock':
            print("You win!")
            player_wins += 1
        else:
            print("Computer wins.")
            computer_wins += 1
    elif player == 'scissors':
        if computer == 'rock':
            print("Computer wins.")
            computer_wins += 1
        else:
            print("You win!")
            player_wins += 1
    else:
        print("Please enter a valid value.")

print("*" * 50)
if (player_wins > computer_wins):
    print("Congrats! You won!")
elif player_wins == computer_wins:
    print("It's a tie.")
else:
    print("Oh no... Computer won.")
