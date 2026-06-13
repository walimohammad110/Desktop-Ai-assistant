import pywhatkit
import text_speach
import speech_to_text

def whats_mess():
    def send_now(phone, message):
      pywhatkit.sendwhatmsg_instantly(phone, message, wait_time=15, tab_close=True)

# Ask contact name by voice
    text_speach.Text_to_speech("Whom do you want to send message?")
    name = speech_to_text.speech_to_voice()

    contacts = {
    "person 3": "+91xxxxxxxxx",
    "person2": "+9xxxxxxxxx",
    "person 1" :"+91xxxxxxxxx"
     }

    phone = contacts.get(name)


    if phone:                                                    # check if name is in contact send message
      text_speach.Text_to_speech("What message should I send?")
      msg = speech_to_text.speech_to_voice()
      send_now(phone, msg)
    else:
      text_speach.Text_to_speech("Contact not found")

