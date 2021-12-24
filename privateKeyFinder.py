from tinyec.ec import SubGroup, Curve
from random import *
import os
import hashlib
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
pubKey = curve1.g*1

print("Creating DAG...Please Wait...")

DAG = []
iteration = 1
while iteration < (2**16):
	A = pubKey*2
	DAG.append(A.x)
	pubKey = A
	iteration = iteration + 1

print("DAG Created...Searching For Key...")


name = 'secp256k1'
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
g = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
h = 1

curve = Curve(a, b, SubGroup(p, g, n, h), name)

pubKey2 = curve.g * 1
iterations = 1
while iterations != (n):
	privKey = int((hashlib.sha256(os.urandom(16)).hexdigest()), 16)
	B = pubKey2*privKey
	
	if B.x in DAG:
		print("privKey")
		print(B.X)
		exit()
	else:
		privKey = int((hashlib.sha256(os.urandom(16)).hexdigest()), 16)
		iterations = iterations+1
