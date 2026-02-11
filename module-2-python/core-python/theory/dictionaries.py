### Dictionaries

# They are used to store data in key-value pairs. Each key is unique and maps to a value.
#  Dictionaries are mutable, meaning you can change their content after they are created.
#  Dictionaries are defined using curly braces {} and key-value pairs are separated by commas.
#  The keys in a dictionary must be of an immutable data type (like strings, numbers, or tuples),
#  The values can be of any data type e.i. mutable or immutable.
#  Elements in a dictionary are accessed using their keys, not by index.

## Example of an immutable key in a dictionary w strings, numbers, and tuples:
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], 5: (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict["key1"]  # Output: 1 
Dict["key2"]  # Output: '2' 
Dict["key3"]  # Output: [3, 3, 3] 
Dict[5]  # Output: (4, 4, 4) 
Dict[('key5')]  # Output: 5 
Dict[(0, 1)]  # Output: 6 

## Empty dictionary
empty_dict = {}
print(empty_dict)  # Output: {} (an empty dictionary)
# adding key-value pairs to the empty dictionary
empty_dict["movie"] = "The Matrix"
empty_dict["year"] = 1999
print(empty_dict)  # Output: {'movie': 'The Matrix', 'year': 1999} (the dictionary after adding key-value pairs)

## Example of a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "cooking"]
}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'traveling', 'cooking']}
print(type(my_dict))  # Output: <class 'dict'>
print(len(my_dict))  # Output: 4 (length of the dictionary, which is the number of key-value pairs)
print(my_dict["name"])  # Output: Alice (accessing the value associated with the key "name")
print(my_dict["hobbies"])  # Output: ['reading', 'traveling', 'cooking'] (accessing the value associated with the key "hobbies")
print(my_dict.get("age"))  # Output: 30 (accessing the value associated with the key "age" using the get() method)

print(my_dict.get("country", "USA"))  # Output: USA (accessing a non-existent key "country" with a default value "USA")
# This avoids KeyError that would occur if we tried to access a non-existent key directly using my_dict["country"] 
my_dict["country"] = "Canada"
print(my_dict.get("country", "USA"))  # Output: Canada (accessing the key "country" after adding it to the dictionary, 
#the default value "USA" is not used because the key now exists in the dictionary)

print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city', 'hobbies']) (getting all the keys in the dictionary)
print(my_dict.values())  # Output: dict_values(['Alice', 30, 'New York', ['reading', 'traveling', 'cooking']]) (getting all the values in the dictionary)
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York'), ('hobbies', ['reading, 'traveling', 'cooking'])]) (getting all the key-value pairs in the dictionary)

## Checking for the presence of keys and values in a dictionary
print("name" in my_dict)  # Output: True (checking if the key "name" exists in the dictionary)
print("country" in my_dict)  # Output: False (checking if the key "country" exists in the dictionary)
print("Alice" in my_dict)  # Output: False (checking if the value "Alice" exists in the dictionary, this will return False because we are checking for values, not keys)
print("Alice" in my_dict.values())  # Output: True (checking if the value "Alice" exists in the dictionary using values() method)
print("age" in my_dict.keys())  # Output: True (checking if the key "age" exists in the dictionary using keys() method)


## Difference between print(my_dict) and print(my_dict.items())
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'traveling', 'cooking'], 'country': 'Canada'} (printing the dictionary directly)
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York'), ('hobbies', ['reading', 'traveling', 'cooking']), ('country', 'Canada')]) (printing a view of the key-value pairs)
# When we print the dictionary directly, it shows the key-value pairs in a standard dictionary format.
# When we print my_dict.items(), it shows a view object that contains the key-value pairs as tuples in a list-like format. 
# The items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
# This view object can be used to iterate over the key-value pairs in the dictionary. Useful for loops

## Modifying a dictionary
my_dict["age"] = 31  # Modifying the value associated with the key "age"
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'hobbies': ['reading', 'traveling', 'cooking']}
my_dict["country"] = "USA"  # Adding a new key-value pair to the dictionary
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'hobbies': ['reading', 'traveling', 'cooking'], 'country': 'USA'}
del my_dict["city"]  # Deleting the key-value pair with the key "city"
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'hobbies': ['reading', 'traveling', 'cooking'], 'country': 'USA'}

# ## Nested dictionaries
nested_dict = {
    "person1": {
        "name": "Alice",
        "age": 30
    },
    "person2": {
        "name": "Bob",
        "age": 25
    }
}
print(nested_dict)  # Output: {'person1': {'name': 'Alice', 'age': 30}, 'person2': {'name': 'Bob', 'age': 25}}
print(nested_dict["person1"])  # Output: {'name': 'Alice', 'age': 30} (accessing the nested dictionary for person1)
print(nested_dict["person1"]["name"])  # Output: Alice (accessing the name of person1)
print(nested_dict["person2"]["age"])  # Output: 25 (accessing the age of person2)
print(nested_dict["person1"]["hobbies"])  # Output: KeyError: 'hobbies' (trying to access a non-existent key "hobbies" in the nested dictionary for person1)
print(nested_dict["person1"].get("hobbies", "No hobbies found"))  # Output: No hobbies found (using get() method to access a non-existent key "hobbies" with a default value)
