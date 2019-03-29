#Author: James Finglas, Technology University Dublin, B00094138
import hashlib
from time import sleep

#declare variable from hash seed for comparison
hashSeed = "c89aa2ffb9edcc6604005196b5f0e0e4" #This will be searched online for the inverse of the seed.

#declare variable to be hashed until it matches hashseed
some_string = b"ecsc" #this will be the starting point of the new seed

#initial hash to feed into the hashing loop
hash = hashlib.md5(some_string) #hash some_string

#declare counter for loop
count = 1

#hashing loop whch shall continuously compare new hash against hashseed until the outcome matches
while hash.hexdigest() != hashSeed: #loop hash into rehash untill hash matches hashseed
    hash = hashlib.md5(hash.hexdigest().encode('utf-8')) #rehash hash
    print("Hex number :" + str(count) + ": " + hash.hexdigest() + " ") #print out new hash with count number
    count += 1 #add 1 to count
    #sleep(0.02) #add 0.02 of a sec wait time between calculatons

#once hash matches, print out the second last hash object
if hash.hexdigest() == hashSeed:
    print("SUCCESS! The answer to the question is: challange - 6fe9b4d366668a1f8a964a72cbc912c8") # print this if you succeed in finding the challange
exit(0)
