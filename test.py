import sys
import time

game_list=['a','b','c']

def count_games(imported_data):
    print("Total games: ", len (imported_data))

count_games(game_list)


def my_function():
  print("Hello from a function")

my_function()

def my_function(doggy):
  print(doggy+ " Refsnes")

def my_function(country): # default if you send nothing
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function("Brazil")

def clearScreen():
  pass


def animate_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

animate_text("Bloom baby bloom")