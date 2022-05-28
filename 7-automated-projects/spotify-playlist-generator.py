import requests, os, spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
DATE = '2000-08-12'
CLIENT_ID = os.environ('CLIENT_ID')
CLIENT_SECRET = os.environ('CLIENT_SECRET')

# obtain list of titles
response = requests.get(f'https://www.billboard.com/charts/hot-100/{DATE}/')
soup = BeautifulSoup(response.text, 'html.parser')
titles = [title.getText().replace('\n', '').replace('\t', '') for title in soup.select('li ul li h3')]

# authentication
sp = spotipy.Spotify(
  auth_manager=SpotifyOAuth(
    scope='playlist-modify-private', 
    redirect_uri='http://example.com', 
    client_id=CLIENT_ID, 
    client_secret = CLIENT_SECRET, 
    show_dialog=True, 
    cache_path='token.txt'
  )
)
user_id = sp.current_user()['id']

# song search
songs = []
year = DATE.split('-')[0]
for song in titles:
  result = sp.search(q=f'track:{song} year:{year}', type='track')
  try:
    songs.append(result['tracks']['items'][0]['uri'])
  except IndexError:
    pass

# playlist creation
playlist = sp.user_playlist_create(user=user_id, name=f'{DATE} Billboard 100', public=False)
sp.playlist_add_items(playlist_id=playlist['id'], items=songs)