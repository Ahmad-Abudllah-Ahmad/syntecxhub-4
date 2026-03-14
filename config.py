# Configuration for the Personal Voice Assistant

WAKE_WORD = "nova"          # Say this word to activate the assistant
WAKE_WORD_REQUIRED = True   # If True, commands without the wake word are ignored

LANGUAGE = "en-US"          # SpeechRecognition language hint
AMBIENT_NOISE_SECONDS = 0.8 # Seconds for ambient noise calibration

LISTEN_TIMEOUT = 6          # How long to wait for speech to start (seconds)
PHRASE_TIME_LIMIT = 7       # Max length of a single utterance (seconds)

PRINT_DEBUG = True          # Print recognized text and debug messages
