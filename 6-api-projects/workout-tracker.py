import requests, os
from datetime import datetime as dt
APP_ID = os.environ('APP_ID')
API_KEY = os.environ('API_KEY')
GENDER = 'F'
WEIGHT = '50'
HEIGHT = '170'
AGE = 30
SHEET_ENDPOINT = os.environ('SHEET_ENDPOINT')
USERNAME = os.environ('USERNAME')
PASSWORD = os.environ('PASSWORD')

# FETCH EXERCISE STATS
headers = {
  'x-app-id': APP_ID,
  'x-app-key': API_KEY
}
params = {
  'query': input("Enter exercises: "),
  'gender': GENDER,
  'weight_kg': WEIGHT,
  'height_cm': HEIGHT,
  'age': AGE
}
response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=params, headers=headers)
result = response.json()
print(result)

# SAVE DATA TO SHEETS
for exercise in result['exercises']:
  params = {
    'workout': {
      'date': dt.now().strftime('%d/%m/%Y'),
      'time': dt.now().strftime('%X'),
      'exercise': exercise['name'].title(),
      'duration': exercise['duration_min'],
      'calories': exercise['nf_calories']
    }
  }
response = requests.post(SHEET_ENDPOINT, json=params, auth=(USERNAME, PASSWORD))