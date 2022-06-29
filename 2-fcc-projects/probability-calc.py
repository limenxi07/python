import copy, random

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      self.contents += [key] * value
  
  def draw(self, balls):
    if balls > len(self.contents):
      return self.contents
    else:
      drawn = random.sample(self.contents, balls)
      for i in drawn:
        self.contents.remove(i)
      return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  total = 0
  req = []
  for key, value in expected_balls.items():
    req += [key] * value
  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn = hat_copy.draw(num_balls_drawn)
    req_count = 0
    for i in req: # lengthy code but could not think of how to better handle repeated colours
      if i in drawn:
        drawn.remove(i)
        req_count += 1
    if req_count == len(req):
      total += 1
  return total / num_experiments





import unittest
random.seed(95)
class UnitTests(unittest.TestCase):
    maxDiff = None
    def test_hat_class_contents(self):
        hat = Hat(red=3,blue=2)
        actual = hat.contents
        expected = ["red","red","red","blue","blue"]
        self.assertEqual(actual, expected, 'Expected creation of hat object to add correct contents.')

    def test_hat_draw(self):
        hat = Hat(red=5,blue=2)
        actual = hat.draw(2)
        expected = ['blue', 'red']
        self.assertEqual(actual, expected, 'Expected hat draw to return two random items from hat contents.')
        actual = len(hat.contents)
        expected = 5
        self.assertEqual(actual, expected, 'Expected hat draw to reduce number of items in contents.')

    def test_prob_experiment(self):
        hat = Hat(blue=3,red=2,green=6)
        probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
        actual = probability
        expected = 0.272
        self.assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')
        hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
        probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
        actual = probability
        expected = 1.0
        self.assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')


if __name__ == "__main__":
    unittest.main()