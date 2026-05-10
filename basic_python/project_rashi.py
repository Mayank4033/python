import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound
import os

def extract_text_between(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        }
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        html = resp.text
    except Exception as e:
        print(f"Requests failed: {e}. Trying Selenium...")
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            html = driver.page_source
            driver.quit()
        except Exception as e2:
            print(f"Selenium also failed: {e2}")
            return None

    soup = BeautifulSoup(html, "lxml")
    text = soup.get_text(separator="\n").strip()

    # Finding start
    start_marker = "ચંદ્રરાશિ પ્રમાણે"
    start_pos = text.find(start_marker)
    if start_pos == -1:
        print(f"Start marker '{start_marker}' not found on page!")
        return None

    end_markers = ["લકી કલર", "લકી નંબર", "ટેરો રાશિફળ", "આજનું રાશિફળ"]

    end_pos = -1
    for marker in end_markers:
        pos = text.find(marker, start_pos + len(start_marker))
        if pos != -1:
            end_pos = pos
            break

    if end_pos == -1:
        print("No suitable end marker found! Taking text till end.")
        end_pos = len(text)

    extracted = text[start_pos + len(start_marker):end_pos].strip()

    # Cleaning extra newlines and spaces
    import re
    extracted = re.sub(r'\n+', '\n', extracted).strip()

    return extracted
def get_rashi_kathan(rashino):
    if rashino==1:
        url = "https://www.divyabhaskar.co.in/rashifal/13/today/"
        result = extract_text_between(url)
        #write text file named as kathan.txt
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==2:
        url = "https://www.divyabhaskar.co.in/rashifal/15/today/"
        result = extract_text_between(url)
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==3:
        url = "https://www.divyabhaskar.co.in/rashifal/16/today/"
        result = extract_text_between(url)
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==4:
        url = "https://www.divyabhaskar.co.in/rashifal/19/today/"
        result = extract_text_between(url)
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==5:
        url = "https://www.divyabhaskar.co.in/rashifal/17/today/"
        result = extract_text_between(url)
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==6:
        url = "https://www.divyabhaskar.co.in/rashifal/18/today/"
        result = extract_text_between(url)
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==7:
        url = "https://www.divyabhaskar.co.in/rashifal/20/today/"
        result = extract_text_between(url)
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==8:
        url = "https://www.divyabhaskar.co.in/rashifal/14/today/"
        result = extract_text_between(url)
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==9:
        url = "https://www.divyabhaskar.co.in/rashifal/21/today/"
        result = extract_text_between(url)
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==10:
        url = "https://www.divyabhaskar.co.in/rashifal/22/today/"
        result = extract_text_between(url)
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==11:
        url = "https://www.divyabhaskar.co.in/rashifal/23/today/"
        result = extract_text_between(url)
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
    elif rashino==12:
        url = "https://www.divyabhaskar.co.in/rashifal/24/today/"
        result = extract_text_between(url)
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
if r>0 and r<=12:

    print("Extracting data please wait....")
    get_rashi_kathan(r)
    print("data extracted successfully \n generating sound....")
    with open("kathan.txt", "r", encoding="utf-8") as f:
        data = f.read()
    text_to_speech_gujarati(data)
else:
    print("Invalid Choice")