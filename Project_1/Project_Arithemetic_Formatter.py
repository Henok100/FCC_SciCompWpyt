# Description: This script formats and arranges a series of arithmetic problems in a visually aligned way. 
# It can optionally display the results of each problem as well.

def arithmetic_arranger(problems, show_answers=False):
    # Check if there are more than 5 problems; if so, return an error message.
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Initialize lists to store each line of the final formatted output.
    first_line = []   # Holds the first operands (numbers) in each problem.
    second_line = []  # Holds the operator (+ or -) and the second operand.
    dash_line = []    # Holds a line of dashes (separator) for each problem.
    results_line = [] # Optionally holds the result of each arithmetic operation.

    # Loop through each problem in the list
    for problem in problems:
        # Split the problem into the two operands and the operator.
        # Example: "32 + 698" becomes ['32', '+', '698']
        op1, operator, op2 = problem.split()

        # Validate operands and operator:
        # Ensure operands are not longer than 4 digits
        if len(op1) > 4 or len(op2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Ensure both operands are numeric (i.e., contain only digits)
        if not op1.isdigit() or not op2.isdigit():
            return "Error: Numbers must only contain digits."

        # Ensure that the operator is either '+' or '-'
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # If the optional show_answers flag is True, calculate the result of the operation
        if show_answers:
            # Perform the appropriate arithmetic operation
            if operator == '+':
                result = str(int(op1) + int(op2))  # Addition
            else:
                result = str(int(op1) - int(op2))  # Subtraction

        # Determine the width for formatting each problem based on the larger operand
        total_width = max(len(op1), len(op2)) + 2  # Add 2 for the operator and space

        # Format the first operand to be right-aligned with the determined width.
        first_line.append(op1.rjust(total_width))
        
        # Format the second line with the operator and second operand.
        second_line.append(f"{operator} {op2.rjust(total_width - 2)}")
        
        # Create a line of dashes ('-') that matches the width of the problem.
        dash_line.append('-' * total_width)
        
        # If showing answers, format the result to be right-aligned with the total width.
        if show_answers:
            results_line.append(result.rjust(total_width))

    # Join all parts of each problem into their respective lines using 4 spaces ('    ') between problems.
    first_line_str = '    '.join(first_line)
    second_line_str = '    '.join(second_line)
    dash_line_str = '    '.join(dash_line)
    
    # If show_answers is True, join and return all lines including the result line.
    if show_answers:
        results_line_str = '    '.join(results_line)
        return f"{first_line_str}\n{second_line_str}\n{dash_line_str}\n{results_line_str}"
    # Otherwise, return just the arranged arithmetic problems without results.
    else:
        return f"{first_line_str}\n{second_line_str}\n{dash_line_str}"

# Example usage: We arrange 4 arithmetic problems and display the answers.
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))


"""
Key Concepts:
Validation:

The script first validates that the input problems follow certain rules:
No more than 5 problems.
Each operand (number) must be no more than 4 digits.
Each operand must consist only of digits (i.e., no letters or special characters).
The operator must be either + or -.
Formatting:

Each operand is right-aligned to ensure the problems are visually consistent.
A line of dashes is used to separate the problem from its solution.
Four spaces separate each problem from the next.
Optional Display of Answers:

If the show_answers flag is set to True, the result of each problem is calculated and displayed under the corresponding dash line.
If show_answers is False, only the formatted problems are shown, without answers.
String Alignment:

rjust(width) is used to right-align each operand so that it aligns neatly when displayed.
"""