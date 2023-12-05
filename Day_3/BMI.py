height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height ** 2
bmi = round(bmi)

if bmi < 18.5:
    print(f"Your BMI is {round(bmi)}, you are underweight.")
elif bmi < 25:
    print(f"You BMI is {round(bmi)}, you are normal weight.")
elif  bmi < 30:
    print(f"Your BMI is {round(bmi)}, you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {round(bmi)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")