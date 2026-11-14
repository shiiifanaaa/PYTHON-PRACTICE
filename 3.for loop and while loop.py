# Print numbers from 1 to 10

for i in range(1, 11):
    print(i)

# Multiplication table

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Print numbers from 1 to 5

i = 1

while i <= 5:
    print(i)
    i += 1

# Break example

for i in range(1, 10):
    if i == 6:
        break
    print(i)

# Continue example

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
