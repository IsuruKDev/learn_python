x = [12,454,252,-1]

print(x, x[0], x[1], x[2], x[3])

# add element at the tail of the list
x.append(100)
print(x)

# add element in middle of the list
x.insert(1,500)
print(x)

# remove element from the list
x.remove(-1)
print(x)

# remove element from the selected index
x.pop(3)
print(x)

# add two lists
y = [0,20,40,60,80,100]
z = x+y
print(z)

print(0 in z)
print(101 not in z)

