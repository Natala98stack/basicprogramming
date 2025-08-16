x=5
y=6
print(x>y)
#if x<y:
   #print(True)
#else:
   #print(False)

#You can always evaluate any expression in Python, and get one of two answers, True or False.
print(10>9)
print(10==9)
print(10<9)

#Running a condition in an if statement
a = 500
b = 40
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
def hakikisha_check():
    global id_number , phone_number
    id_number = "36911661"
    phone_number = "0768830532"
    print(id_number)
hakikisha_check()
input("Type in your ID: ")
input("Type in your phone number: ")
if input() not in "id_number":
    print("No match detected")
else:
    print("100% match detected")


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Checking if an object is an integer or not
x = 200
print(isinstance(x, int))

