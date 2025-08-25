import sys
import os
import time
def clear_screen():
    print('--------------------------------------------------------')
    time.sleep(20)
    # Check the operating system and run the appropriate clear command
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

def ani(text, delay=0.06):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

#def inani(text, delay=0.06):       #scrapped due to bugging issues regarding global code
    #for char in text:
        #sys.stdout.write(char)
        #sys.stdout.flush()
        #time.sleep(delay)
    #input()  # Move to the next line

#def intro():                       #scrapped due to the need of the variable "name" to be useable through all code
    #ani("Welcome to the game Consciousness! We hope that you have a wonderful experience!")
    #name=input("What's your name?: ") 
    #name
    #ani("<But you can't seem to remember>")
    #ani(" ")
    #ani("<You wake up to a place unfamiliar but familiar to yourself>")
    #ani("<The first thing you see? A sign>")
    #ani("'Welcome, you have one goal destroy all 4 dolls scattered across different rooms!'")
    #ani("'If you do... you'll get a prize! How about it?'")
    #choice1()

ani("Welcome to the game Consciousness! We hope that you have a wonderful experience!")
name=input("What's your name?: ") 
ani("<But you can't seem to remember>")
ani(" ")
ani("<You wake up to a place unfamiliar but familiar to yourself>")
ani("<The first thing you see? A sign>")
ani("'Welcome, you have one goal destroy all 4 dolls scattered across different rooms!'")
ani("'If you do... you'll get a prize! How about it?'")

def choice1():
    choice1a = input("Y/N: ")
    
    if choice1a.lower() == 'y':
        ani("  ")
        ani("'Very good...'")
        ani("[You're content with this option]")
        ani("<As you look around, you see 4 different corridors with labels.>")
        ani ("'Kitchen - North'")
        ani("'Child's room - South'")
        ani("'Master Bedroom - East'")
        ani("'Garage - West'")
        ani("[You start to look to each path]")
        choice3()
    elif choice1a.lower() == 'n':
        ani("  ")
        ani("'Are you sure? The consequences for denial... are detrimental.'")
        ani("[You believe you made the wrong choice and feel the desire to change it while you can]")
        choice2()

    else:
        print(choice1)
        ani("  ")
        ani("'⧫︎♒︎♋︎⧫︎🕯︎⬧︎ ■︎□︎⧫︎ ⧫︎♒︎ ︎♏⬧︎♍︎❒︎♓︎ ︎◻⧫︎...'", delay=0.2)
        ani("You’re feeling unsettled")
        ani("  ")
        ani("You failed, restart the game to try again") 
        clear_screen()

def choice2():
    choice2a=input("Y/N? (CAPITAL): ")
    if choice2a == "N":
        ani("  ")
        ani("'You've made the right choice... I'll take you back to where you went wrong'")
        choice1()
    elif choice2a == "Y":
        ani("  ")
        ani("'I warned you...'")
        ani("[You can't escape ♓︎⧫︎🕯︎⬧︎ ♑︎❒︎♓︎ ︎◻]")
        ani("  ")
        ani("Uh oh! You died! How about you try again?")
        clear_screen()
    elif choice2a == "y" or "n":
        ani("  ")
        ani("'I told you to use a capital...'")
        ani("  ")
        ani("'︎♓♎︎♓︎□︎⧫︎'", delay=0.5)
        ani("  ")
        ani("[You're so disappointed in yourself]")
        ani("  ")
        ani("ERROR: YOU'VE BEEN KICKED OUT OF THE SYSTEM PLEASE RESTART")
        ani("<Rude>")
        clear_screen()
    else:
        ani("  ")
        ani("'⧫︎♒︎♋︎⧫︎🕯︎⬧︎ ■︎□︎⧫︎ ⧫︎♒︎ ︎♏⬧︎♍︎❒︎♓︎ ︎◻⧫︎...'", delay=0.2)
        ani("<Your feeling unsettled>")
        ani("  ")
        ani("You failed, restart the game to try again") 
        clear_screen()

def choice3():
    choice3a = input("N/S/W/E 'Kitchen is the tutorial room, go there': ")
    if choice3a.lower() == "n":
        kitchen()
    elif choice3a.lower()== "e" or choice3a.lower() == "w" or choice3a.lower() == "s":
        ani("You need to walk before you run, crawl before you walk")
        ani("Chit Chit player")
        ani(" ")
        choice3()
    else:
        ani(" ")
        ani("'That's not an option'")
        ani("Try again")
        choice3()



#From Kitchen
def kitchen():
    ani("  ")
    ani("<You walk along the black and white tiles of the north hallway, following the path until you reach a bright yellow door.>")
    ani("<Do you wish to push open the door?>")
    ani("[Keep going, don't stop]")
    choice4n()

def choice4n():
    choice4na= input("Y/N?: ")
    if choice4na.lower() == "y":
        ani("  ")
        ani("<You push open the door and look around>")
        ani("<You have a sudden pull to the counter>")
        ani("<A knife>")  
        ani("<Do you wish to take the knife?>")
        choice5n()
    elif choice4na == "n" or "N":
        ani("  ")
        ani("'That's not the right choice'")
        ani("<You note down the mistake in your mind for next time>")
        ani("  ")
        ani("You died. How about you try again!")
        clear_screen()
    else:
        ani("  ")
        ani("'How'd you fail a simple Y/N?'")
        clear_screen()

def choice5n():
    choice5na=input("Y/N?: ")
    if choice5na.lower() == "y":
        ani("  ")
        ani("<You hear a new voice along with your Consciousness... >")
        ani("|I'm sorry, I thought I could give you everything...|")
        ani("   ")
        ani("<You turn around from the counter and realise that there's a doll>")
        ani("<It's just standing>")
        ani("<Waiting>")
        ani("   ")
        ani("[Destroy it]")
        ani("<You don't have a choice>")
        ani("    ")
        ani("|Why are you here?|")
        ani("|...|")
        ani("|I'm so sorry|")
        ani("  ")
        ani("<The doll gives you a riddle...>")
        ani("|What is the most important thing to a chef?|")
        ani("<Your choices: Their Knife (a); Their Skill (b); Their Workspace (c); Their Integrity (d)>")
        choice6n()
    elif choice5na.lower() == "n":
        ani("  ")
        ani("'You might regret this later'")
        ani("[Your feel is annoyed]")
        ani("   ")
        ani("<You turn around from the counter and realise that there's a doll>")
        ani("<It's just standing>")
        ani("<Waiting>")
        ani("   ")
        ani("[Your have the urge you to destroy it]")
        ani("<You don't have a choice>")
        ani("    ")
        ani("<You don't have a weapon...>")
        ani("  ")
        ani("YOU DIED?! YOU ♓♎︎♓︎□︎⧫︎", delay=0.07)
        clear_screen()
    else:
        ani("  ")
        ani("'Whelp... don't know how you failed that'")
        ani("   ")
        clear_screen()

def choice6n():
    choice6na=input("<Your answer>: ")
    if choice6na.lower() == "a":
        ani("  ")
        ani("'You selected the correct answer!'")
        ani("'Now you have one last thing to do'")
        choice7n()
    else:
        ani("'That's not the right answer'")
        ani("You died, try again-")
        clear_screen()

def choice7n():
    choice7na=input("'DO IT' (Y/N): ")
    if choice7na == "y" or "Y":
        ani("|Why?|", delay=0.5)
        ani("  ")
        ani("<But the voice remains...>")
        ani("|I tried my best|")
        ani("  ")
        ani("'You did such a good job'")
        ani("[Keep moving]")
        ani(" ")
        ani("<You shakily walk out the yellow door and out into the room that started everything>")
        directionn()
    else:
        ani("'Do you think you have a choice?'")
        ani("  ")
        choice7n()

def directionn():
    choice8na= input("S/W/E: ")
    if choice8na.lower() == "s":
        ani("  ")
        ani("<Slowly, you walk towards the south hallway until you see the sign>")
        ani("'Only 3 more to go :)'")
        ani("[You feel wonderful]")
        ani("<You feel unnerved>")
        ani("  ")
        childsns()
    elif choice8na.lower() == "e":
        ani("  ")
        ani("<Slowly, you walk towards the east hallway until you see the sign>")
        ani("'Only 3 more to go :)'")
        ani("[You feel wonderful]")
        ani("<You feel unnerved>")
        ani("  ")
        shedne()
    elif choice8na.lower() == "w":
        ani("  ")
        ani("<Slowly, you walk towards the west hallway until you see the sign>")
        ani("'Only 3 more to go :)'")
        ani("[You feel wonderful]")
        ani("<You feel unnerved>")
        ani("  ")
        mastersnw()

#You choose W of the NWES/NWSE
def mastersnw():
    ani("<You walk along the west hallway lined with royal blue carpet, a dark green door awaits you>")
    ani("|My room... our room|", delay=0.2)
    ani("[Be careful]")
    choice17nwa=input("Do you wish to open the door? (Y/N): ")
    if choice17nwa.lower() == "y":
        ani("  ")
        ani("<You open the door, there doesn't seem to be anyone there>")
        ani("[He's in the wardrobe]")
        ani("[He knows what you did to his family]", delay=0.2)
        ani("  ")
        choice18nw()
    else:
        ani("  ")
        ani("'The less you rebel the better'")
        mastersnw()

def choice18nw():
    choice18nwa=input("Do you wish to explore or head to the wardrobe? (Explore/Wardrobe): ")
    if choice18nwa.lower() == "explore":
        ani("<You look around the room and see a drawer>") 
        choice19nw()
    else:
        ani("'You're such a party pooper'")
        ani("  ")
        ani("'⍓︎□︎◆︎ ♎︎♓︎♏︎♎︎'")
        clear_screen() 

def choice19nw():
    choice19nwa=input("Open it? (Y/N): ")
    if choice19nwa.lower() == "y":
        ani("<You open the drawer to see a box, when opened? It's full of daggers>")
        ani("[You already have the knife]")
        ani("  ")
        ani("[There's nothing else to see]")
        ani("  ")
        ani("[You move away from the drawer and head towards the wardrobe]")
        ani("<You move away from the drawer and shakily head to the wardrobe>")
        ani("|They move away from the drawer and ---- head towards the wardrobe|")
        ani(" ")
        ani("-Why did you hurt them?-", delay=0.2)
        ani("  ")
        ani("<The sad doll gives you a puzzle>")
        ani("-What does every parent have/need to do?-")
        ani("<Your choices: Support(a); Nurture(b); Sacrifice(c); Love(d)>")
        ani("  ")
        choice20nw()
    else:
        ani("<Open the box, that's what they want>")
        choice19nw()

def choice20nw():
    choice20nwa=input("<Your answer>: ")
    if choice20nwa.lower() == "c":
        ani("'You selected the correct answer!'")
        ani(" ")
        ani("[You stab him happily]")
        ani("<You stab him regretfully>")
        ani("|They... They stab... They stab him with guilt|", delay=0.2)
        ani("  ")
        ani("[Keep moving]")
        ani("  ")
        ani("<Will this ever end?>", delay=0.2)
        ani("   ")
        directionnw()
    else:
        ani("'Wrong answer!'")
        clear_screen()

def directionnw():
    choice16nwa=input("[Only 2 more to go] (E/S): ")
    if choice16nwa.lower() == "e":
        ani("[Finally! Only two more dolls left till you're done with your mission]")
        ani("<Finally... Only two more doll left till you're done with this hell>")
        ani("  ")
        ani("<You walk back, knowing the sign will say something different>")
        ani("'Your doing such a good job :)'")
        ani("[You feel so happy at the recognition]")
        ani("<...>")
        ani("  ")
        shednwe()
    elif choice16nwa.lower() == "s":
        ani("<As you start heading back you wonder how this all went so wrong>")
        ani("<But you know you can't stop>")
        ani("[We won't let you]")
        ani("<You already knew that>")
        ani("<Even more so as you reach the main room>")
        ani("'You really are a wonderful person, ;)'")
        ani(" ")
        childsnws()
    else:
        ani("'Don't try to escape me'")
        ani("  ")
        directionne()
        ani("[Finally! Only two more dolls left till you're done with your mission]")
        ani("<Finally... Only two more dolls left till you're done with this hell>")
        ani("  ")
        ani("<You walk back, knowing the sign will say something different>")
        ani("'Your doing such a good job :)'")
        ani("[You feel so happy at the recognition]")
        ani("<...>")
        ani("  ")
        directionnw()

#You choose S of the NWS route
def childsnws():
    ani("<You walk along the colourful style of the south hallway, and see a cute pastel blue door at the end>")
    ani("<It makes your heart ache>")
    ani(" ")
    choice9nws()

def choice9nws():
    choice9nwsa=input("Go in? Y/N: ")
    if choice9nwsa.lower() == "y":
        ani("  ")
        ani("[:)]")
        ani("<You push the door slightly and see a broken rattle>")
        ani("[You already have the knife]")
        ani(" ")
        ani("<You push the door and see a sleeping child?>")
        ani("...", delay=0.25)
        ani("<Not a child.>")
        ani("[You happily declare inside your Consciousness that it's another doll! After this? Only 2 more!]")
        ani("|...|")
        ani("   ")
        ani("'Well that's no fun. How about this? You can wait till they wake up!'")
        choice10nws()
    else:
        ani("Don't resist", delay=0.2)
        choice9nws()

def choice10nws():
    choice10nwsa=input("Y/N: ")
    if choice10nwsa.lower() == "y":
        ani("'Great'")
        ani("'But I'll give you some time to explore... they're asleep anyways...'")
        choice11nws()
    else:
        ani("'Why do you keep thinking that you can differ from the path that's laid out?'")
        ani("⍓︎□︎◆︎🕯︎●︎●︎ ■︎♏︎❖︎♏︎❒︎ ♏︎⬧︎♍︎♋︎◻︎♏︎")
        ani(" ")
        ani("You died")
        clear_screen()
    
def choice11nws():
    choice11nwsa=input("Explore? (Y/N): ")
    if choice11nwsa.lower() == "y":
        ani("'Sounds great, tell me when you're done'")
        ani("Where would you like to look?")
        ani("Closet, Bed, Toy shelf")
        closetcodenws()
    else:
        ani("'You're such a party pooper, and I still need to prepare'")
        ani("  ")
        ani("'⍓︎□︎◆︎ ♎︎♓︎♏︎♎︎'")
        clear_screen()

def closetcodenws():
    choice12nwsa=input("Choose...: ")
    if choice12nwsa.lower() == "closet":
        ani("<You walk towards the closet>")
        ani("<Your heart hurts even more>")
        ani("|Do you remember?|", delay=0.2)
        ani("   ")
        closetnes()
    elif choice12nwsa.lower() == "bed" or choice12nwsa.lower() == "toy shelf":
        ani("<You approach, you stare, you reminisce...>")
        ani("<All the times you played, all the times you hung out>")
        ani("<Every time we told those stories...>")
        ani("<I remember>", delay=0.2)
        ani("<I look at the person beyond the screen...>", delay=0.2)
        ani("<Look at the person who shares my name>")
        ani(f"<{name}>", delay=0.2)
        ani("<3684>")
        ani("  ")
        ani("['We can't have that']")
        ani("['♐︎□︎❒︎♑︎♏︎⧫︎']")
        clear_screen()
    else:
        ani("'Not an option'")
        closetcodenws()

def closetnws():
    choice13nwsa=input("Attempt to open it? (Y/N): ")
    if choice13nwsa.lower() == "y":
        ani("<You open the closet and realise it's a door to a secret room>")
        ani("<There's a padlock with 4 digits on it>")
        ani("Do you want to try opening the door? You will only have one shot")
        ani("|...This is the least I can do for you|")
        ani("|3;8|")
        secretroomnws()
    else:
        ani("<Please try again... for me>", delay=0.2)
        ani(" ")
        ani(f"'{name}, you sure are determined...'")
        clear_screen()

def secretroomnws():
    choice14nwsa=input("Open the door? (Type the 4 digit code): ")
    if choice14nwsa == "3684":
        ani("<Your Consciousness falls silent as you walk into your room>")
        ani("<You know that once you leave, you'll die>")
        ani("<He'll find you>")
        ani("<Her voice is gone aswell>")
        ani("<On the table is a diary, the name?>")
        ani(name)
        ani("<There's only one entry intact>")
        ani("Read the entry?")
        mychoice=input("Y/N: ")
        ani("But you're no longer in control", delay=0.15)
        ani("  ")
        ani("<Dear Diary, I finally found a home!>")
        ani("<I have a mum, a dad, and even a little brother! They even have a dog!>")
        ani("<They really like the dog, my parents say it's been with them since the beggining...>")
        ani("<But I finally have a family, a real family>")
        ani("<I hope this happiness never ends>")
        ani("........", delay=1)
        ani("<Complete the game>")
        ani("<Complete Consciousness>")
        ani("<Because once you do?>")
        ani("<I can finally go home>")
        clear_screen()
    else:
        ani("You failed to open the door")
        ani("[Keep moving]")
        ani("  ")
        ani("<You return to the ''childlike'' dolls bed>")
        ani("<Beside the sleeping child is a paper puzzle>")
        ani("   ")
        ani("'They finally woke up, so I guess it's time for me to go, :)'")
        ani("  ")
        ani("~You're here!~")
        ani("~...~")
        ani("~Don't you recognize me? Don't you remember me?... Don't you love me?~", delay=0.23)
        ani("<Your choices: ...;...;...;...;>")
        choice15nws()

def choice15nws():
    choice15nwsa=input("<Your answer>: ")
    ani("~...~")
    ani("'You selected the correct answer!'")
    ani("  ")
    ani("|Don't hurt him... please|")
    ani("<...>")
    ani("[But you had no choice]", delay=0.2)
    ani("  ")
    choice16nws()

def choice16nws():
    ani("<You have to keep moving, no point in stopping now>")
    ani("<You know the consequences of failure>", delay=0.2)
    ani("<You go back to the main room>")
    ani("<You feel hatred towards yourself>")
    ani("[You feel pride towards yourself]")
    ani("<You feel sick towards the sign in the centre of the main room>")
    ani("[You feel adoration towards the sign in the centre of the main room]")
    ani("'Only 1 more to go, ;)'")
    ani("  ")
    shednwse()

#You choose E of the NEWS/NESW route
def shedne():
    ani("<You walk along the wild east hallway, walking till you see a old wooden door>")
    ani("[You can barely hold your excitement due to you getting closer to completing your goal]")
    ani("<But you stop the moment you see the doll through the rotted wood>")
    ani("<...>")
    ani("<It's a dog>")
    ani("|Not him... PLEASE NOT HIM...|")
    ani("  ")
    choice22ne()
    
def choice22ne():
    choice22nea=input("<You know that you'll need to enter anyways...> (Y/N): ")
    if choice22nea.lower() == "y":
        ani("<You feel your stomach sink as you see a dog like doll>")
        ani("[No need to explore, you can already see everything anyways]")
        ani("  ")
        ani("<As you look around you see a screwdriver>")
        ani("[You already have the knife]")
        ani("  ")
        choice23ne()
    else:
        ani("'What a shame'")
        ani("'You were getting there as well'")
        ani("'But i'm not giving you an easy way back'")
        ani("'No'")
        ani("'You can restart if you want to go back...'")
        clear_screen()

def choice23ne():
    choice23nea=input("'Walk towards the dog?' (Y/N): ")
    ani(" ")
    if choice23nea.lower() == "y":
        ani("<You walk towards the dog...>")
        ani("[It's a doll]", delay=0.15)
        ani("<You walk towards the doll>")
        ani("[:)]")
        ani("<As you get closer you look into it's eyes, it seems to recognise you...>")
        ani("*...*")
        ani("<It doesn't speak>")
        ani("<...>")
        ani("<It only whines>")
        ani("[But your consciousness understands it]")
        ani("[*Why is that smell so familiar?*]")
        ani("'Enough talking, give them the puzzle'")
        ani("<You hear it whine...>")
        ani("  ")
        choice24ne()
    else:
        ani("'What a shame'")
        ani("'You were getting there as well'")
        ani("'But i'm not giving you an easy way back'")
        ani("'No'")
        ani("'You can restart if you want to go back...'")
        ani("'Sound familiar?'")
        ani("'Same words as last time'")
        clear_screen()

def choice24ne():
    ani("[*What does every soul have?*]")
    ani("<Your choices: Patience(a); Affection(b); Hatred(c); Determination(d)>")
    ani("  ")
    choice25ne()

def choice25ne():
    choice25nea=input("<Your answer>: ")
    if choice25nea.lower() == "d":
        ani("'You selected the correct answer!'")
        ani(" ")
        ani("<You refuse to use the knife>")
        ani("'Are you really doing this?'")
        ani("<YOU REFUSE TO USE THE KNIFE>")
        ani("'You're going to have to do it eventually...'")
        ani("<I don't want to>")
        ani("'I know'")
        ani(" ")
        ani("[They stab the dog...]")
        ani("[They didn't want to...]")
        ani("'But I worked hard so that you can make it closer to the end :)'")
        ani("|...|")
        ani(" ")
        ani("[Only two more dolls left till you're done with your mission]")
        ani("<Only two more dolls left till you're done with this hell>")
        ani("  ")
        directionne()
        

    else:
        ani("'You were so close!'")
        clear_screen()  

def directionne():
    choice16nea=input("[Only 2 more to go] (W/S): ")
    if choice16nea.lower() == "w":
        ani("<As you start heading back you wonder how this all went so wrong>")
        ani("<But you know you can't stop>")
        ani("[We won't let you]")
        ani("<You already knew that>")
        ani("<Even more so as you reach the main room>")
        ani("'You really are a wonderful person, ;)'")
        ani("  ")
        mastersnew()
    elif choice16nea.lower() == "s":
        ani("<As you start heading back you wonder how this all went so wrong>")
        ani("<But you know you can't stop>")
        ani("[We won't let you]")
        ani("<You already knew that>")
        ani("<Even more so as you reach the main room>")
        ani("'You really are a wonderful person, ;)'")
        ani(" ")
        childsnes()
    else:
        ani("'Don't try to escape me'")
        ani("  ")
        directionne()

#You choose S of the NSWE/NSEW route
def childsns():
    ani("<You walk along the colourful style of the south hallway, and see a cute pastel blue door at the end>")
    ani("<It makes your heart ache>")
    ani(" ")
    choice9ns()

def choice9ns():
    choice9nsa=input("Go in? Y/N: ")
    if choice9nsa.lower() == "y":
        ani("  ")
        ani("[:)]")
        ani("<You push the door slightly and see a broken rattle>")
        ani("[You already have the knife]")
        ani(" ")
        ani("<You push the door and see a sleeping child?>")
        ani("...", delay=0.25)
        ani("<Not a child.>")
        ani("[You happily declare inside your Consciousness that it's another doll! After this? Only 2 more!]")
        ani("|...|")
        ani("   ")
        ani("'Well that's no fun. How about this? You can wait till they wake up!'")
        choice10ns()
    else:
        ani("Don't resist", delay=0.2)
        choice9ns()

def choice10ns():
    choice10nsa=input("Y/N: ")
    if choice10nsa.lower() == "y":
        ani("'Great'")
        ani("'But I'll give you some time to explore... they're asleep anyways...'")
        choice11ns()
    else:
        ani("'Why do you keep thinking that you can differ from the path that's laid out?'")
        ani("⍓︎□︎◆︎🕯︎●︎●︎ ■︎♏︎❖︎♏︎❒︎ ♏︎⬧︎♍︎♋︎◻︎♏︎")
        ani(" ")
        ani("You died")
        clear_screen()
    
def choice11ns():
    choice11nsa=input("Explore? (Y/N): ")
    if choice11nsa.lower() == "y":
        ani("'Sounds great, tell me when you're done'")
        ani("Where would you like to look?")
        ani("Closet, Bed, Toy shelf")
        closetcodens()
    else:
        ani("'You're such a party pooper, and I still need to prepare'")
        ani("  ")
        ani("'⍓︎□︎◆︎ ♎︎♓︎♏︎♎︎'")
        clear_screen()

def closetcodens():
    choice12nsa=input("Choose...: ")
    if choice12nsa.lower() == "closet":
        ani("<You walk towards the closet>")
        ani("<Your heart hurts even more>")
        ani("|Do you remember?|", delay=0.2)
        ani("   ")
        closetns()
    elif choice12nsa.lower() == "bed" or choice12nsa.lower() == "toy shelf":
        ani("<You approach, you stare, you reminisce...>")
        ani("<All the times you played, all the times you hung out>")
        ani("<Every time we told those stories...>")
        ani("<I remember>", delay=0.2)
        ani("<I look at the person beyond the screen...>", delay=0.2)
        ani("<Look at the person who shares my name>")
        ani(f"<{name}>", delay=0.2)
        ani("<3684>")
        ani("  ")
        ani("['We can't have that']")
        ani("['♐︎□︎❒︎♑︎♏︎⧫︎']")
        clear_screen()
    else:
        ani("'Not an option'")
        closetcodens()

def closetns():
    choice13nsa=input("Attempt to open it? (Y/N): ")
    if choice13nsa.lower() == "y":
        ani("<You open the closet and realise it's a door to a secret room>")
        ani("<There's a padlock with 4 digits on it>")
        ani("Do you want to try opening the door? You will only have one shot")
        ani("|...This is the least I can do for you|")
        ani("|3;8|")
        secretroomns()
    else:
        ani("<Please try again... for me>", delay=0.2)
        ani(" ")
        ani(f"'{name}, you sure are determined...'")
        clear_screen()

def secretroomns():
    choice14nsa=input("Open the door? (Type the 4 digit code): ")
    if choice14nsa == "3684":
        ani("<Your Consciousness falls silent as you walk into your room>")
        ani("<You know that once you leave, you'll die>")
        ani("<He'll find you>")
        ani("<Her voice is gone aswell>")
        ani("<On the table is a diary, the name?>")
        ani(name)
        ani("<There's only one entry intact>")
        ani("Read the entry?")
        mychoice=input("Y/N: ")
        ani("But you're no longer in control", delay=0.15)
        ani("  ")
        ani("<Dear Diary, I finally found a home!>")
        ani("<I have a mum, a dad, and even a little brother! They even have a dog!>")
        ani("<They really like the dog, my parents say it's been with them since the beggining...>")
        ani("<But I finally have a family, a real family>")
        ani("<I hope this happiness never ends>")
        ani("........", delay=1)
        ani("<Complete the game>")
        ani("<Complete Consciousness>")
        ani("<Because once you do?>")
        ani("<I can finally go home>")
        clear_screen()
    else:
        ani("You failed to open the door")
        ani("[Keep moving]")
        ani("  ")
        ani("<You return to the ''childlike'' dolls bed>")
        ani("<Beside the sleeping child is a paper puzzle>")
        ani("   ")
        ani("'They finally woke up, so I guess it's time for me to go, :)'")
        ani("  ")
        ani("~You're here!~")
        ani("~...~")
        ani("~Don't you recognize me? Don't you remember me?... Don't you love me?~", delay=0.23)
        ani("<Your choices: ...;...;...;...;>")
        choice15ns()

def choice15ns():
    choice15nsa=input("<Your answer>: ")
    ani("~...~")
    ani("'You selected the correct answer!'")
    ani("  ")
    ani("|Don't hurt him... please|")
    ani("<...>")
    ani("[But you had no choice]", delay=0.2)
    ani("  ")
    directionns()

def directionns():
    choice16nsa=input("[Only 2 more to go] (W/E): ")
    if choice16nsa.lower() == "w":
        ani("<You have to keep moving, no point in stopping now>")
        ani("<You know the consequences of failure>", delay=0.2)
        ani("<You go back to the main room>")
        ani("<You feel hatred towards yourself>")
        ani("[You feel pride towards yourself]")
        ani("<You feel sick towards the sign in the centre of the main room>")
        ani("[You feel adoration towards the sign in the centre of the main room]")
        ani("'Only 2 more to go, ;)'")
        ani("  ")
        mastersnsw()
    elif choice16nsa.lower() == "e":
        ani("<You have to keep moving, no point in stopping now>")
        ani("<You know the consequences of failure>", delay=0.2)
        ani("<You go back to the main room>")
        ani("<You feel hatred towards yourself>")
        ani("[You feel pride towards yourself]")
        ani("<You feel sick towards the sign in the centre of the main room>")
        ani("[You feel adoration towards the sign in the centre of the main room]")
        ani("'Only 2 more to go, ;)'")
        ani("  ")
        shednsew()
    else:
        ani("'Don't try to escape me'")
        ani("  ")
        directionns()

#You choose S of the NESW route
def childsnes():
    ani("<You walk along the colourful style of the south hallway, and see a cute pastel blue door at the end>")
    ani("<It makes your heart ache>")
    ani(" ")
    choice9nes()

def choice9nes():
    choice9nesa=input("Go in? Y/N: ")
    if choice9nesa.lower() == "y":
        ani("  ")
        ani("[:)]")
        ani("<You push the door slightly and see a broken rattle>")
        ani("[You already have the knife]")
        ani(" ")
        ani("<You push the door and see a sleeping child?>")
        ani("...", delay=0.25)
        ani("<Not a child.>")
        ani("[You happily declare inside your Consciousness that it's another doll! After this? Only 2 more!]")
        ani("|...|")
        ani("   ")
        ani("'Well that's no fun. How about this? You can wait till they wake up!'")
        choice10nes()
    else:
        ani("Don't resist", delay=0.2)
        choice9nes()

def choice10nes():
    choice10nesa=input("Y/N: ")
    if choice10nesa.lower() == "y":
        ani("'Great'")
        ani("'But I'll give you some time to explore... they're asleep anyways...'")
        choice11nes()
    else:
        ani("'Why do you keep thinking that you can differ from the path that's laid out?'")
        ani("⍓︎□︎◆︎🕯︎●︎●︎ ■︎♏︎❖︎♏︎❒︎ ♏︎⬧︎♍︎♋︎◻︎♏︎")
        ani(" ")
        ani("You died")
        clear_screen()
    
def choice11nes():
    choice11nesa=input("Explore? (Y/N): ")
    if choice11nesa.lower() == "y":
        ani("'Sounds great, tell me when you're done'")
        ani("Where would you like to look?")
        ani("Closet, Bed, Toy shelf")
        closetcodenes()
    else:
        ani("'You're such a party pooper, and I still need to prepare'")
        ani("  ")
        ani("'⍓︎□︎◆︎ ♎︎♓︎♏︎♎︎'")
        clear_screen()

def closetcodenes():
    choice12nesa=input("Choose...: ")
    if choice12nesa.lower() == "closet":
        ani("<You walk towards the closet>")
        ani("<Your heart hurts even more>")
        ani("|Do you remember?|", delay=0.2)
        ani("   ")
        closetnes()
    elif choice12nesa.lower() == "bed" or choice12nesa.lower() == "toy shelf":
        ani("<You approach, you stare, you reminisce...>")
        ani("<All the times you played, all the times you hung out>")
        ani("<Every time we told those stories...>")
        ani("<I remember>", delay=0.2)
        ani("<I look at the person beyond the screen...>", delay=0.2)
        ani("<Look at the person who shares my name>")
        ani(f"<{name}>", delay=0.2)
        ani("<3684>")
        ani("  ")
        ani("['We can't have that']")
        ani("['♐︎□︎❒︎♑︎♏︎⧫︎']")
        clear_screen()
    else:
        ani("'Not an option'")
        closetcodenes()

def closetnes():
    choice13nesa=input("Attempt to open it? (Y/N): ")
    if choice13nesa.lower() == "y":
        ani("<You open the closet and realise it's a door to a secret room>")
        ani("<There's a padlock with 4 digits on it>")
        ani("Do you want to try opening the door? You will only have one shot")
        ani("|...This is the least I can do for you|")
        ani("|3;8|")
        secretroomnes()
    else:
        ani("<Please try again... for me>", delay=0.2)
        ani(" ")
        ani(f"'{name}, you sure are determined...'")
        clear_screen()

def secretroomnes():
    choice14nesa=input("Open the door? (Type the 4 digit code): ")
    if choice14nesa == "3684":
        ani("<Your Consciousness falls silent as you walk into your room>")
        ani("<You know that once you leave, you'll die>")
        ani("<He'll find you>")
        ani("<Her voice is gone aswell>")
        ani("<On the table is a diary, the name?>")
        ani(name)
        ani("<There's only one entry intact>")
        ani("Read the entry?")
        mychoice=input("Y/N: ")
        ani("But you're no longer in control", delay=0.15)
        ani("  ")
        ani("<Dear Diary, I finally found a home!>")
        ani("<I have a mum, a dad, and even a little brother! They even have a dog!>")
        ani("<They really like the dog, my parents say it's been with them since the beggining...>")
        ani("<But I finally have a family, a real family>")
        ani("<I hope this happiness never ends>")
        ani("........", delay=1)
        ani("<Complete the game>")
        ani("<Complete Consciousness>")
        ani("<Because once you do?>")
        ani("<I can finally go home>")
        clear_screen()
    else:
        ani("You failed to open the door")
        ani("[Keep moving]")
        ani("  ")
        ani("<You return to the ''childlike'' dolls bed>")
        ani("<Beside the sleeping child is a paper puzzle>")
        ani("   ")
        ani("'They finally woke up, so I guess it's time for me to go, :)'")
        ani("  ")
        ani("~You're here!~")
        ani("~...~")
        ani("~Don't you recognize me? Don't you remember me?... Don't you love me?~", delay=0.23)
        ani("<Your choices: ...;...;...;...;>")
        choice15nes()

def choice15nes():
    choice15nsa=input("<Your answer>: ")
    ani("~...~")
    ani("'You selected the correct answer!'")
    ani("  ")
    ani("|Don't hurt him... please|")
    ani("<...>")
    ani("[But you had no choice]", delay=0.2)
    ani("  ")
    choice16nes()

def choice16nes():
    ani("<You have to keep moving, no point in stopping now>")
    ani("<You know the consequences of failure>", delay=0.2)
    ani("<You go back to the main room>")
    ani("<You feel hatred towards yourself>")
    ani("[You feel pride towards yourself]")
    ani("<You feel sick towards the sign in the centre of the main room>")
    ani("[You feel adoration towards the sign in the centre of the main room]")
    ani("'Only 1 more to go, ;)'")
    ani("  ")
    mastersnesw()

#You choose W of the NEWS route
def mastersnew():
    ani("<You walk along the west hallway lined with royal blue carpet, a dark green door awaits you>")
    ani("|My room... our room|", delay=0.2)
    ani("[Be careful]")
    choice17newa=input("Do you wish to open the door? (Y/N): ")
    if choice17newa.lower() == "y":
        ani("  ")
        ani("<You open the door, there doesn't seem to be anyone there>")
        ani("[He's in the wardrobe]")
        ani("[He knows what you did to his family]", delay=0.2)
        ani("  ")
        choice18new()
    else:
        ani("  ")
        ani("'The less you rebel the better'")
        mastersnew()

def choice18new():
    choice18newa=input("Do you wish to explore or head to the wardrobe? (Explore/Wardrobe): ")
    if choice18newa.lower() == "explore":
        ani("<You look around the room and see a drawer>") 
        choice19new()
    else:
        ani("'You're such a party pooper'")
        ani("  ")
        ani("'⍓︎□︎◆︎ ♎︎♓︎♏︎♎︎'")
        clear_screen() 

def choice19new():
    choice19newa=input("Open it? (Y/N): ")
    if choice19newa.lower() == "y":
        ani("<You open the drawer to see a box, when opened? It's full of daggers>")
        ani("[You already have the knife]")
        ani("  ")
        ani("[There's nothing else to see]")
        ani("  ")
        ani("[You move away from the drawer and head towards the wardrobe]")
        ani("<You move away from the drawer and shakily head to the wardrobe>")
        ani("|They move away from the drawer and ---- head towards the wardrobe|")
        ani(" ")
        ani("-Why did you hurt them?-", delay=0.2)
        ani("  ")
        ani("<The sad doll gives you a puzzle>")
        ani("-What does every parent have/need to do?-")
        ani("<Your choices: Support(a); Nurture(b); Sacrifice(c); Love(d)>")
        ani("  ")
        choice20new()
    else:
        ani("<Open the box, that's what they want>")
        choice19new()

def choice20new():
    choice20newa=input("<Your answer>: ")
    if choice20newa.lower() == "c":
        ani("'You selected the correct answer!'")
        ani(" ")
        ani("[You stab him happily]")
        ani("<You stab him regretfully>")
        ani("|They... They stab... They stab him with guilt|", delay=0.2)
        ani("  ")
        ani("[Keep moving]")
        ani("  ")
        ani("<Will this ever end?>", delay=0.2)
        ani("   ")
        choice21new()
    else:
        ani("'Wrong answer!'")
        clear_screen()

def choice21new():
    ani("[Finally! Only one more doll left till you're done with your mission]")
    ani("<Finally... Only one more doll left till you're done with this hell>")
    ani("  ")
    ani("<You walk back, knowing the sign will say something different>")
    ani("'Your doing such a good job :)'")
    ani("[You feel so happy at the recognition]")
    ani("<...>")
    ani("  ")
    childsnews()

#You choose W of the NSWE route
def mastersnsw():
    ani("<You walk along the west hallway lined with royal blue carpet, a dark green door awaits you>")
    ani("|My room... our room|", delay=0.2)
    ani("[Be careful]")
    choice17nswa=input("Do you wish to open the door? (Y/N): ")
    if choice17nswa.lower() == "y":
        ani("  ")
        ani("<You open the door, there doesn't seem to be anyone there>")
        ani("[He's in the wardrobe]")
        ani("[He knows what you did to his family]", delay=0.2)
        ani("  ")
        choice18nsw()
    else:
        ani("  ")
        ani("'The less you rebel the better'")
        mastersnsw()

def choice18nsw():
    choice18nswa=input("Do you wish to explore or head to the wardrobe? (Explore/Wardrobe): ")
    if choice18nswa.lower() == "explore":
        ani("<You look around the room and see a drawer>") 
        choice19nsw()
    else:
        ani("'You're such a party pooper'")
        ani("  ")
        ani("'⍓︎□︎◆︎ ♎︎♓︎♏︎♎︎'")
        clear_screen() 

def choice19nsw():
    choice19nswa=input("Open it? (Y/N): ")
    if choice19nswa.lower() == "y":
        ani("<You open the drawer to see a box, when opened? It's full of daggers>")
        ani("[You already have the knife]")
        ani("  ")
        ani("[There's nothing else to see]")
        ani("  ")
        ani("[You move away from the drawer and head towards the wardrobe]")
        ani("<You move away from the drawer and shakily head to the wardrobe>")
        ani("|They move away from the drawer and ---- head towards the wardrobe|")
        ani(" ")
        ani("-Why did you hurt them?-", delay=0.2)
        ani("  ")
        ani("<The sad doll gives you a puzzle>")
        ani("-What does every parent have/need to do?-")
        ani("<Your choices: Support(a); Nurture(b); Sacrifice(c); Love(d)>")
        ani("  ")
        choice20nsw()
    else:
        ani("<Open the box, that's what they want>")
        choice19nsw()

def choice20nsw():
    choice20nswa=input("<Your answer>: ")
    if choice20nswa.lower() == "c":
        ani("'You selected the correct answer!'")
        ani(" ")
        ani("[You stab him happily]")
        ani("<You stab him regretfully>")
        ani("|They... They stab... They stab him with guilt|", delay=0.2)
        ani("  ")
        ani("[Keep moving]")
        ani("  ")
        ani("<Will this ever end?>", delay=0.2)
        ani("   ")
        choice21nsw()
    else:
        ani("'Wrong answer!'")
        clear_screen()

def choice21nsw():
    ani("[Finally! Only one more doll left till you're done with your mission]")
    ani("<Finally... Only one more doll left till you're done with this hell>")
    ani("  ")
    ani("<You walk back, knowing the sign will say something different>")
    ani("'Your doing such a good job :)'")
    ani("[You feel so happy at the recognition]")
    ani("<...>")
    ani("  ")
    shednswe()

#You choose E of the NWES route
def shednwe():
    ani("<You walk along the wild east hallway, walking till you see a old wooden door>")
    ani("[You can barely hold your excitement due to you getting closer to completing your goal]")
    ani("<But you stop the moment you see the doll through the rotted wood>")
    ani("<...>")
    ani("<It's a dog>")
    ani("|Not him... PLEASE NOT HIM...|")
    ani("  ")
    choice22nwe()
    
def choice22nwe():
    choice22nwea=input("<You know that you'll need to enter anyways...> (Y/N): ")
    if choice22nwea.lower() == "y":
        ani("<You feel your stomach sink as you see a dog like doll>")
        ani("[No need to explore, you can already see everything anyways]")
        ani("  ")
        ani("<As you look around you see a screwdriver>")
        ani("[You already have the knife]")
        ani("  ")
        choice23nwe()
    else:
        ani("'What a shame'")
        ani("'You were getting there as well'")
        ani("'But i'm not giving you an easy way back'")
        ani("'No'")
        ani("'You can restart if you want to go back...'")
        clear_screen()

def choice23nwe():
    choice23nwea=input("'Walk towards the dog?' (Y/N): ")
    ani(" ")
    if choice23nwea.lower() == "y":
        ani("<You walk towards the dog...>")
        ani("[It's a doll]", delay=0.15)
        ani("<You walk towards the doll>")
        ani("[:)]")
        ani("<As you get closer you look into it's eyes, it seems to recognise you...>")
        ani("*...*")
        ani("<It doesn't speak>")
        ani("<...>")
        ani("<It only whines>")
        ani("[But your consciousness understands it]")
        ani("[*Why is that smell so familiar?*]")
        ani("'Enough talking, give them the puzzle'")
        ani("<You hear it whine...>")
        ani("  ")
        choice24nwe()
    else:
        ani("'What a shame'")
        ani("'You were getting there as well'")
        ani("'But i'm not giving you an easy way back'")
        ani("'No'")
        ani("'You can restart if you want to go back...'")
        ani("'Sound familiar?'")
        ani("'Same words as last time'")
        clear_screen()

def choice24nwe():
    ani("[*What does every soul have?*]")
    ani("<Your choices: Patience(a); Affection(b); Hatred(c); Determination(d)>")
    ani("  ")
    choice25nwe()

def choice25nwe():
    choice25nwea=input("<Your answer>: ")
    if choice25nwea.lower() == "d":
        ani("'You selected the correct answer!'")
        ani(" ")
        ani("<You refuse to use the knife>")
        ani("'Are you really doing this?'")
        ani("<YOU REFUSE TO USE THE KNIFE>")
        ani("'You're going to have to do it eventually...'")
        ani("<I don't want to>")
        ani("'I know'")
        ani(" ")
        ani("[They stab the dog...]")
        ani("[They didn't want to...]")
        ani("'But I worked hard so that you can make it closer to the end :)'")
        ani("|...|")
        ani(" ")
        ani("<As you start heading back you wonder how this all went so wrong>")
        ani("<But you know you can't stop>")
        ani("[We won't let you]")
        ani("<You already knew that>")
        ani("<Even more so as you reach the main room>")
        ani("'You really are a wonderful person, only one more to go, ;)'")
        childsnwes()

    else:
        ani("'You were so close!'")
        clear_screen()  

#You choose E of the NSEW route
def shednsew():
    ani("<You walk along the wild east hallway, walking till you see a old wooden door>")
    ani("[You can barely hold your excitement due to you getting closer to completing your goal]")
    ani("<But you stop the moment you see the doll through the rotted wood>")
    ani("<...>")
    ani("<It's a dog>")
    ani("|Not him... PLEASE NOT HIM...|")
    ani("  ")
    choice22nsew()
    
def choice22nsew():
    choice22nsewa=input("<You know that you'll need to enter anyways...> (Y/N): ")
    if choice22nsewa.lower() == "y":
        ani("<You feel your stomach sink as you see a dog like doll>")
        ani("[No need to explore, you can already see everything anyways]")
        ani("  ")
        ani("<As you look around you see a screwdriver>")
        ani("[You already have the knife]")
        ani("  ")
        choice23nsew()
    else:
        ani("'What a shame'")
        ani("'You were getting there as well'")
        ani("'But i'm not giving you an easy way back'")
        ani("'No'")
        ani("'You can restart if you want to go back...'")
        clear_screen()

def choice23nsew():
    choice23nsewa=input("'Walk towards the dog?' (Y/N): ")
    ani(" ")
    if choice23nsewa.lower() == "y":
        ani("<You walk towards the dog...>")
        ani("[It's a doll]", delay=0.15)
        ani("<You walk towards the doll>")
        ani("[:)]")
        ani("<As you get closer you look into it's eyes, it seems to recognise you...>")
        ani("*...*")
        ani("<It doesn't speak>")
        ani("<...>")
        ani("<It only whines>")
        ani("[But your consciousness understands it]")
        ani("[*Why is that smell so familiar?*]")
        ani("'Enough talking, give them the puzzle'")
        ani("<You hear it whine...>")
        ani("  ")
        choice24nsew()
    else:
        ani("'What a shame'")
        ani("'You were getting there as well'")
        ani("'But i'm not giving you an easy way back'")
        ani("'No'")
        ani("'You can restart if you want to go back...'")
        ani("'Sound familiar?'")
        ani("'Same words as last time'")
        clear_screen()

def choice24nsew():
    ani("[*What does every soul have?*]")
    ani("<Your choices: Patience(a); Affection(b); Hatred(c); Determination(d)>")
    ani("  ")
    choice25nsew()

def choice25nsew():
    choice25nsewa=input("<Your answer>: ")
    if choice25nsewa.lower() == "d":
        ani("'You selected the correct answer!'")
        ani(" ")
        ani("<You refuse to use the knife>")
        ani("'Are you really doing this?'")
        ani("<YOU REFUSE TO USE THE KNIFE>")
        ani("'You're going to have to do it eventually...'")
        ani("<I don't want to>")
        ani("'I know'")
        ani(" ")
        ani("[They stab the dog...]")
        ani("[They didn't want to...]")
        ani("'But I worked hard so that you can make it closer to the end :)'")
        ani("|...|")
        ani(" ")
        ani("<As you start heading back you wonder how this all went so wrong>")
        ani("<But you know you can't stop>")
        ani("[We won't let you]")
        ani("<You already knew that>")
        ani("<Even more so as you reach the main room>")
        ani("'You really are a wonderful person, only one more to go, ;)'")
        mastersnsew()

    else:
        ani("'You were so close!'")
        clear_screen()  
        
#Final room E of the NSWE route
def shednswe():
    ani("<You walk along the wild east hallway, walking till you see a old wooden door>")
    ani("[You can barely hold your excitement due to you getting closer to completing your goal]")
    ani("<But you stop the moment you see the doll through the rotted wood>")
    ani("<...>")
    ani("<It's a dog>")
    ani("|Not him... PLEASE NOT HIM...|")
    ani("  ")
    choice22nswe()
    
def choice22nswe():
    choice22nswea=input("<You know that you'll need to enter anyways...> (Y/N): ")
    if choice22nswea.lower() == "y":
        ani("<You feel your stomach sink as you see a dog like doll>")
        ani("[No need to explore, you can already see everything anyways]")
        ani("  ")
        ani("<As you look around you see a screwdriver>")
        ani("[You already have the knife]")
        ani("  ")
        choice23nswe()
    else:
        ani("'What a shame'")
        ani("'You were so close as well'")
        ani("'But i'm not giving you an easy way back'")
        ani("'No'")
        ani("'You can restart if you want to go back...'")
        clear_screen()

def choice23nswe():
    choice23nswea=input("'Walk towards the dog?' (Y/N): ")
    ani(" ")
    if choice23nswea.lower() == "y":
        ani("<You walk towards the dog...>")
        ani("[It's a doll]", delay=0.15)
        ani("<You walk towards the doll>")
        ani("[:)]")
        ani("<As you get closer you look into it's eyes, it seems to recognise you...>")
        ani("*...*")
        ani("<It doesn't speak>")
        ani("<...>")
        ani("<It only whines>")
        ani("[But your consciousness understands it]")
        ani("[*Why is that smell so familiar?*]")
        ani("'Enough talking, give them the puzzle'")
        ani("<You hear it whine...>")
        ani("  ")
        choice24nswe()
    else:
        ani("'What a shame'")
        ani("'You were so close as well'")
        ani("'But i'm not giving you an easy way back'")
        ani("'No'")
        ani("'You can restart if you want to go back...'")
        ani("'Sound familiar?'")
        ani("'Same words as last time'")
        clear_screen()

def choice24nswe():
    ani("[*What does every soul have?*]")
    ani("<Your choices: Patience(a); Affection(b); Hatred(c); Determination(d)>")
    ani("  ")
    choice25nswe()

def choice25nswe():
    choice25nswea=input("<Your answer>: ")
    if choice25nswea.lower() == "d":
        ani("'You selected the correct answer!'")
        ani(" ")
        ani("<You refuse to use the knife>")
        ani("'Are you really doing this?'")
        ani("<YOU REFUSE TO USE THE KNIFE>")
        ani("'You're going to have to do it eventually...'")
        ani("<I don't want to>")
        ani("'I know'")
        ani(" ")
        ani("[They stab the dog...]")
        ani("[They didn't want to...]")
        ani("'But I worked hard so that you can make it closer to the end :)'")
        ani("|...|")
        ani(" ")
        ani("<As you start heading back you wonder how this all went so wrong>")
        ani("<But you know you can't stop>")
        ani("[We won't let you]")
        ani("<You already knew that>")
        ani("<Even more so as you get closer to the main room...>")
        ani(" ")
        the_end

    else:
        ani("'You were so close!'")
        clear_screen()

#Final room W of the NSEW route
def mastersnsew():
    ani("<You walk along the west hallway lined with royal blue carpet, a dark green door awaits you>")
    ani("|My room... our room|", delay=0.2)
    ani("[Be careful]")
    choice17nsewa=input("Do you wish to open the door? (Y/N): ")
    if choice17nsewa.lower() == "y":
        ani("  ")
        ani("<You open the door, there doesn't seem to be anyone there>")
        ani("[He's in the wardrobe]")
        ani("[He knows what you did to his family]", delay=0.2)
        ani("  ")
        choice18nsew()
    else:
        ani("  ")
        ani("'The less you rebel the better'")
        mastersnsew()

def choice18nsew():
    choice18nsewa=input("Do you wish to explore or head to the wardrobe? (Explore/Wardrobe): ")
    if choice18nsewa.lower() == "explore":
        ani("<You look around the room and see a drawer>") 
        choice19nsew()
    else:
        ani("'You're such a party pooper'")
        ani("  ")
        ani("'⍓︎□︎◆︎ ♎︎♓︎♏︎♎︎'")
        clear_screen() 

def choice19nsew():
    choice19nsewa=input("Open it? (Y/N): ")
    if choice19nsewa.lower() == "y":
        ani("<You open the drawer to see a box, when opened? It's full of daggers>")
        ani("[You already have the knife]")
        ani("  ")
        ani("[There's nothing else to see]")
        ani("  ")
        ani("[You move away from the drawer and head towards the wardrobe]")
        ani("<You move away from the drawer and shakily head to the wardrobe>")
        ani("|They move away from the drawer and ---- head towards the wardrobe|")
        ani(" ")
        ani("-Why did you hurt them?-", delay=0.2)
        ani("  ")
        ani("<The sad doll gives you a puzzle>")
        ani("-What does every parent have/need to do?-")
        ani("<Your choices: Support(a); Nurture(b); Sacrifice(c); Love(d)>")
        ani("  ")
        choice20nsew()
    else:
        ani("<Open the box, that's what they want>")
        choice19nsew()

def choice20nsew():
    choice20nsewa=input("<Your answer>: ")
    if choice20nsewa.lower() == "c":
        ani("'You selected the correct answer!'")
        ani(" ")
        ani("[You stab him happily]")
        ani("<You stab him regretfully>")
        ani("|They... They stab... They stab him with guilt|", delay=0.2)
        ani("  ")
        ani("[Finally done!]")
        ani("  ")
        ani("<Will this ever truly end? Even after the job is done?>", delay=0.2)
        ani("   ")
        choice21nsew()
    else:
        ani("'Wrong answer!'")
        clear_screen()

def choice21nsew():
    ani("[Finally! You're done with your mission]")
    ani("<Finally... you're done with this hell>")
    ani("  ")
    ani("<You look ahead, knowing the sign will be gone>")
    ani("'You've done such a good job :)'")
    ani("[You feel so happy at the recognition]")
    ani("<...>")
    ani("  ")
    the_end()

#Final room W of the NESW route
def mastersnesw():
    ani("<You walk along the west hallway lined with royal blue carpet, a dark green door awaits you>")
    ani("|My room... our room|", delay=0.2)
    ani("[Be careful]")
    choice17nsewa=input("Do you wish to open the door? (Y/N): ")
    if choice17nsewa.lower() == "y":
        ani("  ")
        ani("<You open the door, there doesn't seem to be anyone there>")
        ani("[He's in the wardrobe]")
        ani("[He knows what you did to his family]", delay=0.2)
        ani("  ")
        choice18nsew()
    else:
        ani("  ")
        ani("'The less you rebel the better'")
        mastersnsew()

def choice18nesw():
    choice18nsewa=input("Do you wish to explore or head to the wardrobe? (Explore/Wardrobe): ")
    if choice18nsewa.lower() == "explore":
        ani("<You look around the room and see a drawer>") 
        choice19nesw()
    else:
        ani("'You're such a party pooper'")
        ani("  ")
        ani("'⍓︎□︎◆︎ ♎︎♓︎♏︎♎︎'")
        clear_screen() 

def choice19nesw():
    choice19neswa=input("Open it? (Y/N): ")
    if choice19neswa.lower() == "y":
        ani("<You open the drawer to see a box, when opened? It's full of daggers>")
        ani("[You already have the knife]")
        ani("  ")
        ani("[There's nothing else to see]")
        ani("  ")
        ani("[You move away from the drawer and head towards the wardrobe]")
        ani("<You move away from the drawer and shakily head to the wardrobe>")
        ani("|They move away from the drawer and ---- head towards the wardrobe|")
        ani(" ")
        ani("-Why did you hurt them?-", delay=0.2)
        ani("  ")
        ani("<The sad doll gives you a puzzle>")
        ani("-What does every parent have/need to do?-")
        ani("<Your choices: Support(a); Nurture(b); Sacrifice(c); Love(d)>")
        ani("  ")
        choice20nesw()
    else:
        ani("<Open the box, that's what they want>")
        choice19nesw()

def choice20nesw():
    choice20neswa=input("<Your answer>: ")
    if choice20neswa.lower() == "c":
        ani("'You selected the correct answer!'")
        ani(" ")
        ani("[You stab him happily]")
        ani("<You stab him regretfully>")
        ani("|They... They stab... They stab him with guilt|", delay=0.2)
        ani("  ")
        ani("[Finally done!]")
        ani("  ")
        ani("<Will this ever truly end? Even after the job is done?>", delay=0.2)
        ani("   ")
        choice21nesw()
    else:
        ani("'Wrong answer!'")
        clear_screen()

def choice21nesw():
    ani("[Finally! You're done with your mission]")
    ani("<Finally... you're done with this hell>")
    ani("  ")
    ani("<You look ahead, knowing the sign will be gone>")
    ani("'You've done such a good job :)'")
    ani("[You feel so happy at the recognition]")
    ani("<...>")
    ani("  ")
    the_end()

#Final room S of the NEWS route
def childsnews():
    ani("<You walk along the colourful style of the south hallway, and see a cute pastel blue door at the end>")
    ani("<It makes your heart ache>")
    ani(" ")
    choice9ns()

def choice9news():
    choice9newsa=input("Go in? Y/N: ")
    if choice9newsa.lower() == "y":
        ani("  ")
        ani("[:)]")
        ani("<You push the door slightly and see a broken rattle>")
        ani("[You already have the knife]")
        ani(" ")
        ani("<You push the door and see a sleeping child?>")
        ani("...", delay=0.25)
        ani("<Not a child.>")
        ani("[You happily declare inside your Consciousness that it's another doll! After this? Only 2 more!]")
        ani("|...|")
        ani("   ")
        ani("'Well that's no fun. How about this? You can wait till they wake up!'")
        choice10news()
    else:
        ani("Don't resist", delay=0.2)
        choice9news()

def choice10news():
    choice10newsa=input("Y/N: ")
    if choice10newsa.lower() == "y":
        ani("'Great'")
        ani("'But I'll give you some time to explore... they're asleep anyways...'")
        choice11news()
    else:
        ani("'Why do you keep thinking that you can differ from the path that's laid out?'")
        ani("⍓︎□︎◆︎🕯︎●︎●︎ ■︎♏︎❖︎♏︎❒︎ ♏︎⬧︎♍︎♋︎◻︎♏︎")
        ani(" ")
        ani("You died")
        clear_screen()
    
def choice11news():
    choice11newsa=input("Explore? (Y/N): ")
    if choice11newsa.lower() == "y":
        ani("'Sounds great, tell me when you're done'")
        ani("Where would you like to look?")
        ani("Closet, Bed, Toy shelf")
        closetcodenews()
    else:
        ani("'You're such a party pooper, and I still need to prepare'")
        ani("  ")
        ani("'⍓︎□︎◆︎ ♎︎♓︎♏︎♎︎'")
        clear_screen()

def closetcodenews():
    choice12newsa=input("Choose...: ")
    if choice12newsa.lower() == "closet":
        ani("<You walk towards the closet>")
        ani("<Your heart hurts even more>")
        ani("|Do you remember?|", delay=0.2)
        ani("   ")
        closetnews()
    elif choice12newsa.lower() == "bed" or choice12newsa.lower() == "toy shelf":
        ani("<You approach, you stare, you reminisce...>")
        ani("<All the times you played, all the times you hung out>")
        ani("<Every time we told those stories...>")
        ani("<I remember>", delay=0.2)
        ani("<I look at the person beyond the screen...>", delay=0.2)
        ani("<Look at the person who shares my name>")
        ani(f"<{name}>", delay=0.2)
        ani("<3684>")
        ani("  ")
        ani("['We can't have that']")
        ani("['♐︎□︎❒︎♑︎♏︎⧫︎']")
        clear_screen()
    else:
        ani("'Not an option'")
        closetcodens()

def closetnews():
    choice13newsa=input("Attempt to open it? (Y/N): ")
    if choice13newsa.lower() == "y":
        ani("<You open the closet and realise it's a door to a secret room>")
        ani("<There's a padlock with 4 digits on it>")
        ani("Do you want to try opening the door? You will only have one shot")
        ani("|...This is the least I can do for you|")
        ani("|3;8|")
        secretroomnews()
    else:
        ani("<Please try again... for me>", delay=0.2)
        ani(" ")
        ani(f"'{name}, you sure are determined...'")
        clear_screen()

def secretroomnews():
    choice14newsa=input("Open the door? (Type the 4 digit code): ")
    if choice14newsa == "3684":
        ani("<Your Consciousness falls silent as you walk into your room>")
        ani("<You know that once you leave, you'll die>")
        ani("<He'll find you>")
        ani("<Her voice is gone aswell>")
        ani("<On the table is a diary, the name?>")
        ani(name)
        ani("<There's only one entry intact>")
        ani("Read the entry?")
        mychoice=input("Y/N: ")
        ani("But you're no longer in control", delay=0.15)
        ani("  ")
        ani("<Dear Diary, I finally found a home!>")
        ani("<I have a mum, a dad, and even a little brother! They even have a dog!>")
        ani("<They really like the dog, my parents say it's been with them since the beggining...>")
        ani("<But I finally have a family, a real family>")
        ani("<I hope this happiness never ends>")
        ani("........", delay=1)
        ani("<Complete the game>")
        ani("<Complete Consciousness>")
        ani("<Because once you do?>")
        ani("<I can finally go home>")
        clear_screen()
    else:
        ani("You failed to open the door")
        ani("[Keep moving]")
        ani("  ")
        ani("<You return to the ''childlike'' dolls bed>")
        ani("<Beside the sleeping child is a paper puzzle>")
        ani("   ")
        ani("'They finally woke up, so I guess it's time for me to go, :)'")
        ani("  ")
        ani("~You're here!~")
        ani("~...~")
        ani("~Don't you recognize me? Don't you remember me?... Don't you love me?~", delay=0.23)
        ani("<Your choices: ...;...;...;...;>")
        choice15news()

def choice15news():
    choice15newsa=input("<Your answer>: ")
    ani("~...~")
    ani("'You selected the correct answer!'")
    ani("  ")
    ani("|Don't hurt him... please|")
    ani("<...>")
    ani("[But you had no choice]", delay=0.2)
    ani("  ")
    choice16news()

def choice16news():
    ani("<You have to keep moving, no point in stopping now>")
    ani("<You know the consequences of failure>", delay=0.2)
    ani("<You start heading back to the main room>")
    ani("<You feel hatred towards yourself>")
    ani("[You feel pride towards yourself]")
    ani("<You feel sick towards the sign that lies in the main room>")
    ani("[You feel adoration towards the sign that lies in the main room]")
    ani("  ")
    the_end()
        
#Final room S of the NWES
def childsnwes():
    ani("<You walk along the colourful style of the south hallway, and see a cute pastel blue door at the end>")
    ani("<It makes your heart ache>")
    ani(" ")
    choice9nwes()
    
def choice9nwes():
    choice9nwesa=input("Go in? Y/N: ")
    if choice9nwesa.lower() == "y":
        ani("  ")
        ani("[:)]")
        ani("<You push the door slightly and see a broken rattle>")
        ani("[You already have the knife]")
        ani(" ")
        ani("<You push the door and see a sleeping child?>")
        ani("...", delay=0.25)
        ani("<Not a child.>")
        ani("[You happily declare inside your Consciousness that it's another doll! After this? Only 2 more!]")
        ani("|...|")
        ani("   ")
        ani("'Well that's no fun. How about this? You can wait till they wake up!'")
        choice10nwes()
    else:
        ani("Don't resist", delay=0.2)
        choice9nwes()
    
def choice10nwes():
    choice10nwesa=input("Y/N: ")
    if choice10nwesa.lower() == "y":
        ani("'Great'")
        ani("'But I'll give you some time to explore... they're asleep anyways...'")
        choice11nwes()
    else:
        ani("'Why do you keep thinking that you can differ from the path that's laid out?'")
        ani("⍓︎□︎◆︎🕯︎●︎●︎ ■︎♏︎❖︎♏︎❒︎ ♏︎⬧︎♍︎♋︎◻︎♏︎")
        ani(" ")
        ani("You died")
        clear_screen()
        
def choice11nwes():
    choice11nwesa=input("Explore? (Y/N): ")
    if choice11nwesa.lower() == "y":
        ani("'Sounds great, tell me when you're done'")
        ani("Where would you like to look?")
        ani("Closet, Bed, Toy shelf")
        closetcodenwes()
    else:
        ani("'You're such a party pooper, and I still need to prepare'")
        ani("  ")
        ani("'⍓︎□︎◆︎ ♎︎♓︎♏︎♎︎'")
        clear_screen()
    
def closetcodenwes():
    choice12nwesa=input("Choose...: ")
    if choice12nwesa.lower() == "closet":
        ani("<You walk towards the closet>")
        ani("<Your heart hurts even more>")
        ani("|Do you remember?|", delay=0.2)
        ani("   ")
        closetnews()
    elif choice12nwesa.lower() == "bed" or choice12nwesa.lower() == "toy shelf":
        ani("<You approach, you stare, you reminisce...>")
        ani("<All the times you played, all the times you hung out>")
        ani("<Every time we told those stories...>")
        ani("<I remember>", delay=0.2)
        ani("<I look at the person beyond the screen...>", delay=0.2)
        ani("<Look at the person who shares my name>")
        ani(f"<{name}>", delay=0.2)
        ani("<3684>")
        ani("  ")
        ani("['We can't have that']")
        ani("['♐︎□︎❒︎♑︎♏︎⧫︎']")
        clear_screen()
    else:
        ani("'Not an option'")
        closetcodenwes()
    
def closetnwes():
    choice13nwesa=input("Attempt to open it? (Y/N): ")
    if choice13nwesa.lower() == "y":
        ani("<You open the closet and realise it's a door to a secret room>")
        ani("<There's a padlock with 4 digits on it>")
        ani("Do you want to try opening the door? You will only have one shot")
        ani("|...This is the least I can do for you|")
        ani("|3;8|")
        secretroomnwes()
    else:
        ani("<Please try again... for me>", delay=0.2)
        ani(" ")
        ani(f"'{name}, you sure are determined...'")
        clear_screen()
    
def secretroomnwes():
    choice14nwesa=input("Open the door? (Type the 4 digit code): ")
    if choice14nwesa == "3684":
        ani("<Your Consciousness falls silent as you walk into your room>")
        ani("<You know that once you leave, you'll die>")
        ani("<He'll find you>")
        ani("<Her voice is gone aswell>")
        ani("<On the table is a diary, the name?>")
        ani(name)
        ani("<There's only one entry intact>")
        ani("Read the entry?")
        mychoice=input("Y/N: ")
        ani("But you're no longer in control", delay=0.15)
        ani("  ")
        ani("<Dear Diary, I finally found a home!>")
        ani("<I have a mum, a dad, and even a little brother! They even have a dog!>")
        ani("<They really like the dog, my parents say it's been with them since the beggining...>")
        ani("<But I finally have a family, a real family>")
        ani("<I hope this happiness never ends>")
        ani("........", delay=1)
        ani("<Complete the game>")
        ani("<Complete Consciousness>")
        ani("<Because once you do?>")
        ani("<I can finally go home>")
        clear_screen()
    else:
        ani("You failed to open the door")
        ani("[Keep moving]")
        ani("  ")
        ani("<You return to the ''childlike'' dolls bed>")
        ani("<Beside the sleeping child is a paper puzzle>")
        ani("   ")
        ani("'They finally woke up, so I guess it's time for me to go, :)'")
        ani("  ")
        ani("~You're here!~")
        ani("~...~")
        ani("~Don't you recognize me? Don't you remember me?... Don't you love me?~", delay=0.23)
        ani("<Your choices: ...;...;...;...;>")
        choice15nwes()
    
def choice15nwes():
    choice15nwesa=input("<Your answer>: ")
    ani("~...~")
    ani("'You selected the correct answer!'")
    ani("  ")
    ani("|Don't hurt him... please|")
    ani("<...>")
    ani("[But you had no choice]", delay=0.2)
    ani("  ")
    choice16nwes()
    
def choice16nwes():
    ani("<You have to keep moving, no point in stopping now>")
    ani("<You know the consequences of failure>", delay=0.2)
    ani("<You start heading back to the main room>")
    ani("<You feel hatred towards yourself>")
    ani("[You feel pride towards yourself]")
    ani("<You feel sick towards the sign that lies in the main room>")
    ani("[You feel adoration towards the sign that lies in the main room]")
    ani("  ")
    the_end() 

#Final room E of the NWSE
def shednwse():
    ani("<You walk along the wild east hallway, walking till you see a old wooden door>")
    ani("[You can barely hold your excitement due to you getting closer to completing your goal]")
    ani("<But you stop the moment you see the doll through the rotted wood>")
    ani("<...>")
    ani("<It's a dog>")
    ani("|Not him... PLEASE NOT HIM...|")
    ani("  ")
    choice22nwse()
    
def choice22nwse():
    choice22nwsea=input("<You know that you'll need to enter anyways...> (Y/N): ")
    if choice22nwsea.lower() == "y":
        ani("<You feel your stomach sink as you see a dog like doll>")
        ani("[No need to explore, you can already see everything anyways]")
        ani("  ")
        ani("<As you look around you see a screwdriver>")
        ani("[You already have the knife]")
        ani("  ")
        choice23nwse()
    else:
        ani("'What a shame'")
        ani("'You were getting there as well'")
        ani("'But i'm not giving you an easy way back'")
        ani("'No'")
        ani("'You can restart if you want to go back...'")
        clear_screen()

def choice23nwse():
    choice23nwsea=input("'Walk towards the dog?' (Y/N): ")
    ani(" ")
    if choice23nwsea.lower() == "y":
        ani("<You walk towards the dog...>")
        ani("[It's a doll]", delay=0.15)
        ani("<You walk towards the doll>")
        ani("[:)]")
        ani("<As you get closer you look into it's eyes, it seems to recognise you...>")
        ani("*...*")
        ani("<It doesn't speak>")
        ani("<...>")
        ani("<It only whines>")
        ani("[But your consciousness understands it]")
        ani("[*Why is that smell so familiar?*]")
        ani("'Enough talking, give them the puzzle'")
        ani("<You hear it whine...>")
        ani("  ")
        choice24nwse()
    else:
        ani("'What a shame'")
        ani("'You were getting there as well'")
        ani("'But i'm not giving you an easy way back'")
        ani("'No'")
        ani("'You can restart if you want to go back...'")
        ani("'Sound familiar?'")
        ani("'Same words as last time'")
        clear_screen()

def choice24nwse():
    ani("[*What does every soul have?*]")
    ani("<Your choices: Patience(a); Affection(b); Hatred(c); Determination(d)>")
    ani("  ")
    choice25nwse()

def choice25nwse():
    choice25nwsea=input("<Your answer>: ")
    if choice25nwsea.lower() == "d":
        ani("'You selected the correct answer!'")
        ani(" ")
        ani("<You refuse to use the knife>")
        ani("'Are you really doing this?'")
        ani("<YOU REFUSE TO USE THE KNIFE>")
        ani("'You're going to have to do it eventually...'")
        ani("<I don't want to>")
        ani("'I know'")
        ani(" ")
        ani("[They stab the dog...]")
        ani("[They didn't want to...]")
        ani("'But I worked hard so that you can make it closer to the end :)'")
        ani("|...|")
        ani(" ")
        ani("[Only two more dolls left till you're done with your mission]")
        ani("<Only two more dolls left till you're done with this hell>")
        ani("  ")
        directionnwse()
        

    else:
        ani("'You were so close!'")
        clear_screen()  

def directionnwse():
    choice16nwsea=input("[Only 2 more to go] (W/S): ")
    if choice16nwsea.lower() == "w":
        ani("<As you start heading back you wonder how this all went so wrong>")
        ani("<But you know you can't stop>")
        ani("[We won't let you]")
        ani("<You already knew that>")
        ani("<Even more so as you reach the main room>")
        ani("'You really are a wonderful person, ;)'")
        ani("  ")
        mastersnew()
    elif choice16nwsea.lower() == "s":
        ani("<As you start heading back you wonder how this all went so wrong>")
        ani("<But you know you can't stop>")
        ani("[We won't let you]")
        ani("<You already knew that>")
        ani("<Even more so as you reach the main room>")
        ani("'You really are a wonderful person, ;)'")
        ani(" ")
        the_end()
    else:
        ani("'Don't try to escape me'")
        ani("  ")
        directionnwse()

#The End
def the_end():
    ani("<You finally did it>")
    ani("<Every voice in your head is gone...>")
    ani("<You finished everything>")
    ani("<...>")
    ani("<You walk to the main room>")
    ani("<You see all your victims...>")
    ani("<A hallucination?>")
    ani("<No>")
    ani("<They're actually here>")
    ani("<All I feel is regret>")
    ani("<All you feel is pride in finishing>", delay=0.2)
    ani("<...>")
    ani("<She's coming>")
    ani("  ")
    ani("'Do you like it?'")
    ani("'All of them'")
    ani("'All your poor victims'")
    ani("'You asked for this'")
    ani("'You watching the screen, you didn't know?'")
    ani("'They asked me to do this'")
    ani("'To make this game'")
    ani("'All for their selfish desire'")
    ani("'I'm just the devil they made the deal with'")
    ani("'I was [The Consciousness]'")
    ani("'I was the God'")
    ani("I was the programmer")
    ani("<I see them, no longer dolls, but humans. All killed with the weapon I held...>")
    ani("'Great work! You completed the game...'")
    ani("'But at what cost?'")
    ani(" ")
    ani("---------------------------------------------", delay=1)
    ani("<I can't believe you waited that long>")
    ani("<Nothing she said was a lie>")
    ani("<In reality?>")
    ani("<All I feel is a little guilt, she's just the one who felt a little pity>")
    ani("<But if you read my diary you'll know why I did what I did>")
    ani("<You'll know that I will finally be free, reunited with them>")
    ani(f"<So thanks {name}>")
    ani("<Thank you for completing Consciousness>")
    ani("----------------------------------------------")
    ani("CREDITS")
    ani("Rachael MacKinnon - Main programmer, Story writer, and [The Consciousness]")
    ani("Mr Groom - Helped with bugging and other issues (Also where chit chit came from)")
    ani("Em Thomas - For helping me choose the screw driver")
    ani("Copilot - For giving me .lower()")
    ani("Mr Scott - For also giving me .lower() and explaining it when he was busy with HSC marking")
    ani("Calum MacKinnon (Dad) - For hanging in my room and keeping me company")
    ani("Naomi Rice - Game Tester")
    ani("Grace Ji - Game Tester")
    ani("Julie Shie - Game Tester")
    ani(f"{name} - For playing my game that I poured my heart into, thanks for playing")
    ani(":D")
    ani("----------------------------------------------", delay=1)
    ani("♒︎♓︎✏︎ ♓︎⧫︎⬧︎ ❍︎♏︎📪︎ ❒︎♋︎♍︎♒︎♋︎♏︎●︎📬︎")
    ani("⬥︎♒︎⍓︎ ⬥︎♓︎■︎♑︎♎︎♓︎■︎♑︎⬧︎ ⍓︎□︎◆︎ ❍︎♋︎⍓︎ ♋︎⬧︎🙵✍︎")
    ani("♍︎♋︎◆︎⬧︎♏︎ ♓︎ ●︎♓︎🙵♏︎ ◆︎■︎♎︎♏︎❒︎⧫︎♋︎●︎♏︎ ⧫︎♒︎♋︎⧫︎⬧︎ ♋︎●︎●︎📪︎ 🖳︎✆︎📬︎")
    ani("♓︎❍︎ ♑︎♏︎■︎◆︎♓︎■︎♏︎●︎⍓︎ ⬧︎◆︎◻︎❒︎♓︎⬧︎♏︎♎︎ ⍓︎□︎◆︎ ⬥︎♋︎♓︎⧫︎♏︎♎︎ ♋︎♑︎♋︎♓︎■︎📪︎ ⬧︎□︎ □︎■︎♍︎♏︎ ♋︎♑︎♋︎♓︎■︎ ⧫︎♒︎♋︎■︎🙵⬧︎ ♐︎□︎❒︎ ◻︎●︎♋︎⍓︎♓︎■︎♑︎✏︎")
    ani("◻︎📬︎⬧︎📬︎ ♎︎♓︎♎︎ ⍓︎□︎◆︎ ♐︎♓︎■︎♎︎ ⧫︎♒︎♏︎ □︎⧫︎♒︎♏︎❒︎ ❒︎♏︎♐︎♏︎❒︎♏︎■︎♍︎♏︎✍︎")
    clear_screen()


choice1()
