from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    #TODO: Implement abstract method for perimiter
    #TODO: Implement __str__ method to print details
   
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    #TODO: implement perimeter method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    #TODO: implement perimeter method
    

#TODO: Implement Triangle class