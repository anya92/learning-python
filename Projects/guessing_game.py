from random import randint

while True:
  random_num = randint(1, 10)
  guess = int(input("Guess a number between 1 and 10: "))
  while guess != random_num:
    if guess < random_num:
      print("Too low, try again!")
    else:
      print("Too high, try again!")
    guess = int(input("Guess a number between 1 and 10: "))
  print("You guessed it! You won it!")
  play_again = input("Do you want to keep playing? (y/n) ")
  while play_again != 'y' and play_again != 'n':
    play_again = input("Do you want to keep playing? (y/n) ")
  if play_again == 'n':
    break

print("Thanks for playing. Bye!")
