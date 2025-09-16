import speech_recognition as sr
from pydub import AudioSegment
import os

def mp3_to_text(mp3_file_path, output_text_file):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Convert MP3 to WAV (speech_recognition works with WAV files)
    audio = AudioSegment.from_mp3(mp3_file_path)
    wav_file_path = "temp_audio.wav"
    audio.export(wav_file_path, format="wav")
    print("please wait")
    try:
        # Load the WAV file
        with sr.AudioFile(wav_file_path) as source:
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.record(source)
            text = recognizer.recognize_sphinx(audio_data)  # Use Sphinx
            with open(output_text_file, 'w', encoding='utf-8') as text_file:
                text_file.write(text)
            print(f"Transcription saved to {output_text_file}")
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results {e}")
    finally:
        # Clean up the temporary WAV file
        if os.path.exists(wav_file_path):
            os.remove(wav_file_path)

# Example usage
if __name__ == "__main__":
    mp3_file = "d:\\python\\sound\\output.mp3"  # Replace with your MP3 file path
    output_file = "transcription.txt"  # Output text file
    mp3_to_text(mp3_file, output_file)