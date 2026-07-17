# PYTHON

## WHAT IS PROGRAMMING?

Just like a we use English or Nepali to communicate with each other, we use a programming language like Python to communicate with computers.


Programming is the process of giving instructions to a computer to perform various tasks.

---

## WHAT IS PYTHON?

Python is a simple and easy-to-understand programming language that feels like reading simple English. Its readable syntax makes it beginner-friendly and easy to learn.

---

## FEATURES OF PYTHON

* Easy to understand and learn
* Less development time
* Free and Open Source
* High-Level Language
* Portable (Works on Windows, Linux, and macOS)
* Fun and productive to work with

---

## INSTALLATION OF PYTHON

Python can be easily installed from the official website:

https://www.python.org

Download the appropriate version for your operating system and run the installer to complete the setup.

---

# CHAPTER 1: MODULES, COMMENTS AND PIP

## FIRST PYTHON PROGRAM

Create a file named `hello.py` and write:

```python
print("Hello World")
```

Run the file using:

```bash
python hello.py
```

Output:

```text
Hello World
```

---

## MODULES

A module is a file containing code written by someone else (or yourself) that can be imported and used in a Python program.

Example:

```python
import math
```

---

## PIP

PIP is the package manager for Python. It is used to install external modules.

Example:

```bash
pip install flask
```

---

## TYPES OF MODULES

### 1. Built-in Modules

These modules are already installed with Python.

Examples:

* os
* random
* math

### 2. External Modules

These modules must be installed using pip.

Examples:

* flask
* tensorflow
* numpy

---

## USING PYTHON AS A CALCULATOR

Open the terminal and type:

```bash
python
```

This opens the Python REPL (Read-Evaluate-Print Loop).

Example:

```python
>>> 5 + 5
10
>>> 10 * 3
30
```

---

## COMMENTS

Comments are used to explain code and are ignored during program execution.

### Single-Line Comment

```python
# This is a single-line comment
```

### Multi-Line Comment

```python
"""
This is an example
of a multi-line comment
"""
```

---

# CHAPTER 2: VARIABLES AND DATA TYPES

## VARIABLES

A variable is the name given to a memory location used to store data.

Example:

```python
a = 30
name = "Dipak"
c = 71.22
```

Where:

* `a` is an integer variable
* `name` is a string variable
* `c` is a floating-point variable

---

## DATA TYPES

Python automatically identifies the data type of variables.

### Main Data Types

1. Integer (`int`)
2. Float (`float`)
3. String (`str`)
4. Boolean (`bool`)
5. None (`NoneType`)

Example:

```python
a = 71
b = 88.44
name = "Dipak"
```

---

## RULES FOR CHOOSING IDENTIFIERS

* Can contain letters, digits, and underscores.
* Must start with a letter or underscore.
* Cannot start with a digit.
* Spaces are not allowed.

Valid Examples:

```python
dipak
one8
seven
_seven
```

Invalid Examples:

```python
8dipak
my name
```

---

## OPERATORS IN PYTHON

### Arithmetic Operators

```python
+
-
*
/
%
**
//
```

### Assignment Operators

```python
=
+=
-=
*=
/=
```

### Comparison Operators

```python
==
!=
>
<
>=
<=
```

### Logical Operators

```python
and
or
not
```

---

## TYPE() FUNCTION

The `type()` function is used to determine the data type of a variable.

Example:

```python
a = 31
print(type(a))
```

Output:

```python
<class 'int'>
```

Example:

```python
b = "31"
print(type(b))
```

Output:

```python
<class 'str'>
```

---

## TYPE CASTING

Type casting means converting one data type into another.

Examples:

```python
str(31)
```

Output:

```python
"31"
```

```python
int("32")
```

Output:

```python
32
```

```python
float(32)
```

Output:

```python
32.0
```

---

## INPUT() FUNCTION

The `input()` function is used to take input from the keyboard.

Example:

```python
name = input("Enter your name: ")
print(name)
```

**Note:** The input function always returns a string.

---

# CHAPTER 3: STRINGS

## STRINGS

A string is a sequence of characters enclosed within quotation marks.

Examples:

```python
a = 'Dipak'
b = "Dipak"
c = '''Dipak'''
```

---

## STRING INDEXING

Example:

```python
name = "Dipak"
```

| Character | D | i | p | a | k |
| --------- | - | - | - | - | - |
| Index     | 0 | 1 | 2 | 3 | 4 |

Negative Indexing:

| Character | D  | i  | p  | a  | k  |
| --------- | -- | -- | -- | -- | -- |
| Index     | -5 | -4 | -3 | -2 | -1 |

---

## STRING SLICING

Syntax:

```python
string[start:end]
```

Example:

```python
name = "Dipak"
print(name[1:4])
```

Output:

```text
ipa
```

---

## SLICING WITH SKIP VALUE

Example:

```python
word = "amazing"
print(word[1:6:2])
```

Output:

```text
mzn
```

---

## ADVANCED SLICING

```python
word = "amazing"
word[1: 6: 2] # "mzn"
Other advanced slicing techniques:
Word = "amazing"
Word = [:7] # word [0:7] – 'amazing'
Word = [0:] # word [0:7] – 'amazing'
STRING FUNCTIONS
Some of the commonly used functions to perform operations on or manipulate strings
are as follows. Let us assume there is a string ‘str’ as follows:
str = 'harry'
Now when operated on this string ‘str’, these functions do the following:
1. len () function – This function returns the length of the strings.
str = "harry"
print(len(str)) # Output: 5
2. String.endswith("rry") – This function_ tells whether the variable string ends with
the string "rry" or not. If string is "harry", it returns true for "rry" since Harry ends
with rry.
str = "harry"
print(str.endswith("rry")) # Output: True
3. string.count("c") – counts the total number of occurrences of any character.
str = "harry"
count = str.count("r")
print(count) # Output: 2
4. the first character of a given string.
str = "harry"
capitalized_string = str.capitalize()
print(capitalized_string) # Output: "Harry"
5. string.find(word) – This function friends a word and returns the index of first
occurrence of that word in the string.
str = "harry"
14
index = str.find("rr")
print(index) # Output: 2
6. string.replace (old word, new word ) – This function replace the old word with
new word in the entire string.
str = "harry"
replaced_string = str.replace("r", "l")
print(replaced_string) # Output: "hally"
ESCAPE SEQUENCE CHARACTERS
Sequence of characters after backslash "\" → Escape Sequence characters
Escape Sequence characters comprise of more than one character but represent one
character when used within the strings.

```
CHAPTER 4 – LISTS AND TUPLES

## Tuple Methods in Python

```python
a = (1, 7, 2)
### 1. `count()`
Returns the number of times a specified value appears in the tuple.

```python
print(a.count(1))
```

**Output:**
```python
1
```

**Explanation:**
- `a.count(1)` counts how many times `1` appears in the tuple.
- Here, `1` appears **1 time**.

---

### 2. `index()`
Returns the index (position) of the first occurrence of a specified value.

```python
print(a.index(1))
```

**Output:**
```python
0
```

**Explanation:**
- `a.index(1)` returns the index of the first `1`.
- Since indexing starts from **0**, the result is **0**.

---

### Example

```python
a = (1, 7, 2, 1)

print(a.count(1))   # 2
print(a.index(1))   # 0
```

**Output:**
```python
2
0
```

**Summary**

| Method | Purpose | Example |
|--------|---------|---------|
| `count(x)` | Counts how many times `x` appears | `a.count(1)` |
| `index(x)` | Returns the first index of `x` | `a.index(1)` |

CHAPTER 5 – DICTIONARY & SETS
Dictionary is a collection of keys-value pairs.

# Dictionaries in Python

A **dictionary** is a collection of **key-value pairs**.

## Syntax

```python
a = {
    "key": "value",
    "harry": "code",
    "marks": 100,
    "list": [1, 2, 9]
}

print(a["key"])   # Output: value
print(a["list"])  # Output: [1, 2, 9]
```

---

## Properties of Dictionaries

1. **Unordered** – Items are not stored in a fixed order.
2. **Mutable** – You can add, update, or remove items.
3. **Indexed by Keys** – Values are accessed using keys, not numeric indexes.
4. **No Duplicate Keys** – Each key must be unique.

---

## Dictionary Methods

```python
a = {
    "name": "Harry",
    "from": "India",
    "marks": [92, 98, 96]
}
```

### 1. `items()`
Returns all key-value pairs.

```python
print(a.items())
```

**Output:**
```python
dict_items([('name', 'Harry'), ('from', 'India'), ('marks', [92, 98, 96])])
```

---

### 2. `keys()`
Returns all keys.

```python
print(a.keys())
```

**Output:**
```python
dict_keys(['name', 'from', 'marks'])
```

---

### 3. `update()`
Adds or updates key-value pairs.

```python
a.update({"friend": "Rohan"})
print(a)
```

---

### 4. `get()`
Returns the value of a specified key.

```python
print(a.get("name"))
```

**Output:**
```python
Harry
```

---

## Summary

| Method | Purpose | Example |
|---------|---------|---------|
| `items()` | Returns all key-value pairs | `a.items()` |
| `keys()` | Returns all keys | `a.keys()` |
| `update()` | Adds/updates items | `a.update({"age": 20})` |
| `get()` | Returns value of a key | `a.get("name")` |

---

# Sets in Python

A **set** is a collection of **unique (non-repetitive) elements**.

## Syntax

```python
s = set()   # Empty set

s.add(1)
s.add(2)

# OR

s = {1, 2}
```

---

## Properties of Sets

1. **Unordered** – Elements have no fixed order.
2. **Unindexed** – Cannot access elements using an index.
3. **Mutable** – You can add or remove elements.
4. **No Duplicate Values** – Duplicate elements are automatically removed.

Example:

```python
s = {1, 2, 2, 3, 3, 4}
print(s)
```

**Output:**

```python
{1, 2, 3, 4}
```

---

## Set Operations

```python
s = {1, 8, 2, 3}
```

### 1. `len()`
Returns the number of elements.

```python
print(len(s))
```

**Output:**
```python
4
```

---

### 2. `remove()`
Removes a specified element.

```python
s.remove(8)
print(s)
```

---

### 3. `pop()`
Removes and returns a random element.

```python
print(s.pop())
```

---

### 4. `clear()`
Removes all elements.

```python
s.clear()
print(s)
```

**Output:**
```python
set()
```

---

### 5. `union()`
Returns a new set containing elements from both sets.

```python
s = {1, 8, 2, 3}

print(s.union({8, 11}))
```

**Output:**
```python
{1, 2, 3, 8, 11}
```

---

### 6. `intersection()`
Returns common elements from both sets.

```python
s = {1, 8, 2, 3}

print(s.intersection({8, 11}))
```

**Output:**
```python
{8}
```

---

## Summary

| Method | Purpose | Example |
|---------|---------|---------|
| `len(s)` | Returns number of elements | `len(s)` |
| `remove(x)` | Removes an element | `s.remove(8)` |
| `pop()` | Removes a random element | `s.pop()` |
| `clear()` | Removes all elements | `s.clear()` |
| `union()` | Combines two sets | `s.union({8,11})` |
| `intersection()` | Finds common elements | `s.intersection({8,11})` |

CHAPTER 6 – CONDITIONAL EXPRESSION
# Conditional Statements in Python

Conditional statements allow a program to make **decisions** based on conditions.

### Real-Life Examples
- 🎮 Play PUBG **if** today is Sunday.
- 🍦 Order ice cream **if** the weather is sunny.
- 🥾 Go hiking **if** parents allow.

Similarly, Python uses **if, elif, and else** to make decisions.

---

# `if`, `elif`, and `else`

## Syntax

```python
if condition1:
    # Code executes if condition1 is True

elif condition2:
    # Code executes if condition2 is True

else:
    # Code executes if all conditions are False
```

---

## Example 1

```python
a = 22

if a > 9:
    print("Greater")
else:
    print("Lesser")
```

**Output:**

```python
Greater
```

---

## Example 2

```python
age = 18

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")
```

**Output:**

```python
You can vote.
```

---

# Relational Operators

Relational operators compare two values and return **True** or **False**.

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

### Example

```python
a = 10
b = 20

print(a == b)   # False
print(a < b)    # True
print(a >= b)   # False
```

---

# Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | True if **both** conditions are True | `a > 5 and b < 10` |
| `or` | True if **at least one** condition is True | `a > 5 or b < 10` |
| `not` | Reverses the result | `not(a > 5)` |

### Example

```python
age = 20
citizen = True

print(age >= 18 and citizen)   # True
print(age < 18 or citizen)     # True
print(not citizen)             # False
```

---

# `elif` Statement

`elif` means **"else if"**.

It checks another condition if the previous condition is False.

### Syntax

```python
if condition1:
    # Code

elif condition2:
    # Code

elif condition3:
    # Code

else:
    # Code
```

### Example

```python
marks = 75

if marks >= 90:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

else:
    print("Need Improvement")
```

**Output:**

```python
Grade B
```

---

# Important Notes

- There can be **any number of `elif` statements**.
- The **first True condition** is executed.
- The `else` block runs **only if all conditions are False**.
- `else` is **optional**.

---

# Quick Quiz

### Write a program to print **"Yes"** if the user's age is **18 or above**.

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Yes")
else:
    print("No")
```

### Example Output

```
Enter your age: 20
Yes
```

---

# Summary

| Statement | Purpose |
|-----------|---------|
| `if` | Executes code if a condition is True |
| `elif` | Checks another condition if the previous one is False |
| `else` | Executes when all conditions are False |
| Relational Operators | Compare values (`==`, `>`, `<`, `>=`, `<=`, `!=`) |
| Logical Operators | Combine conditions (`and`, `or`, `not`) |



