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
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show() 

# 1. Create the object (This runs __init__)
red_circle = Circle(radius=100, color='blue')

# 2. Tell the object to draw itself (This runs drawCircle)
red_circle.drawCircle()