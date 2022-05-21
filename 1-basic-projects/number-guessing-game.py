import random

def operate(answer, lives):
  x = int(input("Make a guess: "))
  if x == answer and lives > 1:
    print(f"Congratulations, you've chosen the correct number with {lives} lives remaining!")
    lives = 0
  elif x == answer and lives == 1:
    print(f"Congratulations, you've chosen the correct number with {lives} life remaining!")
    lives = 0
  elif x > answer and lives > 2:
    lives -= 1
    print(f"Your guess was too high, try again. You have {lives} lives remaining.")
  elif x > answer and lives == 2:
    lives -= 1
    print(f"Your guess was too high, try again. You have {lives} life remaining.")
  elif x > answer and lives == 1:
    lives -= 1
    print(f"Your guess was too high and you've ran out of guesses. Too bad!")
  elif x < answer and lives > 2:
    lives -= 1
    print(f"Your guess was too low, try again. You have {lives} lives remaining.")
  elif x < answer and lives == 2:
    lives -= 1
    print(f"Your guess was too low, try again. You have {lives} life remaining.")
  elif x < answer and lives == 1:
    lives -= 1
    print(f"Your guess was too low and you've ran out of guesses. Too bad!")
  return lives

def game():
  answer = random.randint(1, 100)
  print("Welcome to the number guessing game! A number between 1 and 100 was chosen.")
  d = input("Choose a difficulty (easy/hard): ")
  if d[0] == "e":
    lives = 10
  elif d[0] == "h":
    lives = 5
  while lives > 0:
    lives = operate(answer, lives)

game()