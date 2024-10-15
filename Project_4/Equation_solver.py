"""
Introduction to the Script:
This script defines an abstract base class 'Equation' and its subclasses 'LinearEquation' 
and 'QuadraticEquation' for solving and analyzing linear and quadratic equations. The script 
utilizes object-oriented programming principles, including inheritance and polymorphism. 

Key Components:
- The 'Equation' class provides a framework for defining mathematical equations with 
  coefficients, types, and methods for solving and analyzing.
- The 'LinearEquation' and 'QuadraticEquation' subclasses implement specific logic for 
  solving their respective equations and analyzing their properties.
- The 'solver' function formats and displays the solutions and analysis results for any 
  given equation instance.

Usage:
You can create instances of 'LinearEquation' or 'QuadraticEquation' with their respective 
coefficients and pass them to the 'solver' function to get formatted results.
"""


# Importing necessary modules
from abc import ABC, abstractmethod  # Importing ABC and abstractmethod for defining abstract base classes
import re  # Importing re for regular expressions to help format the output string

# Abstract base class for all equations
class Equation(ABC):
    # Attributes that must be defined in subclasses
    degree: int  # Degree of the equation (e.g., 1 for linear, 2 for quadratic)
    type: str    # Type of the equation (e.g., "Linear Equation")

    # Constructor that initializes coefficients
    def __init__(self, *args):
        # Validate that the number of arguments matches the degree of the equation
        if (self.degree + 1) != len(args):
            raise TypeError(
                f"'Equation' object takes {self.degree + 1} positional arguments but {len(args)} were given"
            )
        # Check that all coefficients are either integers or floats
        if any(not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")
        # Ensure the leading coefficient (highest degree) is not zero
        if args[0] == 0:
            raise ValueError("Highest degree coefficient must be different from zero")
        # Create a dictionary of coefficients with their respective powers
        self.coefficients = {(len(args) - n - 1): arg for n, arg in enumerate(args)}

    # This method ensures subclasses have the required attributes
    def __init_subclass__(cls):
        # Check if the subclass has the degree attribute
        if not hasattr(cls, "degree"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'"
            )
        # Check if the subclass has the type attribute
        if not hasattr(cls, "type"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'type'"
            )

    # String representation of the equation
    def __str__(self):
        terms = []  # List to hold formatted terms of the equation
        for n, coefficient in self.coefficients.items():
            if not coefficient:  # Skip terms with a coefficient of 0
                continue
            # Format each term based on its degree
            if n == 0:  # Constant term
                terms.append(f'{coefficient:+}')  # Include sign for constant term
            elif n == 1:  # Linear term
                terms.append(f'{coefficient:+}x')  # Include sign for linear term
            else:  # Higher degree terms
                terms.append(f"{coefficient:+}x**{n}")  # Include sign and degree
        # Join all terms into a single string representing the equation
        equation_string = ' '.join(terms) + ' = 0'
        # Remove the "1" in front of x if present, e.g., "1x" becomes "x"
        return re.sub(r"(?<!\d)1(?=x)", "", equation_string.strip("+"))

    # Abstract method to solve the equation (must be implemented in subclasses)
    @abstractmethod
    def solve(self):
        pass

    # Abstract method to analyze the equation (must be implemented in subclasses)
    @abstractmethod
    def analyze(self):
        pass


# Subclass for linear equations
class LinearEquation(Equation):
    degree = 1  # Degree of the linear equation
    type = 'Linear Equation'  # Type of equation as a string

    # Method to solve the linear equation
    def solve(self):
        a, b = self.coefficients.values()  # Unpack coefficients
        x = -b / a  # Calculate the root using the formula x = -b/a
        return [x]  # Return the root in a list

    # Method to analyze the linear equation
    def analyze(self):
        slope, intercept = self.coefficients.values()  # Unpack coefficients
        return {'slope': slope, 'intercept': intercept}  # Return slope and intercept as a dictionary


# Subclass for quadratic equations
class QuadraticEquation(Equation):
    degree = 2  # Degree of the quadratic equation
    type = 'Quadratic Equation'  # Type of equation as a string

    # Constructor that initializes the coefficients and calculates the delta (discriminant)
    def __init__(self, *args):
        super().__init__(*args)  # Call the constructor of the base class
        a, b, c = self.coefficients.values()  # Unpack coefficients
        self.delta = b**2 - 4 * a * c  # Calculate the discriminant (delta)

    # Method to solve the quadratic equation
    def solve(self):
        if self.delta < 0:  # If delta is negative, there are no real roots
            return []  # Return an empty list
        a, b, _ = self.coefficients.values()  # Unpack coefficients
        # Calculate both roots using the quadratic formula
        x1 = (-b + (self.delta) ** 0.5) / (2 * a)
        x2 = (-b - (self.delta) ** 0.5) / (2 * a)
        if self.delta == 0:  # If delta is zero, there is one unique root
            return [x1]  # Return a list with the single root

        return [x1, x2]  # Return a list with both roots

    # Method to analyze the quadratic equation
    def analyze(self):
        a, b, c = self.coefficients.values()  # Unpack coefficients
        x = -b / (2 * a)  # Calculate the x-coordinate of the vertex
        y = a * x**2 + b * x + c  # Calculate the y-coordinate of the vertex (function value at x)
        # Determine the concavity and type of vertex (min/max)
        if a > 0:
            concavity = 'upwards'  # If a is positive, concavity is upwards
            min_max = 'min'  # Vertex is a minimum point
        else:
            concavity = 'downwards'  # If a is negative, concavity is downwards
            min_max = 'max'  # Vertex is a maximum point
        return {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}  # Return analysis results


# Solver function that processes the equation and formats the output
def solver(equation):
    # Ensure the provided argument is an instance of Equation
    if not isinstance(equation, Equation):
        raise TypeError("Argument must be an Equation object")

    # Create the output string with the type of equation
    output_string = f'\n{equation.type:-^24}'  # Centered title with dashes
    output_string += f'\n\n{equation!s:^24}\n\n'  # String representation of the equation centered
    output_string += f'{"Solutions":-^24}\n\n'  # Header for solutions
    results = equation.solve()  # Call the solve method to get results
    # Use match/case to handle different types of results
    match results:
        case []:  # No real roots found
            result_list = ['No real roots']
        case [x]:  # One real root found
            result_list = [f'x = {x:+.3f}']  # Format the root
        case [x1, x2]:  # Two real roots found
            result_list = [f'x1 = {x1:+.3f}', f'x2 = {x2:+.3f}']  # Format both roots
    # Add each result to the output string
    for result in result_list:
        output_string += f'{result:^24}\n'  # Center each result

    output_string += f'\n{"Details":-^24}\n\n'  # Header for details
    details = equation.analyze()  # Call the analyze method to get details
    # Use match/case to format details based on the type of equation
    match details:
        case {'slope': slope, 'intercept': intercept}:  # Linear equation details
            details_list = [f'slope = {slope:>16.3f}', f'y-intercept = {intercept:>10.3f}']
        case {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}:  # Quadratic equation details
            coord = f'({x:.3f}, {y:.3f})'  # Format vertex coordinates
            details_list = [f'concavity = {concavity:>12}', f'{min_max} = {coord:>18}']  # Format analysis results
    # Add each detail to the output string
    for detail in details_list:
        output_string += f'{detail}\n'  # Add detail line

    return output_string  # Return the formatted output string


# Example usage of the solver function with a linear and a quadratic equation
lin_eq = LinearEquation(2, 3)  # Create an instance of LinearEquation with coefficients 2 and 3
quadr_eq = QuadraticEquation(1, -3, 2)  # Create an instance of QuadraticEquation with coefficients 1, -3, and 2
print(solver(quadr_eq))  # Call the solver function and print the output for the quadratic equation