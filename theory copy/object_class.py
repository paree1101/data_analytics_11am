## Classes (Object-Oriented Programming)
# A class is a blueprint for creating objects.
# Objects are instances of a class and contain:
# - Attributes (variables/data)
# - Methods (functions/behaviour)

# The syntax of a class is:
# class ClassName:
# def __init__(self, parameters):
# # initialize attributes
# self refers to the current object

## Example: Circle Class
class Circle:
    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = colour
    
    # Method to add to the radius
    def add_radius(self, r):
        self.radius += r

## Creating Objects
circle1 = Circle(5, "red")
circle2 = Circle(10, "blue")
    

## Accessing Attributes
print(circle1.radius)   # Output: 5
print(circle1.colour)   # Output: red
print(circle1)

## Modifying Attributes (Changing Colour)
circle1.colour = "green"
print(circle1.colour)   # Output: green

## Using Methods
circle1.add_radius(3)
print(circle1.radius)   # Output: 8

## Checking Attributes of Different Objects
print(circle1.radius, circle1.colour)
print(circle2.radius, circle2.colour)


#other method:
#directly: 
import matplotlib.pyplot as plt
 
class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
        # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method to draw circle using matplotlib
    def drawCircle(self):
        import matplotlib.pyplot as plt
        plt.figure()  # 👈 add this line
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()
# 1. Create the object (This runs __init__)
red_circle = Circle(radius=10, color='red')

# 2. Tell the object to draw itself (This runs drawCircle)
red_circle.drawCircle()

## Example: Rectangle Class
class Rectangle:
    def __init__(self, height, width, colour):
        self.height = height
        self.width = width
        self.colour = colour
        # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.colour))
        plt.axis('scaled')
        plt.show()

## Creating Rectangle Objects        
rect1 = Rectangle(4, 6, "yellow")
rect2 = Rectangle(10, 3, "black")

## Accessing Rectangle Attributes
print(rect1.height) 
print(rect1.width)
print(rect1.colour)

## Modifying Rectangle Colour
rect1.colour = "green"
print(rect1.colour)

## Comparing / Checking Attributes
# Compare colours
print(rect1.colour == rect2.colour)  # Output: False

# Compare sizes
print(rect1.height == rect2.height)

rect1.drawRectangle()

## Key Notes
# 🔑 Key idea:
# Class → blueprint
# Object → instance of class

# self → refers to current object

# Attributes → variables inside class
# Methods → functions inside class

# You can:
# - Access attributes using object.attribute
# - Modify attributes directly
# - Call methods using object.method()


#Create a python programme that represents vehicals using a class. 
#Each car should have attributes like maximum speed, mileage. 
#Additionally, you need to create methods in the Vehicle class to assign seating capacity to a vehicle.¶
#Create a method to display all the properties of an object of the class.
class Vehical:
    color = "white"
    def __init__(self, speed, mileage):
        self.speed = speed
        self.mileage = mileage
        self.seating_cap = None
    def assign_seating_cap(self, seating_cap):
        self.seating_cap = seating_cap
    def properties(self):
        print("properties of the vehical:")
        print("Color:", self.color)
        print("Maximum Speed:", self.speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_cap)
#Create two objects of the Vehicle class object that should have a max speed of 200kmph and mileage of 20kmpl with five seating capacities, 
#And another car object should have a max speed of 180kmph and mileage of 25kmpl with four seating capacities.¶
car1 = Vehical(200, 20)
car1.assign_seating_cap(5)
car1.properties()

car2 = Vehical(180, 25)
car2.assign_seating_cap(4)
car2.properties()
