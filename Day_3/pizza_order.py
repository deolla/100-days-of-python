print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small_price = 15
medium_price = 20
large_price = 25
pepperoni_small = 2
pepperoni_large = 3
extra_cheese_price = 2

total = 0

if size == 'S':
    total += small_price
elif size == "M":
    total += medium_price
elif size == "L":
    total += large_price
else:
    print(f"Invalid input")

if add_pepperoni == "Y":
    if size == 'S':
        total += pepperoni_small
    elif size == "M":
        total += pepperoni_large
    else:
        total += pepperoni_large

if extra_cheese == "Y":
    total += extra_cheese_price

print(f"Your total is ${total}.")