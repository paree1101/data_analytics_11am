# Tkinter is a module used to create a standard GUI for the students to interact with the code.
# It is used to create a simple interface for the students to run the code and see the output. 
# It is also used to create a simple interface for the students to ask questions and get answers.
# It is a simple way to interact with the code without having to use the command line or an IDE.

# Uses of Tkinter:
# 1. Create text boxes for user input
# 2. Create buttons to trigger actions
# 3. Display output in a text box or label

# how to install tkinter: pip install tkinter
# if already there then: python -m tkinter

# Example of a simple Tkinter application
import tkinter as tk
root = tk.Tk() # creating the main window of the application
root.title("Simple Tkinter App") # setting the title of the window
root.geometry("300x200") # setting the size of the window
label = tk.Label(root, text="Hello, My name is Paree!", font=("Arial", 25)) # creating a label widget
label.pack(pady=20) # packing the label widget into the window with some padding
button = tk.Button(root, text="Click Me!", font=("Arial", 20), command=lambda: label.config(text="Button Clicked!")) # creating a button widget with a command to change the label text when clicked
button.pack(pady=10) # packing the button widget into the window with some padding
root.mainloop() # starting the main event loop of the application


