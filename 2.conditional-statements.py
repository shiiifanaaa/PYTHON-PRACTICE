# Check whether a number is positive,
# negative or zero

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")

elif num < 0:
    print("Negative number")

else:
    print("Zero")

#Check eligibility to vote based on age

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")

    if age >= 60:
        print("Senior citizen")

    else:
        
        print("Adult")

#EVEN OR ODD

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even")

else:
    print("The number is odd")

else:
    print("You are not eligible to vote")

#LARGEST OF THREE NUMBERS

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(a, "is the largest")

elif b > a and b > c:
    print(b, "is the largest")

elif c > a and c > b:
    print(c, "is the largest")

else:
    print("Two or more numbers are equal at the maximum")

#LEAP YEAR OR NOT

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")

elif year % 100 == 0:
    print("Not a leap year")

elif year % 4 == 0:
    print("Leap year")

else:
    print("Not a leap year")


