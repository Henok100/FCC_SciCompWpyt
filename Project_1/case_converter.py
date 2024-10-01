# Description: This script converts a given PascalCase or camelCase string into snake_case format using a for loop.

def convert_to_snake_case(pascal_or_camel_cased_string):
    # Initialize an empty list to hold each character of the snake_cased string
    snake_cased_char_list = []

    # Loop through each character in the provided string
    for char in pascal_or_camel_cased_string:

        # If the character is uppercase (indicating the start of a new word)
        if char.isupper():
            # Convert the uppercase character to lowercase and prepend it with an underscore ('_')
            converted_character = '_' + char.lower()
            # Append the modified character to the snake_cased_char_list
            snake_cased_char_list.append(converted_character)
        else:
            # If the character is already lowercase, append it as is
            snake_cased_char_list.append(char)

    # After looping through all characters, join the list into a string
    snake_cased_string = ''.join(snake_cased_char_list)

    # If the first character was uppercase, we may have added a leading underscore.
    # Remove any leading underscores by stripping them
    clean_snake_cased_string = snake_cased_string.strip('_')

    # Return the final snake_cased string
    return clean_snake_cased_string

def main():
    # Test the function with a PascalCase string and print the result
    print(convert_to_snake_case('aLongAndComplexString'))

main()


# Description: This script converts a given PascalCase or camelCase string into snake_case format using list comprehension for a more compact approach.

def convert_to_snake_case(pascal_or_camel_cased_string):
    # List comprehension that processes each character in the string:
    # - If the character is uppercase, prepend it with an underscore ('_') and convert it to lowercase.
    # - Otherwise, keep the character as it is (i.e., lowercase characters remain unchanged).
    snake_cased_char_list = ['_' + char.lower() if char.isupper() else char for char in pascal_or_camel_cased_string]

    # Join the list into a single string and strip any leading underscores (which could result from an uppercase first letter)
    return ''.join(snake_cased_char_list).strip('_')

def main():
    # Test the function with another PascalCase string and print the result
    print(convert_to_snake_case('IAmAPascalCasedString'))

main()

"""
Explanation of Key Concepts:
1. for Loop vs. List Comprehension:
Script 1 uses a traditional for loop to iterate over each character in the string, applying a check for uppercase letters and building a list of characters.
Script 2 achieves the same result using a more concise list comprehension, where the entire process of checking and converting characters is done in a single line.
2. char.isupper():
This function checks whether the character is an uppercase letter. It helps identify when to insert an underscore before the letter and convert it to lowercase for the snake_case format.
3. String .join():
This method is used to combine all the elements in the list snake_cased_char_list into a single string. It avoids the need for loops or concatenation inside the for loop.
4. .strip('_'):
This function removes any leading or trailing underscores from the string. In both scripts, this is used to handle cases where the first character of the original string was uppercase, which would have resulted in an extra underscore at the beginning of the result.
"""