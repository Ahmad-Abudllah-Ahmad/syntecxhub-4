# AAA Personal Assistant

AAA Personal Assistant is a sophisticated voice-controlled application designed to streamline daily tasks through natural language interaction. Built with Python, it integrates advanced speech recognition and text-to-speech technologies to provide a hands-free user experience. The application features a professional terminal interface and a robust command-routing architecture.

## Project Overview

The project is structured to ensure modularity and scalability. It consists of a core processing engine, a voice interaction layer, and a professional user interface. The assistant listens for a specific wake word, "nova", before processing user requests, ensuring privacy and accidental trigger avoidance.

## System Features and Capabilities

| Feature | Description | Component |
|---------|-------------|-----------|
| Speech-to-Text | Converts live audio input into processed text strings. | voice/stt.py |
| Text-to-Speech | Provides audio feedback to the user via offline synthesis. | voice/tts.py |
| Command Routing | Patterns matching logic for identifying user intent. | core/command_router.py |
| Application Control| Ability to launch macOS applications via voice commands. | core/actions.py |
| Web Intelligence | Direct integration with web search engines for queries. | core/actions.py |
| Temporal Awareness| Functions to provide real-time date and time information. | core/actions.py |
| Professional UI | Rich-text terminal output with progress indicators. | core/ui.py |

## System Architecture

```mermaid
graph TD
    User((User))
    Microphone[Microphone Input]
    STT[Speech-to-Text Engine]
    Router[Command Router]
    Actions[Action Handlers]
    TTS[Text-to-Speech Engine]
    UI[Professional Terminal UI]
    Speaker[Audio Output]

    User --> Microphone
    Microphone --> STT
    STT --> UI
    STT --> Router
    Router --> Actions
    Actions --> TTS
    TTS --> Speaker
    Actions --> UI
    TTS --> UI
```

## Initialization Flow

```mermaid
sequenceDiagram
    participant Main as assistant.py
    participant UI as core/ui.py
    participant TTS as voice/tts.py
    participant STT as voice/stt.py
    
    Main->>UI: Initialize Console and Theme
    Main->>UI: Print ASCII Banner
    Main->>TTS: Initialize Engine (Offline)
    Main->>STT: Initialize Microphone and Recognizer
    Main->>UI: Print Ready Status
    Main->>TTS: Speak Welcome Message
```

## Main Execution Loop

```mermaid
flowchart TD
    Start([Start Loop]) --> Listen[Capture Audio]
    Listen --> Recognize{Speech Detected?}
    Recognize -- No --> Start
    Recognize -- Yes --> WakeCheck{Wake Word Nova?}
    WakeCheck -- No --> Start
    WakeCheck -- Yes --> Process[Extract Command]
    Process --> Routing[Route to Handler]
    Routing --> Execute[Perform Action]
    Execute --> Feedback[Audio/Visual Feedback]
    Feedback --> ExitCheck{Exit Command?}
    ExitCheck -- No --> Start
    ExitCheck -- Yes --> End([End Session])
```

## Speech Recognition Process

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Calibrating: adjust_for_ambient_noise
    Calibrating --> Listening: recognizer.listen
    Listening --> Recognizing: Google Web Speech API
    Recognizing --> Success: Text Extracted
    Recognizing --> UnknownError: Speech Unclear
    Recognizing --> RequestError: Network Issue
    Success --> [*]
    UnknownError --> Idle
    RequestError --> Idle
```

## Command Routing Logic

```mermaid
flowchart LR
    Input[Input Text] --> Regex1{Exit Pattern?}
    Regex1 -- Yes --> Handler1[handle_exit]
    Regex1 -- No --> Regex2{Help Pattern?}
    Regex2 -- Yes --> Handler2[handle_help]
    Regex2 -- No --> Regex3{Time/Date Pattern?}
    Regex3 -- Yes --> Handler3[handle_time_date]
    Regex3 -- No --> Regex4{Open/Search Pattern?}
    Regex4 -- Yes --> Handler4[handle_action]
    Regex4 -- No --> Default[Handle Unknown]
```

## Action Execution Flow

```mermaid
graph LR
    Command[Command] --> Action[Action Layer]
    Action --> WebBrowser[webbrowser.open]
    Action --> Subprocess[subprocess.run]
    Action --> SystemOS[os.name Check]
    
    WebBrowser --> Search[Search Web]
    WebBrowser --> Sites[Open Sites]
    Subprocess --> Apps[Open macOS Apps]
```

## Technical Stack

| Category | Technology | Purpose |
|----------|------------|---------|
| Language | Python 3.14 | Core logic and scripting. |
| Voice STT| SpeechRecognition | Audio processing and API interface. |
| Voice TTS| pyttsx3 | Offline audio synthesis. |
| UI | Rich | Professional terminal styling. |
| Connectivity| standard-aifc / chunk | Python 3.14 compatibility layers. |
| System | pyobjc | macOS native API bridging. |

## Configuration Parameters

| Parameter | Default Value | Description |
|-----------|---------------|-------------|
| WAKE_WORD | "nova" | The keyword required to trigger command processing. |
| WAKE_WORD_REQUIRED | True | Determines if the wake word is mandatory. |
| LANGUAGE | "en-US" | Language code for speech recognition. |
| LISTEN_TIMEOUT | 6 | Seconds to wait for audio before timing out. |
| PHRASE_TIME_LIMIT | 7 | Maximum length of a single spoken phrase. |
| AMBIENT_NOISE_SECONDS | 0.8 | Duration for background noise calibration. |

## Sample Commands and Actions

| Command Category | Examples | Expected Result |
|------------------|----------|-----------------|
| System Controls | "nova stop", "nova exit" | Application terminates gracefully. |
| Information | "nova what is the time" | Current local time is spoken. |
| Applications | "nova open chrome", "nova open notes" | Corresponding app is launched. |
| Web Search | "nova search for space travel" | Default browser opens a search result. |
| Navigation | "nova open youtube" | Browser navigates to the URL. |

## Installation and Usage

1. Clone the repository to your local machine.
2. Ensure PortAudio is installed (macOS: `brew install portaudio`).
3. Initialize the Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the assistant:
   ```bash
   python assistant.py
   ```
