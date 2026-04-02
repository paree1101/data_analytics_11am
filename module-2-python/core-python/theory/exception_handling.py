# try, except 
try:
    getfile = open("my file", "r")
    getfile.write("My file for exception handling")

except IOError:
    print("Unable to open or read data in file")

else: 
    print("File opened and read successfully")

finally:
    getfile.close()
    print("File closed successfully")


# The try block contains code that may raise an exception 
# while the except block contains code that will be executed if an exception occurs.
#  In this example, we are trying to open a file in read mode and write to it, which will raise an IOError since the file cannot be opened for writing. 
# The except block catches the IOError and prints a message indicating that the file cannot be opened or read.
# The else block contains code that will be executed if no exceptions are raised in the try block. In this case, it will print a message indicating that the file was opened and read successfully.
# The finally block contains code that will be executed regardless of whether an exception was raised or not. In this example, it will close the file and print a message indicating that the file was closed successfully.

def safe_divide(numerator, denominator):
    try:
        result = numerator/denominator
        return result 
    except ZeroDivisionError:
        print("Error, cannot divide by zero.")
        return None
#Test case
numerator = int(input("Enter numerator:"))
denominator = int(input("Enter denominator:"))
print(safe_divide(numerator, denominator))

#Type your code here
import math
def square_root(number1):
    try:
        result = math.sqrt(number1)
        return result
    except ValueError:
        print("Invalid input! Please enter a positive integer or a float value.")
        return None
#Test case
number1 = float(input("Enter a number:"))
print(square_root(number1))