# A string of encrypted text
text = 'mrttaqrhknsw ih puggrur'

# The custom key used for encryption and decryption
custom_key = 'happycoding'

# Function to perform the Vigenère cipher encryption or decryption
def vigenere(message, key, direction=1):  # direction=1 for encryption, -1 for decryption
    key_index = 0  # To keep track of which letter of the key we are on
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # The alphabet used for finding positions of letters
    final_message = ''  # This will hold the result after encrypting/decrypting

    # Loop through each character in the message (convert to lowercase)
    for char in message.lower():

        # If the character is not a letter (e.g. space or punctuation), just add it as is
        if not char.isalpha():
            final_message += char
        else:        
            # Get the current letter from the key, cycling through the key as needed
            key_char = key[key_index % len(key)]  # Use modulo to repeat the key if needed
            key_index += 1  # Move to the next key letter for the next round

            # Find the position of the key letter in the alphabet (used as the "shift" amount)
            offset = alphabet.index(key_char)
            
            # Find the position of the current message letter in the alphabet
            index = alphabet.find(char)
            
            # Calculate the new letter's position by shifting it with the key's offset
            # If direction=1, it shifts forward (encryption); if -1, shifts backward (decryption)
            new_index = (index + offset*direction) % len(alphabet)
            
            # Append the encrypted/decrypted letter to the final message
            final_message += alphabet[new_index]
    
    # Return the full encrypted/decrypted message
    return final_message

# Function to encrypt the message using the Vigenère cipher
def encrypt(message, key):
    return vigenere(message, key)

# Function to decrypt the message using the Vigenère cipher (with direction -1 for reverse shift)
def decrypt(message, key):
    return vigenere(message, key, -1)

# Print the original encrypted text
print(f'\nEncrypted text: {text}')

# Print the custom key used
print(f'Key: {custom_key}')

# Decrypt the text using the custom key
decryption = decrypt(text, custom_key)

# Print the decrypted message
print(f'\nDecrypted text: {decryption}\n')
