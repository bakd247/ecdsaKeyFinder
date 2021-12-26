from tinyec.ec import SubGroup, Curve
from random import *
import os
import hashlib
from ecdsaModule import pubKey
X = int((input("Please Enter Your Public Key X Coordinate:")),16)
Y = int((input("Please Enter Your Public Key Y Coordinate:")),16)
name = 'secp256k1'
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
g = (X,Y)
h = 1

curve1 = Curve(a, b, SubGroup(p, g, n, h), name)
pubKey1 = curve1.g*1
AA = int(input("Please Enter the Size of the Collision List you would like to Create:"))
print("Creating Collision List...Please Wait...")

CollisionList = []
iteration = 1
while iteration < (AA):
	A = pubKey1*2
	CollisionList.append(A.x)
	pubKey1 = A
	iteration = iteration + 1

print("Collision List Created...Searching For Key...")


iterations = 1
while iterations != (n):
	privKey = int((hashlib.sha256(os.urandom(16)).hexdigest()), 16)
	B = pubKey*privKey
	if B.x in CollisionList:
		for i, key in enumerate (CollisionList):
			if key == B.x:
				print("Collision Key Found:")
				print("Iteration Number:", i)
				print("Collision PubKey:", key)
				print("Collision PrivateKey:", privKey)
				half = ((n+1)//2)
				j = i+1
				while j != 0:
					D = (privKey*half)%n
					privKey = D
					j = j-1
				print("Actual Private Key:",D)
				print("Please Do Not Loose This Key...Thank You")
				print("This Key Has Been Written To A File Called foundKeys.txt")
				with open('foundKeys.txt', 'w') as e:
						e.write(str(D))
				exit()
		else:
			privKey = int((hashlib.sha256(os.urandom(16)).hexdigest()), 16)
			iterations = iterations+1
