import sys
import os
import time
import random
"""This function slows down the print function so that it looks like the computer is typing."""
def print_slow(str, delay =0.01, delay2 = 1):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")
    time.sleep(delay2)
"""This function clears the console"""
def reset_console():
    print("\n")
    os.system("cls")
"""This function puts a delay between each line of text"""
def fprint(str, delay =0.1):
    print("\n"+str)
    time.sleep(delay)

player = {"location":"", "items":[]}

"""This is the initial state of items in the game"""
knife = False
key = False
dorothy_killed = False

"""This function is the welcome screen"""
def print_welcome():
    print_slow("""
    HI!
    Let's go on an adventure!""",0.02)
    print_slow("""
    On a sunny day, you took your puppy to the park.""")
    print_slow("""
    You were playing fetch with your puppy, suddently your puppy ran into the distance.""")
    print_slow("""
    You chased your puppy, puppy ran into a mysterious palace in the distance. """)
    print_slow("""
                You ran to the mysterious palace, 
                You are standing in front of the door. 
    *) Type 'yes' to enter the palace.
    *) Type 'no' to stay there.
    *) Type 'quit' on any part of the game to exit. """)
    while True:
        choice = input("\n>")
        if choice == "yes":
            print_slow("You pushed the jammed half opened door.")
            print_slow("You stumblled into the Great Hall.",)
            entrance()
        elif choice == "no":
            print_slow("You stay there wondering where the puppy went :(")
        elif choice == "quit":
            quit_game()
        else:
            fprint("Don't know what you mean.")

"""This function is the enterence i.e the Great Hall"""
def entrance():
    print_slow("""You are now in the Great Hall.""")
    print_slow("""All you see is a wide open empty hall with a big crystal chandelier hanging from the ceiling.""")
    print_slow("""You can go 'north', 'south', 'east', or 'west'.""")
    print_slow("""Where do you want to go?""")

    while True:
        choice = input("\n>")
        """This code determines what instance of the gallery function to run"""
        if choice =="north" and dorothy_killed == False:
            gallery()
        elif choice =="north" and dorothy_killed == True:
            gallery_no_witch()
        elif choice == "south":
            print_slow("You came back outside the palace.")
            print_slow("Would you like to go back in the palace or exit the game?")
            print_slow("""
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
        else:
            fprint("Don't know what you mean.")

def play_room():
    print_slow("""You have entered the play room.""")
    print_slow("""This is the royal game room.""") 
    print_slow("""You see a pool table at the center of the room.""")
    print_slow("""There is a crumpled paper ball on the table with something written over it.""")
    print_slow("""Press 'e' to pick up and read the crumpled paper ball?""") 
    print_slow("""You can go 'east', or 'west'.""")
    while True:
        choice = input("\n>")
        if choice == "east":
            chamber()
        elif choice == "west":
            entrance()
        elif choice == "e":
            print_slow("The paper ball says:") 
            print_slow("""
            'To be the powerful witch of the world, Dorothy needs to drink a puppy’s blood.
            Lock puppy in the magic bound undercroft until sunset' """)
        else:
            fprint("Don't know what you mean.")
 
def arcade():
    print_slow("""You have entered the arcade room.""")
    print_slow("""You see a bunch of arcade games.""")
    print_slow("""You can go 'north', 'south', or 'east'.""")
    while True:
        choice = input("\n>")
        if choice == "north":
            scullery()
        elif choice == "south":
            print_slow("""You see a passage leading to a dungeon, do you want to go in?
            *) Type 'yes' to go in.
            *) Type 'no' to go back.""")
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
        else:
            fprint("Don't know what you mean.")

def gallery():
    global knife
    global key
    global dorothy_killed
 
    print_slow("""You have entered the gallery.""",)
    print_slow("""You see a bunch of paintings on the wall.""",)
    print_slow("""You see a witch meditating in the center of the room, She is holding a golden key.""",)
    print_slow("""KILL THE WITCH, to get access to the golden key.""",)
    print_slow("""Press 'e' to attack Dorothy witch, or to go back to the Great Hall type 'south.'""",)
    
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
            print_slow("You attacked Dorothy!")
            if knife == True:
                dorothy_attack_with_knife()
            elif knife == False:
                dorothy_attack_with_no_knife()
                
        else:
            print_slow("Don't know what you mean.")  

def dorothy_attack_with_knife():
    print_slow("You are Fighting with a knife!")
    print_slow("..........")
    print_slow("Hoohoo!")
    print_slow("You killed Dorothy witch!")
    print_slow("Press 'k' to pick up the golden key.")
    print_slow("""You can go 'south', 'east', or 'west'.""")
    while True:
        choice = input("\n>")
        if choice == "k":
            print_slow("You picked up the golden key.")
            print_slow
            key = True
            dorothy_killed = True
            gallery_no_witch()
            
        elif choice == "quit":
            quit_game()
        else:
            print_slow("Don't know what you mean.")

def dorothy_attack_with_no_knife():
    print_slow("You are Fighting with your bare hands!")
    print_slow("..........",0.3)
    print_slow("You can't kill Dorothy witch she is too powerful!")
    print_slow("You missed Dorothy witch!")
    print_slow("Dorothy witch killed you!",0.3)
    print_slow("You died!",0.3)
    print_slow("GAME OVER!",0.3)
    print_slow("Press 'r' to restart the game.")
    while True:
        choice = input("\n>")
        if choice == "r":
            reset_console()
            print_welcome()
        elif choice == "quit":
            quit_game()
        else:
            print_slow("Don't know what you mean.")
            
def gallery_no_witch():
    global knife
    global key
    print_slow("""You are in the Gallery.""",)
    print_slow("""You see a bunch of paintings on the wall.""",)
    print_slow("""You can go 'south', 'east', or 'west'.""")
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
            print_slow("Don't know what you mean.")

def scullery():
    global knife
    print_slow("""You have entered the scullery.""",)
    print_slow("""It's a mess here in the scullery!""")
    print_slow("""You see dirty broken dishes.""")
    print_slow("""You see a bunch of kitchen utensils.""",)
    print_slow("""You see a knife on the table.""",)
    print_slow("""Press 'e' to pick up the knife.""",)
    print_slow("""You can go 'south'.""")
    while True:
        choice = input("\n>")
        if choice == "south":
            arcade()
        elif choice == "e":
            print_slow("You picked up the knife")
            knife = True
            print_slow("You can now go to the gallery to kill dorothy witch!")
        elif choice == "quit":
            quit_game()
        else:
            print_slow("Don't know what you mean.")

def throne_room():
    print_slow("""You have entered the throne room.""")
    print_slow("""You are in the throne room. You see the red velvet throne.""")
    print_slow("""You can go 'west'.""")
    while True:
        choice = input("\n>")
        if choice == "west" and dorothy_killed == False:
            gallery()
        elif choice =="west" and dorothy_killed == True:
            gallery_no_witch()
        elif choice == "quit":
            quit_game()
        else:
            print_slow("Don't know what you mean.")

def dungeon():
    print_slow("""You have entered the dungeon.""")
    print_slow("""You see a bunch of cages and chains.""")
    print_slow("""You can go 'north', or 'south'.""")
    while True:
        choice = input("\n>")
        if choice == "south":
            undercroft()
        elif choice == "north":
            arcade()
        elif choice == "quit":
            quit_game()
        else:
            print_slow("Don't know what you mean.")

def arena():
    print_slow("""You have entered the arena""")
    print_slow("You have entered the Arena.")
    print_slow("You see a bunch of weapons on the ground.")
    print_slow("You can go 'east'.")
    while True:
        choice = input("\n>")
        if choice == "east" and dorothy_killed == False:
            gallery()
        elif choice =="east" and dorothy_killed == True:
            gallery_no_witch()
        
        elif choice == "quit":
            quit_game()
        else:
            print_slow("I don't understand that. Try again.")

def undercroft():
    global key
    print_slow("""The Undercroft is locked.""")
    print_slow("""You need the golden key to unlock the door.""")
    print_slow("""You can go 'north'.""")
    if key == False:
        no_key()
    elif key == True:
        yes_key()
    else:
            print_slow("Don't know what you mean.")

def no_key():
    print_slow("You do not have the key to unlock the door")
    while True:
        choice = input("\n>")
        if choice == "north":
            dungeon()
       
def yes_key():
    print_slow("Use the golden key to unlock the undercroft")
    print_slow("Press 'u' to unlock the undercroft")
    while True:
        choice = input("\n>")
        if choice == "u":
            print_slow("..........",0.2)
            print_slow("You unlocked the undercroft")
            undercroft_unlocked()
        elif choice == "quit":
            quit_game()
        else:
                print_slow("Don't know what you mean.")

def undercroft_unlocked():
    global key
    print_slow("You are in the Undercroft. and you see your puppy")
    print_slow("You see your puppy tied to a chair")
    print_slow("You untied your puppy")
    print_slow(".......",0.2)
    print_slow("Took your puppy and went outside the mysterious palace")
    print_slow("YOU WON THE GAME",0.5)
    print_slow("Press any key to exit the game")
    while True:
        choice = input("\n>")
        quit_game()

def chamber():
    print_slow("You entered the chamber")
    print_slow("You are in the king and queen’s bedroom.")
    print_slow("You see a large canopy bed with ivory curtains.")
    print_slow("You can go 'west'.")
    while True:
        choice = input("\n>")
        if choice == "west":
            play_room()
        
        elif choice == "quit":
            quit_game()
        else:
            fprint("Don't know what you mean.")

def quit_game():
    fprint("Thank you for playing",0.5)
    quit()
    

print_welcome()
"""https://i.kym-cdn.com/entries/icons/mobile/000/028/021/work.jpg"""


