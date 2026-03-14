import pyttsx3
import core.ui as ui

class TextToSpeech:
    def __init__(self, rate=175, volume=1.0):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        
        # Optionally set a voice (0 for female, 1 for male usually)
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id)

    def say(self, text):
        ui.print_assistant_response(text)
        self.engine.say(text)
        self.engine.runAndWait()
