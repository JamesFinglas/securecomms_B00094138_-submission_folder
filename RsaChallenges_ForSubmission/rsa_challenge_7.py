#Author: James Finglas B00094138 Year 3 Digital Forensics & Cyber security
## Commands to generate keys with openssl from commandline.. not part of this pythonj code.
## openssl genrsa -out mykey.pem
## openssl rsa -in mykey.pem -pubout > mykey.pub
## -------------------------------------------------------------------------

## To run type python rsa.py from the commandline (assuming you've pythonh installed
import binascii
from functools import (reduce)
from itertools import (chain)
from factordb import factordb

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
p = 3133337
q = 25478326064937419292200172136399497719081842914528228316455906211693118321971399936004729134841162974144246271486439695786036588117424611881955950996219646807378822278285638261582099108339438949573034101215141156156408742843820048066830863814362379885720395082318462850002901605689761876319151147352730090957556940842144299887394678743607766937828094478336401159449035878306853716216548374273462386508307367713112073004011383418967894930554067582453248981022011922883374442736848045920676341361871231787163441467533076890081721882179369168787287724769642665399992556052144845878600126283968890273067575342061776244939
n = 79832181757332818552764610761349592984614744432279135328398999801627880283610900361281249973175805069916210179560506497075132524902086881120372213626641879468491936860976686933630869673826972619938321951599146744807653301076026577949579618331502776303983485566046485431039541708467141408260220098592761245010678592347501894176269580510459729633673468068467144199744563731826362102608811033400887813754780282628099443490170016087838606998017490456601315802448567772411623826281747245660954245413781519794295336197555688543537992197142258053220453757666537840276416475602759374950715283890232230741542737319569819793988431443
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
ciphertext2 = 877047627503964563527859854056241853286548710266261291942543955818132370489959838496983429954434494528178229313135354793125902041844995518092695073588272773865176510386504459109444540504995243455296652458363596632448945407597570368304177404561607143991631472612686460090955582314803404185085391881900665937993904325795901688452399415391744151647251408176477627720933717024380735888111455809609800839992904182591275652616244755461341372866557636825262065485442416189938154309976219500988259186981644426083447522183242945513870008042818029602927271842718324310884266107435333212981162347887454715321088536179467180247805306


## ----- decrypt cuphertext then convert number back to a string

# feed cipher text variable into pow calculation
decrypted2 = pow(ciphertext2, d, n)   ## decrypt
#declare new variable by feed outcome of pow calculation into int2string
plaintext2 = int2string(decrypted2)
#print out decrypted rsa text
print (plaintext2)

