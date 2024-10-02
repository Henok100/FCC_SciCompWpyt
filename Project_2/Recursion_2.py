# This script implements the Tower of Hanoi problem, which is a classic 
# mathematical puzzle. The objective is to move a stack of disks from one 
# rod (source) to another rod (target) using a third rod (auxiliary), with 
# the constraint that you can only move one disk at a time and a larger 
# disk cannot be placed on top of a smaller disk. The script uses recursion 
# to solve the problem and prints the state of the rods after each move.

NUMBER_OF_DISKS = 5  # Number of disks in the puzzle
A = list(range(NUMBER_OF_DISKS, 0, -1))  # Initialize source rod with disks (largest to smallest)
B = []  # Auxiliary rod, initially empty
C = []  # Target rod, initially empty

def move(n, source, auxiliary, target):
    # Base case: if there are no disks to move, do nothing
    if n <= 0:
        return

    # Move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
        
    # Move the nth disk from source to target
    target.append(source.pop())
        
    # Display the current state of rods after the move
    print(A, B, C, '\n')
        
    # Move the n - 1 disks that we left on auxiliary onto target
    move(n - 1, auxiliary, source, target)

# Initiate the call to start moving disks from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)
