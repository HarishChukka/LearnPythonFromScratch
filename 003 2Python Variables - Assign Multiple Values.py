print("\nMany Values to Multiple Variables")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
print("\nOne Value to Multiple Variables")
x = y = z = "Orange"
print(x)
print(y)
print(z)

print("\n Unpack a Collection")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(type(fruits))
print(x)
print(y)
print(z)