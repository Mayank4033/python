import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound

def extract_text_between(url, start_marker, end_marker):
    # Try raw requests first
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        html = resp.text
    except Exception:
        html = None

    for source in ('raw', 'selenium'):
        if source == 'selenium' or html is None:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            options = Options()
            options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            html = driver.page_source
            driver.quit()

        soup = BeautifulSoup(html, "lxml")
        text = soup.get_text(separator=" ").strip()
        if start_marker in text and end_marker in text:
            start = text.find(start_marker) + len(start_marker)
            end = text.find(end_marker)
            return text[start:end].strip(" ·:-–")
    return None

def get_rashi_kathan(rashino):
    if rashino==1:
        url = "https://www.divyabhaskar.co.in/rashifal/13/today/"
        result = extract_text_between(url, "ચંદ્રરાશિ પ્રમાણે", "લકી નંબર")
        #write text file named as kathan.txt
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==2:
        url = "https://www.divyabhaskar.co.in/rashifal/15/today/"
        result = extract_text_between(url, "ચંદ્રરાશિ પ્રમાણે", "લકી નંબર")
        #write text file named as kathan.txt
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==3:
        url = "https://www.divyabhaskar.co.in/rashifal/16/today/"
        result = extract_text_between(url, "ચંદ્રરાશિ પ્રમાણે", "લકી નંબર")
        #write text file named as kathan.txt
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==4:
        url = "https://www.divyabhaskar.co.in/rashifal/19/today/"
        result = extract_text_between(url, "ચંદ્રરાશિ પ્રમાણે", "લકી નંબર")
        #write text file named as kathan.txt
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==5:
        url = "https://www.divyabhaskar.co.in/rashifal/17/today/"
        result = extract_text_between(url, "ચંદ્રરાશિ પ્રમાણે", "લકી નંબર")
        #write text file named as kathan.txt
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==6:
        url = "https://www.divyabhaskar.co.in/rashifal/18/today/"
        result = extract_text_between(url, "ચંદ્રરાશિ પ્રમાણે", "લકી નંબર")
        #write text file named as kathan.txt
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==7:
        url = "https://www.divyabhaskar.co.in/rashifal/20/today/"
        result = extract_text_between(url, "ચંદ્રરાશિ પ્રમાણે", "લકી નંબર")
        #write text file named as kathan.txt
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==8:
        url = "https://www.divyabhaskar.co.in/rashifal/14/today/"
        result = extract_text_between(url, "ચંદ્રરાશિ પ્રમાણે", "લકી નંબર")
        #write text file named as kathan.txt
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==9:
        url = "https://www.divyabhaskar.co.in/rashifal/21/today/"
        result = extract_text_between(url, "ચંદ્રરાશિ પ્રમાણે", "લકી નંબર")
        #write text file named as kathan.txt
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==10:
        url = "https://www.divyabhaskar.co.in/rashifal/22/today/"
        result = extract_text_between(url, "ચંદ્રરાશિ પ્રમાણે", "લકી નંબર")
        #write text file named as kathan.txt
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==11:
        url = "https://www.divyabhaskar.co.in/rashifal/23/today/"
        result = extract_text_between(url, "ચંદ્રરાશિ પ્રમાણે", "લકી નંબર")
        #write text file named as kathan.txt
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==12:
        url = "https://www.divyabhaskar.co.in/rashifal/24/today/"
        result = extract_text_between(url, "ચંદ્રરાશિ પ્રમાણે", "લકી નંબર")
        #write text file named as kathan.txt
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")

def text_to_speech_gujarati(text,output_file="output.mp3"):
    try:
        # Create a gTTS object with Gujarati language
        tts = gTTS(text=text, lang='gu', slow=False)
        
        # Save the audio to a file
        tts.save(output_file)
        print(f"Audio saved to {output_file}")
        
        # Play the audio file
        playsound(output_file)
        
        # Optionally, remove the temporary file
        os.remove(output_file)
    except Exception as e:
        print(f"Error during text-to-speech: {str(e)}")

print("enter 1 for મેષ / Aries ")
print("enter 2 for વૃષભ / Taurus ")
print("enter 3 for મિથુન / Gemini ")
print("enter 4 for કર્ક / Cancer ")
print("enter 5 for સિંહ / Leo ")
print("enter 6 for કન્યા / Virgo ")
print("enter 7 for તુલા / Libra ")
print("enter 8 for વૃશ્ચિક / Scorpio ")
print("enter 9 for ધન / Sagittarius ")
print("enter 10 for મકર / Capricorn ")
print("enter 11 for કુંભ / Aquarius ")
print("enter 12 for મીન / Pisces ")
r = int(input("enter the number of your rashi : "))

print("Extracting data please wait....")
#step 1
# //get text from https://www.divyabhaskar.co.in/rashifal/13/today?ref=inbound_RHS and store into file
get_rashi_kathan(r)
print("data extracted successfully \n generating sound....")
with open("kathan.txt", "r", encoding="utf-8") as f:
    data = f.read()
text_to_speech_gujarati(data)