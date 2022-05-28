from bs4 import BeautifulSoup
import requests

# prints most upvoted article
response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')

article_titles = [title.getText() for title in soup.find_all(name='a', class_='titlelink')]
article_links = [link.get('href') for link in soup.find_all(name='a', class_='titlelink')]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

max_index = article_upvotes.index(max(article_upvotes))
# print(f"{article_titles[max_index]}\n{article_links[max_index]}")


# creates text file of top 100 movies
response = requests.get('https://www.imdb.com/list/ls055592025/')
soup = BeautifulSoup(response.text, 'html.parser')
article_titles = [title.getText() for title in soup.select('.lister-item-header a')]
with open('3-miscellaneous-modules/web-scraping/movies.txt', mode='w') as file:
  n = 1
  for title in article_titles:
    file.write(f'{n}) {title}\n')
    n += 1