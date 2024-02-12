x = int(input("Enter a number x: "))
y = int(input("Enter a number y: "))

try:
    z = x / y
    print(z)

except ZeroDivisionError:
    print("zero division error,don't divide by zero")
