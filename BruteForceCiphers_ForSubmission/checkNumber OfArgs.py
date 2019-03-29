#Author: James Finglas B00094138 Year 3 Digital Forensics & Cyber security

#main program
import sys

print ('Please enter 4 arguments \n' )

if len(sys.argv) == 4:
    print ('Number of arguments: ' + str(len(sys.argv)) + '\n')
    print ('This is the correct amount of Arguments. Thank you.')

else:
    print ('Number of arguments: ' + str(len(sys.argv))+ '\n')
    print('Usage: Input must consist of 4 arguments (Remember, the name of the file is always the first argument, you must add 3)' + '\n')
    print ('This is the not correct amount of Arguments. PLease try again.')
exit(0)