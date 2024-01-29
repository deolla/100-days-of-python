print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Child ticket are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        if age >= 45 and age <= 55:
            print("This is for free")
        else:
            bill = 12
            print("Adult ticket is $12")
    
    photo = input("Do you want your photo taken? Y or N?: ")
    if photo == "Y":
        bill += 3
    print(f"your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
