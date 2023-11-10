def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                ascii_offset = ord('A')
            else:
                ascii_offset = ord('a')
            
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text

def main():
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value (an integer): "))

    encrypted_text = caesar_cipher(text, shift)

    print("Original Text:", text)
    print("Encrypted Text:", encrypted_text)

if __name__ == "__main__":
    main()

