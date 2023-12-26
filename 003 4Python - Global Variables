
x = " If you can't run, then walk.."

def myfunc():
  print("\n If you can't fly, then run. \n " + x)

myfunc()

#Create a variable inside a function, with the same name as the global variable
"""
If you create a variable with the same name inside a function, this variable will be local,
 and can only be used inside the function. The global variable with the same name 
 will remain as it was, global and with the original value.

"""

x = " Global variable outside a function"

def myfunc():
  print("\n ")
  x = "variable inside a function"
  print(" Variable form  " + x)

myfunc()

print("Variable form " + x)

"""
The global Keyword
Normally, when you create a variable inside a function, 
that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.

"""

def myfunc():
  global x
  x = "global variable inside a function"

myfunc()

print("Hello " + x)

"""
Use the global keyword if you want to change a global variable inside a function.

"""
print("\n Example 5")
x = "variable outside a function"
print(x)

def myfunc():
  global x
  x = "global variable inside a function"
  print("Inside the function " + x)

myfunc()

print("hello " + x)