import os

from plumbum import colors
from pyfiglet import Figlet

# You got this! :)

def make_folder(foldername):
    # TODO: Step 1!
    os.makedirs(foldername)

def write_file(filename, content):
    # TODO: Step 2!
    with open(filename, 'r') as file:
        file.write(content)

def read_file(filename):
    # TODO: Step 3!
    pass

def add_to_file(filename, content):
    # TODO: Step 4!
    pass

def fancy_print(text):
    # TODO: Step 5!
    print(text)

###################################
#                                 #
#  We've got these ones covered!  #
#                                 #
###################################

def create_file(filename):
    with open(filename, 'x') as file:
        pass
