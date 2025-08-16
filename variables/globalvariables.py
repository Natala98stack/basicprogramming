#Variables are containers for storing data values.
#A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)
y = int(3)
z = float(3)
print(x,y,z)

#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

#Snake case variable name

my_variable_name = "John"
my_var_name = "Collins"

"""Multiple variables"""
x,y,z = "Mango", "Oranges", "Banana"
print(x)
print(y)
print(z)
print(x,y,z)

x = y = z = "Oranges"
print(y)

#Unpacking a collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#local scope variables
def score():
    affordable_amount = 120000
    print(affordable_amount, "KES")

score()



# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome" #created a variable
y = " language"
z = " to learn"
def myfunc(): #funcion defination
    global x , y, z
    x = "What "
    y = "a game "
    z = "that was!"
    print(x + y)
    print(x + y + z)
    print("python is an " + x + " " + y + " " + z)

myfunc() #calls myfunc()

print(x+y+z)
print(y, z)