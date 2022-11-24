import sys
import os
import time
import random

def print_slow(str, delay =0.01):
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


knife = False
key = False


def print_welcome():
    
    fprint("""You took your puppy to the park, you let the puppy lose to run around the park and play. You saw you old friend in
     the park while you two were talking you see you puppy run away from the park, you saw the puppy running into a misterious palace
     you awent with her you are now standing in front of the door in the palace Do you want to go in and find the puppy?
     *) Type 'yes' to go enter the palace.
     *) Type 'no' to stay there.
     *) Type 'quit' to exit the game.""",)
    while True:
        choice = input("\n>")
        if choice == "yes":
            entrance()
        elif choice == "no":
            fprint("You stay there wondering where the puppy went :(")
        elif choice == "quit":
            quit_game()
        else:
            fprint("Don't know what you mean.")

def entrance():
    fprint("""You are in the great hall of the mystery palace. All you see is a crystal chandlier above you and a dirty backpack on the floor. 
    You can go north, south, east, or west.
    Where would you like to go?""")
    
    while True:
        choice = input("\n>")
        if choice =="north":
            gallery()
        elif choice == "south":
            fprint("""You came back outside of the palace, Would you like to go back in the palace or exit the game?
            *) Type 'yes' to go back in the palace.
            *) Type 'no' to exit the game.""")
            while True:
                choice = input("\n> ")
                if choice == "yes":
                    entrance()
                elif choice == "no":
                    quit_game()
                else:
                    fprint("Don't know what you mean.")
        elif choice == "east":
            play_room()
        elif choice == "west":
            arcade()
        elif choice == "quit":
            quit_game()


def play_room():
    fprint("""You have entered the play room.""",1)
    print_slow("""
    This is the royal game room. 
    You see a pool table at the center of the room with a crumpled paper ball with something written over it. 
    You can go east, or west.
    Press 'l' to read the crumpled paper ball?
    """,0.03)
    while True:
        choice = input("\n>")
        if choice == "east":
            chamber()
        elif choice == "west":
            entrance()
        elif choice == "l":
            print("The paper ball says:") 
            print_slow("""
            'To be the powerful witch of the world, Dorothy needs to drink a puppy’s blood.
            Lock puppy in the magic bound undercroft until sunset' """)
        else:
            fprint(f"Sorry, I didn't understand that. Please try again.")

    
def arcade():
    fprint("""You have entered the arcade room.""",1)
    fprint("""You see a bunch of old arcade games. You can go north, south, or east.""")
    while True:
        choice = input("\n>")
        if choice == "north":
            scullery()
        elif choice == "south":
            fprint("You see a passage leading to a dungeon, do you want to go in?")
            while True:
                choice = input("\n>")
                if choice == "yes":
                    dungeon()
                elif choice == "no":
                    arcade()
                else:
                    fprint("Don't know what you mean.")
        if choice == "east":
            entrance()
        elif choice == "quit":
            quit_game()

def gallery():
    global knife
    global key
 
    fprint("""You have entered the gallery.""",1)
    fprint("""You see a bunch of paintings on the wall. You can go west, east, or south.""",1)
    fprint("""You see a witch meditating in the center of the room, She has a golden key.""",1)
    fprint("""KILL THE WITCH, to get access to the golden key.""",1)
    fprint("""Press 'F' to attack Dorothi witch""",1)
    dorothy_attack = ([True, False])
   
    while True:
        choice = input("\n>")
        if choice == "west":
            arena()
        elif choice == "east":
            throne_room()
        elif choice == "south":
            entrance()
        elif choice == "quit":
            quit_game()
        elif choice == "F":
            fprint("You attacked Dorothy!")
            if knife == True:
                fprint("You killed Dorothy witch!")
                fprint("Press 'k' to pick up the golden key")
                while True:
                    choice = input("\n>")
                    if choice == "k":
                        fprint("You picked up the golden key")
                        fprint("You can now go to the throne room to get the treasure!")
                        key = True
                        gallery_no_witch()
                        
                    elif choice == "quit":
                        quit_game()
                    else:
                        fprint("Don't know what you mean.")
            elif knife == False:
                fprint("You missed Dorothy witch!")
                fprint("Dorothy witch killed you!")
                fprint("You died!")
                fprint("GAME OVER!")
                fprint("Press 'r' to restart the game")
                while True:
                    choice = input("\n>")
                    if choice == "r":
                        reset_console()
                        print_welcome()
                    elif choice == "quit":
                        quit_game()
                    else:
                        fprint("Don't know what you mean.")
            dorothy_attack = True
            if dorothy_attack == True:
                fprint("You killed Dorothy!")
                fprint("You got the golden key!")
                fprint("You can now go to the throne room!")
                gallery()
            choice = input("\n>")
            if choice == "yes":
                entrance()
            elif choice == "no":
                quit_game()
            
def gallery_no_witch():
    global knife
    global key
 
    fprint("""The gallery is now free 
            You are looking throught the paintings
            You can go west east or south""",1)
   
    while True:
        choice = input("\n>")
        if choice == "west":
            arena()
        elif choice == "east":
            throne_room()
        elif choice == "south":
            entrance()
        elif choice == "quit":
            quit_game()

        

def scullery():
    global knife
    fprint("""You have entered the scullery.""",1)
    fprint("""You see a bunch of old food. It's a mess here in the scullery!
              You see dirty broken dishes and rusty knife lying around. 
              You can go south.""")
    fprint("""You see knife laying on the floor.
            Press 'k' to pick it up""",1)
    while True:
        choice = input("\n>")
        if choice == "south":
            arcade()
        elif choice == "k":
            fprint("You picked up the knife")
            knife = True
            fprint("You can now go to the gallery to kill dorothy witch!")
            
        
        
        elif choice == "quit":
            quit_game()

def throne_room():
    fprint("""You have entered the throne room.""",1)
    fprint("""You are in the throne room. You see the red velvet throne with a Golden key on it..
            You can go west.""")
    while True:
        choice = input("\n>")
        if choice == "west":
            gallery()
        elif choice == "quit":
            quit_game()

def dungeon():
    fprint("""You have entered the dungeon.""",1)
    fprint("""This is the prison cell. It's pitch dark in here. Turn on the flashlight. 
              You can go south, or north""")
    while True:
        choice = input("\n>")
        if choice == "south":
            undercroft()
        elif choice == "north":
            arcade()
        elif choice == "quit":
            quit_game()

def arena():
    print_slow("""You have entered the arena""",0.1)
    fprint("You have entered the Arena. You found a flashlight, would you like to pick it up? You can go east")
    while True:
        choice = input("\n>")
        if choice == "east":
            gallery()
        
        elif choice == "quit":
            quit_game()
        else:
            fprint("I don't understand that. Try again.")


def undercroft():
    global key
    fprint("""The Undercroft is locked. Unlock it with the golden key.
              You can go north.""")
    if key == False:
        fprint("You do not have the key to unlock the door")
        while True:
            choice = input("\n>")
            if choice == "north":
                dungeon()
    elif key == True:
        fprint("Use the golden key to unlock the undercroft")
        fprint("Press 'u' to unlock the undercroft")
        while True:
            choice = input("\n>")
            if choice == "u":
                fprint("You unlocked the undercroft")
                undercroft_unlocked()
            elif choice == "quit":
                quit_game()
            else:
                fprint("Don't know what you mean.")
       
        
def undercroft_unlocked():
    global key
    fprint("You have unlocked the Undercroft and you see your puppy")
    print_slow("YOU WON THE GAME",0.1)
    print("Press any key to exit the game")
    while True:
        choice = input("\n>")
        quit_game()
                



def chamber():
    fprint("You entered the chamber")
    fprint("""You are in the king and queen’s restroom. 
              You see a large canopy bed with ivory curtains.
              You look around the room only to find a mini key. 
              would you like to pick it?
              You can go west""")
    while True:
        choice = input("\n>")
        if choice == "west":
            play_room()
        
        elif choice == "quit":
            quit_game()
        else:
            fprint("I don't understand that. Try again.")

def quit_game():
    fprint("Thank you for playing",0.5)
    quit()
    

print_welcome()


