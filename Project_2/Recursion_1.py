# This script simulates the Tower of Hanoi problem using an iterative approach. 
# It calculates the allowed moves based on the number of disks and performs 
# those moves between three rods (A, B, and C). The objective is to move all 
# disks from the source rod (A) to the target rod (C) using the auxiliary rod (B), 
# following the rules that only one disk can be moved at a time and a larger 
# disk cannot be placed on top of a smaller disk.

NUMBER_OF_DISKS = 4  # Number of disks in the puzzle
number_of_moves = 2 ** NUMBER_OF_DISKS - 1  # Total moves required to solve the puzzle
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),  # Initialize source rod with disks (largest to smallest)
    'B': [],  # Auxiliary rod, initially empty
    'C': []   # Target rod, initially empty
}

def make_allowed_move(rod1, rod2):    
    forward = False  # Flag to determine the direction of the move
    # Check if the move is allowed
    if not rods[rod2]:  # If the target rod is empty
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:  # Check if the top disk of rod1 is smaller than the top disk of rod2
        forward = True              
    
    if forward:
        # If the move is allowed from rod1 to rod2
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        rods[rod2].append(rods[rod1].pop())  # Move the disk from rod1 to rod2
    else:
        # If the move is allowed from rod2 to rod1
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())  # Move the disk from rod2 to rod1
    
    # Display the current state of all rods after the move
    print(rods, '\n')

def move(n, source, auxiliary, target):
    # Display starting configuration before any moves are made
    print(rods, '\n')
    for i in range(number_of_moves):  # Iterate over the total number of moves
        remainder = (i + 1) % 3  # Determine the remainder to alternate moves
        if remainder == 1:  # For the first move in the set of three
            if n % 2 != 0:  # If the number of disks is odd
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)  # Move between source and target
            else:  # If the number of disks is even
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)  # Move between source and auxiliary
        elif remainder == 2:  # For the second move in the set of three
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)  # Move between source and auxiliary
            else:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)  # Move between source and target
        elif remainder == 0:  # For the third move in the set of three
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)  # Move between auxiliary and target

# Initiate the call to start moving disks from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')
