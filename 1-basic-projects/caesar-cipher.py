s = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encode():
  x = input("Type your message:\n")
  n = int(input("Input your shift number (1-25): "))
  out = []
  for i in x:
    if i in s:
      out.append(s[s.index(i) + n])
    elif i in c:
      out.append(c[c.index(i) + n])
    else:
      out.append(i)
  print("Your encoded result: " + ''.join(out))

def decode():
  x = input("Type your message:\n")
  n = int(input("Input your shift number (1-25): "))
  out = []
  for i in x:
    if i in s:
      out.append(s[s.index(i) - n])
    elif i in c:
      out.append(c[c.index(i) - n])
    else:
      out.append(i)
  print("Your decoded result: " + ''.join(out))

def operate():
  x = input("Type 'encode' to encrypt, or type 'decode' to decrypt: ").lower()
  if x[0] == "e":
    encode()
  elif x[0] == "d":
    decode()
  else: 
    print("Please enter a suitable word.")

operate()
x = input("Type 'yes' if you want to go again, or say no if otherwise.\n").lower()
if x[0] == "y":
  operate()