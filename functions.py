import sys
import os
import time
def clear_screen():
    print('...')
    time.sleep(60)
    # Check the operating system and run the appropriate clear command
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

def ani(text, delay=0.06):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

#def inani(text, delay=0.06):   #scrapped due to bugging issues regarding global code
    #for char in text:
        #sys.stdout.write(char)
        #sys.stdout.flush()
        #time.sleep(delay)
    #input()  # Move to the next line

def intro():
    ani("Welcome to the game Consciousness! We hope that you have a wonderful experience!")
    name=input("What's your name?: ") 
    name
    ani("<But you can't seem to remember>")
    ani(" ")
    ani("<You wake up to a place unfamiliar but familiar to yourself>")
    ani("<The first thing you see? A sign>")
    ani("'Welcome, you have one goal destroy all 4 dolls scattered across different rooms!'")
    ani("'If you do... you'll get a prize! How about it?'")
    choice1()

def choice1():
    choice1a = input("Y/N: ")
    
    if choice1a.lower() == 'y':
        ani("  ")
        ani("'Very good...'")
        ani("[Your Consciousness feels content with this option]")
        ani("<As you look around, you see 4 different corridors with labels.>")
        ani ("'Kitchen - North'")
        ani("'Child's room - South'")
        ani("'Master Bedroom - East'")
        ani("'Garage - West'")
        ani("[You start to look to each path]")
        choice3()
    elif choice1a.lower() == 'n':
        ani("  ")
        ani("'Are you sure? The consequences for denial... are detrimental.'")
        ani("[Your Consciousness believes you made the wrong choice and to change it while you have the chance]")
        choice2()

    else:
        print(choice1)
        ani("  ")
        ani("'⧫︎♒︎♋︎⧫︎🕯︎⬧︎ ■︎□︎⧫︎ ⧫︎♒︎ ︎♏⬧︎♍︎❒︎♓︎ ︎◻⧫︎...'", delay=0.2)
        ani("Your feeling unsettled")
        ani("  ")
        ani("You failed, restart the game to try again") 
        clear_screen()

def choice2():
    choice2a=input("Y/N? (CAPITAL): ")
    if choice2a == "N":
        ani("  ")
        ani("'You've made the right choice... I'll take you back to where you went wrong'")
        choice1()
    elif choice2a == "Y":
        ani("  ")
        ani("'I warned you...'")
        ani("[You can't escape ♓︎⧫︎🕯︎⬧︎ ♑︎❒︎♓︎ ︎◻]")
        ani("  ")
        ani("Uh oh! You died! How about you try again?")
        clear_screen()
    elif choice2a == "y" or "n":
        ani("  ")
        ani("'I told you to use a capital...'")
        ani("  ")
        ani("'︎♓♎︎♓︎□︎⧫︎'", delay=0.5)
        ani("  ")
        ani("[Your Consciousness is dissapointed in yourself]")
        ani("  ")
        ani("ERROR: YOU'VE BEEN KICKED OUT OF THE SYSTEM PLEASE RESTART")
        ani("<Rude>")
        clear_screen()
    else:
        ani("  ")
        ani("'⧫︎♒︎♋︎⧫︎🕯︎⬧︎ ■︎□︎⧫︎ ⧫︎♒︎ ︎♏⬧︎♍︎❒︎♓︎ ︎◻⧫︎...'", delay=0.2)
        ani("<Your feeling unsettled>")
        ani("  ")
        ani("You failed, restart the game to try again") 
        clear_screen()

def choice3():
    choice3a = input("N/S/W/E: ")
    if choice3a.lower() == "n":
        kitchen()
    elif choice3a.lower() == "s":
        childs()
    elif choice3a.lower() == "w":
        master()
    elif choice3a.lower() == "e":
        garage()
    else:
        ani(" ")
        ani("'That's not an option'")
        ani("Try again")
        choice3()
        
choice3()
