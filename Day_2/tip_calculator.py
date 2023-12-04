# A tip calculator.. Calculate the amount of tips that should be paid
# depending on the numbers of people.

print("Welcome to the tip calclator.")

total_bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give 10, 12, 0r 15?? ")
split_bill = input("How many people to split the bill? ")

per = int(percentage) / 100
i = float(total_bill) * per

result = (float(total_bill) + i) / int(split_bill)
print(f"Each person should pay: ${result:.2f}")
# print(f"Each person should pay: ${round(result, 2)}")
