print("Welcome to Treasure Island. \nYour mission is to find the treasure.\n")
choice1 = input('You are at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if choice1 == 'left':
    choice2 = input('You reached a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the Island unharmed. There is a house with 3 doors. RED, YELLOW and BLUE. Which one do you choose?\n').upper()
        if choice3 =="RED":
            print("Trap Triggered! You Died!\n Restart Game.")
        elif choice3 == "YELLOW":
            print("You found the treasure!\n Restart Game.")
        elif choice3 == "BLUE":
            print("A hungry Tiger attacked you. You Died! Restart Game.")
        else:
            print("ERROR!")
    elif choice2 == "swim":
        print("You get attacked by alligators. You Died! Restart Game.")
    else:
        print("ERROR!")
elif choice1 == "right":
    choice4 = input('You find a path through a forest. Type "enter" to enter forest or "give up" to end game.')
    if choice4 == "enter":
        print("You got caught by tribals who protect the treasure and were killed by them. Gmaeover! Restart Game")
else:
    print("ERROR!")
