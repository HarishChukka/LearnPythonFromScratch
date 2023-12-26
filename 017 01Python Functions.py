def my_funcation():
    print("my first funcation")

my_funcation()


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_friends(name):
   print("My friedn name is "+ name)

my_friends("Naresh")
my_friends("Sathish")
my_friends("Nagaraju")

def my_friends(name,lnamee):
   print("My friedn name is "+ name + " My friedn name is "+ lnamee)

my_friends("Naresh","Raju")
# This function expects 2 arguments, but gets only 1:
#Test it
# my_friends("Naresh")

# Arbitrary Arguments, *args
print("!!!!!!!!!!!! \n")
def my_friends(*name):
   print("My friens name is "+ name[0])
   print("My friens name is "+ name[1])
   print("My friens name is "+ name[2])

my_friends("Naresh","Raju","Bala")
#my_friends("Sathish")
#my_friends("Nagaraju")

print("!!!!!!!!!!!! \n")

def my_function(name3, name2, name1):
  print("The youngest child is " + name1)
  print("The youngest child is " + name2)
  print("The youngest child is " + name3)

my_function(name2 = "Babu", name1 = "Appu", name3 = "Rani")

print("!!!!!!!!!!!! \n")

def my_function(**name):
  print("His last name is " + name["lname"])
  print("His last name is " + name["fname"])

my_function(fname = "Babu", lname = "Appu")

print("!!!!!!!!!!!! \n")
def my_function(**name):
  print(" 1 His last name is " + name["lname"])
  print(" 2 His last name is " + name["fname"])
  print(" 3 His last name is " + name["mname"])
  print(" 3 His last name is " + name["sname"])


my_function(fname = "Babu", lname = "Appu",mname="Hani",sname="harishjajd")

print("!!!!!!!!!!!! \n")
def my_function(lname,name= "Norway",):
  print(" 1 His last name is " + name +" "+lname)

my_function("Babu")
my_function("hello")
my_function(name = "Babu", lname = "Appu")

print("!!!!!!!!!!!! \n")
def my_function(calls):
  for tempz in calls:
    print(" 2 His last name is " + tempz +" ")

name=["Babu","hello","Appu","aniuman"]
my_function(name)

print("!!!!!!!!!!!! \n")
def my_function(*calls):
  return 3*calls

#print(" 2 His last name is " + tempz +" ")

name=["Babu","hello","Appu","aniuman"]
print(my_function(name))

print("!!!!!!!!!!!! \n")
def tri_recursion(k):
  if(k < 20):
    
    #result = k + tri_recursion(k +1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(3)