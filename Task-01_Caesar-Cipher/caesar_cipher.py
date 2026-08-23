def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
choice = input("1. Encrypt\n2. Decrypt\nEnter choice: ")

if choice == "1":
    print("Encrypted:", caesar_cipher(message, shift))
elif choice == "2":
    print("Decrypted:", caesar_cipher(message, -shift))
else:
    print("Invalid choice")
