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
value1 = "abcdefghijklmnopqrstuvwxyz"
key1 = value1[k:]+value1[:k]

def caeser_cipher_encryption(text):
    result = ""
    for char in text:
        if char.isupper():
            table = str.maketrans(value,key)
            output = char.translate(table)
            result += output
        elif char.islower():
            table1 = str.maketrans(value1,key1)
            output1 = char.translate(table1)
            result+= output1
        else:
            result += char
    return result


def caeser_cipher_decryption(text):
    result = ""
    for char in text:
        if char.isupper():
            table = str.maketrans(key,value)
            output = char.translate(table)
            result += output
        elif char.islower():
            table1 = str.maketrans(key1,value1)
            output1 = char.translate(table1)
            result+= output1
        else:
            result += char
    return result

    

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
