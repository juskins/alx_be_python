import math


class Shape:
    """Base class for shapes."""
    
    def area(self):
        """
        Calculate the area of the shape.
        This method should be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    
    def __init__(self, length, width):
        """
        Initialize a rectangle with length and width.
        
        Args:
            length: The length of the rectangle
            width: The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    
    def __init__(self, radius):
        """
        Initialize a circle with a radius.
        
        Args:
            radius: The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area (π × radius²)
        """
        return math.pi * self.radius ** 2
