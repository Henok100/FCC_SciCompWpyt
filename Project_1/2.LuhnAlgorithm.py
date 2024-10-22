"""
This script verifies whether a given credit card number is valid using the Luhn algorithm. 
The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, 
including credit card numbers.

How it works:
1. **Doubling Every Second Digit**: Starting from the rightmost digit (the check digit), double the 
value of every second digit. 
2. **Handling Values Greater than 9**: If doubling a digit results in a value greater than 9, subtract 
9 from the result (or alternatively, sum the digits of the result).
3. **Summing All Digits**: Add together all the digits in the modified number.
4. **Divisibility Check**: If the total sum is divisible by 10, then the card number is considered valid.

Example:
- **Credit Card Number**: 4539 1488 0343 6467

**Steps to Validate**:
1. Starting from the right, double every second digit:
   - Original Digits: 4 5 3 9 1 4 8 8 0 3 4 3 6 4 6 7
   - After Doubling Every Second Digit: 4 10 3 18 1 8 8 16 0 6 4 6 6 8 6 14

2. Adjust any doubled values greater than 9:
   - Adjusted Digits: 4 (4) 1 (0) 3 (9) 1 (8) 1 (8) 7 (6) 0 (0) 3 (6) 6 (6) 8 (8) 6 (6) 5 (4) 6 (6) 8 (7)

3. Now sum all the digits:
   - Sum = 4 + 5 + 6 + 9 + 1 + 4 + 8 + 8 + 0 + 3 + 4 + 3 + 6 + 4 + 6 + 7 = 70

4. Check if the sum is divisible by 10:
   - 70 % 10 = 0, which means the card number is valid.

In conclusion, if the final sum is divisible by 10, the card number is considered valid according to the Luhn 
algorithm. This method helps in preventing accidental errors in credit card numbers.
"""


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