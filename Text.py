import time
import os
import sys

class Text:

    """This function slows down the print function so that it looks like the computer is typing."""
    def print_slow(self, str, delay =0.01, delay2 = 1):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print("\n")
        time.sleep(delay2)
    """This function clears the console"""
    def reset_console(self):
        print("\n")
        os.system("cls")
    """This function puts a delay between each line of text"""
    def fprint(self, str, delay =0.1):
        print("\n"+str)
        time.sleep(delay)
text = Text()