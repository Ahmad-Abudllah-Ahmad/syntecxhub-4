"""
Personal Voice Assistant (Project-1)

- STT: SpeechRecognition (Google Web Speech API via SpeechRecognition)
- TTS: pyttsx3 (offline)
- Rule mapping: regex-based routing to actions
- UI: Rich-based professional terminal interface
"""

from __future__ import annotations

import sys
from voice.stt import SpeechToText
from voice.tts import TextToSpeech
from core.command_router import CommandRouter
import core.ui as ui
import config


def main() -> int:
    ui.print_banner()
    
    tts = TextToSpeech()
    stt = SpeechToText(
        language=config.LANGUAGE,
        ambient_noise_seconds=config.AMBIENT_NOISE_SECONDS,
        listen_timeout=config.LISTEN_TIMEOUT,
        phrase_time_limit=config.PHRASE_TIME_LIMIT,
        print_debug=config.PRINT_DEBUG,
    )
    router = CommandRouter(tts=tts)

    welcome_msg = f"Assistant online. Say '[wake]{config.WAKE_WORD}[/wake]' to activate." if config.WAKE_WORD_REQUIRED else "Assistant online."
    ui.print_status("Ready and waiting for your command...", style="success")
    tts.say(welcome_msg)

    while True:
        text = stt.listen_once()
        if not text:
            continue

        normalized = text.strip().lower()

        # Enforce wake word
        if config.WAKE_WORD_REQUIRED:
            if config.WAKE_WORD not in normalized.split():
                if config.PRINT_DEBUG:
                    ui.print_debug("Wake word not detected; ignoring.")
                continue
            normalized = normalized.replace(config.WAKE_WORD, "").strip()

        if not normalized:
            tts.say("Yes? Please say a command.")
            continue

        ui.print_user_input(text)
        
        result = router.handle(normalized)
        if result.should_exit:
            tts.say("Goodbye!")
            return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        ui.console.print("\n[error]Exiting...[/error]")
        raise SystemExit(0)
