# Level 3 – Nested Loops

# Question 1:
print("Print the multiplication table from 1 to 10 using nested loops.")
for i in range (1,11):
    print(f"multiplication of the table {i}")
    for j in range (1,11):
        print(f"{i}*{j}={i*j}")
        
# Question 2:
print("Print the following pattern:")
print("*")
print("**")
print("***")
print("****")
print("*****")
for i in range (1,5):
     print("*"*i)

# Question 3:
print("Print the following pattern:")
print("*****")
print("****")
print("***")
print("**")
print("*")
for i in range(5,0,-1):
    print("*"*i)

# Question 4:
print("Print the following pattern:")
print("1")
print("12")
print("123")
print("1234")
print("12345")
for i in range(1,6):
    for j in range(1,1+i):
        print(j,end="")
    print()

# Question 5:
print("Print the following pattern:")
print("12345")
print("1234")
print("123")
print("12")
print("1")
for i in range(1,6):
    for j in range(1,6,-1):
        print(j,end="")
    print("")

# Question 6:
print("Print the following pattern:")
print("A")
print("AB")
print("ABC")
print("ABCD")
print("ABCDE")
b='ABCDE'
for i in range (1,5):
    for j in range(0,i+1):
        print(b[j],end="")
    print("")



