# set the characters for the password
# use random for generate the random password
# ask to the user for the number of characters for the password
# use tkinter for create the GUI
import random


class pass_generator():
    def nums_of_char(self):
        while True:
            try:
                number_characters = int(
                    input('Length of the Password (min 8):'))
                if number_characters < 8:
                    print("Write a number higher than 7")
                else:
                    break
            except NameError:
                print("Write a number higher than 7")
        print('works')


if __name__ == "__main__":
    instance = pass_generator()
    instance.nums_of_char()
