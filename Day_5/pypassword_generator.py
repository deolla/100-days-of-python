#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

user_input = nr_letters + nr_numbers + nr_symbols

# if user_input > 0:
#     password = ""
#     for i in range(nr_letters):
#         password += random.choice(letters)
#     for i in range(nr_symbols):
#         password += random.choice(symbols)
#     for i in range(nr_numbers):
#         password += random.choice(password)
#     print(f"Your password is {password}")

# if user_input == 0:
#     print("You must enter a number greater than 0!")
#     exit()


# or
password = ""
for _ in range(user_input):
    choice =  random.choice(["letter", "symbols", "numbers"])
    if choice == "letter":
        password += random.choice(letters)
    elif choice == "symbols":
        password += random.choice(symbols)
    elif choice == "numbers":
        password += random.choice(numbers)
print(f"Your password is {password}")