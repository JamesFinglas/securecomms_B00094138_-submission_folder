#Author: James Finglas B00094138 Year 3 Digital Forensics & Cyber security
## Commands to generate keys with openssl from commandline.. not part of this pythonj code.
## openssl genrsa -out mykey.pem
## openssl rsa -in mykey.pem -pubout > mykey.pub
## -------------------------------------------------------------------------

## To run type python rsa.py from the commandline (assuming you've pythonh installed
import binascii

from Crypto.PublicKey import RSA

#create rsa key object
recipient_key = RSA.import_key(open("mykey3").read())

#print key object data segments if required
#print("This is n: " + str(recipient_key.n) + "\n" + "This is d: " + str(recipient_key.d) + "\n" + "This is e: " + str(recipient_key.e) + "\n" + "This is q: " + str(recipient_key.q) + "\n" + "This is p: " + str(recipient_key.p) + "\n")

#define method to convert from string to int
def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)

#define method to convert from int to string
def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")

# -------------------------------------------------------------------------


#declare variables for rsa based pow calculations via the rsa key object data elements extracted from rsa key object
n = recipient_key.n
e = recipient_key.e
d = recipient_key.d
p = recipient_key.p
q = recipient_key.q

## --------------------------------------------------------------------------

#declare cipher text using data from provided cipher text
ciphertext2 = 474862643754336865489984490773307542016161159436213530034995807183836312346778617047666360854948178434525541089212091928949344492697684657497682106740050084305554758259427768463395264318566101255923490595579348647860471822284428834756812967844672795316325109976652375135659724572710513755433401072885408968307124213606768098411795080747616961236626790699862671834311406129266854138764009952421206625693567227556664511584573464971029270576495696636132292906861410359486612705079004947333371264698887189359265840678094723729950785568382017843975809503403984016678927664449791524785943376314787680072596720311587221852

## ----- decrypt cuphertext then convert number back to a string

# feed cipher text variable into pow calculation
decrypted2 = pow(ciphertext2, d, n)   ## decrypt
#declare new variable by feed outcome of pow calculation into int2string
plaintext2 = int2string(decrypted2)
#print out decrypted rsa text
print (plaintext2)
