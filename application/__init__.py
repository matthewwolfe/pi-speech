import os
import speech_recognition
from .commands import commands
from .speaker import Speaker


def app():
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    try:
        print('Getting started')

        with microphone as source: recognizer.adjust_for_ambient_noise(source)
        print('Set minimum energy threshold to {}'.format(recognizer.energy_threshold))

        while True:
            print('Now Listening')

            with microphone as source:
                audio = recognizer.listen(source)
                print('Recognizing')

            try:
                message = recognizer.recognize_wit(audio_data=audio, key=os.getenv('WIT_API_KEY'))

                if message in commands:
                    response = commands[message]()

                    if len(response):
                        Speaker.speak(response)

            except speech_recognition.UnknownValueError:
                print('Error recognizing audio')
            except speech_recognition.RequestError:
                print('Error recognizing audio')

    except KeyboardInterrupt:
        pass
