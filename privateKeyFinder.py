from tinyec.ec import SubGroup, Curve
from random import *
import os
import hashlib
from ecdsaModule import pubKey
X = int((input("Please Enter Your X Coordinate:")),16)
Y = int((input("Please Enter Your Y Coordinate:")),16)
name = 'secp256k1'
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
g = (X,Y)
h = 1

curve1 = Curve(a, b, SubGroup(p, g, n, h), name)
pubKey1 = curve1.g*1

print("Creating CollisionList...Please Wait...")

CollisionList = []
iteration = 1
while iteration < (256):
	A = pubKey1*2
	CollisionList.append(A.x)
	pubKey1 = A
	iteration = iteration + 1

print("CollisionList Created...Searching For Key...")


iterations = 1
while iterations != (n):
	privKey = int((hashlib.sha256(os.urandom(16)).hexdigest()), 16)
	B = pubKey*privKey
	for i, key in enumerate (CollisionList):
		if key == B.x:
			print(i, key)
			print(privKey)
			half = ((n+1)//2)
			j = i+1
			while j != 0:
				D = (privKey*half)%n
				privKey = D
				j = j-1
			E = n-D
			print("This is One of the Private Keys you are Searching For:",D)
			print("And This is The Other:", E)
			print("Please only Use the one That Gives the correct Y Coordinate.")
			exit()
	else:
		privKey = int((hashlib.sha256(os.urandom(16)).hexdigest()), 16)
		iterations = iterations+1
