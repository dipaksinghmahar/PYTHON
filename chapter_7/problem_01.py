# . Write a program to print multiplication table of a given number using for loop.
num=int(input("enter a number:"))
for i in range (1,11):
    print(num,"*",i,"=",num*i)
    i=1+1

'''Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry","Soham","Sachin","Rahul"]'''

l=["Harry","Soham","Sachin","Rahul"]
for name in l:
    if name.startswith("S"):
      print("hello",name)

      
#Attempt problem 1 using while loop.
# Input a number from the user
num = int(input("Enter a number: "))

# Initialize the counter
i = 1

# Run the loop from 1 to 10
while i <= 10:
    # Print the multiplication table
    print(f"{num} x {i} = {num * i}")

    # Increase the counter by 1
    i += 1

# Write a program to find whether a given number is prime or not.
num = int(input("Enter a number: "))
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
