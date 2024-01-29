""" # Printing the length of a string
user_input = input("Input your name: ")
count = len(user_input)
print(count)

# len() - this gives out the length or the number of items in an object.
# Depends on the type of the object passed as an argumentclear

# print the number of a string

user_input = input("Input your name: ")
count = len(user_input.split())
print(count)


user_input = input("What is your name? ")
print(user_input)
if user_input == 'Oluwaseyi':
    print('You are Great')
elif user_input == 'Daniel':
    print('You are loved')
else:
    print('You are Intelligent') 
"""

# swapping inputs
# Don't change the code below
a = input("a:")
b = input("b:")
# Don't change the code above

tmp = a
a = b
b = tmp

# Don't change the code below
print("a = " + a)
print("b = " + b)
# Don't change the code above
