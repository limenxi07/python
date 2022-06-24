## 1. Arithmetic formatter
The arithmetic_arranger() function receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. When a second optional argument is set to true, the answers are displayed.
- The function accepts a maximum of 5 problems. 
- The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error.
- Each operand should only contain digits and should be a maximum of 4 digits. 

## 2. Time calculator
The add_time() function takes in the following parameters, adds the duration time to the start time and returns the result. 
- a start time in the 12-hour clock format (ending in AM or PM)
- a duration time that indicates the number of hours and minutes
- (optional) a starting day of the week, case sensitive
#### Usage:
- If the result is not on the same day, the program will show (n days later) after the time, where "n" is the number of days later. 
- If the function is given the optional starting day of the week parameter, the output will display the day of the week of the result. 
- The function does not make use of any python libraries. 

## 3. Budget app
The Category class instantiates objects based on different budget categories, and has an instance variable 'ledger' that is a list. The class contains the following methods:
- 'deposit': accepts an amount and description (defaults to an empty string); appends an object to the ledger list. 
- 'withdraw': accepts an amount and description (defaults to an empty string); amount is stored in the ledger as a negative number, and returns a boolean indicating whether the withdrawal took place. 
- 'get_balance': returns the current balance of the budget category based on the deposits and withdrawals that have occurred. 
- 'transfer': accepts an amount and another budget category; withdraws the amount and deposits it to the other budget category, and returns and boolean indicating whether the transfer took place.
- 'check_funds': accepts an amount; returns False if the amount is greater than the balance of the budget category. 
#### Budget object displays:
- A title line of 30 characters where the name of the category is centred in a line of * characters. 
- A list of items on the ledger, showing the description (max 23 characters) and the amount (max 7 characters).
- A line displaying the category total.
#### Spending chart function:
The create_spend_chart() function takes a list of categories and returns a string that is a bar chart. 
- Calculates the percentage spent by category (according to only withdrawals, not deposits), with 0-100 as the y-axis. The height of each bar is rounded down to the nearest 10.
- Each category name is written vertically below the bar. 

## 4. Polygon area calculator
#### Rectangle class
The Rectangle class is initialised with width and height attributes. The class contains the following methods:
- 'set_width'
- 'set_height'
- 'get_area'
- 'get_perimeter'
- 'get_diagonal'
- 'get_picture': returns a string that represents the shape using lines of '*', with the number of lines equal to the height and the number of '*' in each line equal to the width (max 50 for height/width).
- 'get_amount_inside': takes another shape as an argument; returns the number of times the passed in shape could fit inside the shape (with no rotations). 
#### Square class
The Square class, a subclass of Rectangle, is initialised with a single side length. It contains a 'set_side' method and accesses the Rectangle class methods, with 'set_width' and 'set_height' setting both the width and height.


## 5. Probability calculator


Project ideas by FreeCodeCamp.