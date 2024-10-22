"""
This script implements the Vigenère cipher, a method of encrypting text by using a key to shift letters. 
The Vigenère cipher is a form of polyalphabetic substitution cipher that uses a keyword to determine the shift for 
each letter in the plaintext.

How it works:
1. **Key Repetition**: The key is repeated over the length of the message. If the key is shorter than the message, 
it will loop back to the beginning of the key once it reaches its end.
2. **Letter Shifting**: Each letter in the message is shifted based on the corresponding letter in the key. 
The shift value is determined by the position of the letter in the alphabet (A=0, B=1, C=2, ..., Z=25).

Example:
- **Plaintext**: "ATTACKATDAWN"
- **Key**: "LEMON"
- **Extended Key**: "LEMONLEMONLE"
    - The key "LEMON" is repeated to match the length of the plaintext.

**Encryption Process**:
- For each letter in the plaintext:
    - A (0) shifted by L (11): (0 + 11) % 26 = 11 → L
    - T (19) shifted by E (4): (19 + 4) % 26 = 23 → X
    - T (19) shifted by M (12): (19 + 12) % 26 = 5 → F
    - A (0) shifted by O (14): (0 + 14) % 26 = 14 → O
    - C (2) shifted by N (13): (2 + 13) % 26 = 15 → P
    - K (10) shifted by L (11): (10 + 11) % 26 = 21 → V
    - A (0) shifted by E (4): (0 + 4) % 26 = 4 → E
    - T (19) shifted by M (12): (19 + 12) % 26 = 5 → F
    - D (3) shifted by O (14): (3 + 14) % 26 = 17 → R
    - A (0) shifted by N (13): (0 + 13) % 26 = 13 → N
    - W (22) shifted by L (11): (22 + 11) % 26 = 7 → H
    - N (13) shifted by E (4): (13 + 4) % 26 = 17 → R

- **Encrypted Text**: "LXFOPVEFRNHR"

**Decryption Process**:
- To decrypt the ciphertext, each letter is shifted backward by the corresponding letter in the key:
    - L (11) shifted by L (11): (11 - 11 + 26) % 26 = 0 → A
    - X (23) shifted by E (4): (23 - 4 + 26) % 26 = 19 → T
    - F (5) shifted by M (12): (5 - 12 + 26) % 26 = 19 → T
    - O (14) shifted by O (14): (14 - 14 + 26) % 26 = 0 → A
    - P (15) shifted by N (13): (15 - 13 + 26) % 26 = 2 → C
    - V (21) shifted by L (11): (21 - 11 + 26) % 26 = 10 → K
    - E (4) shifted by E (4): (4 - 4 + 26) % 26 = 0 → A
    - F (5) shifted by M (12): (5 - 12 + 26) % 26 = 19 → T
    - R (17) shifted by O (14): (17 - 14 + 26) % 26 = 3 → D
    - N (13) shifted by N (13): (13 - 13 + 26) % 26 = 0 → A
    - H (7) shifted by L (11): (7 - 11 + 26) % 26 = 22 → W
    - R (17) shifted by E (4): (17 - 4 + 26) % 26 = 13 → N

- **Decrypted Text**: "ATTACKATDAWN"

The same method can be used for both encryption and decryption, allowing for secure communication using a shared key.
"""

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