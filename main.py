# set the characters for the password
# use random for generate the random password
# use tkinter for create the GUI
import random
import os
import sys
import pyperclip
from tkinter import *
from tkinter.ttk import *

class pass_generator():
    def __init__(self):
        """Setting the number of characters"""
        while True:
            try:
                self.number_characters = int(
                    input('Length of the Password (min 8):'))
                if self.number_characters < 8:
                    print("Write a number higher than 7")
                else:
                    break
            except NameError:
                print("Write a number higher than 7")

    def generate(self):
        """Setiing the password characters"""
        self.lower_letters = 'abcdefghijklmnopqrstuvwxyz'
        self.upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        self.all_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ()[]{}*&^%$#!~'
        self.password = []
        self.counter = 0

        while self.counter <= self.number_characters:
            self.random_char = random.choice(self.all_char)
            self.password.append(self.random_char)
            self.counter += 1
        self.password = ''.join([str(elem) for elem in self.password])
        print(self.password)

if __name__ == "__main__":
    while True:
        instance = pass_generator()
        instance.generate()
        # Ask the user for run again
        run_again = input('\nRun Again? [Y/N]')
        if run_again == 'y' or run_again == 'yes':
            continue
        else:
            os.system('cls')
            sys.exit()
