import os

# youtube-dl kütüphanesini yükleyin
os.system("pip install youtube-dl")

import youtube_dl

# youtube video url
video_url = 'https://www.youtube.com/watch?v=fxeiOe-X6g4'

# ses dosyasını indirmek için ayarlar
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

# video indirme
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])


