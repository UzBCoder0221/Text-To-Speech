import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 30)
engine.setProperty('volume', 1.0) 

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text_to_speech("To change the value of a specific character in a string, refer to the index number, and use single quotes.")

