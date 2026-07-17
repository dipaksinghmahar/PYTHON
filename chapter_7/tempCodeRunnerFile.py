# Write a program to find whether a given number is prime or not.

# Input a number from the user
num = int(input("Enter a number: "))

# Check if the number is less than or equal to 1
if num <= 1:
    print(num, "is not a prime number")

else:
    # Assume the number is prime
    is_prime = True

    # Check for factors from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Display the result
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")