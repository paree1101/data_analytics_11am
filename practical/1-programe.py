a = 10
b = 20
c = a + b
print("The sum of a and b is:", c)
d = a % b
print("The modulus of a and b is:", d)

print(a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR
print(~a)     # Bitwise NOT
print(a << 2) # Left shift
print(a >> 2) # Right shift

print(type(a))

import turtle

class Circle:
    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = colour

    def draw(self):
        t = turtle.Turtle()
        t.color(self.colour)
        t.begin_fill()
        t.circle(self.radius)
        t.end_fill()

# Create object
circle1 = Circle(50, "red")

# Draw it
circle1.draw()

turtle.done()