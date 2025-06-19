Pseudocode
Pseudocode is like english/logic. We use it to express code in a more understandable manner.
Example: "SET score TO 0", which translates to, "score=0"
-Keep it clear and simple
-Use indentation to show structure
-Focus on logic, not syntax
-Comment your thoughts in plain English

Guidelines
1. BEGIN/END: Used to denote the start and end of the pseudocode process.
3. IF/THEN/ELSE/ENDIF: Represents conditional logic.
4. FOR/ENDFOR: Indicates the beginning and end of a loop structure.
5. SET: Assigns a value to a variable.
6. ADD: Typically used to add values or items.
8. PRINT: Outputs information or results.

Variables
Variables are storages. Variables usually equal a number, string or boolean.
E.g:
name=input(My name is:)
score=counter
answer=(True OR False)

VARIABLE CHALLENGE
Task:
START

SET __________________ TO INPUT("Enter your name:")
SET __________________ TO INPUT("Enter your age:")

DISPLAY "Welcome", __________________
DISPLAY "You are", __________________, "years old"

END

Answer:
START

SET name TO INPUT("Enter your name:")
SET age TO INPUT("Enter your age:")

DISPLAY "Welcome", name
DISPLAY "You are", age, "years old"

END

Data Types
Strings: Text (in quotes) E.g. "fur"
Integer: Whole number E.g. 16
FLoat: Number with decimal E.g. 14.6
Boolean: T or F E.g True OR False
List: A bunch of values E.g. ["dog", "cat"]

Task:
SET name TO ___________________________   ← 
SET score TO __________________________   ← 
SET is_logged_in TO ___________________   ← 
SET height TO __________________________  ← 
SET colours TO _________________________  ← 

Answer:
SET name TO string            ← 
SET score TO integer          ← 
SET is_logged_in TO boolean   ← 
SET height TO float           ← 
SET colours TO list           ← 

To print multiple variables: Easier to add commas
e.g.
name = "Bingo"
age = 6
print(name, "is", age, "years old.")

End equivalently makes it so that the line below is inputed into the empty space
print("Hello", end=" ")
print("world!")
# ➜ Hello world!

Operations:
Addition +
Subtraction -
Multiplication *
Division /
Floor division // (division where you leave out the remainder (9//2 = 4)) 
Remainder %
Exponent (powers) **

Assignments:
= (x=5)
+= (x+=1 (adds one to x (x=x+1)))
-= (x-=2)
*= (x*=3)
/= (x/=2)

Comparisons:
== equal to
!= not equal to
> greater than
< less than
>= Greater or equal
<= lesser or equal

e.g.
# String joining
greeting = "Hello" + " " + "World"
print(greeting)  # ➜ Hello World

# String repetition
laugh = "ha" * 3
print(laugh)  # ➜ hahaha