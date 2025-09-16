import yt_dlp

url = "https://youtu.be/zyXmsVwZqX4?si=yqBkGjT79yORvneN"

ydl_opts = {
    'outtmpl': 'Downloads/%(title)s.%(ext)s',
       'format': 'best'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download complete!")
