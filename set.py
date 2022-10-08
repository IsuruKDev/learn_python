# Set data structure - maintain unique elements inside the data structure
unique_set = {"Hello","World","Hello","111",111}
print(unique_set)

unique_set.add('World')
print(unique_set)

# hash function will be using to make uniquness inside the data structure

unique_set.remove(111)
print(unique_set)

another_set = {"bob","dana","danny","ian"}
print(unique_set.union(another_set))
print(unique_set | another_set)
print(another_set - unique_set)
print("dana" in another_set)
print("frank" not in unique_set)




