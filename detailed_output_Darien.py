# Code up a PythonProgram that uses a function to create a detailed output message to the user
# after finding the largest of three numbers.

# Define function with logic to find the largest integer
def largestOfThree(num1, num2, num3):
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
    return largest

# User input
while 1:
    try:
        num1 = int(input("Enter the first integer: "))
    except Exception as exceptionMsg:
        print("Input not an integer, try again, message: ", exceptionMsg)
    else:
        break

while 1:
    try:
        num2 = int(input("Enter your second integer: "))
    except Exception as exceptionMsg:
        print("Input not an integer, try again, message: ", exceptionMsg)
    else:
        break
while 1:
    try:
        num3 = int(input("Enter the third integer: "))
    except Exception as exceptionMsg:
        print("Input not an integer, try again, message: ", exceptionMsg)
    else:
        break

# Function call
largest = largestOfThree(num1, num2, num3)

# Output
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")
print(f"The first integer you inputted was {num1}.")
print(f"The second integer you inputted was {num2}.")
print(f"The third integer you inputted was {num3}.")
quit()
