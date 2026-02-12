### Sets

# Sets can contain elements of different data types, including numbers, strings, and even other sets.
# Sets are unordered collections of unique elements. 
# They are defined using curly braces {} or the set() function.
# Sets are mutable, meaning you can add or remove elements after they are created.
# Sets do not allow duplicate elements. If you try to add a duplicate element, it will be ignored.
# Sets are useful for performing mathematical operations like union, intersection, and difference.

## Example of a set with different data types
my_set = {1, "hello", 3.14, (1, 2), frozenset({3, 4})}
print(my_set)  # Output: {1, 'hello', 3.14, (1, 2), frozenset({3, 4})} (a set containing different data types)
print(type(my_set))  # Output: <class 'set'> (the type of my_set is set)
print(len(my_set))  # Output: 5 (the number of unique elements in the set)
print(3.14 in my_set)  # Output: True (checking if the element 3.14 is in the set)
print("world" in my_set)  # Output: False (checking if the element "world" is in the set)
print(my_set.add(42))  # Output: None (adding an element to the set, the add() method does not return anything)
print(my_set)  # Output: {1, 'hello', 3.14, (1, 2), frozenset({3, 4}), 42} (the set after adding the element 42)
print(my_set.add(1))  # Output: None (trying to add a duplicate element, the set will ignore it)
print(my_set)  # Output: {1, 'hello', 3.14, (1, 2), frozenset({3, 4}), 42} (the set remains unchanged because the duplicate element