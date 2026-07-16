# While lists use square brackets [], tuples use parentheses ().
# Because tuples cannot be changed, they have fewer methods than lists, which makes them slightly faster and memory-efficient.
#Accessing Items (Slicing & Indexing)

# A tuple of numbers
coordinates = (4, 5)

# A tuple of strings
fruits = ("apple", "banana", "cherry")

# A mixed tuple
user = ("Alice", 25, True)

not_a_tuple = ("apple")  # Python sees this as just a string
is_a_tuple = ("apple",)  # This is a valid tuple

fruits = ("apple", "banana", "cherry")

print(fruits[0])   # Output: apple
print(fruits[-1])  # Output: cherry (the last item)
print(fruits[0:2]) # Output: ('apple', 'banana')

numbers = (1, 2, 3, 2, 4, 2)

# 1. count() - Counts how many times an item appears
print(numbers.count(2))  # Output: 3

# 2. index() - Finds the position of the first occurrence of an item
print(numbers.index(4))  # Output: 4