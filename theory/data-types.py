#Different data types in Python
#1. Numeric data types
# a) int (integer)
a = 10
print(a)  # Output: 10
print(type(a))  # Output: <class 'int'>
# b) float (floating-point number)
b = 3.14
print(b)  # Output: 3.14
print(type(b))  # Output: <class 'float'>
# c) complex (complex number)
c = 2 + 3j
print(c)  # Output: (2+3j)
print(type(c))  # Output: <class 'complex'>
#2. String data type
s = "Hello, World!"
print(s)  # Output: Hello, World!
print(type(s))  # Output: <class 'str'>
#3. Boolean data type
is_valid = True
print(is_valid)  # Output: True
print(type(is_valid))  # Output: <class 'bool'>
#4. List data type
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]
print(type(my_list))  # Output: <class 'list'>
#5. Tuple data type
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)
print(type(my_tuple))  # Output: <class 'tuple'>
#6. Dictionary data type
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(type(my_dict))  # Output: <class 'dict'>
#7. Set data type
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
print(type(my_set))  # Output: <class 'set'>
#8. NoneType data type
my_none = None
print(my_none)  # Output: None
print(type(my_none))  # Output: <class 'NoneType'>

#Rules of Lists, Tuples, Sets and Dictionaries with examples

#1. Lists are ordered, mutable, and allow duplicate elements.
example_list = [1, 2, 3, 4, 5, 2]
print(example_list)  # Output: [1, 2, 3, 4, 5, 2]
example_list[0] = 10  # Modifying the first element
print(example_list)  # Output: [10, 2, 3, 4, 5, 2]

#2. Tuples are ordered, immutable, and allow duplicate elements.
example_tuple = (1, 2, 3, 4, 5, 2)
print(example_tuple)  # Output: (1, 2, 3, 4, 5, 2)
# example_tuple[0] = 10  # This will raise a TypeError because tuples are immutable 

#3. Sets are unordered, mutable, and do not allow duplicate elements.
example_set = {1, 2, 3, 4, 5, 2}
print(example_set)  # Output: {1, 2, 3, 4, 5} - Note that the duplicate '2' is removed
example_set.add(6)  # Adding an element to the set
print(example_set)  # Output: {1, 2, 3, 4, 5, 6}

#4. Dictionaries are unordered, mutable, and do not allow duplicate keys.
example_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(example_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
example_dict["age"] = 31  # Modifying the value of the 'age' key
print(example_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'} 


#Dictionaries

#accessing keys 
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York  

#acessing values
print(my_dict.values())  # Output: dict_values(['Alice', 30, 'New York'])

#accessing values using get()
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("age"))   # Output: 30
print(my_dict.get("city"))  # Output: New York  

