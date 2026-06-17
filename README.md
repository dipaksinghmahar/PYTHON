# PYTHON
WHAT IS PROGRAMMING?
Just like we use Hindi or English to communicate with each other, we use a
programming language like Python to communicate with the computer.
Programming is a way to instruct the computer to perform various tasks.
WHAT IS PYTHON?
Python is a simple and easy to understand language which feels like reading simple
English. This Pseudo code nature is easy to learn and understandable by beginners.
FEATURES OF PYTHON
• Easy to understand = Less development time
• Free and open source
• High level language
• Portable: Works on Linux / Windows / Mac.
• Fun to work with!
INSTALLATION
Python can be easily installed from python.org. When you click on the download
button, python can be installed right after you complete the setup by executing the file
for your platform.

CHAPTER 1 – MODULES, COMMENTS & PIP
Let’s write our very first python program. Create a file called hello.py and paste the
below code in it.
print("hello world") # print is a function (more later)
Execute this file (.py file) by typing python hello.py and you will see Hello World printed
on the screen.
MODULES
A module is a file containing code written by somebody else (usually) which can be
imported and used in our programs.
PIP
Pip is the package manager for python. You can use pip to install a module on your
system.
pip install flask # Installs Flask Module
TYPES OF MODULES
There are two types of modules in Python.
1. 2. Built in Modules (Preinstalled in Python)
External Modules (Need to install using pip)
Some examples of built in modules are os, random etc.
Some examples of external modules are tensorflow, flask etc.
USING PYTHON AS A CALCULATOR
We can use python as a calculator by typing “python” + ↵ on the terminal.
This opens REPL or Read Evaluate Print Loop.
COMMENTS
Comments are used to write something which the programmer does not want to
execute. This can be used to mark author name, date etc.
TYPES OF COMMENTS
There are two types of comments in python.
7
1. Single Line Comments: To write a single line comment just add a ‘#’ at the start
of the line.
# This is a Single-Line Comment
2. Multiline Comments: To write multi-line comments you can use ‘#’ at each line
or you can use the multiline string (""" """)
"""This is an amazing
example of a Multiline

CHAPTER 2 – VARIABLES AND DATATYPE
A variable is the name given to a memory location in a program. For example.
a= 30 # variables = container to store a value.
b= "harry" # keywords = reserved words in python
c= 71.22 # identifiers = class/function/variable name
DATA TYPES
Primarily these are the following data types in Python:
1. Integers
2. Floating point numbers
3. Strings
4. Booleans
5. None
Python is a fantastic language that automatically identifies the type of data for us.
a= 71 # identifies a as class <int>
b=88.44 # identifies b as class <float>
name= "harry" # identifies name as class <str>
RULES FOR CHOOSING AN IDENTIFIER
• A variable name can contain alphabets, digits, and underscores.
• A variable name can only start with an alphabet and underscores.
• A variable name can’t start with a digit.
• No while space is allowed to be used inside a variable name.
Examples of a few variable names are: harry, one8, seven, _seven etc.
OPERATORS IN PYTHON
Following are some common operators in python:
1. Arithmetic operators: +, -
, *, / etc.
2. Assignment operators: =, +=, -= etc.
3. Comparison operators: ==, >, >=, <, != etc.
4. Logical operators: and, or, not.
10
TYPE() FUNCTION AND TYPECASTING.
type() function is used to find the data type of a given variable in python.
a = 31
type(a) # class <int>
b = "31"
type (b) # class <str>
A number can be converted into a string and vice versa (if possible)
There are many functions to convert one data type into another.
str(31) =>"31" # integer to string conversion
int("32") => 32 # string to integer conversion
float(32) => 32.0 # integer to float conversion
… and so, on
Here "31" is a string literal and 31 a numeric literal.
INPUT () FUNCTION
This function allows the user to take input from the keyboard as a string.
A = input ("enter name") # if a is "harry", the user entered harry
It is important to note that the output of input is always a string (even is a number is
entered).

CHAPTER 3 – STRINGS
String is a data type in python.
String is a sequence of characters enclosed in quotes.
We can primarily write a string in these three ways.
a ='harry' # Single quoted string
b = "harry" # Double quoted string
c = '''harry''' # Triple quoted string
STRING SLICING
A string in python can be sliced for getting a part of the strings.
Consider the following string:
The index in a sting starts from 0 to (length -1) in Python. In order to slice a string, we use
the following syntax:
Negative Indices: Negative indices can also be used as shown in the figure above. -1
corresponds to the (length - 1) index, -2 to (length - 2).
13
SLICING WITH SKIP VALUE
We can provide a skip value as a part of our slice like this:
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
15
