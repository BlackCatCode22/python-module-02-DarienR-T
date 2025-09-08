# Write a Python program that uses nested if statements (nested decisions) to get three integers from the user
# and outputs the largest of the three. Name your script: largest_of_3.py

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")