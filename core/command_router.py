import re
import core.actions as actions

class CommandResult:
    def __init__(self, should_exit=False):
        self.should_exit = should_exit

class CommandRouter:
    def __init__(self, tts):
        self.tts = tts
        # Map of regex patterns to handler functions
        self.routes = [
            (r"(stop|exit|goodbye|quit)", self.handle_exit),
            (r"(help|what can you do)", self.handle_help),
            (r"(what is the time|time now|current time)", self.handle_time),
            (r"(what is the date|today's date|current date)", self.handle_date),
            (r"open (.*)", self.handle_open),
            (r"search (?:for )?(.*)", self.handle_search),
            (r"google (.*)", self.handle_search),
        ]

    def handle(self, text):
        for pattern, handler in self.routes:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return handler(match)
        
        self.tts.say("I'm sorry, I don't know how to handle that command yet.")
        return CommandResult()

    def handle_exit(self, match):
        return CommandResult(should_exit=True)

    def handle_help(self, match):
        self.tts.say("You can ask me to open apps like 'open chrome', search the web like 'search for space exploration', or ask for the time and date.")
        return CommandResult()

    def handle_time(self, match):
        time_str = actions.get_time()
        self.tts.say(f"The current time is {time_str}")
        return CommandResult()

    def handle_date(self, match):
        date_str = actions.get_date()
        self.tts.say(f"Today is {date_str}")
        return CommandResult()

    def handle_open(self, match):
        app_name = match.group(1).strip()
        success = actions.open_app(app_name)
        if success:
            self.tts.say(f"Opening {app_name}")
        else:
            self.tts.say(f"I couldn't find a way to open {app_name}")
        return CommandResult()

    def handle_search(self, match):
        query = match.group(1).strip()
        self.tts.say(f"Searching for {query}")
        actions.search_web(query)
        return CommandResult()
