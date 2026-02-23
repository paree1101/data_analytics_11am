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
print(my_set.remove("hello"))  # Output: None (removing an element from the set, the remove() method does not return anything)
print(my_set)  # Output: {1, 3.14, (1, 2), frozenset({3, 4}), 42} (the set after removing the element "hello")
print(my_set.remove("world"))  # Output: KeyError: 'world' (trying to remove an element that does not exist in the set will raise a KeyError)
print(my_set.discard("world"))  # Output: None (trying to discard an element that does not exist in the set will not raise an error, the discard() method will simply do nothing)
print(my_set)  # Output: {1, 3.14, (1, 2), frozenset({3, 4}), 42} (the set remains unchanged after trying to discard the non-existent element "world")
print(my_set.clear())  # Output: None (clearing all elements from the set, the clear() method does not return anything)
print(my_set)  # Output: set() (an empty set after clearing all elements)

### Example of set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b))  # Output: {1, 2, 3, 4, 5, 6} (the union of set_a and set_b)
print(set_a.intersection(set_b))  # Output: {3, 4} (the intersection of set_a and set_b)
set_c = set_a & set_b
print(set_c)  # Output: {3, 4} (the intersection of set_a and set_b using the & operator)

set_d = {1, 2}
set_d.issubset(set_a)  # Output: True (checking if set_d is a subset of set_a, which means all elements of set_d are in set_a)
set_a.issuperset(set_d)  # Output: True (checking if set_a is a superset of set_d, which means all elements of set_d are in set_a)

print(set_a.difference(set_b))  # Output: {1, 2} (the difference of set_a and set_b, which are the elements that are in set_a but not in set_b)
print(set_b.difference(set_a))  # Output: {5, 6} (the difference of set_b and set_a, which are the elements that are in set_b but not in set_a) 
