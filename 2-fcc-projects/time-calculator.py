def add_time(start, duration, day=None):
  DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  days = 0
  hour = int(start.split(':')[0]) + int(duration.split(':')[0])
  min = int(start.split(':')[1][:2]) + int(duration.split(':')[1][:2])
  counter = start.split(' ')[1]

  # calculations
  while min > 59:
    min = min - 60
    hour += 1
  
  while hour > 11:
    hour -= 12
    if counter == 'AM':
      counter = 'PM'
    else:
      counter = 'AM'
      days += 1

  if day != None:
    day_index = DAYS.index(day.capitalize()) + days
    while day_index > 6:
      day_index -= 7
    day = DAYS[day_index]
    
  # output formatting
  if min < 10:
    min = '0' + str(min)
  if hour == 0:
    hour = '12'

  if day is None and days == 0:
    return f'{hour}:{min} {counter}'
  elif day is None and days == 1:
    return f'{hour}:{min} {counter} (next day)'
  elif day is None:
    return f'{hour}:{min} {counter} ({days} days later)'
  elif days == 0:
    return f'{hour}:{min} {counter}, {day}'
  elif days == 1:
    return f'{hour}:{min} {counter}, {day} (next day)'
  else:
    return f'{hour}:{min} {counter}, {day} ({days} days later)'



import unittest
class UnitTests(unittest.TestCase):
  maxDiff = None
  def test_same_period(self):
    actual = add_time("3:30 PM", "2:12")
    expected = "5:42 PM"
    self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12" to return "5:42 PM"')

  def test_different_period(self):
      actual = add_time("11:55 AM", "3:12")
      expected = "3:07 PM"
      self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:55 AM", "3:12" to return "3:07 PM"')

  def test_next_day(self):
      actual = add_time("9:15 PM", "5:30")
      expected = "2:45 AM (next day)"
      self.assertEqual(actual, expected, 'Expected time to end with "(next day)" when it is the next day.')

  def test_period_change_at_twelve(self):
      actual = add_time("11:40 AM", "0:25")
      expected = "12:05 PM"
      self.assertEqual(actual, expected, 'Expected period to change from AM to PM at 12:00')

  def test_twenty_four(self):
      actual = add_time("2:59 AM", "24:00")
      expected = "2:59 AM (next day)"
      self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00" to return "2:59 AM"')

  def test_two_days_later(self):
      actual = add_time("11:59 PM", "24:05")
      expected = "12:04 AM (2 days later)"
      self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05" to return "12:04 AM (2 days later)"')

  def test_high_duration(self):
      actual = add_time("8:16 PM", "466:02")
      expected = "6:18 AM (20 days later)"
      self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02" to return "6:18 AM (20 days later)"')

  def test_no_change(self):
      actual = add_time("5:01 AM", "0:00")
      expected = "5:01 AM"
      self.assertEqual(actual, expected, 'Expected adding 0:00 to return initial time.')

  def test_same_period_with_day(self):
      actual = add_time("3:30 PM", "2:12", "Monday")
      expected = "5:42 PM, Monday"
      self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12", "Monday" to return "5:42 PM, Monday"')

  def test_twenty_four_with_day(self):
      actual = add_time("2:59 AM", "24:00", "saturDay")
      expected = "2:59 AM, Sunday (next day)"
      self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00", "saturDay" to return "2:59 AM, Sunday (next day)"')

  def test_two_days_later_with_day(self):
      actual = add_time("11:59 PM", "24:05", "Wednesday")
      expected = "12:04 AM, Friday (2 days later)"
      self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05", "Wednesday" to return "12:04 AM, Friday (2 days later)"')

  def test_high_duration_with_day(self):
      actual = add_time("8:16 PM", "466:02", "tuesday")
      expected = "6:18 AM, Monday (20 days later)"
      self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02", "tuesday" to return "6:18 AM, Monday (20 days later)"')

if __name__ == "__main__":
  unittest.main()
