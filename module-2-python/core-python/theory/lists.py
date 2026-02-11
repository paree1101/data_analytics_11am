### Lists
# Lists are ordered sequences 
# Lists are mutable (can be changed after creation)
# Lists can contain duplicate elements
# Lists can contain elements of different data types
# Lists are defined using square brackets []
# Elements in a list are indexed, starting from 0

## Example of a list
my_list = [1, 2, 3, 4.3, "hard rock"]
print(my_list)  # Output: [1, 2, 3, 4.3, 'hard rock']
print(type(my_list))  # Output: <class 'list'>
print(my_list[0])  # Output: 1 (accessing the first element)
print(my_list[1:4])  # Output: [2, 3, 4.3] (slicing the list)
print(my_list[1:4:2])  # Output: [2, 4.3] (slicing with a step)
print(my_list + [6, 7])  # Output: [1, 2, 3, 4.3, 'hard rock', 6, 7] (concatenating lists)
a = [1, 2, 3] + [4, 5]
print(a)  # Output: [1, 2, 3, 4, 5] (concatenating two lists)
print(my_list * 2)  # Output: [1, 2, 3, 4.3, 'hard rock', 1, 2, 3, 4.3, 'hard rock'] (repeating the list)
print(len(my_list))  # Output: 5 (length of the list)

## Mutability of lists
# Lists can be modified after creation
my_list[0] = 10  # Modifying the first element  
print(my_list)  # Output: [10, 2, 3, 4.3, 'hard rock']

del my_list[1]  # Deleting the element at index 1 
print(my_list)  # Output: [10, 3, 4.3, 'hard rock']

my_list.append("new element")  # Adding a new element to the end of the list
print(my_list)  # Output: [10, 2, 3, 4.3, 'hard rock', 'new element']

C = [1]
C.append([2, 3, 4, 5])
print(C)  # Output: [1, [2, 3, 4, 5]] (the entire list [2, 3, 4, 5] is added as a single element)
len(C)  # Output: 2 (the list C has two elements: 1 and [2, 3, 4, 5])

my_list.extend([6, 7])  # Adding multiple elements to the end of the list
print(my_list)  # Output: [10, 2, 3, 4.3, 'hard rock', 'new element', 6, 7]

my_list.insert(1, "inserted element")  # Inserting an element at index 1
print(my_list)  # Output: [10, 'inserted element', 2, 3, 4.3, 'hard rock', 'new element']

my_list.remove(3)  # Removing the element with value 3
print(my_list)  # Output: [10, 'inserted element', 2, 4.3, 'hard rock', 'new element']

my_list.pop()  # Removing the last element
print(my_list)  # Output: [10, 'inserted element', 2, 4.3, 'hard rock']

my_list.pop(1)  # Removing the element at index 1
print(my_list)  # Output: [10, 2, 4.3, 'hard rock']

my_list.clear()  # Removing all elements from the list
print(my_list)  # Output: [] (the list is now empty)

## Difference between pop() and del
my_list = [1, 2, 3, 4, 5]
popped_element = my_list.pop()  # pop() removes and returns the last element
print(popped_element)  # Output: 5 (the popped element)
print(my_list)  # Output: [1, 2, 3, 4] (the list after popping the last element)
del my_list[0]  # del removes the element at index 0 but does not return it
print(my_list)  # Output: [2, 3, 4] (the list after deleting the first element)

## Nested lists
nested_list = [1, 2, [3, 4], 5]
print(nested_list)  # Output: [1, 2, [3, 4], 5]
print(nested_list[2])  # Output: [3, 4] (accessing the nested list)
print(nested_list[2][0])  # Output: 3 (accessing the first element of the nested list)
# We can also have nested lists with different data types like tuples
nested_list2 = [1, 2.555, 3, 4, ("cafe", 6)]

## Converting string to list
my_string = "Hello, World!"
my_list_from_string = list(my_string)
print(my_list_from_string)  # Output: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!'] (each character in the string becomes an element in the list)

my_string2 = "Python Programming"
my_list_from_string2 = my_string2.split()  # Splitting the string into a list of words
print(my_list_from_string2)  # Output: ['Python', 'Programming'] (the string is split into words based on whitespace)
my_string_new = "A, B, C, D"
my_list3 = my_string_new.split(",")  # Splitting the string into a list based on a comma delimiter
print(my_list3)  # Output: ['A', ' B', ' C', ' D'] (the string is split into elements based on comma delimiter)

## List Aliasing
list1 = [1, 2, 3]
list2 = list1  # list2 is now an alias for list1
print(list1)  # Output: [1, 2, 3]
print(list2)  # Output: [1, 2, 3]
list2[0] = 10  # Modifying list2 will also modify list1
print(list1)  # Output: [10, 2, 3] (list1 is also modified because list2 is an alias for list1)
print(list2)  # Output: [10, 2, 3] (list2 is modified)

## List Cloning
list1 = [1, 2, 3]
list3 = list1.copy()  # Creating a clone of list1
print(list3)  # Output: [1, 2, 3] (list3 is a clone of list1)
list3[0] = 20  # Modifying list3 will not affect list1
print(list1)  # Output: [1, 2, 3] (list1 is not modified because list3 is a clone of list1)
print(list3)  # Output: [20, 2, 3] (list3 is modified)

# use command: help(list)  
# This will display the documentation for the list data type, 
# including its methods and usage.  

