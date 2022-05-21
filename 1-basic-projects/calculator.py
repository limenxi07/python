cont = 'n'
v = 0

def operate(n1, p, n2):
  global v
  if p == "+":
    v = n1 + n2
    print(f"{n1} + {n2} = {v}")
  elif p == "-":
    v = n1 - n2
    print(f"{n1} - {n2} = {v}")
  elif p == "*":
    v = n1 * n2
    print(f"{n1} * {n2} = {v}")
  elif p == "/":
    v = n1 / n2
    print(f"{n1} / {n2} = {v}")

while True:
  if cont == 'n':
    n1 = float(input("Enter the first number: "))
    p = input("Enter the operation (+, -, * or /): ")
    n2 = float(input("Enter the second number: "))
    operate(n1, p, n2)
    cont = input(f"Type 'y' to continue calculating with {v}, or type 'n' to start a new calculation: ")
  else:
    p = input("Enter the operation (+, -, * or /): ")
    n2 = float(input("Enter the second number: "))
    operate(v, p, n2)
    cont = input(f"Type 'y' to continue calculating with {v}, or type 'n' to start a new calculation: ")