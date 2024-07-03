import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper = """
    ________
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
images = [Rock, Paper, Scissors]
comp_choice = random.randint(0, 2)
if user_choice >= 3 or user_choice < 0:
    print("You entered invalid number. You lose!")
else:
    print(images[user_choice])

print('Computer chose:')
print(images[comp_choice])
if user_choice == 0 and comp_choice == 2:
    print("You win!")
elif user_choice < comp_choice:
    print("You lose!")
elif user_choice == 2 and comp_choice == 0:
    print("You lose!")
elif user_choice > comp_choice:
    print("You win!")
elif user_choice == comp_choice:
    print("Draw!")
else:
    print("INVALID!")