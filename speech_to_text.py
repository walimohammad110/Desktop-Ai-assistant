import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

recognizer = sr.Recognizer()

def speech_to_voice():
    while True:
      try:
        print("Listening...")

        samplerate = 16000
        duration = 5

        recording = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="int16"
        )

        sd.wait()
        sf.write("voice.wav", recording, samplerate)

        with sr.AudioFile("voice.wav") as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
        break

      except sr.UnknownValueError:
        print("Please try again")

      except sr.RequestError:
        print("Internet connection error")

      except Exception as e:
        print("Error:", e)


