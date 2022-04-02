import os
from datetime import datetime

import yaml
import textwrap
import questionary

def ask_question(message):
    return questionary.text(message).ask()

def ask_paragraph(message):
    return textwrap.fill(ask_question(message)) + "\n"

def ask_choice(message, choices):
    return questionary.select(message, choices).ask()

# get the string-formatted date (eg. 2022-01-01)
def get_date():
    return datetime.today().strftime('%Y-%m-%d')

# loads a journal yaml config file, creating it if missing
def load_config(filename):
    if not os.path.exists(filename):
        save_config(filename, {
            "author": "",
            "path": ""
        })

    with open(filename, "r") as file:
        return yaml.safe_load(file)

# save the config to a file
def save_config(filename, config):
    with open(filename, "w") as file:
            yaml.dump(config, file)