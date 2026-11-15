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

#NESTED IF......

#CHECK POSITIVE NUMBER AND THEN EVEN OR ODD

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")

    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

elif num < 0:
    print("Negative number")

else:
    print("Number is zero")


#VOTING ELIGIBILIY AND CITIZENSHIP

age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ")

if age < 0:
    print("Invalid age")

elif age >= 18 and citizen == "yes":
    print("You are eligible to vote")

else:
    print("You are not eligible to vote")

#LARGEST OF THREE NUMBERS

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b:
    if a >= c:
        print(a, "is the largest")
    else:
        print(c, "is the largest")

else:
    if b >= c:
        print(b, "is the largest")
    else:
        print(c, "is the largest")

#USERNAME AND PASSWORD VERIFICATION

correct_username = "shifana"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username:
    if password == correct_password:
        print("Login successful!")
    else:
        print("Incorrect password")

else:
    print("Invalid username")


#ADMISSION ELIGIBILITY USING MARKS

maths = int(input("Enter Mathematics marks: "))
physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))

if (maths < 0 or maths > 100 or
    physics < 0 or physics > 100 or
    chemistry < 0 or chemistry > 100):

    print("Invalid marks")

else:
    total = maths + physics + chemistry

    print("Total marks:", total)

    if maths >= 60 and physics >= 50 and chemistry >= 50 and total >= 180:
        print("Eligible for admission")

    else:
        print("Not eligible for admission")

#DIVISIBILITY BY 2 AND 3

num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")

elif num % 2 == 0:
    print("Divisible only by 2")

elif num % 3 == 0:
    print("Divisible only by 3")

else:
    print("Not divisible by 2 or 3")

#ELECTRICITY BILL CALCULATOR

units = int(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units")

elif units <= 100:
    bill = units * 2
    print("Electricity bill: Rs.", bill)

elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)
    print("Electricity bill: Rs.", bill)

elif units <= 300:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
    print("Electricity bill: Rs.", bill)

else:
    bill = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)
    print("Electricity bill: Rs.", bill)

#MENU BASED CALCULATOR

print("====== CALCULATOR ======")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", a + b)

elif choice == 2:
    print("Result:", a - b)

elif choice == 3:
    print("Result:", a * b)

elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Division by zero is not allowed")

else:
    print("Invalid choice")


