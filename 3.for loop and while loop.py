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


#sum of first N natural numbers

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#Factorial of a number

n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)

#Sum of digits of a number

n = int(input("Enter a number: "))

total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print("Sum of digits =", total)

#multiplication table generator
num = int(input("Enter the number: "))
limit = int(input("Enter the table limit: "))

print("Multiplication Table of", num)

for i in range(1, limit + 1):
    print(num, "x", i, "=", num * i)

# sum of natural numbers using while

n = int(input("Enter a number: "))

i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum =", total)

#even numbers using while

i = 2

while i <= 50:
    print(i)
    i += 2

#number guessing game 

secret_number = 7

guess = int(input("Guess the number: "))

while guess != secret_number:

    if guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")

    guess = int(input("Guess again: "))

print("Congratulations! You guessed correctly.")

#skip odd numbers using continue

for i in range(1, 11):

    if i % 2 != 0:
        continue

    print(i)

#use of PASS

for i in range(1, 6):

    if i == 3:
        pass

    print(i)

#stop a loop when a particular number is found using break

for i in range(1, 11):

    if i == 6:
        break

    print(i)
