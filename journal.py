import os, fnmatch

from sail.cli_lib import ask_question, ask_paragraph, ask_choice, get_date, load_config, save_config

from functions import fancy_print, make_folder, create_file, write_file, add_to_file, read_file

data = load_config("config.yaml")
author = data['author']
path = data['path']

def pick_journal():
    author = ask_question("What is your name?")
    path = ask_question("What is a good folder for your journal?")

    save_config("config.yaml", dict(author=author, path=path))
    
    if path != "sail_journal":
        make_folder(path)

def write_journal():
    entry = get_date() + ".txt"

    os.chdir(path)
    journal_list = os.listdir()

    if not journal_list or entry not in journal_list:
        create_file(entry)

        write_file(entry, f"Journal Entry: {entry}")

    print("Writing into entry " + entry)
    add_content(entry)

def add_content(filename):
    writing = ask_paragraph("What would you like to write about?")
    add_to_file(filename, writing)

def read_entries():
    os.chdir(path)
    journal_list = os.listdir()

    if not journal_list:
        print("You don't have any entries yet, write something!")
        return

    entry = ask_choice("Choose an entry to read:", journal_list)
    
    content = read_file(entry)
    if content == None:
        print("Nothing in this entry!")
    else:
        print(content)


fancy_print("Gratitude Journal")

choice = ask_choice("What would you like to do?", [
    "Pick Journal",
    "Write Journal",
    "Read Entries",
    "I'm Feeling Lucky",
    "Load the SAIL Journal",
    "Quit"
])

if choice == "Pick Journal":
    pick_journal()
elif choice == "Write Journal":
    write_journal()
elif choice == "Read Entries":
    read_entries()
elif choice == "Load the SAIL Journal":
    save_config("config.yaml", dict(author="SAIL Student", path="sail_journal"))
else:
    print("Goodbye, have a lovely day!")
