print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
user_input = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n')


if user_input == 'right':
    print("\nOps! Not again, Its on you😒 Game Over🤦‍♀️🤦‍♂️\n").lower()
else:
    if user_input == 'left':
        print("\nYou are doing well!!\n")
        decision = input("You don reach lake. If you look wella you go see one island for middle of lake. Type \"wait\"  to wait for a boat. Type \"swim\" to swim across.\n").lower()
        if decision == 'swim':
            print('\nGame Over, I can believe you failed that😔😒🙄\n')
        elif decision == "wait":
            print("\nMy oga!! plenty!!\n")
            selection = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
            if selection == "red":
                print("\nGame Over, like seriously?? (ㆆ_ㆆ)")
            elif selection == "blue":
                print("\nGame Over, ￣へ￣ ＞︿＜")
            elif selection == "yellow":
                print("\nYou win! finally!!🫡 🤓 ○( ＾皿＾)っ Hehehe…")
            else:
                print("\nOpen your eyes wella o, this selection no dey here")
        else:
            print("\nOpen your eyes wella o, this selection no dey here")
    else:
        print("\nOpen your eyes wella o, this selection no dey here")
        

            
