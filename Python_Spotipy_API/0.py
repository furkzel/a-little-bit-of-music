import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pandas as pd

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="#####", client_secret="#####"))

def get_user_id(link_of_user):

    return (link_of_user.split("/")[-1]).split("?")[0]


def playlists_of_user(link_of_user):

    P = []

    playlists = sp.user_playlists(get_user_id(link_of_user))
    for playlist in playlists['items']:
        P.append(((playlist['id'])))
    return P


def get_playlist_tracks(username, playlist_id):

    names = []
    artists = []
    dates = []
    times = []
    tempos = []
    energy = []
    genres = []

    df = pd.DataFrame()

    results = sp.user_playlist_tracks(username, playlist_id)
    tracks = results['items']
    for i in tracks:
        names.append(i.get("track").get("name"))
        artists.append(i.get("track").get("artists")[0].get("name"))
        times.append(i.get("track").get("duration_ms"))
        dates.append(i.get("track").get("album").get("release_date"))
        genres.append(sp.artist(i.get("track").get("artists")[0].get("id")).get("genres"))
        audio_features = sp.audio_features(i.get("track").get("id"))
        tempos.append(audio_features[0].get("tempo"))
        energy.append(audio_features[0].get("energy"))  
        
    df = pd.DataFrame({"name": names, "artist": artists, "tempo":tempos, "energy":energy, "time": times, "date": dates, "genres": genres})
    df.sort_values(by="energy", inplace=True)
    return df.to_csv("deneme.csv", index=True)
    
get_playlist_tracks(get_user_id("https://open.spotify.com/user/ctg7owlu0gi2phloai3vw0gm5?si=4bb3c8c6caf94182e"), get_user_id("https://open.spotify.com/playlist/0iJlikXUzMMrn4U630v92o?si=12e69289062548ee"))