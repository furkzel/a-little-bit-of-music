import urllib.request

import librosa
import librosa.display
import requests
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from IPython.display import Audio
import numpy as np
import matplotlib.pyplot as plt

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="###", client_secret="###"))

# This function return a string that contain ID of element embed in link.

def get_ID(link):
    
   return (link.split("/")[-1]).split("?")[0]


get_ID("https://open.spotify.com/track/4reyAmWUdNFX6F70rX3ZoS?si=8a43b65ca49f47e0")

############################################################################################################

access_token = '###'
headers = {'Authorization': 'Bearer ' + access_token}

track_name = 'Scream of the Butterfly'
artist_name = 'Acid Bath'

query = f'{track_name} {artist_name}'
url = f'https://api.spotify.com/v1/search?q={query}&type=track&market=US&limit=1'

response = requests.get(url, headers=headers)
data = response.json()
track_id = data['tracks']['items'][0]['id']

url = f'https://api.spotify.com/v1/tracks/{track_id}'
preview_url = data['preview_url']

############################################################################################################

filename = '###'
y, sr = librosa.load(filename, duration=30)
S_full, phase = librosa.magphase(librosa.stft(y))
idx = slice(*librosa.time_to_frames([10, 15], sr=sr))
fig, ax = plt.subplots()
img = librosa.display.specshow(librosa.amplitude_to_db(S_full[:, idx], ref=np.max), y_axis='log', x_axis='time', sr=sr, ax=ax)
fig.colorbar(img, ax=ax)
ax.set(title='Power spectrogram')

S_filter = librosa.decompose.nn_filter(S_full, aggregate=np.median, metric='cosine', width=int(librosa.time_to_frames(2, sr=sr)))
S_filter = np.minimum(S_full, S_filter)

margin_i, margin_v = 2, 10
power = 2

mask_i = librosa.util.softmask(S_filter, margin_i * (S_full - S_filter), power=power)
mask_v = librosa.util.softmask(S_full - S_filter, margin_v * S_filter, power=power)

S_foreground = mask_v * S_full
S_background = mask_i * S_full

fig, ax = plt.subplots(nrows=3, sharex=True, sharey=True)
img = librosa.display.specshow(librosa.amplitude_to_db(S_full[:, idx], ref=np.max), y_axis='log', x_axis='time', sr=sr, ax=ax[0])
ax[0].set(title='Full spectrum')
ax[0].label_outer()

librosa.display.specshow(librosa.amplitude_to_db(S_background[:, idx], ref=np.max), y_axis='log', x_axis='time', sr=sr, ax=ax[1])
ax[1].set(title='Background')
ax[1].label_outer()

librosa.display.specshow(librosa.amplitude_to_db(S_foreground[:, idx], ref=np.max), y_axis='log', x_axis='time', sr=sr, ax=ax[2])
ax[2].set(title='Foreground')
fig.colorbar(img, ax=ax)

plt.show()

y_foreground = librosa.istft(S_foreground * phase)

Audio(data=y_foreground[10*sr:15*sr], rate=sr, autoplay=True)