def caesar_cipher(text, shift, mode='encrypt'):
    """
    Perform Caesar Cipher encryption or decryption.
    
    Args:
        text (str): The input message.
        shift (int): The shift value for the cipher.
        mode (str): 'encrypt' for encryption, 'decrypt' for decryption.
        
    Returns:
        str: The encrypted or decrypted message.
    """
    result = ""
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')
            # Perform the shift with wrap-around using modulo
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result

# User input
mode = input("Enter mode ('encrypt' or 'decrypt'): ").strip().lower()
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))

# Call the function and display the result
output = caesar_cipher(message, shift_value, mode)
print(f"Result ({mode}ed): {output}")
