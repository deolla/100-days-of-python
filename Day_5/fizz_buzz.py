for m in range(1, 101):
    if m % 3 == 0 and m % 5 == 0:
        print("FizzBuzz")
    elif m % 5 == 0:
        print("Buzz")
    elif m % 3 == 0:
        print("Fizz")
    else:
        print(m)
# or

for i in range(1, 100 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
     