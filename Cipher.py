# This script implements the Vigenère cipher, a method of encrypting text by using a key to shift letters.
# The key is repeated over the length of the message, and each letter in the message is shifted 
# based on the corresponding letter in the key. This script can both encrypt and decrypt messages.

# The encrypted text we want to decode
text = 'mrttaqrhknsw ih puggrur'

# The key used for encryption and decryption
custom_key = 'happycoding'

# Function that performs the Vigenère cipher, capable of both encryption and decryption
def vigenere(message, key, direction=1):  # 'direction=1' means encryption; 'direction=-1' means decryption
    key_index = 0  # To track which character in the key we are using
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # The alphabet used for shifting letters
    final_message = ''  # This will store the encrypted or decrypted result

    # Loop through each character in the message after converting it to lowercase
    for char in message.lower():

        # If the character is not a letter (like space or punctuation), just add it to the result as is
        if not char.isalpha():
            final_message += char
        else:        
            # Get the corresponding key character based on the current key_index
            # The modulo operator ensures that we cycle through the key as needed
            key_char = key[key_index % len(key)]
            key_index += 1  # Move to the next key character for the next iteration

            # Find the position of the key character in the alphabet (this determines how much to shift)
            offset = alphabet.index(key_char)
            
            # Find the position of the current message character in the alphabet
            index = alphabet.find(char)
            
            # Calculate the new position of the message character by shifting it
            # 'direction' determines if it's encryption (+) or decryption (-)
            new_index = (index + offset*direction) % len(alphabet)
            
            # Add the new encrypted/decrypted character to the final message
            final_message += alphabet[new_index]
    
    # Return the full encrypted or decrypted message
    return final_message

# Function to encrypt a message using the Vigenère cipher
def encrypt(message, key):
    return vigenere(message, key)

# Function to decrypt a message using the Vigenère cipher
def decrypt(message, key):
    return vigenere(message, key, -1)  # 'direction=-1' means we are decrypting (reverse shift)

# Print the original encrypted text
print(f'\nEncrypted text: {text}')

# Print the key used for encryption/decryption
print(f'Key: {custom_key}')

# Decrypt the text using the custom key and print the decrypted message
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')

"""
Breakdown:

The Vigenère cipher algorithm:

    For each letter in the message, the corresponding letter from the key determines how much the message letter is shifted within the alphabet.

    When decrypting, the shift is reversed by applying direction = -1 to move backwards in the alphabet.

Handling non-alphabet characters: Any character that isn't a letter (such as spaces or punctuation) is left unchanged.

Key cycling: The key repeats itself over the length of the message using the modulo operator, ensuring that the key is reused as needed.
"""