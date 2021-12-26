from tinyec.ec import SubGroup, Curve
import time

name = 'secp256k1'
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
g = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
h = 1
curve = Curve(a, b, SubGroup(p, g, n, h), name)
pubKey = curve.g*1
CollisionList = []
iteration = 1
AA = int(input("Please Enter the Size of the collision List You would Like To Create:"))
print("Creating Benchmark Collision List...Please Wait...")
t = time.process_time()
while iteration < (AA):
	A = pubKey*2
	CollisionList.append(A.x)
	pubKey = A
	iteration = iteration + 1

elapsed_time = time.process_time() - t
print("Benchmark Collision List of key size", iteration)
print("Created in...")
print(elapsed_time,"seconds at")
C = iteration//elapsed_time
print(C," keys per second")

print("List Search Benchmark...Please Wait...")
t1 = time.process_time()
B = curve.g* iteration
if B.x in CollisionList:
	print("Test Key Found!")
elapsed_time1 = time.process_time() - t1
print(elapsed_time1)
print("Comparisions per second")
