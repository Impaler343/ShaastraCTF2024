# doesnt work yet
def SieveOfEratosthenes(n): 

	# Create a boolean array 
	# "prime[0..n]" and initialize 
	# all entries it as true. 
	# A value in prime[i] will 
	# finally be false if i is 
	# Not a prime, else true. 
	prime = [True for i in range(n+1)] 
	p = 2
	while (p * p <= n): 

		# If prime[p] is not 
		# changed, then it is a prime 
		if (prime[p] == True): 

			# Update all multiples of p 
			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1
	res = []
	# Print all prime numbers 
	for p in range(2, n+1): 
		if prime[p]: 
			res.append(p)
	return res
primes = SieveOfEratosthenes(4096)

def private(phi,e):
	k = 2
	d = (1 + (k*phi))/e
	while(d%1 != 0):
		k += 1
		d = (1 + (k*phi))/e
	return d
def private_from_public(n,e):
	global primes
	for i in primes:
		for j in primes:
			if(i*j == n):
				return private((i-1)*(j-1),e)
	else:
		return 0,0
	
public_key = 14537813
e = 5
private_key = private_from_public(public_key,e)
print(private_key)

def decrypt2(val,n,d):
	x = val
	while(d > 1):
		while(x<n and d > 1):
			d -= 1
			x *= val
		x = x%n
	return x
a = [13831133, 12917356, 10030587, 10030587, 7776496, 10814604, 6081412, 10030587, 12646311, 9767093, 8851505, 7850875, 256117, 13831133, 11803398, 7205927, 2220894, 12646311, 6081412, 10030587, 2170797, 11065575, 13799515, 12522469, 2708638]
flag = ""
for i in a:
	flag += chr(decrypt2(i,public_key,private_key))
print(flag)