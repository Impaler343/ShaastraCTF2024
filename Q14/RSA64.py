# Python for RSA asymmetric cryptographic algorithm.
# For demonstration, values are
# relatively small compared to practical application
import math


def gcd(a, h):
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp


p = 3623
q = 3631
n = p*q
e = 2
phi = (p-1)*(q-1)

while (e < phi):

	# e must be co-prime to phi and
	# smaller than phi.
	if(gcd(e, phi) == 1):
		break
	else:
		e = e+1

# Private key (d stands for decrypt)
# choosing d such that it satisfies
# d*e = 1 + k * totient

k = 2
d = (1 + (k*phi))/e
while(d%1 != 0):
	k += 1
	d = (1 + (k*phi))/e
def RSA(val,n,e):
	
	# Encryption c = (msg ^ e) % n
	c = pow(val, e)
	c = int(math.fmod(c, n))
	#print("Encrypting: ",val,n,e,c)
	return c

# Message to be encrypted
msg = "ShaastraCTF{}"
#msg = "hi"
print("Message data = ", msg)
encrypted = []
for i in msg:
	encrypted.append(RSA(ord(i),n,e))
print("Encrypted data = ", encrypted)
print("public key :",n)
print("private key :", d)

def decrypt2(val,n,d):
	x = val
	while(d > 1):
		while(x<n and d > 1):
			d -= 1
			x *= val
		x = x%n
	return x
decrypted = ""
a = []
for i in encrypted:
	x = decrypt2(i,n,d)
	a.append(x)
	decrypted += chr(x)
print(a)
print("Original Message Sent = ",decrypted)