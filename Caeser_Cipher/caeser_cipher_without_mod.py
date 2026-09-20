import sys

while True:
    try:
        k = int(input("Enter the integer between 0 and 25:- "))
        if k < 0 or k > 25:
            print("Invailid Input")
        else:
            print(k)
            break
    except ValueError:
        print("Invalid data type")

value = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = value[k:]+value[:k]

def caeser_cipher_encryption(text):
    table = str.maketrans(value,key)
    output = text.translate(table)
    return output 
def caeser_cipher_decryption(text):
    table = str.maketrans(key,value)
    output = text.translate(table)
    return output

def main():
    while True:
        print("1.Encryption\n2.Decryption\n3.Exit")
        usr = input("Choose an option:- ")
        if usr == "1":
            text = input("Enter a string to encrypt:- ")
            print(f" The Encrypted string is :- {caeser_cipher_encryption(text)}")

        elif usr == "2":
            text = input("Enter a string to decrypt:- ")
            print(f"The decrypted string is :- {caeser_cipher_decryption(text)}")

        elif usr == "3":
            print("Exiting....")
            sys.exit()
        else:
            print("Invalid option")  

main() 
