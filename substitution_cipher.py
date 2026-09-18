def substitution_cipher(text):
    value  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key  = "QWERTYUIOPASDFGHJKLZXCVBNM"
    table = str.maketrans(value,key)

    output = text.translate(table)
    return output 

def main():
    text = input("Enter the string :-")
    print(substitution_cipher(text))
    
main()