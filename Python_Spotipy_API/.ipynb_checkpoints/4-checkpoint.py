import urllib.request

import librosa
import requests
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from IPython.display import Audio

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="###", client_secret="###"))

# This function return a string that contain ID of element embed in link.

def get_ID(link):
    
   return (link.split("/")[-1]).split("?")[0]


get_ID("https://open.spotify.com/track/4reyAmWUdNFX6F70rX3ZoS?si=8a43b65ca49f47e0")


access_token = 'BQArUPycyg3aSkJOXhZNL9-Mm1osdIgyrgnkOc1hCYsoLRmy9hmgNeqmo5BqLD1TKlH5_dxdaaKy-YZhufDr3LV5WMwVSGdOCGJw1xUNLY1YsIgGkmPxw_jMVKG4vQhjUU8-BMEuPul4D0DmT3mzZA5D_P5D02SCaf_o-pf3i9qAF3N_gydXvqy-ocR4nxQIGbE61Hi91KjAJQ'
headers = {'Authorization': 'Bearer ' + access_token}

track_name = 'Scream of the Butterfly'
artist_name = 'Acid Bath'

query = f'{track_name} {artist_name}'
url = f'https://api.spotify.com/v1/search?q={query}&type=track&market=US&limit=1'

response = requests.get(url, headers=headers)
data = response.json()
track_id = data['tracks']['items'][0]['id']

url = f'https://api.spotify.com/v1/tracks/{track_id}'
response = requests.get(url, headers=headers)
data = response.json()
preview_url = data['preview_url']


filename = 'Music Theory and Its Applications\screamofthebutterfly.mp3'
y, sr = librosa.load(filename, duration=30)
S_full, phase = librosa.magphase(librosa.stft(y))
Audio(data=y[10*sr:15*sr], rate=sr)