import os, io
from contextlib import redirect_stdout

import pytest

from functions import fancy_print, make_folder, create_file, write_file, add_to_file, read_file

class TestStepOne:
    folder = "test_folder"

    def test_make_folder(self, tmp_path):
        os.chdir(tmp_path)

        make_folder(self.folder)

        excepted = False
        try:
            make_folder(self.folder)
        except FileExistsError:
            excepted = True
        print("We shouldn't throw an exception!")
        assert not excepted

class TestStepTwo:
    file = "tmp.txt"
    text = "Hello world!"

    def test_write_file(self, tmp_path):
        os.chdir(tmp_path)

        open(self.file, 'x')

        excepted = False
        try:
            write_file(self.file, self.text)
        except:
            excepted = True
        print("We shouldn't throw an exception!")
        assert not excepted

        print("The file should exist!")
        assert os.path.exists(self.file)

        with open(self.file, 'r') as file_content:
            print("The file should have what we wrote!")
            assert file_content.read() == self.text

class TestStepThree:
    file = "tmp.txt"
    text = "Hello world!"

    def test_read_file(self, tmp_path):
        os.chdir(tmp_path)

        with open(self.file, 'w') as file_content:
            file_content.write(self.text)
        
        assert read_file(self.file) == self.text

class TestStepFour:
    file = "tmp.txt"
    text = "Hello world!"
    text2 = "Line 2!"

    def test_append_file(self, tmp_path):
        os.chdir(tmp_path)

        add_to_file(self.file, self.text)
        add_to_file(self.file, self.text2)
        
        assert read_file(self.file) == (self.text + self.text2)

class TestStepFive:
    text = "Hi"

    def test_fancy_print(self):
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            fancy_print("Hi")
        assert stdout.getvalue() != "Hi\n"