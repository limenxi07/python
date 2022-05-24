import requests, datetime as dt
USERNAME = 'kahjsdfkjashdf'
TOKEN = 'akjsdhfkajsdfasdjkf'
GRAPH = 'graph1'
HEADERS = {"X-USER-TOKEN": TOKEN}

user_params = { # create a user
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}
response = requests.post(url="https://pixe.la/v1/users", json=user_params)

graph_params = { # create a graph
  "id": GRAPH,
  'name': 'Reading graph',
  'unit': 'no. of minutes',
  'type': 'int',
  'color': 'ajisai'
}
requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs", json=graph_params, headers=HEADERS)

post_params = { # create a pixel
  "date": dt.datetime.now().strftime("%Y%m%d"),
  'quantity': '45'
}
requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH}", json=post_params, headers=HEADERS)

update_params = { # update a pixel
  'quantity': '90'
}
requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH}/20220524", json=update_params, headers=HEADERS)

requests.post(url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH}/20220524", headers=HEADERS) # delete a pixel