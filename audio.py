from moviepy import VideoFileClip
def video_to_audio(video_path,audio_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        print(f"audio saved successfully at : {audio_path}")
    except Exception as e:
        print("error : ",e)
video_path = input("paste url of the video : ").strip('"')
audio_path = r"D:\python\sound\output.mp3"
video_to_audio(video_path,audio_path)