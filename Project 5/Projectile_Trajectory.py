"""
This script simulates the trajectory of a projectile given its initial speed, height, and launch angle.
It consists of two main classes:

1. Projectile: 
   - Handles the physics calculations such as displacement and trajectory coordinates. 
   - Uses trigonometric functions to compute the horizontal and vertical components of the motion.

2. Graph: 
   - Takes the calculated trajectory coordinates and generates both a table of values and a visual representation.
   - The graph is text-based, plotting the projectile's path using symbols.

The script also includes a helper function to initialize a projectile and display its trajectory and details.

Example:
- Projectile launched with a speed of 10 m/s, height of 3 m, and angle of 45 degrees.
"""


import math

# Constant for gravitational acceleration (in m/s^2)
GRAVITATIONAL_ACCELERATION = 9.81

# Symbols used for plotting the projectile and axis in the graph
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    # __slots__ is used to restrict the attributes allowed for this class, optimizing memory usage.
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        # Initialize the projectile with speed (m/s), height (m), and angle (degrees).
        self.__speed = speed  # Speed of the projectile
        self.__height = height  # Initial height from the ground
        self.__angle = math.radians(angle)  # Convert angle to radians for trigonometric calculations

    # The __str__ method provides a readable string representation when you print the object.
    def __str__(self):
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {self.angle}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    # This private method calculates the horizontal displacement (range) of the projectile.
    def __calculate_displacement(self):
        # Horizontal and vertical components of the velocity
        horizontal_component = self.__speed * math.cos(self.__angle)  # Speed * cos(angle) gives the horizontal component
        vertical_component = self.__speed * math.sin(self.__angle)  # Speed * sin(angle) gives the vertical component
        
        # The squared vertical component and height are used to calculate the overall displacement
        squared_component = vertical_component ** 2  # Vertical velocity squared
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height  # 2gh for the height
        
        # sqrt(v^2 + 2gh) gives the total effect of gravity and initial height
        sqrt_component = math.sqrt(squared_component + gh_component)
        
        # Horizontal displacement formula combining all components
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION

    # Calculates the y-coordinate (height) of the projectile at a given x-coordinate (horizontal distance).
    def __calculate_y_coordinate(self, x):
        height_component = self.__height  # Initial height of the projectile
        angle_component = math.tan(self.__angle) * x  # Tangent of the angle multiplied by the distance gives part of the height
        
        # GRAVITATIONAL_ACCELERATION * x² / (2 * speed² * cos²(angle)) calculates the effect of gravity over the distance
        acceleration_component = GRAVITATIONAL_ACCELERATION * x ** 2 / (
            2 * self.__speed ** 2 * math.cos(self.__angle) ** 2)
        
        # y = initial height + angle contribution - gravity's effect
        y_coordinate = height_component + angle_component - acceleration_component

        return y_coordinate

    # Calculates and returns a list of all (x, y) coordinates of the projectile's path.
    def calculate_all_coordinates(self):
        return [
            (x, self.__calculate_y_coordinate(x))  # Pair of x and corresponding y for each step of the distance
            for x in range(math.ceil(self.__calculate_displacement()))  # Displacement defines how far the projectile goes
        ]

    # Properties to access speed, height, and angle in a protected manner (getters and setters).

    @property
    def height(self):
        return self.__height  # Getter for height

    @property
    def angle(self):
        return round(math.degrees(self.__angle))  # Getter for angle, converting back to degrees

    @property
    def speed(self):
        return self.__speed  # Getter for speed

    @height.setter
    def height(self, n):
        self.__height = n  # Setter for height

    @angle.setter
    def angle(self, n):
        self.__angle = math.radians(n)  # Setter for angle, converting input degrees to radians

    @speed.setter
    def speed(self, s):
        self.__speed = s  # Setter for speed
    
    # The __repr__ method provides a more detailed string for debugging.
    def __repr__(self):
        return f'{self.__class__}({self.speed}, {self.height}, {self.angle})'

class Graph:
    # __slots__ is used to restrict the attributes allowed for this class, optimizing memory usage.
    __slots__ = ('__coordinates')

    def __init__(self, coord):
        # Takes in the coordinates of the projectile trajectory to graph it later
        self.__coordinates = coord

    # __repr__ method to return a string for debugging purposes
    def __repr__(self):
        return f"Graph({self.__coordinates})"

    # Creates a text-based table showing the x and y coordinates of the projectile's trajectory
    def create_coordinates_table(self):
        table = '\n  x      y\n'  # Table header
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'  # Format: right-aligned x and y coordinates with 2 decimal precision for y

        return table

    # Creates a visual trajectory graph of the projectile's path using characters.
    def create_trajectory(self):
        # Round all the coordinates to the nearest integer to plot on the graph
        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]

        # Determine the maximum x and y to create a grid
        x_max = max(rounded_coords, key=lambda i: i[0])[0]  # Max x-value
        y_max = max(rounded_coords, key=lambda j: j[1])[1]  # Max y-value

        # Create a grid filled with spaces (' ') for the size of the trajectory
        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        # Place the projectile symbol at each coordinate in the grid
        for x, y in rounded_coords:
            matrix_list[-1 - y][x] = PROJECTILE  # -1-y makes sure the plot is flipped vertically (since index 0 is top)

        # Join the rows of the grid to form the graph
        matrix = ["".join(line) for line in matrix_list]

        # Add axis labels (⊣ for y-axis and T for x-axis)
        matrix_axes = [y_axis_tick + row for row in matrix]
        matrix_axes.append(" " + x_axis_tick * (len(matrix[0])))  # x-axis at the bottom

        # Return the final graph as a string
        graph = "\n" + "\n".join(matrix_axes) + "\n"

        return graph

# Utility function to demonstrate the projectile and graph creation
def projectile_helper(speed, height, angle):
    # Create a projectile object with the provided values
    projectile = Projectile(speed, height, angle)
    
    # Print the details of the projectile
    print(projectile)
    
    # Calculate the trajectory coordinates and create a graph
    coordinates = projectile.calculate_all_coordinates()
    graph = Graph(coordinates)
    
    # Print the table of coordinates
    print(graph.create_coordinates_table())
    
    # Print the graph of the trajectory
    print(graph.create_trajectory())

# Call the helper function with specific values (speed=10 m/s, height
