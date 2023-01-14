from music21 import *

import numpy as np
import pandas as pd
import math

import requests

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="###", client_secret="###"))


# This function return a string that contain ID of element embed in link.

def get_ID(link):

   return (link.split("/")[-1]).split("?")[0]


# This function takes the user's ID element as a parameter and returns datas about of playlists owned by a user.

def playlists_datas_of_user(ID):
    
    playlists_dataframe = pd.DataFrame()

    images = []
    uri = []
    tracks = []
    snapshot_id = []
    external_urls = []
    public = []
    types = []
    id = []
    name = []
    owner = []
    primary_color = []
    href = []
    description = []
    collaborative = []

    heads = set()
    
    for item in sp.user_playlists(ID)['items']:
        
        images.append(item.get('images')[0].get('url'))
        uri.append(item.get('uri'))
        tracks.append(item.get('tracks').get('total'))
        snapshot_id.append(item.get('snapshot_id'))
        external_urls.append(item.get('external_urls').get('spotify'))
        public.append(item.get('public'))
        types.append(item.get('type'))
        id.append(item.get('id'))
        name.append(item.get('name'))
        owner.append(item.get('owner').get('display_name'))
        primary_color.append(item.get('primary_color'))
        href.append(item.get('href'))
        description.append(item.get('description'))
        collaborative.append(item.get('collaborative'))

    return pd.DataFrame({"name": name , "id": id, "external_urls": external_urls, "snapshot_id": snapshot_id, "tracks": tracks, "uri": uri, "images": images, "description": description})

# This function takes the playlist's ID element as a parameter and returns datas about of tracks in a playlist.

def playlist_tracks(ID):

    albums = []
    artists = []
    id = []
    name = []
    popularity = []
    uri = []

    danceability = []
    energy = []
    key = []
    loudness = []
    mode = []
    speechiness = []
    acousticness = []
    instrumentalness = []
    liveness = []
    valence = []
    tempo = []
    types = []
    duration_ms = []
    time_signature = []

    for item in sp.playlist_tracks(ID)['items']:
            
        albums.append(item.get('track').get('album').get('name'))
        artists.append(item.get('track').get('artists')[0].get('name'))
        id.append(item.get('track').get('id'))
        name.append(item.get('track').get('name'))
        popularity.append(item.get('track').get('popularity'))
        uri.append(item.get('track').get('uri'))

        danceability.append(item.get('track').get('danceability'))
        energy.append(item.get('track').get('energy'))
        key.append(item.get('track').get('key'))
        loudness.append(item.get('track').get('loudness'))
        mode.append(item.get('track').get('mode'))
        speechiness.append(item.get('track').get('speechiness'))
        acousticness.append(item.get('track').get('acousticness'))
        instrumentalness.append(item.get('track').get('instrumentalness'))
        liveness.append(item.get('track').get('liveness'))
        valence.append(item.get('track').get('valence'))
        tempo.append(item.get('track').get('tempo'))
        types.append(item.get('track').get('type'))
        duration_ms.append(item.get('track').get('duration_ms'))
        time_signature.append(item.get('track').get('time_signature'))
    
    return pd.DataFrame({"name": name , "id": id, "uri": uri, "artists": artists, "albums": albums, "popularity": popularity, "danceability": danceability, "energy": energy, "key": key, "loudness": loudness, "mode": mode, "speechiness": speechiness, "acousticness": acousticness, "instrumentalness": instrumentalness, "liveness": liveness, "valence": valence, "tempo": tempo, "duration_ms": duration_ms})



def analysis_of_track(ID):

    start = []
    duration = []
    confidence = []
    loudness = []
    tempo = []
    tempo_confidence = []
    key = []
    key_confidence = []
    mode = []
    mode_confidence = []
    time_signature = []
    time_signature_confidence = []


    for item in sp.audio_analysis(ID)['segments']:
        print(item.get('pitches'))

analysis_of_track("5xFuYnKruaC6AVbg9GDHuv")


def pitches_of_track(ID):

    pitches = []
    
    for item in sp.audio_analysis(ID)['segments']:
        p = item.get('pitches')
        pitches.append(p)

    return pitches

stream = stream.Stream()

def F(ID):

    scores = []

    for pitch in pitches_of_track(ID):
        for subpitch in pitch:
            subpitch = map_to_pitch(subpitch)
            score = note.Note(pitch=subpitch)
            scores.append(score)

    global stream

    for score in scores:
        stream.append(score)

    stream.show("musicxml")

F("3VM35337X7Ro1tesUHnZ95")


def map_to_pitch(x):
    # Map x to a pitch in the range C4 to B4
    pitch = int(12 * math.log(x / 440.0, 2) + 69)
    return pitch
    