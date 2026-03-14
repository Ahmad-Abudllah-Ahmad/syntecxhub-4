import os
import webbrowser
from datetime import datetime
import subprocess

def get_time():
    return datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.now().strftime("%B %d, %Y")

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return True

def open_app(app_name):
    app_name = app_name.lower()
    
    # Common mappings
    if "chrome" in app_name:
        return webbrowser.open("https://www.google.com")
    elif "youtube" in app_name:
        return webbrowser.open("https://www.youtube.com")
    
    # macOS specifically
    if os.name == 'posix':
        try:
            # Try to open as a macOS application
            subprocess.run(["open", "-a", app_name], check=True, capture_output=True)
            return True
        except subprocess.CalledProcessError:
            # Fallback for common names
            fallbacks = {
                "calculator": "Calculator",
                "notes": "Notes",
                "terminal": "Terminal",
                "finder": "Finder",
                "safari": "Safari"
            }
            if app_name in fallbacks:
                try:
                    subprocess.run(["open", "-a", fallbacks[app_name]], check=True)
                    return True
                except:
                    pass
    
    return False
