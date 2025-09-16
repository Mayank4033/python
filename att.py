import whisper
from pydub import AudioSegment
import os

def mp3_to_text_whisper(mp3_file_path, output_text_file):
    # Convert MP3 to WAV
    audio = AudioSegment.from_mp3(mp3_file_path)
    wav_file_path = "temp_audio.wav"
    audio.export(wav_file_path, format="wav")

    # Load Whisper model
    model = whisper.load_model("tiny")  # Options: tiny, base, small, medium, large
    result = model.transcribe(wav_file_path)

    # Save transcription
    text = result["text"]
    with open(output_text_file, 'w', encoding='utf-8') as text_file:
        text_file.write(text)
    print(f"Transcription saved to {output_text_file}")

    # Clean up
    if os.path.exists(wav_file_path):
        os.remove(wav_file_path)

if __name__ == "__main__":
    mp3_file = "d:\\python\\sound\\output.mp3"
    output_file = "transcription.txt"
    mp3_to_text_whisper(mp3_file, output_file)