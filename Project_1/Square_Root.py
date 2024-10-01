"""
This script finds the square root of a given number using the Bisection Method, 
a numerical technique for solving equations by repeatedly narrowing down the interval 
where the solution lies.
"""
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    # The bisection method is a numerical technique used to find the root (or zero) of a function. 
    # In this case, we're using it to find the square root of a number. 
    # The idea is to repeatedly narrow down the interval [low, high] where the root lies by checking the midpoint.

    # Parameters:
    # square_target: The number for which we want to find the square root.
    # tolerance: How close the approximation of the square root needs to be (i.e., the margin of error we're allowing).
    # max_iterations: The maximum number of steps we will take before giving up if no accurate root is found.

    # Check for edge cases: square root of negative numbers is not defined in real numbers.
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    # Special cases: if the target is 0 or 1, return the result immediately.
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        # Set initial bounds for bisection: 
        # 'low' starts at 0 and 'high' starts at either 1 (if target is less than 1) or the target number itself.
        low = 0
        high = max(1, square_target)

        # Initialize root to None, will be set when we find a valid approximation.
        root = None
        
        # Loop through up to the maximum number of iterations to narrow down the interval [low, high].
        for _ in range(max_iterations):
            mid = (low + high) / 2  # Find the midpoint of the current interval.
            square_mid = mid**2  # Calculate the square of the midpoint.
            
            # Check if the squared value is close enough to the target (within the tolerance).
            if abs(square_mid - square_target) < tolerance:
                root = mid  # If it's close enough, we've found the root!
                break

            # If the square of the midpoint is less than the target, the root must be larger, so adjust 'low'.
            elif square_mid < square_target:
                low = mid

            # If the square of the midpoint is greater than the target, the root must be smaller, so adjust 'high'.
            else:
                high = mid

        # If we reach the maximum number of iterations without finding a root within the tolerance, print a message.
        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        # If we found a root, print the result.
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    # Return the root value or None if no root was found within the maximum iterations.
    return root

# Example usage:
N = 16  # We're finding the square root of 16
square_root_bisection(N)  # Call the function to compute the square root of N

