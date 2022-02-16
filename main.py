# set the characters for the password
# use random for generate the random password
# use tkinter for create the GUI
import random
import os
import sys

class pass_generator():
    def __init__(self):
        """Setting the number of characters"""
        while True:
            try:
                self.length = int(
                    input('Length of the Password (min 8):'))
                if self.length < 8:
                    print("Write a number higher than 7")
                else:
                    break
            except NameError:
                print("Write a number higher than 7")

    def generate(self):
        """Setiing the password characters"""
        self.lower = "abcdefghijklmnopqrstuvwxyz"
        self.upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.digits = "0123456789 !@#$%^&*()"
        self.string = self.lower + self.upper + self.digits
        self.password = "".join(random.sample(self.string, self.length))


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
