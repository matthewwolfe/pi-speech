import shlex
import subprocess


class Speaker:

    @staticmethod
    def speak(text):
        subprocess.call(["say", shlex.quote(text)])
