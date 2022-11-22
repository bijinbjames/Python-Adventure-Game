import sys
import os
import time
import random

def print_slow(str, delay =0.1):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def reset_console():
    print("\n")
    os.system("cls")

def fprint(str, delay =0.1):
    print("\n"+str)
    time.sleep(delay)

def sprint(str, delay =0.1):
    print(str)
    time.sleep(delay)

""" This is the main room of the game. It is where the player will 
    start the game. It is also where the player will be able to 
    access all other rooms in the game."""

def print_welcome():
    fprint("""You took your puppy to the park, you let the puppy lose to run around the park and play. You saw you old friend in
     the park while you two were talking you see you puppy run away from the park, you saw the puppy running into a misterious palace
     you awent with her you are now standing in front of the doon in the palace Do you want to go in and find the puppy?""")
    while True:
        choice = input("\n>")
        if choice == "north":
            entrance()
        elif choice == "south":
            play_room()
        elif choice == "east":
            arcade()
        elif choice == "west":
            gallery()
        else:
            fprint("That is not a valid direction.")

def entrance():
    fprint("You are in the great hall of the mystery palace. All you see is a crystal chandlier above you and a dirty backpack on the floor. You can go north, south, east, or west.")
    print("Would you like to pick it up or ignore?")
    while True:
        choice = input("\n>")
        if choice == "pick it up":
            fprint("You picked up the backpack.")
            fprint("You now have a backpack.")
            backpack = True
        else:
            break


def play_room():
    pass
    
def arcade():
    pass

def gallery():
    pass

def scullery():
    pass

def throne_room():
    pass

def dungeon():
    pass

def arena():
    pass

def undercroft():
    pass

def chamber():
    pass
