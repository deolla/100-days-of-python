names = names_string.split(", ")
# The codde below converts the input into an array separated
# each name int the input by a comma and spaces
# Don't change the code above.
import random

rand = random.randint(0, len(names) - 1)
person = names[rand]
print(person + " is goint to buy the meal today!")