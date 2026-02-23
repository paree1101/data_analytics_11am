### Functions
# Functions are reusable blocks of code that perform a specific task. They allow us to break our code into smaller, more manageable pieces, and they can be called multiple times throughout our program.
# The syntax for defining a function in Python is:
# def function_name(parameters):
#     # code to execute
#     return value  # optional
# The function_name is the name of the function, and parameters are the inputs that the function can take. The code block inside the function is executed when the function is called, and the return statement is used to return a value from the function (if needed).
# Example of a simple function
def greet(name):
    return f"Hello, {name}!"  # This function takes a name as input and returns a greeting message  

# Calling the function
print(greet("Alice"))  # Output: Hello, Alice! (the function is called with the argument "Alice", and it returns the greeting message)

# Functions can also have default parameter values, which are used when the caller does not provide a value for that parameter
def greet(name="World"):
    return f"Hello, {name}!"  # This function has a default value for the name parameter, which is "World"  

# Calling the function without an argument will use the default value
print(greet())  # Output: Hello, World! (the function is called without an argument, so it uses the default value "World" for the name parameter) 

# Functions can also take multiple parameters
def add(a, b):
    return a + b  # This function takes two parameters, a and b, and returns their sum

print(add(3, 5))  # Output: 8 (the function is called with the arguments 3 and 5, and it returns their sum, which is 8)

# Functions can also return multiple values using tuples
def get_coordinates():
    x = 10
    y = 20
    return x, y  # This function returns two values, x and y, as a tuple

coordinates = get_coordinates()  # The function is called and the returned tuple is stored in the variable coordinates
print(coordinates)  # Output: (10, 20) (the coordinates are printed as a tuple)
print(coordinates[0])  # Output: 10 (the first value in the tuple, which is x, is accessed and printed)
print(coordinates[1])  # Output: 20 (the second value in the tuple, which is y, is accessed and printed)

# Default functions in python
print()
len()
sorted()
sum()
max()
min()

# sorted() function vs sort() method
my_list = [3, 1, 4, 1, 5]
# Using sorted() function
sorted_list = sorted(my_list)  # This creates a new sorted list and does not modify the original list
print(sorted_list)  # Output: [1, 1, 3, 4, 5] (the sorted list is printed)
print(my_list)  # Output: [3, 1, 4, 1, 5] (the original list remains unchanged)

# Using sort() method
my_list.sort()  # This sorts the original list in place and does not return a new list
print(my_list)  # Output: [1, 1, 3, 4, 5] (the original list is now sorted)

# Example for setting param with default value

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)
isGoodRating()
isGoodRating(10) # Output: this album sucks it's rating is 4
                          # this album is good its rating is 10



# Function withoiut return statement
def MJ():
    print("Michael Jackson is the King of Pop")  # This function prints a message but does not return any value

# Function with no body
def empty_function():
    pass  # The pass statement is used as a placeholder for an empty function body, allowing the function to be defined without any code inside it
print(empty_function())  # Output: None (the function is called, but since it does not return any value, it returns None by default)

# Using loops inside functions
def print_numbers(n):
    for i in range(n):
        print(i)  # This function takes a number n as input and prints the numbers from 0 to n-1 using a for loop  
print_numbers(5)  # Output: 0 1 2 3 4 (the function is called with the argument 5, and it prints the numbers from 0 to 4)  

def printStuff(Stuff):
    for i, s in enumerate(Stuff):
        print(f"Index: {i}, Value: {s}")  # This function takes a list called Stuff as input and uses a for loop with enumerate() to print the index and value of each element in the list
album_ratings = [5, 4, 3, 5, 2]
printStuff(album_ratings)  # Output: Index: 0, Value: 5 ... Index: 4, Value: 2 (the index and value of each element in the album_ratings list are printed)

# Collecting arguments in a function using *args and **kwargs
def collect_args(*args):
    print("Positional arguments:", args)  # This function collects all positional arguments into a tuple called args and prints it
collect_args(1, 2, 3)  # Output: Positional arguments: (1, 2, 3) (the function is called with three positional arguments, and they are collected into a tuple and printed)

def ArtistNames(*names):
    for name in names:
        print(name)  # This function takes a variable number of positional arguments (artist names) and prints each name on a new line  
ArtistNames("Michael Jackson", "Madonna", "Prince")  # Output: Michael Jackson ... Prince (the function is called with three artist names, and each name is printed on a new line)

def collect_kwargs(**kwargs):
    print("Keyword arguments:", kwargs)  # This function collects all keyword arguments into a dictionary called kwargs and prints it
collect_kwargs(name="Alice", age=30)  # Output: Keyword arguments: {'name': 'Alice', 'age': 30} (the function is called with two keyword arguments, and they are collected into a dictionary and printed)

def collect_all_args(*args, **kwargs):
    print("Positional arguments:", args)  # This function collects both positional and keyword arguments and prints them
    print("Keyword arguments:", kwargs)
collect_all_args(1, 2, name="Alice", age=30)  # Output: Positional arguments: (1, 2) ... Keyword arguments: {'name': 'Alice', 'age': 30} (the function is called with both positional and keyword arguments,

# and they are collected and printed separately)

# Global and local variables in functions
global_var = "I am a global variable"  # This is a global variable that can be accessed from anywhere in the code
def local_variable():
    local_var = "I am a local variable"  # This is a local variable that can only be accessed within this function
    print(local_var)  # Output: I am a local variable (the local variable is printed within the function)
local_variable()  # The function is called to demonstrate the use of a local variable
print(global_var)  # Output: I am a global variable (the global variable is printed outside the function)

# Scope of variables in functions
def outer_function():
    outer_var = "I am an outer variable"  # This variable is defined in the outer function and can be accessed by the inner function
    def inner_function():
        inner_var = "I am an inner variable"  # This variable is defined in the inner function and can only be accessed within this function
        print(outer_var)  # Output: I am an outer variable (the outer variable is accessed and printed within the inner function)
        print(inner_var)  # Output: I am an inner variable (the inner variable is printed within the inner function)
    inner_function()  # The inner function is called to demonstrate access to both the outer and inner variables
outer_function()  # The outer function is called to execute the code and demonstrate variable scope

def Thriller():
    Date = 1982 
    return Date  # This function returns the value of the variable Date, which is 1982
Date = 2007 
print(Thriller())  # Output: 1982 (the function is called, and it returns the value of Date defined within the function, which is 1982, demonstrating that the local variable Date in the function does not affect the global variable Date defined outside the function)

print(Date)  # Output: 2007 (the global variable Date is printed, showing that it remains unchanged by the function's local variable)

# if variable is not defined in the local scope, the function will look for it in the global scope
def ACDC(y):
    print(Rating)
    return y * Rating  # This function takes a parameter y and multiplies it by the variable Rating, which is not defined within the function but is expected to be found in the global scope
Rating = 5  # This is a global variable that will be accessed by the ACDC   function
Z = ACDC(10)  # The function is called with the argument 10, and it will print the value of Rating (which is 5) and return the product of y and Rating (which is 50)
print(Rating)  # Output: 5 (the global variable Rating is printed, showing that it is accessible both inside and outside the function)
print(Z)  # Output: 50 (the result of the function call, which is the product of y and Rating, is printed)

# The global keyword can be used to modify a global variable from within a function
def modify_global():
    global Rating  # This tells the function that we want to use the global variable Rating instead of creating a new local variable
    Rating = 10  # This modifies the global variable Rating to have a new value of 10
print(Rating)  # Output: 5 (the original value of the global variable Rating is printed)
modify_global()  # The function is called to modify the global variable Rating
print(Rating)  # Output: 10 (the modified value of the global variable Rating is printed, showing that it has been changed by the function using the global keyword)    

# Python Program to Count words in a String using Dictionary
def freq(string):
    
    #step1: A list variable is declared and initialized to an empty list.
    words = []
    
    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()
    
    #step3: Declare a dictionary
    Dict = {}
    
    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
        
    #step5: Print the dictionary
    print("The Frequency of words is:",Dict)
    
#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb")


