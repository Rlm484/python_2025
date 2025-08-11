#NOT MINE
def start_game():
    print("Welcome to 'Escape the Haunted House'!")
    print("You must navigate through the rooms, solve puzzles, and find the exit.")
    print("Type commands like 'go north', 'take key', or 'answer'.")
    print("Good luck!")
    foyer()

def foyer():
    print("You are in the foyer. There is a creepy staircase going up and a door to the west.")
    choice = input("What do you do? (go up / go west) ")
    if choice == "go up":
        attic()
    elif choice == "go west":
        kitchen()
    else:
        print("Invalid choice. Try again.")
        foyer()

def attic():
    print("The attic is full of cobwebs. You see a key on the floor.")
    choice = input("What do you do? (take key / go down) ")
    if choice == "take key":
        print("You pick up the key. It might be useful later.")
        # Add logic to track the key
        foyer()
    elif choice == "go down":
        foyer()
    else:
        print("Invalid choice. Try again.")
        attic()


def kitchen():
    pass
# Add more rooms...

# Start the game
#start_game()

maxAttempts=3

def checker():
    print("dsaudsh")

while True:
    x=int(input("val"))
    if x==1:
        break
    else:
        x=input("val")

print('left the loop')