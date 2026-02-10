### String Manipulation Operations
# 1. Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name 
# Output: 'John Doe'


#2. Repetition
greeting = "Hello! "
repeated_greeting = greeting * 3   
# Output: 'Hello! Hello! Hello! ' 

# 3. Indexing
name = "The BodyGuard"
print(name[0])  # Output: 'T'
print(name[1])  # Output: 'h'
print(name[-1])  # Output: 'd'

# 4. Slicing
text = "Python Programming"
substring = text[0:6]  # 'Python' 
# Output: 'Python'
name = "The BodyGuard"
name[::2]  # Output: 'TeBdGad' (every second character)
name[0:5:2]  # Output: 'TeB' (characters at index 0, 2, and 4)

# 5. String Methods
message = "Hello, World!"
print(message.lower())  # Output: 'hello, world!'
print(message.upper())  # Output: 'HELLO, WORLD!'
print(message.replace("World", "Python"))  # Output: 'Hello, Python!'
print(message.split(", "))  # Output: ['Hello', 'World!']   
print(message.find("o"))  # Output: 4 (index of first occurrence of 'o')
print(message.count("o"))  # Output: 2 (number of occurrences of 'o')

# 6. Length of a String
text = "Hello, World!"  
length = len(text)
# Output: 13 (number of characters in the string)

# 7. String Formatting
name = "Alice"  
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
# Output: 'My name is Alice and I am 30 years old.' 

number = int(input("Enter a number: "))
power = pow(number, 2)
print(f"The square of {number} is {power}.")    
