from tinyec.ec import SubGroup, Curve
from os import urandom
import time
X = int((input("Please Enter Your Public Key X Coordinate In Hexidecimal Format:")),16)
Y = int((input("Please Enter Your Public Key Y Coordinate In Hexidecimal Format:")),16)
name = 'secp256k1'
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
g = (X,Y)
h = 1
if (((X * X * X) % p) + 7) != (Y * Y) % p:
	print("The Public Key X and Y Coordinates You Entered Are NOT Valid...NOTE: DO NOT Include 02, 03 Or 04 At The Begining Of The X Coordinate And Make Sure You Are Using Hexidecimal Format. If You Need Assistance...Please Contact Technical Support...Please Try Again...Enter Valid X and Y Coordinates For Your Public Key...")
	exit()
else:
	curve1 = Curve(a, b, SubGroup(p, g, n, h), name)
	pubKeyHalves = curve1.g * 1  
	EnteredPublicKey = curve1.g * 1
	CollisionList = []
	HalvesCollisionList = []
	half = 57896044618658097711785492504343953926418782139537452191302581570759080747169
	AA = int(input("Please Enter the Size of the Collision List you would like to Create. Best Performance around 10,000:"))
	AAA = (AA*2)
	print("Creating Collision List...Please Wait...")
	place = pubKeyHalves * ((half ** AA)%n)
	CollisionList.append(place.x)
	for iterationMultiples in range (AAA):
		iterationMultiple = place + place
		CollisionList.append(iterationMultiple.x)
		place = iterationMultiple
	CollisionList.reverse	
	tupleCollisionList = tuple(CollisionList)
	print("Collision List Created...")
	print("Creating Lookup Table...")
	from wordAdder import multiplyNum
	print("Lookup table Created...Searching for Your Key...Please Wait....")
	print("Total Key Comparisons per Round:", AAA)
	iterations = 1
	while iterations < (half):
		t = time.process_time()
		privKey = (int((((urandom(32))[2:])).hex(), 16))%n		##Change this value for testing from a random 256 bit hash to a known private Key Integer...
		privateKey1 = (privKey * (half ** AA))%n				##Then Enter the Public key or Public key of a multiple
		for hashIteration in range(AAA):
			keyB = multiplyNum(privateKey1)
			if keyB.x in tupleCollisionList:
				for item, key in enumerate (tupleCollisionList):
					if key != keyB.x:
							pass
					else:
						print("Key Found")
						privateKey = (privateKey1*(2**(AA - item)))%n
						keyC = multiplyNum(privateKey)
						if keyC.y != EnteredPublicKey.y:
							privateKey = n - privateKey
						else:
							privateKey = privateKey
						print("Hash Iteration:", hashIteration)
						print("Collision Public Key:", keyB.x)
						print("Collision Private Key:", privateKey1)
						print("Public Key Your Entered", EnteredPublicKey)
						print("Actual Private Key:", privateKey)
						print("Please Do Not Loose This Key...Thank You")
						print("This Key Has Been Written To A File Called foundKeys.txt")
						with open('foundKeys.txt', 'w') as e:
							e.write(str(privateKey))
						exit()
			else:
				privateKey1 += privateKey1
				keyB += keyB
		elapsed_time = time.process_time() - t
		print("Average Key Strings Compared Per Second",(AAA//elapsed_time))
		print("Average Seconds per Round ", elapsed_time)
		iterations += iterations
