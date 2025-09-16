from pydub import AudioSegment
import speech_recognition as sr

# convert mp3 to wav
sound = AudioSegment.from_mp3("D:\python\sound\output.mp3")
sound.export("D:\python\sound\output.wav", format="wav")

# now transcribe
r = sr.Recognizer()
with sr.AudioFile("D:\python\sound\output.wav") as source:
    audio = r.record(source)
    text = r.recognize_google(audio)  # no API key needed
    print("Transcription:", text)
