"""
Script Name: TelepathicTA
Coder Name: Andrew Klieger
Script Name: AndrewKlieger_TelepathyTA1.0
Data Script Name:
Purpose: To run the text adventure I have created.
What happens when the script is run?: Text will ask the user for instruction on what to do in various moments of action
Language Learning and Computer Science
"""
# Need these for timed lines and colors
import time

import Data_Script_TA
from colorama import Fore

Data_Script_TA.stringsave()
# Invalid input option
def what():
    print("Bro what")


def alter2():
    user = input("Do you want to " + Fore.LIGHTRED_EX + " SLAP " + Fore.RESET + " or "
                 + Fore.MAGENTA + "DEFEND?: " + Fore.RESET)

    # user attacks
    if user.upper() == "SLAP":
        print("You Slap the butterfly!")
        time.sleep(1.5)
        print("It dies...")
        time.sleep(1.5)
        print("You monster!!")
        time.sleep(1.5)
        print("after killing the butterfly, You find me")
        time.sleep(1.5)
        print("enjoy your casual ending...")
        time.sleep(1.5)
        print("Butterfly murderer...")
        # Murderer End
        exit()
        # defending
    else:
        what()


def first():
    # "Print" means the computer will display whatever is in the print parenthesis
    # time.sleep means how long the computer will wait before displaying another line.
    # Start
    print("How to play: just type in an answer to the question the computer is giving you after a colon")
    time.sleep(1.5)
    print("If you type something the computer does not understand, it will repeat the question")
    print("They will mostly be yes or no questions")
    time.sleep(1.5)
    print("Have fun~")
    time.sleep(5)
    print("What's up")
    time.sleep(1.5)
    print("...Is anyone there?")
    time.sleep(1.5)
    # Question that needs user input which changes if user says y/n or something else
    while True:

        user = input("Can you " + Fore.LIGHTGREEN_EX + "Hear " + Fore.RESET + "me?: ")
        time.sleep(1.5)
        # User decides if they want to start
        # "or" means the user can type either answer with the same response
        if user.upper() == "YES" or user.upper() == 'Y':
            # Long Prints
            print("Ah thank goodness!")
            time.sleep(1.5)
            print("I am your best friend remember?")
            time.sleep(3)
            print("Listen to me! I have been captured by an evil entity, you must help!")
            time.sleep(2)
            print("I am aware that you are blind and deaf... But you have my telepathy to guide you!")
            time.sleep(2)
            print("You can't see or hear, so you must rely on my words")
            time.sleep(2)
            print("I believe this entity is the same one who made you blind and deaf!")
            time.sleep(1.5)
            print("okay first choice!")
            time.sleep(1.5)
            # User is asked if they will save the computer
            break

        # Beginning "no's"
        elif user.upper() == "NO" or user.upper() == 'N':
            print("bruh")
            break


def second():
    user = input("Will you save me(type: yes): ")
    time.sleep(1.5)
    # User gives an answer
    if user.upper() == "YES" or user.upper() == 'Y':
        print("Great!! Let us commence forth")
        time.sleep(1.5)
    # An else which does not change the story at all
    else:
        print("...sorry you have no choice")
        time.sleep(1.5)
        # Asks user first real choice

    # User returns to first print here since it is "While true"


def alter():
    while True:
        print("I will be your eyes!")
        time.sleep(1.5)
        print("You walk along a very boring and uncharacteristic dirt trail")
        time.sleep(1.5)
        print("it seems there is a fork in the road!")
        time.sleep(1.5)
        print("Look a sign!")
        time.sleep(1.5)
        print("Easy or hardcore paths..., or at least, that's what the sign says ")
        time.sleep(1.5)
        # Path Choice
        user = input(
            "Alright, would you like to go down the " + Fore.YELLOW + "casual " + Fore.RESET + "path or the "
            + Fore.RED + "hardcore " + Fore.RESET + "path? or go back...? (Go casual if you are short on time) : ")
        time.sleep(1.5)
        # Casual choice path
        if user.lower() == "casual" or user.upper() == "CASUAL PATH":
            print("yeah no... sorry you are a gamer try again")
            time.sleep(1.5)

        elif user.lower() == "hardcore" or user.lower() == "hardcore path":
            print("Haha sick!")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("I know you can't see this but are you sure you should've gone down this path?")
            time.sleep(1.5)
            print("From what I'm seeing, it looks pretty scary...")
            time.sleep(1.5)
            print("Look out! A uoᴉʇɐuᴉɯoqɐ! They are the scourge of this world")
            time.sleep(1.5)
            print("You can't escape, you have to" + Fore.RED + " FIGHT " + Fore.RESET)
            time.sleep(1.5)
            # User returns to first print here since it is "While true"
            # Fights the uoᴉʇɐuᴉɯoqɐ
            break
        elif user.lower() == "back":
            print("You can't go back now!")
            time.sleep(1.5)


def alter1():
    while True:
        user = input(
            "Do you want to " + Fore.RED + " FIGHT " + Fore.RESET + " or " + Fore.CYAN + " ESCAPE!!!: " + Fore.RESET)
        time.sleep(1.5)
        # Engage in the fight
        if user.upper() == "FIGHT":
            print("You " + Fore.RED + "FIGHT" + Fore.RESET + " the butterfly!")
            time.sleep(1.5)
            alter2()

        elif user.upper() == "DEFEND":
            print("You brace for impact from the butterfly!")
            time.sleep(1.5)
            print("It does nothing... cause it's a butterfly")

        # User continues without a fight
        elif user.upper() == "ESCAPE":
            print("You run away... from the butterfly...")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("After running away from the butterfly, you find me!")
            time.sleep(1.5)
            print("Enjoy your casual ending")
            time.sleep(1.5)
            print("Loser...")
            # Loser end
            exit()
        # If not correct answer prints this else
        else:
            what()

    # Hardcore choice path


def third():
    while True:

        user = input(
            "Do you want to " + Fore.RED + " FIGHT " + Fore.RESET + " or " + Fore.CYAN + " ESCAPE!!!: "
            + Fore.RESET)
        # Failed escape attempt
        if user.lower() == "escape":
            time.sleep(1.5)
            print("Dude I literaly just said you can't escape!")
        # User fights enemy
        elif user.lower() == "fight":
            print("You" + Fore.RED + " FIGHT " + Fore.RESET + "the uoᴉʇɐuᴉɯoqɐ!!!")
            break


def fourth():
    while True:

        user = input("Do you want to " + Fore.LIGHTRED_EX + " SLAP " + Fore.RESET + " or "
                     + Fore.MAGENTA + "DEFEND?: " + Fore.RESET)
        # User defends and is impervious
        if user.lower() == "defend":
            print("You defended and the uoᴉʇɐuᴉɯoqɐ couldn't harm you!")
            time.sleep(1.5)
        # User kills enemy
        elif user.lower() == "slap":
            print("You can't see the enemy, but you slap as hard as you can!")
            time.sleep(1.5)
            print("You definetly hit something's face!")
            time.sleep(1.5)
            print("You killed the uoᴉʇɐuᴉɯoqɐ!")
            time.sleep(1.5)
            # User returns to first print here since it is "While true"
            break


def fifth():
    while True:
        # User choice to keep walking
        user = input("Do you want to keep" + Fore.YELLOW + " walking?: " + Fore.RESET)
        # User will have to keep moving
        if user.lower() == "no":
            time.sleep(1.5)
            print("You stand around doing nothing")
            time.sleep(1.5)
            print("...")
            time.sleep(5)
            print("okay that's enough nothing!")
        # User continues
        elif user.lower() == "yes":
            time.sleep(1.5)
            print("Lets keep moving!")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("Woah be quiet!")
            time.sleep(1.5)
            print("It's a sleeping uoᴉʇɐuᴉɯoqɐ! It's blocking the whole path...")
            time.sleep(5)
            print("There's a key around its neck!")
            time.sleep(1.5)
            print("You gotta get that key...")
            # User returns to first print here since it is "While true"
            break
        else:
            what()
            time.sleep(1.5)


def sixth():
    while True:
        # User can go back or get key
        user = input("Do you want to get close and nab the key?: ")
        # Lazy end
        if user.lower() == "no":
            time.sleep(1.5)
            print("You decide not to even try and go back without rescuing me")
            time.sleep(3)
            print("Thanks a lot.")
            exit()
        # User continues with stealing key
        elif user.lower() == "yes":
            time.sleep(1.5)
            print("Be veeerrryyy careful!")
            time.sleep(3)
            print("uh oh")
            time.sleep(1.5)
            print("The uoᴉʇɐuᴉɯoqɐ is 100% awake!")
            time.sleep(1.5)
            # User returns to first print here since it is "While true"
            break


def seventh():
    while True:

        user = input("Do you still want to get the key?!?!: ")
        # user is forced to get key
        if user.lower() == "no":
            time.sleep(1.5)
            print("You are THIS close to making me angry.")
            time.sleep(1.5)
            print("You are getting that key whether you like it or not.")
        # user steals key
        elif user.lower() == "yes":
            time.sleep(3)
            print("You easily do a front handspring into a backflip"
                  " and steal the key")
            time.sleep(1.5)
            # User returns to first print here since it is "While true"
            break


def eighth():
    while True:
        # User is asked to continue
        user = input(
            "Do you want to keep" + Fore.YELLOW + " "
                                                  "walking?: " + Fore.RESET)
        # Break end
        if user.lower() == "no":
            time.sleep(1.5)
            print("You decide to sit down and take a break")
            time.sleep(1.5)
            print("...")
            time.sleep(3)
            print("You sat on a poisonous plant and died")
            exit()
        # user continues
        elif user.lower() == "yes":
            time.sleep(1.5)
            print("You find yourself in a very pretty clearing")
            time.sleep(1.5)
            print("Despite its beauty, you can't help but feel afraid...")
            time.sleep(1.5)
            print("There is a house in the distance")
            time.sleep(1.5)
            print("However, It's surrounded by a field of strange grass!")
            time.sleep(1.5)
            # User returns to first print here since it is "While true"
            break


def ninth():
    while True:
        # User is asked to venture into the grass
        user = input("Do you want to go into the grass?: ")
        time.sleep(1.5)
        # User has to go into grass
        if user.lower() == "no":
            time.sleep(1.5)
            print("Well too bad!")
            time.sleep(1.5)
            print("I need you to save me so... YOU BETTER EXPLORE!")
        # User explores grass
        elif user.lower() == "yes":
            time.sleep(1.5)
            print("You take a BIG FAT step into the grass")
            time.sleep(1.5)
            print("!!!!!!!")
            time.sleep(1.5)
            print("The grass is pulling you underneath the ground!")
            time.sleep(1.5)
            print("...")
            time.sleep(3)
            print("You seem to be in some type of dark cave...")
            time.sleep(1.5)
            print("Not like it matters to you though...")
            time.sleep(3)
            print("cause you're blind...")
            time.sleep(1.5)
            print("Fear not! I can still hear things with my"
                  " telekinesis! ")
            time.sleep(1.5)
            print("Try feeling around with your hands!")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("..!")
            time.sleep(2)
            print("How lucky! you've found yourself a weapon!")
            time.sleep(1.5)
            print("seems like it shoots things!")
            time.sleep(2)
            print("Do you hear that?")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("Oh no it's bats!")
            time.sleep(1.5)
            print("Use your NEW weapon!")
            # User returns to first print here since it is "while True"
            break


def tenth():
    while True:
        # User is asked to engage fighting with a bat
        user = input(
            "Do you want to " + Fore.RED + " FIGHT "
            + Fore.RESET + " or " + Fore.CYAN +
            " ESCAPE!!!:" " " + Fore.RESET)
        # ditch end
        if user.lower() == "escape":
            time.sleep(1.5)
            print("You tried to escape but just ran "
                  "and fell into a ditch in the cave")
            print("Game over")
            exit()
            time.sleep(1.5)
        # User fights bat
        elif user.lower() == "fight":
            print("You" + Fore.RED + " FIGHT " + Fore.RESET
                  + "the bats!!!")
            break


def eleventh():
    while True:
        user = input("Do you want to " + Fore.LIGHTRED_EX +
                     " SHOOT " + Fore.RESET + " or "
                     + Fore.MAGENTA + "DEFEND?: " +
                     Fore.RESET)
        # User defends from the bat
        if user.lower() == "defend":
            print("The bats nibbled on you, "
                  "but were unable to harm you!")
            time.sleep(1.5)
        # User kills bat
        elif user.lower() == "shoot":
            print("*BANG*")
            time.sleep(1.5)
            print("You definitely shot something!")
            time.sleep(1.5)
            print("You killed the bat!...somehow")
            time.sleep(1.5)
            # User returns to first print here since it is
            # "While true"
            break


def twelfth():
    while True:
        user = input(
            "Do you want to keep" + Fore.YELLOW +
            " " "walking?: " + Fore.RESET)
        # User waits before walking
        if user.lower() == "no":
            time.sleep(1.5)
            print("You stand around doing nothing")
            time.sleep(1.5)
            print("...")
            time.sleep(10)
            print("okay that's enough nothing!")
        # User keeps going through cave
        elif user.lower() == "yes":
            time.sleep(1.5)
            print("You stumble around the cave "
                  "some more")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("What's this?")
            time.sleep(1.5)
            print("Looks like some kind of door "
                  " with a keyhole")
            # User returns to first print here
            # since it is "While true"
            break


def thirteenth():
    while True:
        # User can use key here
        user = input("Do you want to use "
                     "the key you stole?: ")
        # Starve end
        if user.lower() == "no":
            print("You decide not to use "
                  "the key and die of "
                  "starvation in the "
                  " cave.")
            exit()
        # User unlocks door
        elif user.lower() == "yes":
            print("You unlock the door.")
            time.sleep(1.5)
        print("It seems like a way out!")
        time.sleep(1.5)
        print("Quickly let's go!")
        time.sleep(1.5)
        print("After exiting the cave you "
              "feel a dark presence")
        time.sleep(1.5)
        print("what you feel right now "
              "is...")
        time.sleep(4)
        break


def end_one():
    time.sleep(1.5)
    print("Is a feeling of excitement and dread!")
    time.sleep(1.5)
    print("You are very close to the end I can feel it")
    time.sleep(3)
    print("You approach a shady house")
    time.sleep(1.5)
    print("You feel drawn to it")
    time.sleep(1.5)
    while True:

        time.sleep(1.5)
        user = input("Do you want to go in through the " + Fore.GREEN + " FRONT DOOR? " + Fore.RESET + "or the" +
                     Fore.BLUE + "BACK DOOR?: " + Fore.RESET)
        if user.lower() == "back door":
            time.sleep(1.5)
            print("Seems to be locked, maybe you could find a key?")

        elif user.lower() == "front door" or "front":
            time.sleep(2)
            print("You enter through the front door")
            time.sleep(1.5)
            print("The door is creaky, and so are the floorboards")
            time.sleep(3)
            print("Did you just hear that?")
            time.sleep(1.5)
            print("of course you didn't...")
            time.sleep(1.5)
            print("There was a clicking sound-")
            time.sleep(1)
            print("OH NO! That was the door locking itself!")
            time.sleep(1.5)
            print("guess we have to keep moving into the house...")
            break


def end_two():
    while True:

        # User choice to keep walking
        user = input("Do you want to keep" + Fore.YELLOW + " walking?: " + Fore.RESET)
        # User will have to keep moving
        if user.lower() == "no":
            time.sleep(1.5)
            print("You sit down in an old chair")
            time.sleep(1.5)
            print("...")
            time.sleep(5)
            print("it feels nice")
        # User continues
        elif user.lower() == "yes":
            time.sleep(1.5)
            print("Be careful, the floorboards seem unstable...")
            time.sleep(1.5)
            print("Oh my-")
            time.sleep(1)
            print("There is a sleeping snake here.")
            time.sleep(3)
            print("And now it has seen you!!")
            time.sleep(2)
            print("Beware! These snakes can bite through defenses!")
            break


def end_three():
    while True:

        user = input(
            "Do you want to " + Fore.RED + " FIGHT " + Fore.RESET + " or " + Fore.CYAN + " ESCAPE!!!: "
            + Fore.RESET)
        # Failed escape attempt
        if user.lower() == "escape":
            time.sleep(1.5)
            print("There's nowhere to escape to!")
        # User fights enemy
        elif user.lower() == "fight":
            print("You" + Fore.RED + " FIGHT " + Fore.RESET + "the snake!!!")
        user = input("Do you want to " + Fore.LIGHTRED_EX + " SHOOT " + Fore.RESET + " or "
                     + Fore.MAGENTA + "DODGE?: " + Fore.RESET)
        break


def end_four():
    user = input("Do you want to " + Fore.LIGHTRED_EX + " SHOOT " + Fore.RESET + " or "
                 + Fore.MAGENTA + "DODGE?: " + Fore.RESET)
    # User defends and is impervious
    if user.lower() == "shoot":
        print("You shoot the snake, but it ate the bullet!")
        time.sleep(1.5)
    # User kills enemy
    elif user.lower() == "dodge":
        print("You leap out of the way majestically")
        time.sleep(1.5)
        print("The snake then does something you would never expect...")
        time.sleep(1.5)
        print("TO BE CONTINUED")
        exit()


first()
second()
alter()
third()
fourth()
fifth()
sixth()
seventh()
eighth()
ninth()
tenth()
eleventh()
twelfth()
thirteenth()
end_one()
end_two()
end_three()
end_four()
