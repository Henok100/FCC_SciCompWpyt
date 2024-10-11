# This script defines two vector classes: R2Vector for 2D vectors and R3Vector for 3D vectors.
# These classes allow you to perform basic vector operations like addition, subtraction, 
# dot product, and cross product. Additionally, comparison operators (like ==, <, >) 
# are implemented based on vector norms (the length of the vector).
# The R3Vector class inherits from R2Vector and extends it to 3D space by adding the z-coordinate.
# Main components:
# - R2Vector class: handles 2D vectors and operations.
# - R3Vector class: extends R2Vector to 3D and adds cross product functionality.
# - Methods include norm, addition, subtraction, multiplication (dot product), and cross product for R3Vector.

class R2Vector:
    def __init__(self, *, x, y):
        # Constructor for R2Vector, initializing with x and y components.
        # 'self' refers to the instance of the class being created.
        # The x and y values are passed as keyword arguments.
        self.x = x  # Assign x-coordinate
        self.y = y  # Assign y-coordinate

    def norm(self):
        # Calculate the magnitude (norm) of the vector using the Pythagorean theorem.
        # The magnitude is the square root of the sum of the squares of the components (x and y).
        return sum(val**2 for val in vars(self).values())**0.5  # sqrt(x^2 + y^2)

    def __str__(self):
        # Convert the vector into a human-readable string format, returning the coordinates as a tuple.
        return str(tuple(getattr(self, i) for i in vars(self)))  # Returns (x, y)

    def __repr__(self):
        # Representation method for the vector when printing or inspecting it.
        # Returns the class name and the x and y values, formatted as 'R2Vector(x=val, y=val)'.
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]  # Create 'x=val, y=val'
        args = ', '.join(arg_list)  # Join the argument list into a string
        return f'{self.__class__.__name__}({args})'  # Return class name and arguments

    def __add__(self, other):
        # Overload the + operator to add two R2Vector objects.
        # If the other object is not of the same type (R2Vector), return NotImplemented.
        if type(self) != type(other):
            return NotImplemented
        # Add corresponding components of the vectors (x and y) to form a new vector.
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)  # Return a new instance of R2Vector

    def __sub__(self, other):
        # Overload the - operator to subtract two R2Vector objects.
        # If the other object is not of the same type, return NotImplemented.
        if type(self) != type(other):
            return NotImplemented
        # Subtract corresponding components of the vectors (x and y).
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)  # Return a new instance of R2Vector

    def __mul__(self, other):
        # Overload the * operator to handle two cases:
        # 1. Scalar multiplication: multiply vector by a number (int or float).
        if type(other) in (int, float):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}  # Multiply each component by scalar
            return self.__class__(**kwargs)  # Return new scaled vector
        # 2. Dot product: multiply two vectors of the same type component-wise and return the sum.
        elif type(self) == type(other):
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]  # Multiply each component
            return sum(args)  # Return the dot product as a scalar value
        return NotImplemented  # Return NotImplemented if operation is not defined for the type

    def __eq__(self, other):
        # Overload the == operator to compare two vectors by checking if their components are equal.
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))  # Check if x and y match

    def __ne__(self, other):
        # Overload the != operator by negating the result of ==.
        return not self == other

    def __lt__(self, other):
        # Overload the < operator to compare vectors by their magnitudes (norms).
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()  # Compare based on vector length

    def __gt__(self, other):
        # Overload the > operator to compare vectors by their magnitudes.
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()  # Compare based on vector length

    def __le__(self, other):
        # Overload the <= operator by using the result of the > operator.
        return not self > other

    def __ge__(self, other):
        # Overload the >= operator by using the result of the < operator.
        return not self < other

class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        # Constructor for R3Vector, inheriting from R2Vector and adding a z-component.
        super().__init__(x=x, y=y)  # Initialize x and y using the superclass (R2Vector)
        self.z = z  # Assign z-coordinate

    def cross(self, other):
        # Calculate the cross product of two R3Vectors.
        # Cross product is only defined for 3D vectors and results in a new vector perpendicular to both inputs.
        if type(self) != type(other):
            return NotImplemented
        # Use the determinant formula to compute the cross product.
        kwargs = {
            'x': self.y * other.z - self.z * other.y,  # Cross product formula for the x-component
            'y': self.z * other.x - self.x * other.z,  # Cross product formula for the y-component
            'z': self.x * other.y - self.y * other.x   # Cross product formula for the z-component
        }
        
        return self.__class__(**kwargs)  # Return a new R3Vector

# Example usage of R3Vector class to demonstrate vector operations
v1 = R3Vector(x=2, y=3, z=1)  # Create a 3D vector v1 with x=2, y=3, z=1
v2 = R3Vector(x=0.5, y=1.25, z=2)  # Create another 3D vector v2 with x=0.5, y=1.25, z=2
print(f'v1 = {v1}')  # Print v1, which uses the __str__ method to display coordinates
print(f'v2 = {v2}')  # Print v2
v3 = v1 + v2  # Add vectors v1 and v2 using the overloaded + operator
print(f'v1 + v2 = {v3}')  # Print the result of v1 + v2
v4 = v1 - v2  # Subtract vectors v1 and v2 using the overloaded - operator
print(f'v1 - v2 = {v4}')  # Print the result of v1 - v2
v5 = v1 * v2  # Compute the dot product of v1 and v2 using the overloaded * operator
print(f'v1 * v2 = {v5}')  # Print the result of the dot product
v6 = v1.cross(v2)  # Compute the cross product of v1 and v2 using the cross method
print(f'v1 x v2 = {v6}')  # Print the result of the cross product
