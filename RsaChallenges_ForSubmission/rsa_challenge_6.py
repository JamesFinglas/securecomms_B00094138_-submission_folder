#Author: James Finglas B00094138 Year 3 Digital Forensics & Cyber security
## Commands to generate keys with openssl from commandline.. not part of this pythonj code.
## openssl genrsa -out mykey.pem
## openssl rsa -in mykey.pem -pubout > mykey.pub
## -------------------------------------------------------------------------

## To run type python rsa.py from the commandline (assuming you've pythonh installed
import binascii
from functools import (reduce)
from itertools import (chain)

from Crypto.PublicKey import RSA

#create rsa key object
#recipient_key = RSA.import_key(open("mykey3").read())

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
#n = recipient_key.n
e = 65537
#d = recipient_key.d
p = 163598797232837275790583032413921422452851861145478369331976309880028992955089558380171554447759405365296693377570783300198791468861355639873166150884714034914366548252757855530548966926710596087588892893653952147784119788340592861717511574050564549916735627066568966135368285851889401719649796310308064172229
q = 151928351783926490385254692544226090032004315756120674902384041799040568083955129227360764179393042678005292005933989750269377019057534023167675372696224003953154715102625798599561576746593076228704448522848509650863715575134525964992439285085243915010868628145127710442853766119688772555932018349278733467937
n = p * q
test = (p-1)*(q-1)

from functools import (reduce)
from itertools import (chain)

# modInv :: Int -> Int -> Maybe Int
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m
## --------------------------------------------------------------------------


d = modinv(e,test)

#declare cipher text using data from provided cipher text
ciphertext2 = 4413233431418367729487001191499320110908628864393005850336194538378846901872012263024060279733910394528568658924541767014298273106072428208428621362441660742168169457839232452898840402021800460905562638079257404470183053387353849960252811956727755974787563684430128654542847575219444418360279725423441999278619584162289488016498634231451443666882615379215688913514242136494373656647328276909398980200846880640231426382657437148137610018777974884800967755913109702229247523206388812041488414941125272083962209616158810973532091497979384180936871075352614021504627549173686729322478688708849605857667792183339692021980


## ----- decrypt cuphertext then convert number back to a string

# feed cipher text variable into pow calculation
decrypted2 = pow(ciphertext2, d, n)   ## decrypt
#declare new variable by feed outcome of pow calculation into int2string
plaintext2 = int2string(decrypted2)
#print out decrypted rsa text
print (plaintext2)
