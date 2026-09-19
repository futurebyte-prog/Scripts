import sys

def ROT13(text):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char)-ord('A')+13)%26 + ord('A'))
        elif char.islower():
            result += chr((ord(char)-ord('a')+13)%26 + ord('a'))   
        else:
            result += char   
    return result          


def ROT13_encoder():
    text= input("Enter the text or string you want to encode in ROT13 :- ")
    print(ROT13(text))

def ROT13_decoder():
    text = input("Enter the text or string you want to decode in ROT13 :- ")
    print(ROT13(ROT13(text)))

def main():
    while True:
        print("1.Encode\n2.Decode\n3.Exit")
        usr = input("Choose an option")
        if usr == "1":
            ROT13_encoder()
        elif usr == "2":
            ROT13_decoder()
        elif usr == "3":
            sys.exit()
        else:
            print("Invalid Input")

main()
                        