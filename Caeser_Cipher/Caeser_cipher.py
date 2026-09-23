import sys
import secrets

usr = secrets.randbelow(26)

def caeser_cipher_encryption(text):
    result = "" 
    for char in text:
        if char.isupper():
            new_index = (ord(char) - ord('A') + usr )%26
            new_char = chr(ord('A') + new_index) 
            result += new_char
        elif char.islower():
            new_index = (ord(char) - ord('a') + usr )%26
            new_char = chr(ord('a') + new_index)
            result += new_char
        else:
            result += char
    return result

def caeser_cipher_decryption(text):
    result = ""
    for char in text:
        if char.isupper():
            new_index = (ord(char) - ord('A') - usr)%26
            new_char = chr(ord('A') + new_index)
            result += new_char
        elif char.islower():
            new_index = (ord(char) - ord('a') - usr)%26
            new_char = chr(ord('a') + new_index)
            result += new_char
        else:
            result += char
    return result
        
def main():
    while True:
        print("1.Encryption\n2.Decryption\n3.Exit")
        user = input("Choose an option :-")
        if user == "1":
            text = input("Enter a string to encrypt:- ")
            print(f"The Encrypted string is :- {caeser_cipher_encryption(text)}")
        elif user == "2":
            text = input("Enter a string to decrypt:- ")
            print(f"The decrypted string is :- {caeser_cipher_decryption(text)}")
        elif user == "3":
            print("Exiting....")
            sys.exit()
        else:
            print("Invalid option")

main()
    
