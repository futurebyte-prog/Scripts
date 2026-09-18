def dirty_hex_to_string():

    messy_hex = input("Enter the Messy Hex:- ")
    clean_hex = messy_hex.replace(",","").replace("0x","")
    ascii_string = bytes.fromhex(clean_hex).decode('ascii')
    print(ascii_string)

def clean_hex_to_string():

    clean_hex = input("Enter the clean Hex:-")
    cleaner_hex = clean_hex.replace(",","")
    ascii_string = bytes.fromhex(cleaner_hex).decode('ascii')
    print(ascii_string)

def main():
    print(" 1.I have a messy hex(with 0x)\n 2.I have clean hex(without 0x)\n")
    option = int(input("Choose a option:- "))
    if(option == 1 ):
        dirty_hex_to_string()
    elif(option == 2):
        clean_hex_to_string()
    else:
        print("Invalid option")

main()        
