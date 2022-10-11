# tuple

isuruk = ("Isuru Kularathna", 38, "Sri Lanka","Malaysia")

print(isuruk)
print(type(isuruk))

print()

print("Full Name : ",isuruk[0])
print("Age : ",isuruk[1])
print("Citizen : ",isuruk[2])
print("Work At : ",isuruk[3])
#print("Full Name : ",isuruk[0])
print()

name, age, origin, live = isuruk
print(name, age, origin,live)

print("\n\n")

# slicing

x = ['a','b','c','d','e']
y = x[2:]
z = x[:2]
z1 = x[-1]
z2 = x[:-1]
z3 = x[1:-1]
print(y,z,z1,z2,z3)
print(len(x))

print("\n\n")

greeting = "Hello World"
print(greeting[0:5])
print(greeting[6:])