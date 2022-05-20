import pandas
### LIST COMPREHENSION
# 1 - squaring numbers
numbers1 = [1, 2, 3, 5]
squared_numbers = [i ** 2 for i in numbers1]

# 2 - filtering even numbers
numbers2 = [2, 5, 7, 8]
result = [i for i in numbers2 if i%2 == 0]
print(result)

# 3 - data overlap
with open("resource1.txt") as f1:
  f1_data = f1.readlines()

with open("resource2.txt") as f2:
  f2_data = f2.readlines()

result = [int(i) for i in f1_data if i in f2_data]


### DICTIONARY COMPREHENSION
# 1 - example
dict1 = {"student1": 80}
dict2 = {student:score for (student, score) in dict1.items() if score >= 60}

# 2 - exercise 1
sentence = "the Quick Brown Fox jumps over the Lazy Dog."
result = {word: len(word) for word in sentence.split()}

# 3 - exercise 2
celcius = {
  "Monday": 12,
  "Tuesday": 14,
  "Wednesday": 15,
  "Thursday": 14,
  "Friday": 21,
  "Saturday": 22,
  "Sunday": 24,
}
fahrenheit = {day: value * 9/5 + 32 for (day, value) in celcius.items()}
print(fahrenheit)


### PANDAS DATAFRAME COMPREHENSION 
dataframe1 = pandas.DataFrame(celcius)
for (index, row) in dataframe1.iterrows():
  if row.placeholder == "placeholder":
    pass