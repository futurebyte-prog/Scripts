def ROT13(text):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char)-ord('A')+13)%26 + ord('A'))
        elif char.islower():
            result += chr((ord(char)-ord('a')+13)%26 + ord('a'))   
        else:
            result += char   
    print(result)          


def main():
    text= input("Enter the text or string at which you want to apply ROT13 :- ")
    ROT13(text)


main()