## For Loops
# A for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects.
# The syntax of a for loop is:
# for variable in iterable:
#     # code to execute for each element in the iterable
# The variable takes the value of each element in the iterable one by one, and the code block is executed for each element.

# Example of a for loop iterating over a list
my_list = [1, 2, 3, 4, 5]
for number in my_list:
    print(number)  # Output: 1 2 3 4 5 (each number in the list is printed on a new line)

# Example of a for loop iterating over a string
my_string = "Hello"
for char in my_string:
    print(char)  # Output: H e l l o (each character in the string is printed on a new line)

# For loops can also be used with the range() function to iterate over a sequence of numbers
for i in range(5):
    print(i)  # Output: 0 1 2 3 4 (the range() function generates a sequence of numbers from 0 to 4)

Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)

# Another way to iterate over the list Genres using a for loop with an index
for i in range(len(Genres)):
    print(Genres[i])

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i]) 

# For loops can also be used with the enumerate() function to get both the index and the value of each element in an iterable
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")  # Output: Index: 0, Value: 1 ... Index: 4, Value: 5 (the index and value of each element in the list are printed)

# For loops can also be used with the zip() function to iterate over multiple iterables in parallel
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, char in zip(list1, list2):
    print(f"Number: {num}, Character: {char}")  # Output: Number: 1, Character: a ... Number: 3, Character: c (the number and character from both lists are printed in parallel)

# For loops can also be used with the items() method of a dictionary to iterate over key-value pairs
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")  # Output: Key: name, Value: Alice ... Key: city, Value: New York (the key and value of each item in the dictionary are printed)

# For loops can also be used with the sorted() function to iterate over a sorted sequence
for number in sorted(my_list, reverse=True):
    print(number)  # Output: 5 4 3 2 1 (the numbers in the list are printed in descending order)

# For loops can also be used with the break and continue statements to control the flow of the loop
for number in my_list:
    if number == 3:
        break  # This will exit the loop when number is 3
    print(number)  # Output: 1 2 (the numbers 1 and 2 are printed, but the loop stops when it reaches 3)

for number in my_list:
    if number == 3:
        continue  # This will skip the rest of the loop when number is 3 and move to the next iteration
    print(number)  # Output: 1 2 4 5 (the numbers 1, 2, 4, and 5 are printed, but the number 3 is skipped)

# For loops can also be nested, meaning you can have a for loop inside another for loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")  # Output: i: 0, j: 0 ... i: 2, j: 1 (the values of i and j are printed for each combination of i and j)

# For loops can also be used with list comprehensions to create new lists based on existing iterables
squared_numbers = [number ** 2 for number in my_list]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25] (a new list containing the squares of the numbers in my_list)

### While Loops
# A while loop is used to repeatedly execute a block of code as long as a certain condition is true.
# The syntax of a while loop is: 
# while condition:
#     # code to execute while the condition is true
# The condition is evaluated before each iteration of the loop, and if it is true, the code block is executed. If the condition is false, the loop is terminated.   

# Example of a while loop
count = 0
while count < 5:
    print(count)  # Output: 0 1 2 3 4 (the value of count is printed on each iteration of the loop)
    count += 1  # Incrementing count by 1 on each iteration to eventually make the condition false and terminate the loop

# While loops can also be used with the break and continue statements to control the flow of the loop
count = 0
while count < 5:
    if count == 3:
        break  # This will exit the loop when count is 3
    print(count)  # Output: 0 1 2 (the values of count are printed until it reaches 3, at which point the loop stops)
    count += 1

count = 0
while count < 5:
    if count == 3:
        count += 1  # Incrementing count to avoid an infinite loop when count is 3
        continue  # This will skip the rest of the loop when count is 3 and move to the next iteration
    print(count)  # Output: 0 1 2 4 (the values of count are printed, but the value 3 is skipped)
    count += 1

# While loops can also be nested, meaning you can have a while loop inside another while loop
i = 0
while i < 3:
    j = 0
    while j < 2:
        print(f"i: {i}, j: {j}")  # Output: i: 0, j: 0 ... i: 2, j: 1 (the values of i and j are printed for each combination of i and j)
        j += 1
    i += 1

# While loops can also be used with the else statement, which is executed when the loop condition becomes false (i.e., when the loop is terminated without encountering a break statement)
count = 0
while count < 5:
    print(count)  # Output: 0 1 2 3 4 (the value of count is printed on each iteration of the loop)
    count += 1
else:
    print("Loop has ended")  # Output: Loop has ended (this is printed after the loop condition becomes false and the loop is terminated)


# iterate through list dates and stop at the year 1973, then print out the number of iterations
dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")


# Write a while loop to display the values of the Rating of an album playlist stored in thePlayListRatings list. 
# If the score is less than 6, exit the loop. 
# The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]
while(i < len(PlayListRatings) and Rating >= 6):
    print(Rating)
    i = i + 1 # This prints the value 10 only once 
    Rating = PlayListRatings[i]
    i = i + 1 # This prints the value 10 twice, but it also prints the value 5 which is less than 6, so we need to add a condition to check for that

# when orange is no more in the list, stop the loop and print the new list of orange squares
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while i < len(squares) and squares[i] == 'orange':
    new_squares.append(squares[i])
    i += 1
print(new_squares) 


# Note: Be cautious when using while loops, as they can lead to infinite loops if the condition never becomes false. Always ensure that there is a way for the loop to terminate.

