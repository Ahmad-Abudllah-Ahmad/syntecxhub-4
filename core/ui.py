from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.theme import Theme
from rich.live import Live
from rich.spinner import Spinner

# Define a professional theme
custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "bold green",
    "user": "bold green",
    "assistant": "bold cyan",
    "wake": "magenta",
    "debug": "dim white"
})

console = Console(theme=custom_theme)

def print_banner():
    banner = """
      █████╗      █████╗      █████╗ 
     ██╔══██╗    ██╔══██╗    ██╔══██╗
     ███████║    ███████║    ███████║
     ██╔══██║    ██╔══██║    ██╔══██║
     ██║  ██║    ██║  ██║    ██║  ██║
     ╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝
    """
    console.print(Panel(
        Text(banner, style="cyan"), 
        title="[bold white]AAA Personal Assistant[/bold white]", 
        subtitle="[bold yellow]Powered by AAA[/bold yellow]",
        border_style="cyan"
    ))

def print_status(message, style="info"):
    console.print(f"[{style}]•[/] {message}")

def print_debug(message):
    console.print(f"[debug][DEBUG] {message}[/debug]")

def print_user_input(text):
    console.print(Panel(Text(text, style="user"), title="[bold white]You[/bold white]", border_style="green"))

def print_assistant_response(text):
    console.print(Panel(Text(text, style="assistant"), title="[bold white]Assistant[/bold white]", border_style="cyan"))

def show_listening(message="Listening..."):
    # Return a Live context or a simple styled text
    return Text(f"  {message}", style="wake")
