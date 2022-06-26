def arithmetic_arranger(problems, show_ans=False):
  if show_ans:
    out = ['', '', '', '']
  else:
    out = ['', '', '']

  # check for error situations
  if len(problems) > 5:
    return 'Error: Too many problems.'
  
  for problem in problems:
    op = problem.split(' ')[1]
    try:
      n1 = int(problem.split(' ')[0])
      n2 = int(problem.split(' ')[2])
      sn1 = len(str(n1))
      sn2 = len(str(n2))
    except ValueError:
      return 'Error: Numbers must only contain digits.'

    if n1 > 9999 or n2 > 9999:
      return "Error: Numbers cannot be more than four digits."
    elif op not in '+-':
      print(op)
      return "Error: Operator must be '+' or '-'."
    
    # problem formatting & solving
    if op == '+':
      ans = str(n1 + n2)
    else:
      ans = str(n1 - n2)
    
    if sn1 > sn2:
      length = sn1 + 2
    else:
      length = sn2 + 2
    
    out[0] = out[0] + ' ' * (length - sn1) + str(n1) + '    '
    out[1] = out[1] + op + ' ' * (length - sn2 - 1) + str(n2) + '    '
    out[2] = out[2] + '-' * length + '    '
    
    try:
      out[3] = out[3] + ' ' * (length - len(ans)) + ans + '    '
    except IndexError:
      pass
  
  out = [i.rstrip() for i in out]
  return '\n'.join(out).rstrip()



import unittest
class UnitTests(unittest.TestCase):
  maxDiff = None
  def test_two_problems_arrangement1(self):
    actual = arithmetic_arranger(['3801 - 2', '123 + 49'])
    expected = '  3801      123\n-    2    +  49\n------    -----'
    self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["3801 - 2", "123 + 49"]')
  
  def test_two_problems_arrangement2(self):
    actual = arithmetic_arranger(['1 + 2', '1 - 9380'])
    expected = '  1         1\n+ 2    - 9380\n---    ------'
    self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["1 + 2", "1 - 9380"]')
  
  def test_four_problems_arrangement(self):
    actual = arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49'])
    expected = '    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----'
    self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]')
  
  def test_five_problems_arrangement(self):
    actual = arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'])
    expected = '  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------'
    self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]')

  def test_too_many_problems(self):
    actual = arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87'])
    expected = 'Error: Too many problems.'
    self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many problems."')
  
  def test_incorrect_operator(self):
    actual = arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49'])
    expected = "Error: Operator must be '+' or '-'."
    self.assertEqual(actual, expected, '''Expected calling "arithmetic_arranger()" with a problem that uses the "/" operator to return "Error: Operator must be '+' or '-'."''')
  
  def test_too_many_digits(self):
    actual = arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'])
    expected = 'Error: Numbers cannot be more than four digits.'
    self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that has a number over 4 digits long to return "Error: Numbers cannot be more than four digits."')
  
  def test_only_digits(self):
    actual = arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'])
    expected = 'Error: Numbers must only contain digits.'
    self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."')
  
  def test_two_problems_with_solutions(self):
    actual = arithmetic_arranger(['3 + 855', '988 + 40'], True)
    expected = '    3      988\n+ 855    +  40\n-----    -----\n  858     1028'
    self.assertEqual(actual, expected, 'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with ["3 + 855", "988 + 40"] and a second argument of `True`.')
  
  def test_five_problems_with_solutions(self):
    actual = arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)
    expected = '   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028'
    self.assertEqual(actual, expected, 'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with five arithmetic problems and a second argument of `True`.')
  

if __name__ == "__main__":
  unittest.main()
