class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []
  
  def __str__(self):
    n = round((30 - len(self.name))/2)
    history = ''
    for i in self.ledger:
      width = max(len(str(j['amount'])) for j in self.ledger) + 23
      text = i['description'][:23]
      cost = str(round(i['amount'], 2))[:7]
      if cost[-3] != '.':
        cost += '0'
      history += f"{text}{' ' * (width - len(text) - len(cost))} {cost}\n"
    return f'{"*" * n}{self.name}{"*" * n}\n{history}Total: {self.get_balance()}'

  def deposit(self, amount, description=''):
    self.ledger.append({'amount': float(amount), 'description': description})
  
  def check_funds(self, amount):
    return float(amount) <= self.get_balance()

  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({'amount': -float(amount), 'description': description})
      return True
    else:
      return False
  
  def get_balance(self):
    total = 0
    for i in self.ledger:
      total += i['amount']
    return total
  
  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f'Transfer to {category.name}')
      category.deposit(amount, f'Transfer from {self.name}')
      return True
    else:
      return False
  


def create_spend_chart(list):
  chart = ['Percentage spent by category', '100| ', ' 90| ', ' 80| ', ' 70| ', ' 60| ', ' 50| ', ' 40| ', ' 30| ', ' 20| ', ' 10| ', '  0| ']

  # data processing
  categories = []
  for category in list:
    spent = 0
    for i in category.ledger:
      if i['amount'] < 0:
        spent += abs(i['amount'])
    categories.append({'name': category.name, 'spent': spent})
  total = sum(i['spent'] for i in categories)
  for i in categories:
    i['percentage'] = int((i['spent']/total) * 10)
  
  # chart formatting
  for i in range(1, 12):
    for category in categories:
      if category['percentage'] >= 11 - i:
        chart[i] += 'o  '
      else:
        chart[i] += '   '

  # label formatting
  chart.append('    ' + '-' * (len(categories) * 3 + 1))
  length = max(len(i['name']) for i in categories)
  chart += length * ['     ']
  for i in range(length):
    for category in categories:
      if len(category['name']) > i:
        chart[13+i] += (category['name'][i] + '  ')
      else:
        chart[13+i] += '   '

  return '\n'.join(chart) 




import unittest
class UnitTests(unittest.TestCase):
    maxDiff = None
    def setUp(self):
        self.food = Category("Food")
        self.entertainment = Category("Entertainment")
        self.business = Category("Business")

    def test_deposit(self):
        self.food.deposit(900, "deposit")
        actual = self.food.ledger[0]
        expected = {"amount": 900, "description": "deposit"}
        self.assertEqual(actual, expected, 'Expected `deposit` method to create a specific object in the ledger instance variable.')

    def test_deposit_no_description(self):
        self.food.deposit(45.56)
        actual = self.food.ledger[0]
        expected = {"amount": 45.56, "description": ""}
        self.assertEqual(actual, expected, 'Expected calling `deposit` method with no description to create a blank description.')

    def test_withdraw(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        actual = self.food.ledger[1]
        expected = {"amount": -45.67, "description": "milk, cereal, eggs, bacon, bread"}
        self.assertEqual(actual, expected, 'Expected `withdraw` method to create a specific object in the ledger instance variable.')

    def test_withdraw_no_description(self):
        self.food.deposit(900, "deposit")
        good_withdraw = self.food.withdraw(45.67)
        actual = self.food.ledger[1]
        expected = {"amount": -45.67, "description": ""}
        self.assertEqual(actual, expected, 'Expected `withdraw` method with no description to create a blank description.')
        self.assertEqual(good_withdraw, True, 'Expected `withdraw` method to return `True`.')

    def test_get_balance(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        actual = self.food.get_balance()
        expected = 854.33
        self.assertEqual(actual, expected, 'Expected balance to be 854.33')

    def test_transfer(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        transfer_amount = 20
        food_balance_before = self.food.get_balance()
        entertainment_balance_before = self.entertainment.get_balance()
        good_transfer = self.food.transfer(transfer_amount, self.entertainment)
        food_balance_after = self.food.get_balance()
        entertainment_balance_after = self.entertainment.get_balance()
        actual = self.food.ledger[2]
        expected = {"amount": -transfer_amount, "description": "Transfer to Entertainment"}
        self.assertEqual(actual, expected, 'Expected `transfer` method to create a specific ledger item in food object.')
        self.assertEqual(good_transfer, True, 'Expected `transfer` method to return `True`.')
        self.assertEqual(food_balance_before - food_balance_after, transfer_amount, 'Expected `transfer` method to reduce balance in food object.')
        self.assertEqual(entertainment_balance_after - entertainment_balance_before, transfer_amount, 'Expected `transfer` method to increase balance in entertainment object.')
        actual = self.entertainment.ledger[0]
        expected = {"amount": transfer_amount, "description": "Transfer from Food"}
        self.assertEqual(actual, expected, 'Expected `transfer` method to create a specific ledger item in entertainment object.')

    def test_check_funds(self):
        self.food.deposit(10, "deposit")
        actual = self.food.check_funds(20)
        expected = False
        self.assertEqual(actual, expected, 'Expected `check_funds` method to be False')
        actual = self.food.check_funds(10)
        expected = True
        self.assertEqual(actual, expected, 'Expected `check_funds` method to be True')

    def test_withdraw_no_funds(self):
        self.food.deposit(100, "deposit")
        good_withdraw = self.food.withdraw(100.10)
        self.assertEqual(good_withdraw, False, 'Expected `withdraw` method to return `False`.')

    def test_transfer_no_funds(self):
        self.food.deposit(100, "deposit")
        good_transfer = self.food.transfer(200, self.entertainment)
        self.assertEqual(good_transfer, False, 'Expected `transfer` method to return `False`.')

    def test_to_string(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        self.food.transfer(20, self.entertainment)
        actual = str(self.food)
        expected = f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
        self.assertEqual(actual, expected, 'Expected different string representation of object.')

    def test_create_spend_chart(self):
        self.food.deposit(900, "deposit")
        self.entertainment.deposit(900, "deposit")
        self.business.deposit(900, "deposit")
        self.food.withdraw(105.55)
        self.entertainment.withdraw(33.40)
        self.business.withdraw(10.99)
        actual = create_spend_chart([self.business, self.food, self.entertainment])
        expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
        self.assertEqual(actual, expected, 'Expected different chart representation. Check that all spacing is exact.')

if __name__ == "__main__":
    unittest.main()