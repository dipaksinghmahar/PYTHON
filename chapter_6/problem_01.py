# Write a program to find the greatest of four numbers entered by the user.
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
d=int(input("enter fourth number:"))    
if a>b and a>c and a>d:
    print("a is greatest")
elif b>c and b>d:
    print("b is greatest")
elif c>d:
    print("c is greatest")
else:
    print("d is greatest")

'''Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.'''
st_mark=int(input("Enter marks of subject 1:"))
nd_mark=int(input("Enter marks of subject 2:"))
rd_mark=int(input("Enter marks of subject 3:"))
total=st_mark+nd_mark+rd_mark   
if total>=120 and st_mark>=33 and nd_mark>=33 and rd_mark>=33:
    print("You have passed the exam")
else:
    print("You have failed the exam")

'''A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.'''

# Program to Detect Spam Comments

comment = input("Enter a comment: ")

# Convert to lowercase for case-insensitive checking
comment = comment.lower()

if ("make a lot of money" in comment or
    "buy now" in comment or
    "subscribe this" in comment or
    "click this" in comment):
    print("Spam detected!")
else:
    print("Not a spam comment.")

# Write a program to find whether a given username contains less than 10 characters or not.
username = input("Enter a username: ")
if len(username)<10:
    print("username contain less than 10 characters")
else:
    print("username contain more than 10 characters")

#Write a program which finds out whether a given name is present in a list or not.
li=["Harry", "Ron", "Hermione", "Draco", "Neville"]
name =input("enter the user name:")
if name in li:
 print("name is the present in the list")
else:
    print("name is not present int he lst")

'''Write a program to calculate the grade of a student from his marks from the
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F'''
# Program to Calculate Student Grade

marks = float(input("Enter your marks (0-100): "))

if marks >= 90 and marks <= 100:
    print("Grade: Ex")
elif marks >= 80 and marks < 90:
    print("Grade: A")
elif marks >= 70 and marks < 80:
    print("Grade: B")
elif marks >= 60 and marks < 70:
    print("Grade: C")
elif marks >= 50 and marks < 60:
    print("Grade: D")
elif marks >= 0 and marks < 50:
    print("Grade: F")
else:
    print("Invalid marks! Please enter marks between 0 and 100.")


#Write a program to find out whether a given post is talking about “Harry” or not.
post = input("Enter the post: ")
if "harry" in post.lower():
    print("This post is talking about Harry.")
else:
    print("This post is not talking about Harry.")