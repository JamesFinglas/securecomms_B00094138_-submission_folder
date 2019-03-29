#Author: James Finglas B00094138 Year 3 Digital Forensics & Cyber security

from Crypto.PublicKey import RSA

#create key object by deconstructing rsa private key file data
recipient_key = RSA.import_key(open("mykey2").read())

#print data segements from key object
print("This is n: " + str(recipient_key.n) + "\n" + "This is d: " + str(recipient_key.d) + "\n" + "This is e: " + str(recipient_key.e) + "\n")
