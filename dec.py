# Function to simulate ASCII code encryption with a specific public key
def encrypt_ascii_codes():
    e, n = 119, 2533
    ascii_codes = list(range(128))
    # Encrypt each ASCII code using the public key (e, n)
    encrypted_codes = [(code ** e) % n for code in ascii_codes]
    return encrypted_codes

# Function to decrypt an encrypted message based on ASCII codes
def decrypt_message(ascii_codes, encrypted_message):
    message_d = ""  # Initialize an empty string to store the decrypted message
    for i in encrypted_message:
        for j in range(128):
            if ascii_codes[j] == i:
                # Match the encrypted code with the original ASCII code and append the corresponding character to the decrypted message
                message_d += chr(j)
    print(message_d)

# Encrypted message to be decrypted
message = [1730, 815, 1476, 1476, 1226, 1297, 8, 502, 1226, 1520, 1476, 2303, 900]

# Decrypt the message using the ASCII codes and print the result
decrypt_message(encrypt_ascii_codes(), message)
