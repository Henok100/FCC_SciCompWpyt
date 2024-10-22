"""
Polygon Area Calculator Project

This script defines two classes, Rectangle and Square, to model geometric shapes 
and calculate their properties such as area, perimeter, diagonal, and visual 
representation.

Class Descriptions:
1. Rectangle:
   - Initializes with width and height.
   - Methods include:
     - set_width(width): Sets the rectangle's width.
     - set_height(height): Sets the rectangle's height.
     - get_area(): Returns the area of the rectangle.
     - get_perimeter(): Returns the perimeter of the rectangle.
     - get_diagonal(): Returns the length of the diagonal.
     - get_picture(): Returns a string representation of the rectangle using asterisks.
     - get_amount_inside(shape): Determines how many times a given shape can fit inside the rectangle.

2. Square (inherits from Rectangle):
   - Initializes with a single side length.
   - Methods include:
     - set_side(side): Sets both width and height to the given side length.
     - Overrides set_width and set_height to ensure the square remains valid.

Usage Example:
- Create a Rectangle or Square instance, modify its dimensions, and call the methods to 
  retrieve the desired properties or visual representations.
"""

class Rectangle:
    """
    Rectangle Class Documentation

    The Rectangle class models a rectangle shape and provides various methods to 
    manipulate and retrieve information about its dimensions and properties.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.

        Parameters:
        - width (float): The width of the rectangle.
        - height (float): The height of the rectangle.

        This method sets the initial width and height of the rectangle.
        """
        self.width = width  # Set the width attribute to the provided width
        self.height = height  # Set the height attribute to the provided height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Format: 'Rectangle(width=5, height=10)' (example).
        
        This method is useful for displaying the rectangle's dimensions in a readable format.
        """
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'  # Return a formatted string showing the class name and dimensions

def set_width(self, width):
    """
    Sets the width of the rectangle.

    Parameters:
    - width (float): The new width for the rectangle.

    This method updates the width attribute to the provided value.
    """
    self.width = width  # Update the width attribute with the new width


def set_height(self, height):
    """
    Sets the height of the rectangle.

    Parameters:
    - height (float): The new height for the rectangle.

    This method updates the height attribute to the provided value.
    """
    self.height = height  # Update the height attribute with the new height


def get_area(self):
    """
    Calculates the area of the rectangle.

    Returns:
    - float: The area of the rectangle calculated as width * height.

    This method multiplies the width by the height to get the area.
    """
    return self.width * self.height  # Return the area of the rectangle


def get_perimeter(self):
    """
    Calculates the perimeter of the rectangle.

    Returns:
    - float: The perimeter of the rectangle calculated as 2 * width + 2 * height.

    This method adds together the lengths of all sides of the rectangle.
    """
    return 2 * self.width + 2 * self.height  # Return the perimeter of the rectangle


def get_diagonal(self):
    """
    Calculates the diagonal length of the rectangle.

    Returns:
    - float: The length of the diagonal calculated using the Pythagorean theorem.

    This method computes the diagonal as the square root of the sum of the squares of width and height.
    """
    return (self.width ** 2 + self.height ** 2) ** .5  # Return the length of the diagonal


def get_picture(self):
    """
    Generates a string representation of the rectangle using asterisks.

    Returns:
    - str: A string made of '*' characters representing the rectangle.
    - If the width or height exceeds 50, returns "Too big for picture."

    This method creates a visual representation of the rectangle using '*' characters.
    """
    strr = ''  # Initialize an empty string to build the picture
    if self.width > 50 or self.height > 50:
        return "Too big for picture."  # Check if dimensions are too large for representation
    for _ in range(self.height):
        for _ in range(self.width):
            strr += '*'  # Append '*' for each width
        strr += '\n'  # Add a new line after each row
    return strr  # Return the completed picture


def get_amount_inside(self, shape):
    """
    Calculates how many instances of a given shape can fit inside the rectangle.

    Parameters:
    - shape (Rectangle): Another rectangle or square object.

    Returns:
    - int: The number of times the shape can fit inside the rectangle.

    This method determines how many times the width and height of the passed shape can fit inside the rectangle.
    """
    return (self.width // shape.width) * (self.height // shape.height)  # Calculate the number of shapes that can fit inside

class Square(Rectangle):
    """
    Represents a square shape, inheriting from the Rectangle class.

    The Square class initializes a square with a specific side length,
    using the properties of a rectangle (width and height).
    """

    def __init__(self, side):
        """
        Initializes a new Square instance.

        Parameters:
        - side (float): The length of one side of the square.

        This constructor calls the parent class (Rectangle) initializer with
        the same value for width and height since all sides of a square are equal.
        """
        super().__init__(side, side)  # Initialize the Rectangle with equal width and height


    def set_side(self, side):
        """
        Sets the length of one side of the square.

        Parameters:
        - side (float): The new side length for the square.

        This method updates both width and height to the same value, as all sides of a square are equal.
        """
        self.width = side  # Set the width to the new side length
        self.height = side  # Set the height to the new side length


    def set_width(self, side):
        """
        Sets the width of the square (and thus height as well).

        Parameters:
        - side (float): The new width for the square.

        This method updates both width and height to ensure the square remains uniform.
        """
        self.width = side  # Set the width to the new side length
        self.height = side  # Set the height to the new side length


    def set_height(self, side):
        """
        Sets the height of the square (and thus width as well).

        Parameters:
        - side (float): The new height for the square.

        This method updates both width and height to maintain the square's properties.
        """
        self.width = side  # Set the width to the new side length
        self.height = side  # Set the height to the new side length


    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
        - str: A string indicating the class name and the length of its side.

        This method provides a readable format for the square instance.
        """
        return f'{self.__class__.__name__}(side={self.width})'  # Return a formatted string showing the square's side length


#Example
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))