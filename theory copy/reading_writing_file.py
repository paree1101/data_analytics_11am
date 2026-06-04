# Reading and Writing Files in Python
# Reading a File
file = open('/Users/pareesangani/Desktop/data_analytics_11am/module-2-python/core-python/practical/example.txt', 'r')  # Open the file in read mode
content = file.read()  # Read the entire content of the file
print(content)  # Print the content of the file
file.close()  # Close the file  

# Better way to read a file using 'with' statement (automatically closes the file)
with open('/Users/pareesangani/Desktop/data_analytics_11am/module-2-python/core-python/practical/example.txt', 'r') as file:
    content = file.read()
    print(content) 

#Output each line separately
with open('/Users/pareesangani/Desktop/data_analytics_11am/module-2-python/core-python/practical/example.txt', 'r') as file:
    content = file.readlines()  # Read the file line by line into a list
    print(content)  # Print the list of lines

# Writing to a File
with open('/Users/pareesangani/Desktop/data_analytics_11am/module-2-python/core-python/practical/example2.txt', 'w') as file:  # Open the file in write mode
    file.write("This is a new file created using Python.\n")  # Write a line to the file
    file.write("This is the second line.\n")  # Write another line to the file