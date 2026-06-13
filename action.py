import text_speach
import speech_to_text
import webbrowser
import whatsapp
import datetime




def Action(data):
    user_data=data.lower()
    if "what is your name" in user_data:
      text_speach.Text_to_speech("my name is jarvis")
      return "my name is jarvis"
    elif"hello" in user_data or "hye" in user_data:
        text_speach.Text_to_speech("hello i am jarvis , how can i help you ")
        return " hello i am jarvis , how can i help you"
    elif "good morning" in user_data :
        text_speach.Text_to_speech("good morning dear sir how can i help")
        return "good morning dear sir how can i help"
    elif "time" in user_data:
     current = datetime.datetime.now()
     time = f"{current.hour}:{current.minute}"
     text_speach.Text_to_speech(time)
     return time
    elif "shutdown" in user_data:
     text_speach.Text_to_speech("ok sir i am shutting down")
     return "ok sir"
    elif "play music" in user_data:
       text_speach.Text_to_speech("playing music")
       webbrowser.open("https://www.youtube.com/watch?v=nvSOtuHu7_Y&list=RDnvSOtuHu7_Y&start_radio=1")
       return "playing music"
    elif "send message" in user_data:
       text_speach.Text_to_speech("sending whatsaapp message")
       whatsapp.whats_mess()
       return "sending whatsaapp message"
       
      
    else:
       text_speach.Text_to_speech("sorry i am unable to understand")
       return " sorry i am unable to understand"

