# PYTHON

## WHAT IS PROGRAMMING?

Just like we use English or Nepali to communicate with each other, we use a programming language like Python to communicate with computers.

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

print(word[:7])
print(word[0:])
```

Output:

```text
amazing
amazing
```

---

# STRING FUNCTIONS

Assume:

```python
str = "Dipak"
```

### 1. len()

Returns the length of the string.

```python
print(len(str))
```

Output:

```text
5
```

---

### 2. endswith()

Checks whether a string ends with a given value.

```python
print(str.endswith("pak"))
```

Output:

```text
True
```

---

### 3. count()

Counts the occurrences of a character.

```python
print(str.count("p"))
```

Output:

```text
1
```

---

### 4. capitalize()

Capitalizes the first character.

```python
print(str.capitalize())
```

Output:

```text
Dipak
```

---

### 5. find()

Returns the index of the first occurrence of a substring.

```python
print(str.find("pa"))
```

Output:

```text
2
```

---

### 6. replace()

Replaces a substring with another substring.

```python
print(str.replace("p", "b"))
```

Output:

```text
Dibak
```

---

# ESCAPE SEQUENCE CHARACTERS

Escape sequence characters begin with a backslash (`\`) and represent special characters.

| Escape Sequence | Meaning      |
| --------------- | ------------ |
| \n              | New Line     |
| \t              | Tab Space    |
| \               | Backslash    |
| '               | Single Quote |
| "               | Double Quote |

Example:

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

---

# SUMMARY

## Chapter 1

* Introduction to Python
* Modules
* PIP
* Comments
* Python as a Calculator

## Chapter 2

* Variables
* Data Types
* Operators
* Type Casting
* Input Function

## Chapter 3

* Strings
* String Indexing
* String Slicing
* String Functions
* Escape Sequence Characters


#SUN 21 JUN
