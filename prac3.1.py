name = input("What is your name?: ")
health = 100
food = 50
in_cave = True
hours = int(input("How many hours did you wait in the cave? "))

if health < 50 or food < 20:
    print("Warning: You are weak!")

if food < 0:
    print("you died from hunger")

if food < 0:
    print("you died from a heart attack")

health -= hours * 5
food -= hours * 3

print (f"{name}, your health is now {health} and you have {food} pieces of food left")

if hours > 5 and food > 0 and health > 0:
    print("You survived the night in the cave!")
else:
    print("You left too early and got attacked")