import sys

def encryption(message, shift):
    encrypted = ""

    for char in message:
        if char.isupper():
            offset = ((ord(char) + shift - 65) % 26 + 65)
            encrypted += chr(offset)
        elif char.islower():
            offset = ((ord(char) + shift - 97) % 26 + 97)
            encrypted += chr(offset)
        else:
            encrypted += char
    return encrypted

def decryption(encrypted_message, shift):
    decrypted = ""

    for char in encrypted_message:
        if char.isupper():
            offset = ((ord(char) - shift - 65) % 26 + 65)
            decrypted += chr(offset)
        elif char.islower():
            offset = ((ord(char) - shift - 97) % 26 + 97)
            decrypted += chr(offset)
        else:
            decrypted += char
    
    return decrypted

def main():
    text = str(input("Enter the string you want to encrypt: "))
    shift = int(input("Enter the shift you want to encrypt the message with: "))
    encrypted = encryption(text, shift)
    print(encrypted)
    decrypted = decryption(encrypted, shift)
    print(f"And decrypted the string is {decrypted}")

if __name__=="__main__":
    main()