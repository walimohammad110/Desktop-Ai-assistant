import pyttsx3
def Text_to_speech(text):
    engine = pyttsx3.init()
    
    rate= engine.getProperty('rate')
    engine.setProperty('rate','rate-70')
    engine.say(text)
    engine.runAndWait()
