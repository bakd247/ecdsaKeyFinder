from tinyec.ec import SubGroup, Curve
from os import urandom
from binarySearch import binarySearch
from tqdm import tqdm, trange
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
	EnteredPublicKey = curve1.g * 1
	CollisionList = []
	PosOneList = []
	N = 115792089237316195423570985008687907852837564279074904382605163141518161494337
	half = 57896044618658097711785492504343953926418782139537452191302581570759080747169
	AA = int(input("Please Enter the Size of the Collision List you would like to Create. Best Performance around 10,000:"))
	AAA = (AA*2)
	BB = AA
	print("Creating Collision List...Please Wait...")
	place = EnteredPublicKey * ((half ** AA)%N)
	PosOneList.append(place.x)
	PosOneList.append(-AA)
	tuplePosOneList = tuple(PosOneList)
	CollisionList.append(tuplePosOneList)
	AA = -AA + 1
	for iterationMultiples in trange (AAA,total=AAA,ascii=True,ncols=100,colour='#00ff00',unit='Keys Stored',desc='Keys Stored In Memory...'):
		PosTwoList = []
		iteratedMultiple = place + place
		PosTwoList.append(iteratedMultiple.x)
		PosTwoList.append(AA)
		tuplePosTwoList = tuple(PosTwoList)
		CollisionList.append(tuplePosTwoList)
		place = iteratedMultiple
		AA += 1
print("SortingList...Please Wait...")
CollisionList.sort(key = lambda i:i[0])
tupleCollisionList = tuple(CollisionList)
print("List Sorted...Searching For Key")
print("Creating Easy Count List...Please Wait...")
from wordAdder import multiplyNum

def easyCount():
	for counter in range (1,4294967297):
		counterKey = multiplyNum(counter)
		easyCountPlace = binarySearch(tupleCollisionList,counterKey.x)
		if easyCountPlace != -1:
			RecoveredKey = counter
			print("Private Key Recovered:", RecoveredKey)
			print("X-CoordinateFound:", counterKey.x)
			KeyFound = True
			exit()

def checkTwos():
	twosCheckSpot = 1
	for twoSpot in range(2):
		for subTwoSpot in range(256):
			twosNewSpotCheck = twosCheckSpot + twosCheckSpot
			if twosNewSpotCheck < 4294967297:
				pass
			else:
				spotToCheck = multiplyNum(twosNewSpotCheck)
				easyCountPlace = binarySearch(tupleCollisionList,spotToCheck.x)
				if spotToCheck != -1:
					RecoveredKey = twosCheckSpot
					print("Private Key Recovered:", RecoveredKey)
					print("X-CoordinateFound:", twosNewSpotCheck.x)
					KeyFound = True
					exit()
				else:
					print("Key Found With Error...Please COntact Support")
				twosCheckSpot = twosNewSpotCheck

def checkThrees():
	threesCheckSpot = 1
	for threeSpot in range(3):
		for subThreeSpot in range(192):
			threesNewSpotCheck = threesCheckSpot + threesCheckSpot
			if threesNewSpotCheck < 4294967297:
				pass
			else:
				spotToCheck = multiplyNum(threesNewSpotCheck)
				easyCountPlace = binarySearch(tupleCollisionList,spotToCheck.x)
				if spotToCheck != -1:
					RecoveredKey = threesCheckSpot
					print("Private Key Recovered:", RecoveredKey)
					print("X-CoordinateFound:", threesNewSpotCheck.x)
					KeyFound = True
					exit()
				else:
						print("Key Found With Error...Please COntact Support")
				threesCheckSpot = threesNewSpotCheck

print("Checking Easily Countable Positions...")
counter = 1
while counter < 4294967297:
	easyCount()
	counter += 1
print("Checking Powers of 2...")
checkTwos()
print("Checking Powers of Three..")
checkThrees()

keyFound = False
while keyFound != True:
	t = time.process_time()
	privKey = 96167372826517772003102616924874179248677911977546683183271655183059990594886 ##(int((((urandom(32))[2:])).hex(), 16))%N
	privateKey1 = (privKey * (half ** BB))%N
	newKey = multiplyNum(privateKey1)
	for hashIteration in trange(AAA,total=AAA,ascii=True,ncols=100,colour='#00ff00',unit='Comparisons',desc='Searching...'):
		keyToFind = int(newKey.x)
		result = binarySearch(tupleCollisionList, keyToFind)
		if result != -1:
			if result[1] <= 0:
				RecFunct = ((privateKey1 * (2 ** hashIteration)) * (2 ** (abs(result[1]))))%N
			else:
				RecFunct = ((privateKey1 * (half ** hashIteration)) * (2 ** (abs(result[1]))))%N
			recoveredKey = multiplyNum(RecFunct)
			if recoveredKey.y != EnteredPublicKey.y:
				RecFunct = N - RecFunct
			print("X-Coordinate Found of Collision Key Found:", result)
			print("Collision PrivateKey:", privateKey1)
			print("Here is the Private Key for the PublicKey that you Entered:", RecFunct)
			keyFound = True
			exit()
		else:
			newKey += newKey

	elapsed_time = time.process_time() - t
	print("Average Random Key Strings Created Per Second",(AAA//elapsed_time))
	print("Average Seconds per Round ", elapsed_time)
