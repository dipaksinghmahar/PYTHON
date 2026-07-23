# ---------------------------------
# LEVEL 2 – Intermediate Loops
# ---------------------------------
# Question 1:
print("Print all numbers divisible by 3 from 1 to 100.")
for i in range(1,101):
    if (i % 3 ==0):
        print(i)

# Question 2:
print("Print all numbers divisible by both 3 and 5 from 1 to 100.")
for i in range(1,101):
    if (i%3==0 and i%5==0):
        print(i)

# Question 3:
print("Print all multiples of 5 from 1 to 100.")
for i in range (1,101):
    if (i%5==0):
        print(i)

# Question 4:
print("Find the factorial of a given number.")
number=int(input("enter the value of the number :"))
result=1
for i in range (1,number+1):
    result=result*i
    print(result)

# Question 5:
print("Count the number of digits in a given number.")
b=input("Enter the digit :")
count=0
for i in b:
    count=count+1
print(count) 

# Question 6:
print("Reverse a given number using a loop.")
a=int(input("enter the number:"))
for i in range (a,1,-1):
    print(i)

# Question 7:
print("Check whether a given number is a palindrome.")
b=input("enter the value :")
rev=""
for i in b:
    rev=rev +i
if b==rev :
    print("yes, it is palindrome")
else:
    print("no,it is not a palindrome")
 