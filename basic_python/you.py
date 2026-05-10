import yt_dlp

url = input("Paste YouTube URL: ")
filename = input("Enter file name (without extension): ")

ydl_opts = {
    'format': 'bestvideo[height<=720]+bestaudio/best',  # 720p max
    'outtmpl': f'Downloads/{filename}.%(ext)s',
    'merge_output_format': 'mp4'  # ensures final file is mp4
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("✅ Download complete!")