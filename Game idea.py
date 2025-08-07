print("Welcome to the game consciousness! We hope that you have a wonderful experience!")
name= input("What's your name?: ")
print("<But you can't seem to remember>")
print(" ")
print("You wake up to a place unfamiliar but familiar to yourself, the first thing you see? A sign")
print("'Welcome, you have one goal destroy all 4 dolls scattered across different rooms!'")
print("'If you do... you'll get a prize! How about it?'")
choice1=input("Y/N?: ")
if choice1 == "Y" or "y":
    print("'Very good...'")
    print("[Your consciousness feels content with this option]")
    print("As you look around, you see 4 different corridors with labels.") 
    print("'Kitchen - North'")
    print("'Child's room - South'") 
    print("'Master Bedroom - East'")
    print("'Garage - West'")
    print("Where would you like to go?")
    choice3=input("N/S/W/E (You can only go to the kitchen in the demo): ")
    if choice3 == "N" or "n":
        print("You walk along the carpet of the hallway, following the path until you reach a bright yellow door.")
        print("Do you wish to push open the door?")
        print("<You feel nervous, this place is weird...>")
        print("[Your consciousness urges you to keep going, don't stop]")
        choice4= input("Do you wish to go forward? Y/N: ")
        if choice4 == "y" or "Y":
            print("You push open the door and look around")
            print("You have a sudden pull to the counter")
            print("A knife")   
            print("Do you wish to take the knife?")
            choice5=input("Y/N: ") 
            if choice5 == "Y" or "y":
                print("You here a new voice along with your consciousness...")
                print("|Why can't I do anything right? I'm sorry my child...|")
                print("   ")
                print("Thank you for completing 'consciousness' the demo")
            if choice5 == "N" or "n":
                print("You might regret this later")
                print("[Your consciousness is annoyed]")
                print("   ")
                print("Thank you for completing 'consciousness' the demo")
                
            else:
                print("Whelp... don't know how you failed that")
                print("   ")
                print("Thank you for completing 'consciousness' the demo")
        if choice4 == "N" or "n":
            print("'Thats not the right choice'")
            print("[Try to keep moving]")
            print("  ")
            print("You died. How about you try again!")
        else:
            print("How'd you fail a simple Y/N?")
    else: 
        print("How'd you fail a simple input?")
if choice1 == "N" or "n":
    print("'Are you sure? The consequences for denial... are detrimental.'")
    print("[Your consciousness believes you made the wrong choice and to change it while you have the chance]")
    choice2=input("Y/N? (USE A CAPITAL): ")
    if choice2 == "N":
        print("'You've made the right choice...'")
        print("[Your consciousness is happy]")
    if choice2 == "Y":
        print("'I warned you...'")
        print("[You can't disobey him]")
        print("  ")
        print("Uh oh! You died! How about you try again? :)")
    if choice2 == "y" or "n":
        print("'I told you to use a capital...'")
        print("Idiot")
        print("[Your consciousness is dissapointed in yourself]")
        print("ERROR: YOU'VE BEEN KICKED OUT OF THE SYSTEM PLEASE RESTART")
        print("<Rude... Wait- >")
    else:
        print("'That's not the script...'")
        print("[Your consciousness is unsettled]")
        print("  ")
        print("You failed, restart the game to try again")
else:
    print("'That's not the script'")
    print("[Your consciousness is unsettled]")
    print("  ")
    print("You failed, restart the game to try again")
