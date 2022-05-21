b = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
valid = ['1','2','3','4','5','6','7','8','9']
status = 0 
turns = 0

def print_board():
  print(" {} | {} | {} ".format(b[0], b[1], b[2]))
  print("-----------")
  print(" {} | {} | {} ".format(b[3], b[4], b[5]))
  print("-----------")
  print(" {} | {} | {} ".format(b[6], b[7], b[8]))
  if status == 1:
    print("Player 1 has won. Congratulations!")
  elif status == 2:
    print("Player 2 has won. Congratulations!")
  elif status == 3:
    print("The match has ended in a draw. Good game!")

def check():
  global status
  global turns
  if b[0]==b[1]==b[2]=='X' or b[3]==b[4]==b[5]=='X' or b[6]==b[7]==b[8]=='X' or b[0]==b[3]==b[6]=='X' or b[1]==b[4]==b[7]=='X' or b[2]==b[5]==b[8]=='X' or b[0]==b[4]==b[8]=='X' or b[2]==b[4]==b[6]=='X':
    status = 1
  elif b[0]==b[1]==b[2]=='O' or b[3]==b[4]==b[5]=='O' or b[6]==b[7]==b[8]=='O' or b[0]==b[3]==b[6]=='O' or b[1]==b[4]==b[7]=='O' or b[2]==b[5]==b[8]=='O' or b[0]==b[4]==b[8]=='O' or b[2]==b[4]==b[6]=='O':
    status = 2
  elif turns == 9:
    status = 3

def move1():
  x = 'wrong'
  while x not in valid:
    x = input("Player 1, enter your move: ")
    if x not in valid:
      print("Please choose a valid number from 1 to 9.") 
  b[int(x)-1] = 'X'
  global turns
  turns += 1

def move2():
  x = 'wrong'
  while x not in valid:
    x = input("Player 2, enter your move: ")
    if x not in valid:
      print("Please choose a valid number from 1 to 9.") 
  b[int(x)-1] = 'X'
  global turns
  turns += 1

def game():
  while status == 0:
    move1()
    check()
    print_board()
    if status == 0:
      move2()
      check()
      print_board()

print("Welcome to Tic Tac Toe! Note how the boxes in the tic tac toe grid are numbered; you will have to use these board positions to make your move.")
print(" 1 | 2 | 3 ")
print("-----------")
print(" 4 | 5 | 6")
print("-----------")
print(" 7 | 8 | 9 ")
game()