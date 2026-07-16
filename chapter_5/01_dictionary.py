# Dictionary Example
info = {
    "name": "dipak",
    "age": 25,
    "country": "nepal",
    "hobbies": ["reading", "travelling", "coding"]
}

# PROPERTIES OF PYTHON DICTIONARIES 
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys.

print(info)
print(info["name"])
print(info["age"])
print(info["country"])
print(info["hobbies"])

# Update dictionary
info.update({"name": "deepak"})
print(info)

# Create student dictionary
student = {"name": "Dipak"}

# Add new items
student["age"] = 22
student["course"] = "Computer Engineering"

print(student)

# get() method
print(student.get("age"))
print(student.get("address"))              # None
print(student.get("address", "Not Found")) # Not Found

# Update existing value
student["age"] = 23
print(student)

# Update multiple values
student.update({
    "age": 24,
    "city": "Kathmandu"
})

print(student)

# Delete an item
del student["city"]
print(student)

# Remove using pop()
age = student.pop("age")

print(age)
print(student)