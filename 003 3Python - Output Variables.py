
#Python - Output Variables
print("\n Python - Output Variables ")

x = "If you can't fly, then run."
print(x)

x = "If you can't run, then walk. "
y = "If you can't walk, then crawl."
z = " But whatever you do,"
print(x, y, z)

x = " you have to keep moving forward "
y = ".. "
z = "\n awesome"
print(x + y + z)


x = 5
y = 10
print(x + y)

#  when you try to combine a string and a number with the + operator,
# Python will give you an error:

x = 5
y = "John"
#print(x + y)

"""The best way to output multiple variables in the print() function 
is to separate them with commas,
 which even support different data types:"""

x = 5
y = "John"
print(x, y)