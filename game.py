import sys
import os
import time
from Text import text

player = {"location":"", "items":[]}

"""This is the initial state of items in the game"""
knife = False
key = False
dorothy_killed = False

"""This function is the welcome screen"""
def print_welcome():
    text.print_slow("""
    HI!
    Let's go on an adventure!""",0.02)
    text.print_slow("""
    On a sunny day, you took your puppy to the park.""")
    text.print_slow("""
    You were playing fetch with your puppy, suddently your puppy ran into the distance.""")
    text.print_slow("""
    You chased your puppy, puppy ran into a mysterious palace in the distance. """)
    text.print_slow("""
                You ran to the mysterious palace, 
                You are standing in front of the door. 
    *) Type 'yes' to enter the palace.
    *) Type 'no' to stay there.
    *) Type 'quit' on any part of the game to exit. """)
    while True:
        choice = input("\n>")
        if choice == "yes":
            text.print_slow("You pushed the jammed half opened door.")
            text.print_slow("You stumblled into the Great Hall.",)
            entrance()
        elif choice == "no":
            text.print_slow("You stay there wondering where the puppy went :(")
        elif choice == "quit":
            quit_game()
        else:
            text.fprint("Don't know what you mean.")

"""This function is the enterence i.e the Great Hall"""
def entrance():
    text.print_slow("""You are now in the Great Hall.""")
    text.print_slow("""All you see is a wide open empty hall with a big crystal chandelier hanging from the ceiling.""")
    text.print_slow("""You can go 'north', 'south', 'east', or 'west'.""")
    text.print_slow("""Where do you want to go?""")

    while True:
        choice = input("\n>")
        """This code determines what instance of the gallery function to run"""
        if choice =="north" and dorothy_killed == False:
            gallery()
        elif choice =="north" and dorothy_killed == True:
            gallery_no_witch()
        elif choice == "south":
            text.print_slow("You came back outside the palace.")
            text.print_slow("Would you like to go back in the palace or exit the game?")
            text.print_slow("""
            *) Type 'yes' to go back in the palace.
            *) Type 'no' to exit the game.""")
            while True:
                choice = input("\n> ")
                if choice == "yes":
                    entrance()
                elif choice == "no":
                    quit_game()
                else:
                    text.fprint("Don't know what you mean.")
        elif choice == "east":
            play_room()
        elif choice == "west":
            arcade()
        elif choice == "quit":
            quit_game()
        else:
            text.fprint("Don't know what you mean.")

def play_room():
    text.print_slow("""You have entered the play room.""")
    text.print_slow("""This is the royal game room.""") 
    text.print_slow("""You see a pool table at the center of the room.""")
    text.print_slow("""There is a crumpled paper ball on the table with something written over it.""")
    text.print_slow("""Press 'e' to pick up and read the crumpled paper ball?""") 
    text.print_slow("""You can go 'east', or 'west'.""")
    while True:
        choice = input("\n>")
        if choice == "east":
            chamber()
        elif choice == "west":
            entrance()
        elif choice == "e":
            text.print_slow("The paper ball says:") 
            text.print_slow("""
            'To be the powerful witch of the world, Dorothy needs to drink a puppy’s blood.
            Lock puppy in the magic bound undercroft until sunset' """)
        else:
            text.fprint("Don't know what you mean.")
 
def arcade():
    text.print_slow("""You have entered the arcade room.""")
    text.print_slow("""You see a bunch of arcade games.""")
    text.print_slow("""You can go 'north', 'south', or 'east'.""")
    while True:
        choice = input("\n>")
        if choice == "north":
            scullery()
        elif choice == "south":
            text.print_slow("""You see a passage leading to a dungeon, do you want to go in?
            *) Type 'yes' to go in.
            *) Type 'no' to go back.""")
            while True:
                choice = input("\n>")
                if choice == "yes":
                    dungeon()
                elif choice == "no":
                    arcade()
                else:
                    text.fprint("Don't know what you mean.")
        if choice == "east":
            entrance()
        elif choice == "quit":
            quit_game()
        else:
            text.fprint("Don't know what you mean.")

def gallery():
    global knife
    global key
    global dorothy_killed
 
    text.print_slow("""You have entered the gallery.""",)
    text.print_slow("""You see a bunch of paintings on the wall.""",)
    text.print_slow("""You see a witch meditating in the center of the room, She is holding a golden key.""",)
    text.print_slow("""KILL THE WITCH, to get access to the golden key.""",)
    text.print_slow("""Press 'e' to attack Dorothy witch, or to go back to the Great Hall type 'south.'""",)
    
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
        elif choice == "e":
            text.print_slow("You attacked Dorothy!")
            if knife == True:
                dorothy_attack_with_knife()
            elif knife == False:
                dorothy_attack_with_no_knife()
                
        else:
            text.print_slow("Don't know what you mean.")  

def dorothy_attack_with_knife():
    text.print_slow("You are Fighting with a knife!")
    text.print_slow("..........")
    text.print_slow("Hoohoo!")
    text.print_slow("You killed Dorothy witch!")
    text.print_slow("Press 'k' to pick up the golden key.")
    text.print_slow("""You can go 'south', 'east', or 'west'.""")
    while True:
        choice = input("\n>")
        if choice == "k":
            text.print_slow("You picked up the golden key.")
            text.print_slow
            key = True
            dorothy_killed = True
            gallery_no_witch()
            
        elif choice == "quit":
            quit_game()
        else:
            text.print_slow("Don't know what you mean.")

def dorothy_attack_with_no_knife():
    text.print_slow("You are Fighting with your bare hands!")
    text.print_slow("..........",0.3)
    text.print_slow("You can't kill Dorothy witch she is too powerful!")
    text.print_slow("You missed Dorothy witch!")
    text.print_slow("Dorothy witch killed you!",0.3)
    text.print_slow("You died!",0.3)
    text.print_slow("GAME OVER!",0.3)
    text.print_slow("Press 'r' to restart the game.")
    while True:
        choice = input("\n>")
        if choice == "r":
            text.reset_console()
            print_welcome()
        elif choice == "quit":
            quit_game()
        else:
            text.print_slow("Don't know what you mean.")
            
def gallery_no_witch():
    global knife
    global key
    text.print_slow("""You are in the Gallery.""",)
    text.print_slow("""You see a bunch of paintings on the wall.""",)
    text.print_slow("""You can go 'south', 'east', or 'west'.""")
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
        else:
            text.print_slow("Don't know what you mean.")

def scullery():
    global knife
    text.print_slow("""You have entered the scullery.""",)
    text.print_slow("""It's a mess here in the scullery!""")
    text.print_slow("""You see dirty broken dishes.""")
    text.print_slow("""You see a bunch of kitchen utensils.""",)
    text.print_slow("""You see a knife on the table.""",)
    text.print_slow("""Press 'e' to pick up the knife.""",)
    text.print_slow("""You can go 'south'.""")
    while True:
        choice = input("\n>")
        if choice == "south":
            arcade()
        elif choice == "e":
            text.print_slow("You picked up the knife")
            knife = True
            text.print_slow("You can now go to the gallery to kill dorothy witch!")
        elif choice == "quit":
            quit_game()
        else:
            text.print_slow("Don't know what you mean.")

def throne_room():
    text.print_slow("""You have entered the throne room.""")
    text.print_slow("""You are in the throne room. You see the red velvet throne.""")
    text.print_slow("""You can go 'west'.""")
    while True:
        choice = input("\n>")
        if choice == "west" and dorothy_killed == False:
            gallery()
        elif choice =="west" and dorothy_killed == True:
            gallery_no_witch()
        elif choice == "quit":
            quit_game()
        else:
            text.print_slow("Don't know what you mean.")

def dungeon():
    text.print_slow("""You have entered the dungeon.""")
    text.print_slow("""You see a bunch of cages and chains.""")
    text.print_slow("""You can go 'north', or 'south'.""")
    while True:
        choice = input("\n>")
        if choice == "south":
            undercroft()
        elif choice == "north":
            arcade()
        elif choice == "quit":
            quit_game()
        else:
            text.print_slow("Don't know what you mean.")

def arena():
    text.print_slow("""You have entered the arena""")
    text.print_slow("You have entered the Arena.")
    text.print_slow("You see a bunch of weapons on the ground.")
    text.print_slow("You can go 'east'.")
    while True:
        choice = input("\n>")
        if choice == "east" and dorothy_killed == False:
            gallery()
        elif choice =="east" and dorothy_killed == True:
            gallery_no_witch()
        
        elif choice == "quit":
            quit_game()
        else:
            text.print_slow("I don't understand that. Try again.")

def undercroft():
    global key
    text.print_slow("""The Undercroft is locked.""")
    text.print_slow("""You need the golden key to unlock the door.""")
    text.print_slow("""You can go 'north'.""")
    if key == False:
        no_key()
    elif key == True:
        yes_key()
    else:
            text.print_slow("Don't know what you mean.")

def no_key():
    text.print_slow("You do not have the key to unlock the door")
    while True:
        choice = input("\n>")
        if choice == "north":
            dungeon()
       
def yes_key():
    text.print_slow("Use the golden key to unlock the undercroft")
    text.print_slow("Press 'u' to unlock the undercroft")
    while True:
        choice = input("\n>")
        if choice == "u":
            text.print_slow("..........",0.2)
            text.print_slow("You unlocked the undercroft")
            undercroft_unlocked()
        elif choice == "quit":
            quit_game()
        else:
                text.print_slow("Don't know what you mean.")

def undercroft_unlocked():
    global key
    text.print_slow("You are in the Undercroft. and you see your puppy")
    text.print_slow("You see your puppy tied to a chair")
    text.print_slow("You untied your puppy")
    text.print_slow(".......",0.2)
    text.print_slow("Took your puppy and went outside the mysterious palace")
    text.print_slow("YOU WON THE GAME",0.5)
    text.print_slow("Press any key to exit the game")
    while True:
        choice = input("\n>")
        quit_game()

def chamber():
    text.print_slow("You entered the chamber")
    text.print_slow("You are in the king and queen’s bedroom.")
    text.print_slow("You see a large canopy bed with ivory curtains.")
    text.print_slow("You can go 'west'.")
    while True:
        choice = input("\n>")
        if choice == "west":
            play_room()
        
        elif choice == "quit":
            quit_game()
        else:
            text.fprint("Don't know what you mean.")

def quit_game():
    text.fprint("Thank you for playing",0.5)
    quit()
    

print_welcome()
"""https://i.kym-cdn.com/entries/icons/mobile/000/028/021/work.jpg"""
