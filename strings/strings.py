# always represented by either single quotes or double quotes.
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
x = "Hi"
print(x)

#Looping Through a String
#Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
  print(x)

#You can also get a character at any position

y = "Collins Natala"
print(y[9])

#To get the length of a string we use the len() function

y = "Collins Natala"
print(len(y))

#To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are earned!"
print("earned" in txt)
#or print only if "earned" is present:
txt = "The best things in life are earned!"
if "earned" in txt:
  print("Yes, 'earned' is present.")

#Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)
#or you can use it in an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

"""slicing strings"""
#You can return a range of characters by using the slice syntax.

# by Specifing the start index and the end index, separated by a colon, to return a part of the string.

b = "Collins Natala"
print(b[2:5])

b = "Collins Natala"
print(b[:5])

#Negative indexing
b = "Collins Natala"
print(b[-7:-2])

"""modifying strings"""

#Uppercase: This method returns the string in upper case: upper()

X = "Natala"
print(x.upper())

#Removing whitespace

a = " Natala "
print(a.strip())

#Replacing String
a = "Jatala"
print(a.replace("J", "N"))

#Spliting String
a = "Collins, Natala"
print(a.split(","))

#Concatenating string
a = "Collins"
b = "Natala"
c = a + " " + b
print(c)

"""F-Strings"""
#used to combine strings and numbers
age = 36
txt = f"My name is Collins and I am {age}"
print(txt)