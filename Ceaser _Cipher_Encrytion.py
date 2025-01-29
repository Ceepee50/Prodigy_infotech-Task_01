def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
def main():
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            print("Encrypted text:", caesar_encrypt(text, shift))
        elif choice == "2":
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            print("Decrypted text:", caesar_decrypt(text, shift))
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")
if __name__ == "__main__":
    main()
