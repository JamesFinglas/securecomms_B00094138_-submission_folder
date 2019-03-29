#Author: James Finglas B00094138 Year 3 Digital Forensics & Cyber security
#based on open-source code located on Github , presneted by: VoxelPixel
#main program

import re
import sys

###########################################ROT5#################################################
#declare Rot5 decryption definition
def cipher_decryption_one():
    message = input("Please enter yout text to be decrypted: " + "\n")

#check if input is an int or not
    if not re.search('[\d\s]+', message): #\d = int, \s = space, + = one time or more, [] = a set, with logical OR
        print('Invalid input, Please enter an Integer.')
        sys.exit(0) #exit due to bad input
    encrypt_message = ""
    messageArray = []
    messageArray += message

    for i in range(10):
        for x in range(len(messageArray)):
            if messageArray[x] == chr(32):
                encrypt_message += " "
            else:
                messageArray[x] = chr(ord(messageArray[x]) + 1)
                if (ord(messageArray[x]) == 58):
                    messageArray[x] = chr(48)
        encrypt_message += ''.join(messageArray)
        encrypt_message += "\n"

    print (encrypt_message)

##################################################ROT13##############################################

#define rot13 encryption method(ceaser cipher)
def cipher_encryption_two():
    message = input("Please enter your text to be decrypted: " + "\n").upper()

    encrypt_message = ""
    messageArray = []
    messageArray += message

    for i in range(26):
        for x in range(len(messageArray)):
            if messageArray[x] == chr(32):
                encrypt_message += " "
            else:
                messageArray[x] = chr(ord(messageArray[x]) + 1)
                if ord(messageArray[x]) > 90:
                    messageArray[x] = chr(ord(messageArray[x])-26)
        encrypt_message += ''.join(messageArray)
        encrypt_message += "\n"

    print(encrypt_message)

#################################################ROT47###############################################

#define rot47 encryption method
def cipher_encryption_three():
    message = input("Please enter your message to be encrypted: ")
    key = 47
    encrypt_message = ""
    messageArray = []
    messageArray += message

#begin substitution sequence
    for i in range(47):
        for x in range(len(message)):
            #temp = ord(message[i]) + key
            if ord(message[x]) == 32:
                encrypt_message += " "
            else:
                messageArray[x] = chr(ord(messageArray[x]) + 1)
                if ord(messageArray[x]) > 126:
                    messageArray[x] = chr(ord(messageArray[x])-94) #-= 94
        encrypt_message += ''.join(messageArray)
        encrypt_message += "\n"

    print(encrypt_message)
################################################MAIN#################################################

#define main function
def main():
    rot5 = "5678901234"
    zero_to_nine ="0123456789"

    choice = int(input("1. ROT5 Decryption\n2. ROT13 Encryption\n3. ROT47 Decryption\n4. Chose(1,2,3): "))
    if choice == 1:
        print("---ROT5 Encryption---")
        cipher_decryption_one()

    elif choice == 2:
        print("---ROT13 Encryption---")
        cipher_encryption_two()

    elif choice == 3:
        print("---ROT47 Encryption---")
        cipher_encryption_three()

    else:
        print("Invalid selection, please try again")

#define main program
if __name__ == "__main__":
    main()
