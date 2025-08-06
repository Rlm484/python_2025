print("Welcome to the game consciousness! We hope that you have a wonderful experience!")
name=("What's your name?: ")
print("<But you can't seem to remember>")
print(" ")
print("You wake up to a place unfamiliar but familiar to yourself, the first thing you see? A sign")
print("Welcome, you have one goal destroy all 4 dolls scattered across different rooms!")
print("If you do... you'll get a prize! How about it?")
choice1=input("Y/N? (USE A CAPITAL): ")
if choice1 == "Y":
    print("Very good...")
    print("[Your consciousness feels content with this option]")
if choice1 == "N":
    print("Are you sure? The consequences for denial... are detrimental.")
    print("[Your consciousness believes you made the wrong choice and to change it while you have the chance]")
    choice2=input("Y/N? (USE A CAPITAL): ")
    if choice2 == "Y":
        print("You've made the right choice...")
        print("Your consciousness is happy")
    if choice2 == "N":
        print("I warned you...")
        print("[Your consciousness is fading away]")
        print("  ")
        print("Uh oh! You died! How about you try again? :)")
    else:
        print("That's not the script...")
        print("  ")
        print("You failed, restart the game to try again")
else:
    print("That's not the script")
    print("  ")
    print("You failed, restart the game to try again")
