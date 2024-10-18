"""
This script simulates drawing colored balls from a hat and calculates the probability
of drawing a specific combination of colors. It defines a 'Hat' class to represent
the hat containing colored balls, allowing for the initialization of the hat with 
specified quantities of each color. The 'draw' method enables the random removal of 
balls from the hat.

The script also includes a function 'experiment' that performs multiple trials of 
drawing balls from the hat and checks if the drawn balls match the expected combination 
of colors. By running the experiment a specified number of times, it calculates the 
probability of drawing the desired outcome.

This is useful for understanding probability in scenarios involving random sampling 
from a finite set.
"""

import copy  # Importing the copy module to allow deep copying of objects
import random  # Importing the random module to enable random selection of balls
from collections import Counter  # Importing Counter to easily count occurrences of each ball color

class Hat:
    def __init__(self, **colors):
        """
        Initializes a Hat object containing colored balls.
        Accepts keyword arguments where the key is the color of the ball
        and the value is the number of balls of that color.
        If no colors are provided, raises a ValueError.
        """
        self.contents = []  # List to hold the contents of the hat

        if not colors:  # Check if no colors were provided
            raise ValueError("At least one keyword argument must be provided.")
        for key, value in colors.items():  # Iterate through the provided colors
            for _ in range(value):  # Add the specified number of balls to the hat
                self.contents.append(f'{key}')  # Append the color to the contents list

    def draw(self, draw_num):
        """
        Draws a specified number of balls from the hat randomly.
        If the number to draw exceeds the number of balls available, all balls are drawn.
        Returns a list of the drawn balls.
        """
        removed_ball = []  # List to hold the drawn balls
        if draw_num >= len(self.contents):  # Check if more balls are requested than available
            removed_ball = self.contents.copy()  # Copy all balls
            self.contents.clear()  # Clear the contents of the hat
            return removed_ball  # Return all balls drawn

        for _ in range(draw_num):  # Draw the specified number of balls
            removed_ball.append(self.contents.pop(random.randint(0, len(self.contents) - 1)))  # Randomly remove a ball
        return removed_ball  # Return the list of drawn balls

def matches_expected(balls_drawn, expected_balls):
    """
    Checks if the drawn balls match the expected quantities of colors.
    Takes a dictionary of balls drawn and a dictionary of expected balls.
    Returns True if the drawn balls meet or exceed the expected amounts; otherwise, False.
    """
    for color, count in expected_balls.items():  # Iterate through each expected color
        if balls_drawn.get(color, 0) < count:  # Check if the drawn count is less than expected
            return False  # Return False if the expected count is not met
    return True  # Return True if all expected counts are met

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Conducts multiple experiments to determine the probability of drawing 
    a specified combination of colored balls from the hat.
    
    Parameters:
    - hat: an instance of the Hat class
    - expected_balls: a dictionary of expected ball colors and counts
    - num_balls_drawn: the number of balls to draw in each experiment
    - num_experiments: the number of experiments to perform
    
    Returns the probability of drawing the expected combination of balls.
    """
    successful_experiments = 0  # Counter for successful experiments
    for _ in range(num_experiments):  # Perform the number of specified experiments
        Hat = copy.deepcopy(hat)  # Create a deep copy of the hat for each experiment
        balls_drawn = Hat.draw(num_balls_drawn)  # Draw the specified number of balls
        balls_drawn = dict(Counter(balls_drawn))  # Count the occurrences of each drawn ball color

        if matches_expected(balls_drawn, expected_balls):  # Check if the drawn balls match expectations
            successful_experiments += 1  # Increment the success count

    return successful_experiments / num_experiments  # Return the probability of success

# Create a Hat object with specified colors and quantities
hat = Hat(black=6, red=4, green=3)

# Run the experiment with the hat and specified parameters
probability = experiment(hat=hat,
                  expected_balls={'red': 2, 'green': 1},  # Expected combination of colors
                  num_balls_drawn=5,  # Number of balls to draw
                  num_experiments=2000)  # Number of experiments to perform

print(probability)  # Print the resulting probability

