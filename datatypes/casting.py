"""Casting is the process of explicitly converting one data type into another using built-in functions.
Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string
literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string
represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals"""

#Numeric Casting: Allows you to convert btwn int(), float() and complex() types

x = int(4.890)  # converts float to int
print(x)
y = float(34)  # converts int to float
print(y)
z = complex(3) # converts int to complex
print(z)

#String Casting: converts numbers or oter types to strings

a = str(100)
print(a)
b = str(3.56)
print(b)

#Note: if a str contains a valid number you can cast it

num = int("42")
print(num)
price = float("32.67")
print(price)

# Value Error: it's the error you'll get when a str isn't properly formatted ie bad = int("hello") hello isn't an int

"""Use case scenarios"""

age = int(input("Enter Your Age:"))
print(age)

# Ensure to review casting collections after going through lists, tuples, sets and dictionaries.







