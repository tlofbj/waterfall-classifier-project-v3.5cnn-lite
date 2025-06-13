from datetime import datetime
from termcolor import cprint

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

def gprint(text):
    cprint(text, on_color="on_green", attrs=['bold'])

def rprint(text):
    cprint(text, on_color="on_red", attrs=['bold'])

def yprint(text):
    cprint(text, color="yellow")

def mprint(text):
    cprint(text, color="magenta")
