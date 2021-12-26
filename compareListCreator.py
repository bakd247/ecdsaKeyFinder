from tinyec.ec import SubGroup, Curve

X = int((input("Please Enter Your Public Key X Coordinate:")),16)
Y = int((input("Please Enter Your Public Key Y Coordinate:")),16)
AA = int(input("Please Enter The Size Of The Refrence List You Would Like To Create:"))
name = 'secp256k1'
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
g = (X,Y)
h = 1

curve = Curve(a, b, SubGroup(p, g, n, h), name)

privKey = 1
pubKey = curve.g*1
iteration = 1
keys = []

while iteration <= (AA):
	
	s1 = pubKey*(2)
	keys.append(s1.x)
	pubKey = s1
	iteration = iteration+1	
	
with open('compareList.txt', 'w') as e:
	for i, item in enumerate(keys):
		e.write(str(i))
		e.write(",")
		e.write("%s\n" % item)
print("List Created...Please See File Named compareList.txt")
