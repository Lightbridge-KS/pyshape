from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for geometric shapes.

    Parameters
    ----------
    color : str
        The color of the shape.

    Attributes
    ----------
    color : str
        The color of the shape.
    count : int
        Class variable tracking the number of shape instances created.
    """

    count = 0
    def __init__(self, color):
        self.color = color
        self.__class__.count += 1  # Increment the class variable
    
    # For Dev
    def __repr__(self) -> str:
        """Return developer representation of the shape.

        Returns
        -------
        str
            Developer string representation showing class name and color.
        """
        cls = self.__class__.__name__
        return f"{cls}(color={self.color})"
    # For User
    def __str__(self) -> str:
        """Return user-friendly string representation of the shape.

        Returns
        -------
        str
            User-friendly string showing shape type and color.
        """
        cls = self.__class__.__name__
        return f"{cls} with {self.color} color"
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape.

        This is an abstract method that must be implemented by subclasses.

        Returns
        -------
        str
            String representation of the area calculation.
        """
        pass


class Circle(Shape):
    """A circle shape.

    Parameters
    ----------
    color : str
        The color of the circle.
    radius : float
        The radius of the circle.

    Attributes
    ----------
    radius : float
        The radius of the circle.
    """
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        
    def area(self):
        """Calculate the area of the circle.

        Returns
        -------
        str
            String showing the circle area calculation using π r².
        """
        import math
        A = math.pi * self.radius ** 2
        return f"The circle area = pi x {self.radius}^2 = {A}"
    

class Square(Shape):
    """A square shape.

    Parameters
    ----------
    color : str
        The color of the square.
    side : float
        The length of one side of the square.

    Attributes
    ----------
    side : float
        The length of one side of the square.
    """
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side
    def area(self):
        """Calculate the area of the square.

        Returns
        -------
        str
            String showing the square area calculation using side².
        """
        return f"The square area = {self.side ** 2}"
    


class Triangle(Shape):
    """A triangle shape.

    Parameters
    ----------
    color : str
        The color of the triangle.
    width : float
        The base width of the triangle.
    height : float
        The height of the triangle.

    Attributes
    ----------
    width : float
        The base width of the triangle.
    height : float
        The height of the triangle.
    """
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    def area(self):
        """Calculate the area of the triangle.

        Returns
        -------
        str
            String showing the triangle area calculation using ½ × base × height.
        """
        return f"The triangle area = {self.width * self.height * 0.5}"