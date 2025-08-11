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




print("Welcome to the game Consciousness! We hope that you have a wonderful experience!")
name= input("What's your name?: ")
print("<But you can't seem to remember>")
print(" ")
print("<You wake up to a place unfamiliar but familiar to yourself, the first thing you see? A sign>")
print("'Welcome, you have one goal destroy all 4 dolls scattered across different rooms!'")
print("'If you do... you'll get a prize! How about it?'")
choice1=input("Y/N?: ")


if choice1.lower() == "y":
    print("  ")
    print ("'Very good...'")
    print("[Your Consciousness feels content with this option]")
    print("<As you look around, you see 4 different corridors with labels.>")
    print("'Kitchen - North'")
    print("'Child's room - South'")
    print("'Master Bedroom - East'")
    print("'Garage - West'")
    print("<Where would you like to go?>")
    choice3=input("N/S/W/E (You can only go to the kitchen in the demo): ")
    if choice3.lower() == "n":
        print("<You walk along the carpet of the hallway, following the path until you reach a bright yellow door.>")
        print("<Do you wish to push open the door?>")
        print("[Your Consciousness urges you to keep going, don't stop]")
        choice4= input("Y/N?: ")
        if choice4.lower() == "y":
            print("<You push open the door and look around>")
            print("<You have a sudden pull to the counter>")
            print("<A knife>")  
            print("<Do you wish to take the knife?>")
            choice5=input("Y/N?: ")
            if choice5.lower() == "y":
                print("<You here a new voice along with your Consciousness... >")
                print("|I'm sorry, I thought I could give you everything...|")
                print("   ")
                print("Thank you for completing 'Consciousness' the demo")
                clear_screen()
            if choice5.lower() == "n":
                print("'You might regret this later'")
                print("[Your Consciousness is annoyed]")
                print("   ")
                print("Thank you for completing 'Consciousness' the demo")
                clear_screen()
            else:
                print("'Whelp... don't know how you failed that'")
                print("   ")
                print("Thank you for completing 'Consciousness' the demo")
                clear_screen()
        if choice4.lower() == "n":
            print("'That's not the right choice'")
            print("[Try to keep moving]")
            print("  ")
            print("You died. How about you try again!")
            clear_screen()
        else:
            print("'How'd you fail a simple Y/N?'")
            clear_screen()
    else:
        print("'How'd you fail a simple input?'")
        clear_screen()


if choice1.lower() == "n":
    print("'Are you sure? The consequences for denial... are detrimental.'")
    print("[Your Consciousness believes you made the wrong choice and to change it while you have the chance]")
    choice2=input("Y/N? (CAPITAL): ")
    if choice2 == "N":
        print("'You've made the right choice... But you made it too late'")
        print("You died")
        print("'♌︎♏︎⧫︎⧫︎♏︎❒︎ ■︎□︎⧫︎ ❍︎♋︎🙵♏︎ ⧫︎♒︎♏︎ ⬧︎♋︎❍︎♏︎ ❍︎♓︎⬧︎⧫︎♋︎🙵♏︎'")
        clear_screen()
    if choice2 == "Y":
        print("'I warned you...'")
        print("[You can't escape ♓︎⧫︎🕯︎⬧︎ ♑︎❒︎♓︎ ︎◻]")
        print("  ")
        print("Uh oh! You died! How about you try again?")
        clear_screen()
    if choice2 == "y" or "n":
        print("'I told you to use a capital...'")
        print("'︎♓♎︎♓︎□︎⧫︎'")
        print("[Your Consciousness is dissapointed in yourself]")
        print("ERROR: YOU'VE BEEN KICKED OUT OF THE SYSTEM PLEASE RESTART")
        print("<Rude>")
        clear_screen()
    else:
        print("  ")
        print("'⧫︎♒︎♋︎⧫︎🕯︎⬧︎ ■︎□︎⧫︎ ⧫︎♒︎ ︎♏⬧︎♍︎❒︎♓︎ ︎◻⧫︎...'")
        print("Your feeling unsettled")
        print("  ")
        print("You failed, restart the game to try again") 
        clear_screen()


else:
    print("  ")
    print("'⧫︎♒︎♋︎⧫︎🕯︎⬧︎ ■︎□︎⧫︎ ⧫︎♒︎ ︎♏⬧︎♍︎❒︎♓︎ ︎◻⧫︎...'")
    print("Your feeling unsettled")
    print("  ")
    print("You failed, restart the game to try again") 
    clear_screen()