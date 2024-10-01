import re  # The 're' module is used for regular expressions, which allow us to search for patterns in strings
import secrets  # The 'secrets' module provides cryptographically secure random number generation, useful for generating passwords securely
import string  # The 'string' module contains predefined constants like ascii_letters, digits, and punctuation

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    This function generates a password with the specified requirements:
    - length: total length of the password (default: 16 characters)
    - nums: the minimum number of digits required
    - special_chars: the minimum number of special characters required
    - uppercase: the minimum number of uppercase letters required
    - lowercase: the minimum number of lowercase letters required
    """

    # Define the possible character sets for the password
    letters = string.ascii_letters  # Contains both lowercase and uppercase letters (a-z, A-Z)
    digits = string.digits          # Contains digits (0-9)
    symbols = string.punctuation    # Contains special characters like !@#$%&*

    # Combine all possible characters into a single string
    all_characters = letters + digits + symbols

    # Continue generating passwords until one meets all requirements
    while True:
        password = ''  # Start with an empty password string
        # Generate a random password of the specified length
        for _ in range(length):
            password += secrets.choice(all_characters)  # Randomly pick characters from 'all_characters' and append to password
        
        # List of constraints: each tuple contains (minimum_required, regex pattern to check for that type of character)
        constraints = [
            (nums, r'\d'),  # At least 'nums' number of digits (0-9). Regex pattern \d matches any digit.
            (special_chars, fr'[{symbols}]'),  # At least 'special_chars' number of special characters. The pattern checks for any character in 'symbols'.
            (uppercase, r'[A-Z]'),  # At least 'uppercase' number of uppercase letters (A-Z). Regex [A-Z] matches uppercase letters.
            (lowercase, r'[a-z]')  # At least 'lowercase' number of lowercase letters (a-z). Regex [a-z] matches lowercase letters.
        ]

        # Check if the password meets all constraints
        if all(
            constraint <= len(re.findall(pattern, password))  # For each constraint, check if the count of matching characters meets the minimum required
            for constraint, pattern in constraints  # Iterate over each constraint and its corresponding regex pattern
        ):
            break  # If the password meets all requirements, exit the while loop

    # Return the valid password
    return password
    
if __name__ == '__main__':
    # If this script is being executed directly (not imported as a module), generate and print a password
    new_password = generate_password()  # Generate a password using the default parameters (length=16, at least 1 digit, 1 special char, 1 uppercase, 1 lowercase)
    print('Generated password:', new_password)  # Output the generated password