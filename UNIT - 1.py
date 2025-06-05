#Prac 1 - 

#How to type in a name from the user
myName = input('Enter your name: ')
#3 diff methods to 'print'
print(myName)
#I believe it wil print the name inputed by the user due to the muteable inside the code
print()
#I believe it will print myName due to it having no code. This means it will probably assume that the code above is the code needed
print(f"My name is {myName}")
#I believe it will print due to it using default programming from python and will say My name is ...

#Core Programming Concepts
#1. Sequence - Every program has an order, top to bottom
print(f"Hello {myName}! Welcome to a new journey.")
print('Ready to begin? (type y/n)')

#Use if statements to choose things; branching or conditional logic
answer=input("Y or N: ")
print(answer)
if answer == ("Y") or answer == ("y"):
    print(f"Very well {myName}, let's begin!")
elif answer == ("N") or answer == ("n"):
    print(f"Okay {myName}, i'll see you if you return")
else:
    print("Sorry, that's not a valid answer. Please restart the game...")

#Loops
#lives = 3
#while lives > 3:
#    print("Keep going!")
#for level in range(1,4):
#    print("Level", level)

#29/0/2025
#----------------------------------------------------------------------------------
#Variables store info, e.g. int - numbers, str - text, bool - true or false, list - collection of items
#craft = 3

#servings = False

#Functions let you reuse code
#def sayHi(sx):
#    print("Hi",sx)

#sayHi(f'{myName}')

#Input and Output
#input()
#print()

#Data types
#int
#float - numbers with decimals
#str
#Data types - classifying
#Will determine logical (Checking), mathematical (Calculations), or retationable (Comparing) operations
#does the coudgfsg true
#pizza=input("Pizza amount? - ")
#print(gahdshdghjagd)
#if pizza !="0":
#    servings=True
#    print("T")
#else:
    # do nothing
    
#Data - Raw facts/figures
#Info - processed data
#Knowledge - understanding
#-----------------------------------------------------------------------------------

#Prac 2 - 