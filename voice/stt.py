import speech_recognition as sr
import core.ui as ui

class SpeechToText:
    def __init__(self, language="en-US", ambient_noise_seconds=0.8, listen_timeout=5, phrase_time_limit=5, print_debug=True):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = language
        self.ambient_noise_seconds = ambient_noise_seconds
        self.listen_timeout = listen_timeout
        self.phrase_time_limit = phrase_time_limit
        self.print_debug = print_debug

        if self.print_debug:
            ui.print_debug(f"STT initialized (lang={self.language})")

    def listen_once(self):
        with self.microphone as source:
            if self.print_debug:
                ui.print_status(f"Calibrating for {self.ambient_noise_seconds}s...", style="warning")
            self.recognizer.adjust_for_ambient_noise(source, duration=self.ambient_noise_seconds)
            
            ui.print_status("Listening...", style="wake")
            
            try:
                audio = self.recognizer.listen(source, timeout=self.listen_timeout, phrase_time_limit=self.phrase_time_limit)
            except sr.WaitTimeoutError:
                if self.print_debug:
                    ui.print_debug("Listen timeout (no speech detected)")
                return None

        try:
            if self.print_debug:
                ui.print_status("Recognizing...", style="info")
            text = self.recognizer.recognize_google(audio, language=self.language)
            return text
        except sr.UnknownValueError:
            if self.print_debug:
                ui.print_debug("Recognition error: Unknown value")
            return None
        except sr.RequestError as e:
            if self.print_debug:
                ui.print_debug(f"Recognition error: Request failed; {e}")
            return None
