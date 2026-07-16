# ==========================
# PYTHON SETS - ALL OPERATIONS
# ==========================

# Properties of Sets
# 1. Unordered
# 2. Mutable
# 3. No duplicate values
# 4. Unindexed

# Create a set
fruits = {"apple", "banana", "mango"}
print("Original Set:", fruits)

# Empty set
empty_set = set()
print("Empty Set:", empty_set)

# Duplicate values are removed automatically
numbers = {1, 2, 2, 3, 4, 4, 5}
print("No Duplicates:", numbers)

# Add an element
fruits.add("orange")
print("After add():", fruits)

# Add multiple elements
fruits.update(["grapes", "kiwi"])
print("After update():", fruits)

# Check membership
print("apple" in fruits)
print("pineapple" in fruits)

# Length
print("Length:", len(fruits))

# Remove an element
fruits.remove("banana")
print("After remove():", fruits)

# Discard (does not raise error if element doesn't exist)
fruits.discard("watermelon")
print("After discard():", fruits)

# Pop (removes a random element)
item = fruits.pop()
print("Popped Item:", item)
print("After pop():", fruits)

# Copy a set
new_fruits = fruits.copy()
print("Copied Set:", new_fruits)

# Union
A = {1, 2, 3}
B = {3, 4, 5}
print("Union:", A.union(B))
print("Union (|):", A | B)

# Intersection
print("Intersection:", A.intersection(B))
print("Intersection (&):", A & B)

# Difference
print("Difference:", A.difference(B))
print("Difference (-):", A - B)

# Symmetric Difference
print("Symmetric Difference:", A.symmetric_difference(B))
print("Symmetric Difference (^):", A ^ B)

# Subset
C = {1, 2}
print("Is C subset of A?", C.issubset(A))

# Superset
print("Is A superset of C?", A.issuperset(C))

# Disjoint
D = {6, 7}
print("Are A and D disjoint?", A.isdisjoint(D))

# Loop through a set
print("Looping through fruits:")
for fruit in new_fruits:
    print(fruit)

# Clear the set
new_fruits.clear()
print("After clear():", new_fruits)

# Frozen Set (Immutable)
frozen = frozenset([10, 20, 30])
print("Frozen Set:", frozen)