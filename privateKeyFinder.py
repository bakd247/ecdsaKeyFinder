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

print("Creating DAG...Please Wait...")

DAG = []
iteration = 1
while iteration < (2**16):
	A = pubKey1*2
	DAG.append(A.x)
	pubKey1 = A
	iteration = iteration + 1

print("DAG Created...Searching For Key...")


iterations = 1
while iterations != (n):
	privKey = int((hashlib.sha256(os.urandom(16)).hexdigest()), 16)
	B = pubKey*privKey
	if B.x in DAG:
		print("privKey")
		print(B.X)
		exit()
	else:
		privKey = int((hashlib.sha256(os.urandom(16)).hexdigest()), 16)
		iterations = iterations+1
