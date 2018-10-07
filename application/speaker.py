import os


class Speaker:

    @staticmethod
    def speak(text):
        os.system("say '%s' &" % text)
