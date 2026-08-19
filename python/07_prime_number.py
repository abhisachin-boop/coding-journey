# Check whether a number is prime

number = int(input("Enter a number: "))

if number < 2:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    print("Prime" if is_prime else "Not prime")
