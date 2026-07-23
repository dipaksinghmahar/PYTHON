def avg():
    a=int(input("enter the value of a :"))
    b=int(input("enter the value of b :"))
    c=int(input("enter the value of c :"))
    d=(a+b+c)/3
    print("the average of the value is :",d)
avg()

# a function cannot be empty .So,we can write pass
def average():
    pass


# argument with function
# if a function have two argument then we should call two argument
# When we call a function with arguments without using keywords, they are called positional arguments.
def add(fname):         #fname is parameter
    print(fname + "hoina hola")
add("email")    #email is an argument
add("age")
add("cast")

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

