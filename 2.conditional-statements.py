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

else:
    print("You are not eligible to vote")
