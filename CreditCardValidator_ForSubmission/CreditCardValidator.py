#Author: James Finglas B00094138 Year 3 Digital Forensics & Cyber security

import random
#######################################################################CARD VALIDATION##########################################################################################

#define card number validation function
def userInputValidation():
    userInput = input("Please input the number you wish to validte: ")

    #enter if checks only if user input matches the declared lenght
    if len(userInput) == 13 or len(userInput) == 14 or len(userInput) == 15 or len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
        userInput = str(userInput)

        #enter this inner set of inner if checks only if the initial range of object indexs match any of the given ranges
        if int(userInput[0:6]) in range(222100,272100) and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) in range(3528,3590) and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:3]) in range(300,306) and len(userInput) == 14:
            print("This is a valid credit card number")
        elif int(userInput[0:2]) == 34 and len(userInput) == 15:
            print("This is a valid credit card number")
        elif int(userInput[0:2]) == 36 and len(userInput) == 14:
            print("This is a valid credit card number")
        elif int(userInput[0:2]) == 37 and len(userInput) == 15:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 4026 and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:6]) == 417505 and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 4508 and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 4844 and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 4913 and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 4917 and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 5018 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 5020 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 5038 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:2]) == 51 and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:2]) == 52 and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:2]) == 53 and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:2]) == 54 and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:2]) == 55 and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 5893 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:6]) in range(622126,622926) and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 6011 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 6304 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:3]) == 637 and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:3]) == 638 and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:3]) == 639 and len(userInput) == 16:
            print("This is a valid credit card number")
        elif int(userInput[0:3]) == 644 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:3]) == 645 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:3]) == 646 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:3]) == 647 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:3]) == 648 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:3]) == 649 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:3]) == 648 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:2]) == 65 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 6759 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 6761 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 6762 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        elif int(userInput[0:4]) == 6763 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("This is a valid credit card number")
        else:
            #print out error if initial indexs do not meet any of the given ranges
            print ("Invalid credit card number")
    #if no lenght is not matched, exit and output error message
    if len(userInput) < 13 or len(userInput) > 19:
        print("Invalid credit card number")

################################################################################CARD VENDOR VALIDATOR######################################################################3

#define card vendor check function
def userInputVendorValidation():
    userInput = input("Please input the number whos vendor you wish to output: ")

    #enter if statements only if the length of the input matches the declared lengths
    if len(userInput) == 13 or len(userInput) == 14 or len(userInput) == 15 or len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
        userInput = str(userInput)

        #enter the if statements only if the initial indexs match the given ranges
        if int(userInput[0:6]) in range(222100,272100) and len(userInput) == 16:
            print("The vendor for this card is: MasterCard")
        elif int(userInput[0:4]) in range(3528,3590) and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendir for this card is: JCB")
        elif int(userInput[0:3]) in range(300,306) and len(userInput) == 14:
            print("The vendor for this card is: Diners Club - Carte Blanche")
        elif int(userInput[0:2]) == 34 and len(userInput) == 15:
            print("The vendor for this card is: American Express")
        elif int(userInput[0:2]) == 36 and len(userInput) == 14:
            print("The vendor for this card is: Diners Club - International")
        elif int(userInput[0:2]) == 37 and len(userInput) == 15:
            print("The vendor for this card is: American Express")
        elif int(userInput[0:4]) == 4026 and len(userInput) == 16:
            print("The vendor for this card is: Visa Electron")
        elif int(userInput[0:6]) == 417500 and len(userInput) == 16:
            print("The vendor for this card is: Visa Electron")
        elif int(userInput[0:4]) == 4508 and len(userInput) == 16:
            print("The vendor for this card is: Visa Electron")
        elif int(userInput[0:4]) == 4844 and len(userInput) == 16:
            print("The vendor for this card is: Visa Electron")
        elif int(userInput[0:4]) == 4913 and len(userInput) == 16:
            print("The vendor for this card is: Visa Electron")
        elif int(userInput[0:4]) == 4917 and len(userInput) == 16:
            print("The vendor for this card is: Visa Electron")
        elif int(userInput[0:4]) == 5018 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Maestro")
        elif int(userInput[0:4]) == 5020 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Maestro")
        elif int(userInput[0:4]) == 5038 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Maestro")
        elif int(userInput[0:2]) == 51 and len(userInput) == 16:
            print("The vendor for this card is: MasterCard")
        elif int(userInput[0:2]) == 52 and len(userInput) == 16:
            print("The vendor for this card is: MasterCard")
        elif int(userInput[0:2]) == 53 and len(userInput) == 16:
            print("The vendor for this card is: MasterCard")
        elif int(userInput[0:2]) == 54 and len(userInput) == 16:
            print("The vendor for this card is: MasterCard or Diners Club - USA & Canada")
        elif int(userInput[0:2]) == 55 and len(userInput) == 16:
            print("The vendor for this card is: MasterCard")
        elif int(userInput[0:4]) == 5893 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendior for this card is: Maestro")
        elif int(userInput[0:6]) in range(622126,622926) and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Discover")
        elif int(userInput[0:4]) == 6011 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Discover")
        elif int(userInput[0:4]) == 6304 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Maestro")
        elif int(userInput[0:3]) == 637 and len(userInput) == 16:
            print("The vendor for this card is: Discover")
        elif int(userInput[0:3]) == 638 and len(userInput) == 16:
            print("The vendor for this card is: Discover")
        elif int(userInput[0:3]) == 639 and len(userInput) == 16:
            print("The vendor for this card is: Discover")
        elif int(userInput[0:3]) == 644 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Discover")
        elif int(userInput[0:3]) == 645 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Discover")
        elif int(userInput[0:3]) == 646 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Discover")
        elif int(userInput[0:3]) == 647 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Discover")
        elif int(userInput[0:3]) == 648 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Discover")
        elif int(userInput[0:3]) == 649 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Discover")
        elif int(userInput[0:3]) == 648 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Discover")
        elif int(userInput[0:2]) == 65 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Discover")
        elif int(userInput[0:4]) == 6759 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Maestro")
        elif int(userInput[0:4]) == 6761 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Maestro")
        elif int(userInput[0:4]) == 6762 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Maestro")
        elif int(userInput[0:4]) == 6763 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            print("The vendor for this card is: Maestro")
        else:
            #if no match is found print out error message
            print ("Invalid credit card number")
    #if the length does not match print out error message
    if len(userInput) < 13 or len(userInput) > 19:
        print("Invalid credit card number")

##############################################################################################CARD GENERATOR#############################################################################################################################

#define initial card generator function, this function requires a user input object from genInput() function
def generator():
    userInput= input("Please select from the following options (1-10): \n1: American Express\n2: Diners Club - Carte Blanche\n3: Diners Club - International\n4: Diners Club - USA & Canada\n5: Discover\n6: InstaPayment\n7: JCB\n8: Maestro\n9: MasterCard\n10: Visa Electron \nSelect(1-10):")
    genInput(userInput)

#define genInput function(), this feeds a user input object to the card generator function
def genInput(userInput):
    if userInput == str(1):
        gen1(userInput)
    elif userInput == str(2):
        gen2(userInput)
    elif userInput == str(3):
        gen3(userInput)
    elif userInput == str(4):
        gen4(userInput)
    elif userInput == str(5):
        gen5(userInput)
    elif userInput == str(6):
        gen6(userInput)
    elif userInput == str(7):
        gen7(userInput)
    elif userInput == str(8):
        gen8(userInput)
    elif userInput == str(9):
        gen9(userInput)
    elif userInput == str(10):
        gen10(userInput)
    else:
        print("Invalid input, please restart and enter a number")

#define first card generator function for american express choice
def gen1(total):
    check = 1
    while check == 1:
        americanExpress = [34,37]
        firstPart = random.choice(americanExpress)
        #print(firstPart)
        secondPart = random.randint(000000000000,99999999999999)
        #print(sencondPart)
        userInput2 =str(firstPart)+str(secondPart)
        #print(userInput)
        check = checkSum2(userInput2)
        #print(check)
        if check == 0:
            print(userInput2)

#define second card generator function for diners club carte blanche choice
def gen2(total):
    check = 1
    while check == 1:
        dinersClubCarteBlanche = [300,301,302,303,304,305]
        firstPart = random.choice(dinersClubCarteBlanche)
        #print(firstPart)
        secondPart = random.randint(00000000000,99999999999)
        #print(sencondPart)
        userInput2 =str(firstPart)+str(secondPart)
        #print(userInput)
        check = checkSum(userInput2)
        #print(check)
        if check == 0:
            print(userInput2)

#define third card generator function for diners club international choice
def gen3(total):
    check = 1
    while check == 1:
        #dinersClubInternatonal
        firstPart = 36
        #print(firstPart)
        secondPart = random.randint(000000000000,99999999999999)
        #print(sencondPart)
        userInput2 =str(firstPart)+str(secondPart)
        #print(userInput)
        check = checkSum2(userInput2)
        #print(check)
        if check == 0:
            print(userInput2)


#define fourth card generator function for diners club usa and canada choice
def gen4(total):
    check = 1
    while check == 1:
        #dinersClubUsaAndCanada
        firstPart = 54
        #print(firstPart)
        secondPart = random.randint(000000000000,99999999999999)
        #print(sencondPart)
        userInput2 =str(firstPart)+str(secondPart)
        #print(userInput)
        check = checkSum2(userInput2)
        #print(check)
        if check == 0:
            print(userInput2)

#define fifth card generator function for discover choice
def gen5(total):
    check = 1
    while check == 1:
        discover = [644,645,646,647,648,649]
        firstPart = random.choice(discover)
        #print(firstPart)
        secondPart = random.randint(0000000000000,9999999999999999)
        #print(sencondPart)
        userInput2 =str(firstPart)+str(secondPart)
        #print(userInput)
        check = checkSum2(userInput2)
        #print(check)
        if check == 0:
            print(userInput2)

#define sixth card generator function for instapayment choice
def gen6(total):
    check = 1
    while check == 1:
        instaPayment = [637,638,639]
        firstPart = random.choice(instaPayment)
        #print(firstPart)
        secondPart = random.randint(0000000000000,9999999999999)
        #print(sencondPart)
        userInput2 =str(firstPart)+str(secondPart)
        #print(userInput)
        check = checkSum2(userInput2)
        #print(check)
        if check == 0:
            print(userInput2)

#define seventh card generator function for jcb choice
def gen7(total):
    check = 1
    while check == 1:
        jCB = [3528,3589]
        firstPart = random.choice(jCB)
        #print(firstPart)
        secondPart = random.randint(000000000000,999999999999999)
        #print(sencondPart)
        userInput2 =str(firstPart)+str(secondPart)
        #print(userInput)
        check = checkSum2(userInput2)
        #print(check)
        if check == 0:
            print(userInput2)

#define eight card generator function for maestro choice
def gen8(total):
    check = 1
    while check == 1:
        maestro = [5018,5020,5038,5893,6304,6759,6761,6762,6763]
        firstPart = random.choice(maestro)
        #print(firstPart)
        secondPart = random.randint(000000000000,999999999999999)
        #print(sencondPart)
        userInput2 =str(firstPart)+str(secondPart)
        #print(userInput)
        check = checkSum2(userInput2)
        #print(check)
        if check == 0:
            print(userInput2)

#define ninth card generator function for mastercard choice
def gen9(total):
    check = 1
    while check == 1:
        masterCard = [51,52,53,54,55]
        firstPart = random.choice(masterCard)
        #print(firstPart)
        secondPart = random.randint(00000000000000,99999999999999)
        #print(sencondPart)
        userInput2 =str(firstPart)+str(secondPart)
        #print(userInput)
        check = checkSum2(userInput2)
        #print(check)
        if check == 0:
            print(userInput2)

#define tenth card generator function for visa electron choice
def gen10(total):
    check = 1
    while check == 1:
        visaElectron = [4026,4508,4844,4913,4917]
        firstPart = random.choice(visaElectron)
        #print(firstPart)
        secondPart = random.randint(000000000000,999999999999)
        #print(sencondPart)
        userInput2 =str(firstPart)+str(secondPart)
        #print(userInput)
        check = checkSum2(userInput2)
        #print(check)
        if check == 0:
            print(userInput2)

###########################################################################################CARD CHECKSUM##########################################################################################3

#define intial checksum calculation function, currently not used
def checkSum(userInput):
    #userInput =list(userInput)
    total = 0
    additionVar = 0
    multiplyVar = 0
    #final = 1
    multiplyArray = []
    additionArray = []
    for index in range(len(userInput)):
        if int(userInput[index]) % 2 == 0:
            multiplyVar = int(userInput[index]) * 2
            multiplyArray.append(multiplyVar)
    for index in range(len(userInput)):
        if int(userInput[index]) % 2 != 0:
            additionVar = int(userInput[index])
            additionArray.append(additionVar)
    for index in range(len(multiplyArray)):
        total = total + multiplyArray[index]
    for index in range(len(additionArray)):
        total = total + additionArray[index]
    if total % 10 == 0:
        #final: bool = 0
        print("Valid according to the checksum calculator")
        return (0)
    else:
        #final: bool = 1
        print("Invalid according to the checksum calculator")
        return(1)

#define intial checksum calculation function, this is currently the main checksum function
def checkSum2(userInput):
    #userInput =list(userInput)
    total = 0
    additionVar = 0
    multiplyVar = 0
    #final = 1
    multiplyArray = []
    additionArray = []
    for index in range(len(userInput)):
        if int(userInput[index]) % 2 == 0:
            multiplyVar = int(userInput[index]) * 2
            multiplyArray.append(multiplyVar)
    for index in range(len(userInput)):
        if int(userInput[index]) % 2 != 0:
            additionVar = int(userInput[index])
            additionArray.append(additionVar)
    for index in range(len(multiplyArray)):
        total = total + multiplyArray[index]
    for index in range(len(additionArray)):
        total = total + additionArray[index]
    if total % 10 == 0:
        #final: bool = 0
        print("Valid according to the checksum calculator")
        return (0)
    else:
        return(1)

#################################################################################PARTIAL CARD CHECKSUM###########################################################################################

#define secondary alternate checksum calculation function, this is only called in the special case sceanario where our
#lecturer will enter 12 digits.
def alternateChecksum(userInput):
    #12 character input only
    loopValue = 1
    if len(userInput) in range(10,15):
            addVar = random.randint(000,999)
            userInput=userInput+(str(addVar))
            total = 0
            multiplyArray = []
            additionArray =[]
            for index in range(len(userInput) -2):
                if int(userInput[index]) % 2 == 0:
                    multiplyVar = int(userInput[index]) * 2
                    multiplyArray.append(multiplyVar)
                if int(userInput[index]) % 2 != 0:
                    additionVar = int(userInput[index])
                    additionArray.append(additionVar)
            for index in range(len(multiplyArray)):
                total = total + multiplyArray[index]
            for index in range(len(additionArray)):
                total = total + additionArray[index]
                checkValue = 10 - total % 10
                print(checkValue)
                while checkValue % 10 != 0:
                    checkValue +=1
                print(checkValue)
                newCheckValue = (10 - checkValue) %10
                print("this is the new check value: " + str(newCheckValue))
                print("this is the total: " + userInput + str(newCheckValue))
                loopValue =0
    else:
        print("Invalid Input! Please restart and input 12,13,14 or 15 digits to calculate the partial checksum.")

###########################################################user card checksum validation#######################################################################

#define user card checksum validation function
def userInputChecksum():
    userInput = input("Please input the number you wish to validte: ")

    #enter this if statement only in the special case of out lecturer entering 12 digits to generate a valid checksum
    if len(userInput) == 12:
        (alternateChecksum(userInput))

    #enter this if statement only if the length of the user input matches the given range
    if len(userInput) == 13 or len(userInput) == 14 or len(userInput) == 15 or len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
        userInput = str(userInput)

        #enter this inner set of if statements if the initial indexs match the given length
        if int(userInput[0:6]) in range(222100,272100) and len(userInput) == 16:
            (checkSum(userInput))
        elif int(userInput[0:4]) in range(3528,3590) and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:3]) in range(300,306) and len(userInput) == 14:
            (alternateChecksum(userInput))
        elif int(userInput[0:2]) == 34 and len(userInput) == 15:
            (checkSum(userInput))
        elif int(userInput[0:2]) == 36 and len(userInput) == 14:
            (checkSum(userInput))
        elif int(userInput[0:2]) == 37 and len(userInput) == 15:
            (checkSum(userInput))
        elif int(userInput[0:4]) == 4026 and len(userInput) == 16:
            (checkSum(userInput))
        elif int(userInput[0:6]) == 417505 and len(userInput) == 16:
           (checkSum(userInput))
        elif int(userInput[0:4]) == 4508 and len(userInput) == 16:
            (checkSum(userInput))
        elif int(userInput[0:4]) == 4844 and len(userInput) == 16:
            (checkSum(userInput))
        elif int(userInput[0:4]) == 4913 and len(userInput) == 16:
            (checkSum(userInput))
        elif int(userInput[0:4]) == 4917 and len(userInput) == 16:
            (checkSum(userInput))
        elif int(userInput[0:4]) == 5018 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:4]) == 5020 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:4]) == 5038 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:2]) == 51 and len(userInput) == 16:
            (checkSum(userInput))
        elif int(userInput[0:2]) == 52 and len(userInput) == 16:
            (checkSum(userInput))
        elif int(userInput[0:2]) == 53 and len(userInput) == 16:
            (checkSum(userInput))
        elif int(userInput[0:2]) == 54 and len(userInput) == 16:
            (checkSum(userInput))
        elif int(userInput[0:2]) == 55 and len(userInput) == 16:
            (checkSum(userInput))
        elif int(userInput[0:4]) == 5893 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:6]) in range(622126,622926) and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:4]) == 6011 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:4]) == 6304 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:3]) == 637 and len(userInput) == 16:
            (checkSum(userInput))
        elif int(userInput[0:3]) == 638 and len(userInput) == 16:
            (checkSum(userInput))
        elif int(userInput[0:3]) == 639 and len(userInput) == 16:
            (checkSum(userInput))
        elif int(userInput[0:3]) == 644 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:3]) == 645 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:3]) == 646 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:3]) == 647 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:3]) == 648 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:3]) == 649 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:3]) == 648 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:2]) == 65 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:4]) == 6759 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:4]) == 6761 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:4]) == 6762 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        elif int(userInput[0:4]) == 6763 and len(userInput) == 16 or len(userInput) == 17 or len(userInput) == 18 or len(userInput) == 19:
            (checkSum(userInput))
        else:
            #if the indexs do not match print out error message
            print ("Invalid credit card number")
    #if the length does not match print out error message
    if len(userInput) < 12 or len(userInput) > 19:
        print("Invalid credit card number!")

#########################################################MAIN#################################################################

#declare main function
if __name__ == "__main__":
    #intital print statement
    print("Welcome to my Credit Card Validation, Vendor Issuuer, Checksum Calculator & Card Generator")

    #declare array of function objects for our menu
    choices = {1:userInputValidation,2:userInputVendorValidation,3:userInputChecksum,4:generator}

    #define user choice
    choice = input("1. Credit Card Validatior\n2. Determine Credit Card Vendor issuer\n3. Calculate Credit Card Checksum Validity\n4. Generator\n5. Chose(1,2,3,4): ").strip()
    if not choice.isdigit() or int(choice) not in choices:
        exit("Invalid Selection, please restart and try again.")

    #user choice2
    choices[int(choice)]()