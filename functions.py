import sys
import os
import time
def clear_screen():
    print('...')
    time.sleep(20)
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
        ani("[Your Consciousness believes you made the wrong choice and to change it while you can]")
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



#From Kitchen
def kitchen():
    ani("  ")
    ani("<You walk along the black and white tiles of the north hallway, following the path until you reach a bright yellow door.>")
    ani("<Do you wish to push open the door?>")
    ani("[Your Consciousness urges you to keep going, don't stop]")
    choice4n()

def choice4n():
    choice4na= input("Y/N?: ")
    if choice4na.lower() == "y":
        ani("  ")
        ani("<You push open the door and look around>")
        ani("<You have a sudden pull to the counter>")
        ani("<A knife>")  
        ani("<Do you wish to take the knife?>")
        choice5n()
    elif choice4na == "n" or "N":
        ani("  ")
        ani("'That's not the right choice'")
        ani("<You note down the mistake in your mind for next time>")
        ani("  ")
        ani("You died. How about you try again!")
        clear_screen()
    else:
        ani("  ")
        ani("'How'd you fail a simple Y/N?'")
        clear_screen()

def choice5n():
    choice5na=input("Y/N?: ")
    if choice5na.lower() == "y":
        ani("  ")
        ani("<You hear a new voice along with your Consciousness... >")
        ani("|I'm sorry, I thought I could give you everything...|")
        ani("   ")
        ani("<You turn around from the counter and realise that there's a doll>")
        ani("<It's just standing>")
        ani("<Waiting>")
        ani("   ")
        ani("[Your consciousness urges you to destroy it]")
        ani("<You don't have a choice>")
        ani("    ")
        ani("|Why are you here?|")
        ani("|...|")
        ani("|I'm so sorry|")
        ani("  ")
        ani("<The doll gives you a riddle...>")
        ani("|What is the most important thing to a chef?|")
        ani("<Your choices: Their Knife (a); Their Skill (b); Their Workspace (c); Their Integrity (d)>")
        choice6n()
    elif choice5na.lower() == "n":
        ani("  ")
        ani("'You might regret this later'")
        ani("[Your Consciousness is annoyed]")
        ani("   ")
        ani("<You turn around from the counter and realise that there's a doll>")
        ani("<It's just standing>")
        ani("<Waiting>")
        ani("   ")
        ani("[Your consciousness urges you to destroy it]")
        ani("<You don't have a choice>")
        ani("    ")
        ani("<You don't have a weapon...>")
        ani("  ")
        ani("YOU DIED?! YOU ♓♎︎♓︎□︎⧫︎", delay=0.07)
        clear_screen()
    else:
        ani("  ")
        ani("'Whelp... don't know how you failed that'")
        ani("   ")
        clear_screen()

def choice6n():
    choice6na=input("<Your answer>: ")
    if choice6na == "a" or "A":
        ani("  ")
        ani("'You selected the correct answer!'")
        ani("'Now you have one last thing to do'")
        choice7n()
    else:
        ani("'That's not the right answer'")
        ani("You died, try again-")
        clear_screen()

def choice7n():
    choice7na=input("'DO IT (Y/N): '")
    if choice7na == "y" or "Y":
        ani("|Why?|", delay=0.5)
        ani("  ")
        ani("<But the voice remains...>")
        ani("|I tried my best|")
        ani("  ")
        ani("'You did such a good job'")
        ani("[Your Consciousness tell you to keep moving]")
        ani(" ")
        ani("<You shakely walk out the yellow door and out into the room that started everything>")
        choice8n()
    else:
        ani("'Do you think you have a choice?'")
        ani("  ")
        choice7n()

def choice8n():
    choice8na= input("S/W/E: ")
    if choice8na.lower() == "s":
        ani("  ")
        ani("<Slowly, you walk towards the south hallway until you see the sign>")
        ani("'Only 3 more to go :)'")
        ani("[You feel wonderful]")
        ani("<You feel unnerved>")
        ani("  ")
        childsn()
    elif choice8na.lower() == "w":
        ani("asds")

def childsn():
    ani("<You walk along the colourful hallway  see a cute pastel blue door at the end of the hallway>")
    ani("<It makes your heart ache>")
    ani(" ")
    choice9n()

def choice9n():
    choice9na=input("Go in? Y/N: ")
    if choice9na.lower() == "y":
        ani("  ")
        ani("[:)]")
        ani("<You push the door slightly and see a broken rattle>")
        ani(" ")
        ani("[You already have a knife]")
        ani("<You push the door and see a sleeping child?")
        ani("...", delay=0.25)
        ani("<Not a child.>")
        ani("[Your Consciousness happily declares it's another doll! After this? Only 2 more!]")
        ani("|...|")
        ani("   ")
        ani("'Well that's no fun. How about this? I'll give you a puzzle since they're sleeping!'")
        choice10n()
    else:
        ani("Don't resist", delay=0.2)
        choice9n()

def choice10n():
    ani("asd")
    

intro()
