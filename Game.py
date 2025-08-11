import sys
import os
import colorama
import time

def clear_screen():
    print('...')
    time.sleep(20)
    # Check the operating system and run the appropriate clear command
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

def ani(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

def inani(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    input()  # Move to the next line



ani("Welcome to the game Consciousness! We hope that you have a wonderful experience!")
name= inani("What's your name?: ")
ani("<But you can't seem to remember>")
ani(" ")
ani("<You wake up to a place unfamiliar but familiar to yourself, the first thing you see? A sign>")
ani("'Welcome, you have one goal destroy all 4 dolls scattered across different rooms!'")
ani("'If you do... you'll get a prize! How about it?'")
choice1=input("Y/N?: ")


if choice1.lower() == "y":
    ani("  ")
    ani("'Very good...'")
    ani("[Your Consciousness feels content with this option]")
    ani("<As you look around, you see 4 different corridors with labels.>")
    ani ("'Kitchen - North'")
    ani("'Child's room - South'")
    ani("'Master Bedroom - East'")
    ani("'Garage - West'")
    ani("[You start]")
    choice3=inani("N/S/W/E: ")
    if choice3.lower() == "n":
        ani("  ")
        ani("<You walk along the carpet of the hallway, following the path until you reach a bright yellow door.>")
        ani("<Do you wish to push open the door?>")
        ani("[Your Consciousness urges you to keep going, don't stop]")
        choice4= inani("Y/N?: ")
        if choice4.lower() == "y":
            ani("  ")
            ani("<You push open the door and look around>")
            ani("<You have a sudden pull to the counter>")
            ani("<A knife>")  
            ani("<Do you wish to take the knife?>")
            choice5=inani("Y/N?: ")
            if choice5.lower() == "y":
                ani("  ")
                ani("<You here a new voice along with your Consciousness... >")
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
                ani("||")
            if choice5.lower() == "n":
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
                ani("YOU DIED?! YOU ♓♎︎♓︎□︎⧫︎")
                clear_screen()
            else:
                ani("  ")
                ani("'Whelp... don't know how you failed that'")
                ani("   ")
                clear_screen()
        if choice4.lower() == "n":
            ani("  ")
            ani("'That's not the right choice'")
            ani("[Try to keep moving]")
            ani("  ")
            ani("You died. How about you try again!")
            clear_screen()
        else:
            ani("  ")
            ani("'How'd you fail a simple Y/N?'")
            clear_screen()
    else:
        ani("  ")
        ani("'How'd you fail a simple input?'")
        clear_screen()


if choice1.lower() == "n":
    ani("  ")
    ani("'Are you sure? The consequences for denial... are detrimental.'")
    ani("[Your Consciousness believes you made the wrong choice and to change it while you have the chance]")
    choice2=inani("Y/N? (CAPITAL): ")
    if choice2 == "N":
        ani("  ")
        ani("'You've made the right choice... But you made it too late'")
        ani("You died")
        ani("  ")
        ani("'♌︎♏︎⧫︎⧫︎♏︎❒︎ ■︎□︎⧫︎ ❍︎♋︎🙵♏︎ ⧫︎♒︎♏︎ ⬧︎♋︎❍︎♏︎ ❍︎♓︎⬧︎⧫︎♋︎🙵♏︎'")
        clear_screen()
    if choice2 == "Y":
        ani("  ")
        ani("'I warned you...'")
        ani("[You can't escape ♓︎⧫︎🕯︎⬧︎ ♑︎❒︎♓︎ ︎◻]")
        ani("  ")
        ani("Uh oh! You died! How about you try again?")
        clear_screen()
    if choice2 == "y" or "n":
        ani("  ")
        ani("'I told you to use a capital...'")
        ani("  ")
        ani("'︎♓♎︎♓︎□︎⧫︎'")
        ani("  ")
        ani("[Your Consciousness is dissapointed in yourself]")
        ani("  ")
        ani("ERROR: YOU'VE BEEN KICKED OUT OF THE SYSTEM PLEASE RESTART")
        ani("<Rude>")
        clear_screen()
    else:
        ani("  ")
        ani("'⧫︎♒︎♋︎⧫︎🕯︎⬧︎ ■︎□︎⧫︎ ⧫︎♒︎ ︎♏⬧︎♍︎❒︎♓︎ ︎◻⧫︎...'")
        ani("Your feeling unsettled")
        ani("  ")
        ani("You failed, restart the game to try again") 
        clear_screen()


else:
    ani("  ")
    ani("'⧫︎♒︎♋︎⧫︎🕯︎⬧︎ ■︎□︎⧫︎ ⧫︎♒︎ ︎♏⬧︎♍︎❒︎♓︎ ︎◻⧫︎...'")
    ani("Your feeling unsettled")
    ani("  ")
    ani("You failed, restart the game to try again") 
    clear_screen()