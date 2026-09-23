import sys

value = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
key = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
   

def substitution_encryption(text):
    table = str.maketrans(value,key)
    output =  text.translate(table)
    return output

def substitution_decryption(text):
    table = str.maketrans(key,value)
    output = text.translate(table)
    return output

def main():
   while True :
       
        print("1.Encryption\n2.Decryption\n3.Exit")
        usr_input = int(input("Choose a option:-"))

        if usr_input == 1:
            text = input("Enter the text to encrypt:- ")
            print(substitution_encryption(text))
        elif usr_input == 2:
            text = input("Enter the text to decrypt:- ")
            print(substitution_decryption(text))
        elif usr_input == 3:
            print ("Exiting....")
            sys.exit()
        else:
            print("Invalid Input")
            sys.exit()
            
main()


    