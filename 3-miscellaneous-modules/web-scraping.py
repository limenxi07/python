from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')

article_titles = [title.getText() for title in soup.find_all(name='a', class_='titlelink')]
article_links = [link.get('href') for link in soup.find_all(name='a', class_='titlelink')]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

max_index = article_upvotes.index(max(article_upvotes))
print(f"{article_titles[max_index]}\n{article_links[max_index]}")
