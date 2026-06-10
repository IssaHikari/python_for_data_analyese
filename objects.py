import matplotlib.pyplot as plt


class Circle(object):
    def __init__(self,radius = 2,color = "red"):
        self.radius = radius
        self.color = color
    

    def add_radius(self , r):
        self.radius = self.radius + r
        return self.radius
    
    def drowCircle(self):
        plt.gca().add_patch(plt.Circle((0 , 0) , radius=self.radius , fc=self.color))
        plt.axis('scaled')
        plt.show()





RedCircle = Circle(10, 'red')
RedCircle.drawCircle()






# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()




class Vehicle(object):
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self , seating_capacity):
        self.seating_capacity = seating_capacity

    def display(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)