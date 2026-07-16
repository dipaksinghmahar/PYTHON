# ============================================
# Python Dictionary & Set Practice Questions
# ============================================

# 1. Hindi to English Dictionary Lookup
words = {
    "namaste": "Hello",
    "pani": "Water",
    "kitab": "Book",
    "ghar": "House",
    "dost": "Friend"
}

word = input("Enter a Hindi word: ")
print("Meaning:", words.get(word, "Word not found"))

print("\n" + "="*40)

# 2. Input 8 numbers and display unique numbers
numbers = set()

print("Enter 8 numbers:")
for i in range(8):
    num = int(input(f"Number {i+1}: "))
    numbers.add(num)

print("Unique Numbers:", numbers)

print("\n" + "="*40)

# 3. Can a set contain 18 (int) and '18' (str)?
s = {18, "18"}
print("Set containing 18 and '18':", s)
print("Answer: Yes, because one is an integer and the other is a string.")

print("\n" + "="*40)

# 4. Length of the following set
s = set()
s.add(20)
s.add(20.0)
s.add("20")

print("Set:", s)
print("Length of set:", len(s))
print("Answer: Length is 2 because 20 and 20.0 are considered equal.")

print("\n" + "="*40)

# 5. Type of s = {}
s = {}
print("Type of s:", type(s))
print("Answer: {} creates an empty dictionary, not a set.")

print("\n" + "="*40)

# 6. Favorite Language Dictionary
fav_lang = {}

print("Enter details of 4 friends:")
for i in range(4):
    name = input("Friend Name: ")
    language = input("Favorite Language: ")
    fav_lang[name] = language

print("Favorite Languages Dictionary:")
print(fav_lang)

print("\n" + "="*40)

# 7. Duplicate Names
print("Q7 Answer:")
print("If two friends have the same name, the second entry overwrites the first because dictionary keys must be unique.")

print("\n" + "="*40)

# 8. Duplicate Languages
print("Q8 Answer:")
print("If two friends have the same favorite language, nothing happens because dictionary values can be duplicated.")

print("\n" + "="*40)

# 9. Can you change values inside a list?
my_list = [10, 20, 30]
print("Original List:", my_list)

my_list[1] = 50

print("Modified List:", my_list)
print("Answer: Yes, lists are mutable.")