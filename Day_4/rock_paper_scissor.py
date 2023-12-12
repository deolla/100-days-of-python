
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = [0, 1, 2]
user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if user_input not in choice:
    print('Invalid input. Please try again.')
else:

    if user_input == 0:
        print(rock)
    elif user_input == 1:
        print(paper)
    elif user_input == 2:
        print(scissors)
    else:
        print('Invalid input. Please try again.')
    
    computer_choice = random.choice(choice)
    print("computer choose: ")
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    elif computer_choice == 2:
        print(scissors)
    else:
        print('Invalid input. Please try again.')

    if user_input == computer_choice:
        print("It's a draw")
    elif(
    (user_input == 0 and computer_choice == 2) or
    (user_input == 1 and computer_choice == 0) or
    (user_input == 2 and computer_choice == 1)
    ):
        print("you win!")
    else:
        print("You lose")
