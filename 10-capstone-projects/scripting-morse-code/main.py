TEXT_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
MORSE_TO_TEXT = {value:key for key, value in TEXT_TO_MORSE.items()}

def operate():
  dirn = True
  while dirn:
    dirn = input("Enter 'ENG' to convert English into Morse Code, and enter 'MOR' to convert Morse Code into English. ")
    if dirn == 'ENG':
      msg = input('Enter your message:\n').upper()
      out = []
      for i in msg:
        if i in TEXT_TO_MORSE:
          out.append(f'{TEXT_TO_MORSE[i]} ')
        elif i == ' ':
          out.append(' / ')
        else:
          out.append(i)
      print('Your translated message:\n', ''.join(out))
      break
    elif dirn == 'MOR':
      msg = input('Enter your message:\n').split(' ')
      print(msg)
      out = []
      for i in msg:
        if i in MORSE_TO_TEXT:
          out.append(MORSE_TO_TEXT[i])
        elif i == '/':
          out.append(' ')
        else:
          out.append(i)
      print('Your translated message:\n', ''.join(out))
      break
    else:
      print('Please enter a valid command.')

if __name__ == '__main__':
  cont = True
  while cont:
    operate()
    cont_boo = input('Would you like to translate another message? (y/n) ')
    if cont_boo == 'n':
      cont = False
