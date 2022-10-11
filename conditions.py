# 0-34 W
# 35-54 S
# 55-64 C
# 65-74 B
# 75 and above


x = 64
result = None

if x>= 79:
    print("You are passed for PTE with good values")
else:
    print("Not enough score for level overall 8 similar to IELTS")

if x>= 49:
    result = "Pass"
else:
    result = "Fail"

print(result)
print("\n\n")

marks = 75
grade = None

if marks > 100 or marks < 0:
    print("Invalid marks")
    exit()

if marks<35:
    grade = 'W'
elif marks >= 35 and marks <55:
    grade = 'S'
elif marks >= 55 and marks <65:
    grade = 'C'
elif marks >=65 and marks <75:
    grade = 'B'
else:
    grade = 'A'

print(grade)

height = 140

job = "Security" if height > 150 else "Labor"

print(job)


