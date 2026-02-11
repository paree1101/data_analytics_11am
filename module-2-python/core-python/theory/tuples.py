### Tuples
# Tuples are ordered sequences
# Tuples are similar to lists but are immutable (cannot be changed after creation)
# Tuples can contain duplicate elements
# Tuples can contain elements of different data types
# Tuples are defined using parentheses ()
# Elements in a tuple are indexed, starting from 0

## Example of a tuple
my_tuple = (1, 2, 3, 4.3, "hard rock")
print(my_tuple)  # Output: (1, 2, 3, 4.3, 'hard rock')
print(type(my_tuple))  # Output: <class 'tuple'>
print(my_tuple[0])  # Output: 1 (accessing the first element)
print(my_tuple[1:4])  # Output: (2, 3, 4.3) (slicing the tuple)
print(my_tuple[1:4:2])  # Output: (2, 4.3) (slicing with a step)
print(my_tuple + (6, 7))  # Output: (1, 2, 3, 4.3, 'hard rock', 6, 7) (concatenating tuples)
print(my_tuple * 2)  # Output: (1, 2, 3, 4.3, 'hard rock', 1, 2, 3, 4.3, 'hard rock') (repeating the tuple)
print(len(my_tuple))  # Output: 5 (length of the tuple)

## Immutability of tuples
# Once a tuple is created, its elements cannot be modified
# my_tuple[0] = 10  # This will raise a TypeError because tuples are immutable
# to manipulate a tuple you can create a new object 
ratings = (4, 5, 3)
# to sort the ratings in ascending order, we can create a new tuple
sorted_ratings = tuple(sorted(ratings))
print(sorted_ratings)  # Output: (3, 4, 5) (sorted() returns a list, so we convert it back to a tuple)  

## Nested tuples
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple)  # Output: (1, 2, (3, 4), 5)
print(nested_tuple[2])  # Output: (3, 4) (accessing the nested tuple)
print(nested_tuple[2][0])  # Output: 3 (accessing the first element of the nested tuple)   

