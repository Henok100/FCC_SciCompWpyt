# This script verifies whether a given credit card number is valid using the Luhn algorithm.
# The Luhn algorithm works by doubling every second digit from the right (starting from the second-to-last digit).
# If the result of doubling a digit is greater than 9, the two digits are summed together (e.g., 12 becomes 1 + 2 = 3).
# Finally, all the digits are summed, and if the total is divisible by 10, the card number is considered valid.

def verify_card_number(card_number):
    sum_of_odd_digits = 0  # This will store the sum of all digits in the odd positions (from the right)
    
    # Reverse the card number so we can easily access odd/even positions from the right
    card_number_reversed = card_number[::-1]  
    
    # Select all odd-positioned digits (0-indexed, so we use [::2] to grab every other digit)
    odd_digits = card_number_reversed[::2]  
    
    # Loop through each odd-positioned digit and add them directly to the sum
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)  # Convert digit to integer and accumulate it into sum_of_odd_digits

    sum_of_even_digits = 0  # This will store the sum of all doubled even-positioned digits
    
    # Select all even-positioned digits (starting from index 1, and every other after that)
    even_digits = card_number_reversed[1::2]  
    
    # Loop through each even-positioned digit
    for digit in even_digits:
        number = int(digit) * 2  # Double the digit
        
        # If doubling the digit gives a result >= 10, sum the individual digits (e.g., 12 becomes 1 + 2)
        if number >= 10:
            number = (number // 10) + (number % 10)  # Split the number into its tens and units digits, then add them together
            
        sum_of_even_digits += number  # Add the result to the sum_of_even_digits

    # Calculate the total sum by adding both odd and even digit sums
    total = sum_of_odd_digits + sum_of_even_digits

    # Return True if the total is divisible by 10, meaning the card number is valid according to the Luhn algorithm
    return total % 10 == 0


def main():
    card_number = '4111-1111-4555-1241'  # Example card number to be verified
    
    # Create a translation table to remove hyphens and spaces from the card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    
    # Translate the card number (removing any hyphens or spaces) using the translation table
    translated_card_number = card_number.translate(card_translation)

    # Verify the card number and print whether it is valid or invalid
    if verify_card_number(translated_card_number):
        print('VALID!')  # Print VALID! if the card passes the Luhn check
    else:
        print('INVALID!')  # Print INVALID! if the card fails the Luhn check


# Call the main function to run the verification process
main()


"""
Breakdown:

Reversing the card number: This allows us to easily process every second digit starting from the right, which is a requirement of the Luhn algorithm.

Processing odd-positioned digits: We just sum them directly.

Processing even-positioned digits: We double each one, and if the result is greater than 9, we split it into two digits and sum those digits.

Final check: If the total sum of the processed digits is divisible by 10, the card is valid.
"""