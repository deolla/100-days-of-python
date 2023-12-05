# Create a love calculator using count() and lower()
print("Welcome to the love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


add = name1 + name2

e = add.lower().count('t')
f = add.lower().count('r')
g = add.lower().count('u')
h = add.lower().count('e')
true = e + f + g + h

a = add.lower().count('l')
b = add.lower().count('o')
c = add.lower().count('v')
d = add.lower().count('e')
love = a + b + c + d

love_score =  int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")