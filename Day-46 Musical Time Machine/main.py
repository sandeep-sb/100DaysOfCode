from pprint import pprint
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("What year would you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
response.raise_for_status()
website_tag = response.text

soup = BeautifulSoup(website_tag, "html.parser")
songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_name = [song.getText() for song in songs]
print(song_name)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="07bddc3b036f4c2e9ae3ace59230ba46",
                                               client_secret="4edce2c290c64fe2b975d5aef77385b3",
                                               scope="playlist-modify-private",
                                               redirect_uri="http://example.com",
                                               username="3yncuctsqeejh192ppxuk0vur",
                                               cache_path="token.txt"))
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_name:
    result = sp.search(f"track:{song}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
print(song_uris)

playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist_id)

sp.playlist_add_items(playlist_id=playlist_id["id"], items=song_uris, position=None)