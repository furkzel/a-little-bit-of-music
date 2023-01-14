import spotipy
import spotipy.util as util
import pandas as pd
import matplotlib.pyplot as plt

# Replace with your own Spotipy client ID, client secret, and redirect URI
client_id = '###'
client_secret = '###'

# Replace with the user whose track genre counts you want to get
username = 'brkykhrmn7'

# Request authorization
scope = 'user-library-read'
token = util.prompt_for_user_token(username, scope, client_id, client_secret)

# Create a Spotipy client
sp = spotipy.Spotify(auth=token)

# Get the user's tracks
results = sp.current_user_saved_tracks()
tracks = results['items']
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

# Extract the genres of the tracks
genres = []
for track in tracks:
    track_genres = track['track']['album']['artists'][0]['genres']
    genres.extend(track_genres)

# Count the number of occurrences of each genre
genre_counts = {}
for genre in genres:
    if genre not in genre_counts:
        genre_counts[genre] = 1
    else:
        genre_counts[genre] += 1

# Convert the genre counts to a pandas dataframe
df = pd.DataFrame.from_dict(genre_counts, orient='index', columns=['count'])

# Plot the data as a pie chart
plt.pie(df['count'], labels=df.index, autopct='%1.1f%%')
plt.axis('equal')
plt.show()

def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

get_playlist_tracks("5IJkpanz7A7SPzoJfemFB")






