#Bluey's Backyard Adventure
print("Hello, welcome to Bluey's backyard!")
name = input("What's your name?: ")
print(f"{name}? That's a nice name.")
age = input("How old are you?: ")
snack = input("Well, what snack do you want to bring?: ")
game_length = float(input(f"{snack}? That sounds yum! But how long are we going to play? (in minutes e.g. 15.5 OR 1): "))
water_play = bool(input("Do you like water play? (Yes/No): "))

print (f"Hi {name}! You're {age} years old and ready to play in Bluey's backyard. You'll play for {game_length} minute/s and bring your favourite snack, {snack}. Water play? If so you'll need to bring a towel? {water_play}! It looks like we'll be having a great day! ")
