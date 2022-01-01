from tinyec.ec import SubGroup, Curve
from random import *
import os
import hashlib
from ecdsaModule import pubKey

X = int((input("Please Enter Your Public Key X Coordinate In Hex Format:")),16)
Y = int((input("Please Enter Your Public Key Y Coordinate In Hex Format:")),16)

name = 'secp256k1'
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
g = (X,Y)
h = 1
 
if (((X * X * X)%p) + 7) != ((Y * Y)%p):
	print("The Public Key X and Y Coordinates You Entered Are NOT Valid...NOTE: DO NOT Include 02, 03 Or 04 At The Begining Of The X Coordinate And Make Sure You Are Using Hexidecimal Format. If You Need Assistance...Please Contact Technical Support...Please Try Again...Enter Valid X and Y Coordinates For Your Public Key...")
	exit()
else:
	curve1 = Curve(a, b, SubGroup(p, g, n, h), name)
	pubKey1 = curve1.g * 1
	pubKeyHalves = curve1.g * 1
	PublicKey = curve1.g * 1
	CollisionList = []
	HalvesCollisionList = []

	AA = int(input("Please Enter the Size of the Collision List you would like to Create. A Size between 65,000 and 4 billion is the recomended range. Best Performance around 100,000:"))
	print("Creating Collision List...Please Wait...")

	iteration = 1
	while iteration < (AA):
		A = pubKey1 * 2
		CollisionList.append(A.x)
		pubKey1 = A
		iteration = iteration + 1

	print("Collision List Created...")

	AAA = int(input("Please Enter the Size of the Halves Collision List you would like to Create. NOTE: Keep this number smaller for better performance. Best Performance around 256:"))

	iterationHalves = 1
	while iterationHalves < (AAA):
		CC = (pubKeyHalves * 57896044618658097711785492504343953926418782139537452191302581570759080747169)
		HalvesCollisionList.append(CC.x)
		pubKeyHalves = CC
		iterationHalves = iterationHalves + 1
	
	print("Halves Collision List Created...")
	print("Searching For Key...Please Wait...")
	iterations = 1
	privKey = int((hashlib.sha256(os.urandom(16)).hexdigest()), 16)
	
	while iterations < (n):

		II = 1
		while II < (5000):
			a = (privKey * (57896044618658097711785492504343953926418782139537452191302581570759080747169)%n)
			privKey = a
			II = II + 1
		BB = pubKey * privKey
		if BB.y == PublicKey.y:
				
			print("Found Private Key:", privateKey)
			print("Matching Public Key:", BB.x)
			print("Please Do Not Loose This Key...Thank You")
			print("This Key Has Been Written To A File Called foundKeys.txt")
			with open('foundKeys.txt', 'w') as e:
				e.write(str(privateKey))
			exit()

		elif BB.x == PublicKey.x:
			privateKey = n - privateKey
			print("Found Private Key:", privKey)
			print("Matching Public Key:", BB.x)
			print("Please Do Not Loose This Key...Thank You")
			print("This Key Has Been Written To A File Called foundKeys.txt")
			with open('foundKeys.txt', 'w') as e:
				e.write(str(privateKey))
			exit()
		else:
			hashIteration = 1
			while hashIteration < (10000):
			B = BB * 2
			if B.x in CollisionList:
				for i, key in enumerate (CollisionList):
					if key == B.x:
						privateKey = ((privKey * (2**hashIteration))%n)
						print("Collision Key Found in Large Collision List:")
						print("Iteration Number:", i)
						print("Collision Public Key:", key)
						print("Collision Private Key:", privateKey)
						j = i + 1
						while j != 0:
							D = (privateKey * (57896044618658097711785492504343953926418782139537452191302581570759080747169))%n
							privateKey = D
							j = j - 1
		
						pub = pubKey*D
						if pub.y != PublicKey.y:
							D = n - D
						else:
							D = D
						print("Actual Private Key:", D)
						print("Please Do Not Loose This Key...Thank You")
						print("This Key Has Been Written To A File Called foundKeys.txt")
						with open('foundKeys.txt', 'w') as e:
								e.write(str(D))
						exit()
			elif B.x in HalvesCollisionList:
				for i, key in enumerate (HalvesCollisionList):
					if key == B.x:
						privateKey = ((privKey * (2**hashIteration))%n)
						print("Collision Key Found in Halves Collision List:")
						print("Iteration Number:", i)
						print("Collision Public Key:", key)
						print("Collision Private Key:", privateKey)
				
						j = i + 1
						while j != 0:
							D = (privateKey * 2)%n
							privateKey = D
							j = j - 1
		
						pub = pubKey * D
						if pub.y != PublicKey.y:
							D = n - D
						else:
							D = D
						print("Actual Private Key:", D)
						print("Please Do Not Loose This Key...Thank You")
						print("This Key Has Been Written To A File Called foundKeys.txt")
						with open('foundKeys.txt', 'w') as e:
								e.write(str(D))
						exit()		
		
			BB = B
			hashIteration = hashIteration + 1

		else:
			privKey = int((hashlib.sha256(os.urandom(16)).hexdigest()), 16)
			iterations = iterations + 1
