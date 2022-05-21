import random
print("Fill in the following prompts to generate a random, completely secure password.")
a = int(input("How many letters would you like? "))
b = int(input("How many symbols would you like? "))
c = int(input("How many numbers would you like? "))
d = [a, b, c]
x = ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''','0123456789']
out = []

for i in range(3):
  while d[i] > 0:
    out.append(x[i][random.randint(0, len(x[i])-1)])
    d[i] -= 1

random.shuffle(out)
print("Here is your password: ", ''.join(out))