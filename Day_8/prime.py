def prime_checker(num):
    """This function checks if the number is prime or not"""

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input())
prime_checker(num=n)
