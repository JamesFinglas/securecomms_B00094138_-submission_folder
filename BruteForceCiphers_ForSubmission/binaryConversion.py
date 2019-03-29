#Author: James Finglas B00094138 Year 3 Digital Forensics & Cyber security

#main program definition
def inputInteger(message):
    while True:
        try:
            userInput = int(input(message))
            print(bin(userInput)[2:])
        except ValueError:
            print("That is not an integer")
            continue
        else:
            return userInput
            break

#main program
myInt = inputInteger("Please enter a positive Integer to be converted into binary: ")