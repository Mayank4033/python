# import asyncio
from deep_translator import GoogleTranslator

def translate_text(text):
    translator = GoogleTranslator()
    result = GoogleTranslator(source='auto', target='hi').translate(text)
    return result.text
def converter(*words):
    list=[]
    for word in words:
        text= translate_text(word)
        print(f"{word} is converted into hindi")
        list.append(text)
    return list

def main():
    list = converter('spoon','book','hand','knief','sunset','water')
    print("all words in gujarati are : ")
    for item in list:
        print(item)

main()