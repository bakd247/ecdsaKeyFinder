from tinyec.ec import SubGroup, Curve
from os import urandom
from ecdsaModule import pubKey
import time
##Initiate ECDSA
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
	##Create Multiples and Halves Lists as tuples
	##Only need to save X-Coordinates Becuase of Modular Inverses being accounted for below...
	AA = int(input("Please Enter the Size of the Multiples Collision List you would like to Create. Best Performance around 100,000:"))
	print("Creating Collision List...Please Wait...")
	iteration = 1
	while iteration < (AA):
		A = pubKey1 + pubKey1
		CollisionList.append(A.x)
		pubKey1 = A
		iteration = iteration + 1
	tupleCollisionList = tuple(CollisionList)
	print("Multiples Collision List Created...")
	AAA = int(input("Please Enter the Size of the Halves Collision List you would like to Create. Best Performance around 100,000:"))
	power = (57896044618658097711785492504343953926418782139537452191302581570759080747169 ** AAA)%n
	place = pubKeyHalves * power
	iterationHalves = 1
	while iterationHalves < (AAA):
		CC = place + place
		HalvesCollisionList.append(CC.x)
		place = CC
		iterationHalves = iterationHalves + 1
	HalvesCollisionList.reverse()
	tupleHalvesCollisionList = tuple(HalvesCollisionList)
	print("Halves Collision List Created...")
	print("Searching For Key...Please Wait...")
	#Random Search For a Match to any One of the Factors accounting for modular inverses
	privKey = (int((((urandom(32))[2:])).hex(), 16))%n			##Change This Value to a known private key integer for testing...
	iterations = 1
	while iterations < (n):
		t = time.process_time()
		BB = pubKey * privKey
		if BB.y == PublicKey.y:
			privateKey = privKey
			print("Found Private Key:", privateKey)
			print("Matching Public Key:", BB.x)
			print("Please Do Not Loose This Key...Thank You")
			print("This Key Has Been Written To A File Called foundKeys.txt")
			with open('foundKeys.txt', 'w') as e:
				e.write(str(privateKey))
			exit()
		elif BB.x == PublicKey.x:
			privateKey = n - privKey
			print("Found Private Key:", privateKey)
			print("Matching Public Key:", BB.x)
			print("Please Do Not Loose This Key...Thank You")
			print("This Key Has Been Written To A File Called foundKeys.txt")
			with open('foundKeys.txt', 'w') as e:
				e.write(str(privateKey))
			exit()
		else:
			hashIteration = 1
			a = (privKey * (57896044618658097711785492504343953926418782139537452191302581570759080747169**5000)%n)
			B = BB * a
			while hashIteration < (10000):
				B = (BB + BB)
				if B.x in tupleCollisionList:
					for i, key in enumerate (tupleCollisionList):
						if key == B.x:
							privateKey = ((privKey * (2**hashIteration))%n)
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
								print("Collision Key Found in Multiples Collision List:")
								print("Iteration Number:", i)
								print("Collision Public Key:", key)
								print("Collision Private Key:", privateKey)
								print("Actual Private Key:", D)
								print("Please Do Not Loose This Key...Thank You")
								print("This Key Has Been Written To A File Called foundKeys.txt")
								with open('foundKeys.txt', 'w') as e:
									e.write(str(D))
								exit()
				elif BB.x in tupleHalvesCollisionList:
					for i, key in enumerate (tupleHalvesCollisionList):
						if key == B.x:
							privateKey = ((privKey * (2**hashIteration))%n)
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
								print("Collision Key Found in Halves Collision List:")
								print("Iteration Number:", i)
								print("Collision Public Key:", key)
								print("Collision Private Key:", privateKey)
								print("Actual Private Key:", D)
								print("Please Do Not Loose This Key...Thank You")
								print("This Key Has Been Written To A File Called foundKeys.txt")
								with open('foundKeys.txt', 'w') as e:
									e.write(str(D))
								exit()	
				BB = B
				hashIteration = hashIteration + 1
			##Keys per second is shown after 10000 random keys are generated as public keys
			elapsed_time = time.process_time() - t
			C = ((10000)//elapsed_time)
			print(C," keys per second")
			CCC = ((iterations*10000))
			print("Total Positions Tried:",CCC)
			privKey = int((hashlib.sha256(os.urandom(16)).hexdigest()), 16)
			iterations = iterations + 1
