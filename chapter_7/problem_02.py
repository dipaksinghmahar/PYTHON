# Question 1:
print("Print the numbers from 1 to 10 using a for loop.")
for i in range (1,11):
   print(i)

# Question 2:
print("Print the numbers from 10 to 1 in reverse order.")
for i in range (10,0,-1):
  print(i)
    
# Question 3:
print("Print all even numbers from 1 to 20")
for i in range(2,21,2):
    print(i)

# Question 4:
print("Print all odd numbers from 1 to 20.")
for i in range(1,20,2):
    print(i)

# Question 5:
print("Print your name 5 times using a loop.")
for i in range(1,6):
    print("dipak")

# Question 6
print("Find the sum of numbers from 1 to 100.")
sum=0
for i in range(1,101):
    sum=i+sum
    print(sum)

# Question 7:
print("Print the multiplication table of 7.")
for i in range (1,11):
    print(f"7*{i}={7*i}")

# Question 8:
print("Count how many numbers are between 1 and 100.")
count = 0  # 1. Start your counter at 0
for i in range(1, 101):
  count += 1  # 2. Add 1 to the counter for every number we see
  print(count)  # 3. Print the final total headcount

# Question 9:
print("Print every character of the string: name = Python")
name="python"
for i in name:
    print(i)

# Question 10:
print("Print numbers from 1 to 20, but stop when the number becomes 12.(Hint: break)")
for i in range (1,21):
    if i==12:
        print("stope in 12")
        break
    print(i)

