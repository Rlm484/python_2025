#Bluey's Backyard Adventure - Exercise 1:
print("Hello, welcome to Bluey's backyard!")
print(" ")
name = input("What's your name?: ")
print(f"{name}? That's a nice name.")
print(" ")
age = input("How old are you?: ")
print(" ")
snack = input("Well, what snack do you want to bring?: ")
game_length = float(input(f"{snack}? That sounds yum! But how long are we going to play? (in minutes e.g. 15.5 OR 1): "))
print(" ")
water_play = str(input("Do you like water play? (Yes/No): "))
if water_play == "Yes":
    water_play=True
elif water_play == "yes":
    water_play=True
elif water_play == "no":
    water_play=True
else:
    water_play=False
print(" ")
print (f"Hi {name}! You're {age} years old and ready to play in Bluey's backyard. You'll play for {game_length} minute/s and bring your favourite snack, {snack}. Water play? If so you'll need to bring a towel? {water_play}! It looks like we'll be having a great day! ")

#Bluey's Backyard Adventure - Exercise 2:
print(" ")
print("Bluey and her friends are planning a big backyard play day!")
print("Here's the games...")
games_list = ["Keepy Uppy", "Magic Asparagus", "Shadowlands", "Obstacle Course", "Muffin Cone"]
print(games_list)
print(" ")
print("It seems Bluey & Bingo have created a new game! Grannies!")
print("Here's the updated list of games...")
games_list.append ("Grannies")
print(games_list)
print(" ")
print("Bluey & Bingo now want to change 'Magic Asparagus' to 'Magic Wand'...")
games_list[1] = "Magic Wand"
print(games_list)
print(" ")
for game in games_list:
    print("Let's play:", game)
print(" ")


def count_games(games):
    print("Wow! We're plaing", len (games), "games!")

count_games(games_list)

print("We're going to have so much fun")
print(":)")
#print(f"There are {count_games()} games")
#def = define, brackets are just needed, len means length, need another count_games cause it actually runs the function
    
print("hello")