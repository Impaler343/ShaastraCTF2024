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
def private_from_public(n):
	global primes
	p=q = n**0
	i = 0
	j = len(primes)-1
	while(p < primes[i]):
		i += 1
	p = primes[i-1]
	while(q > primes[j]):
		j -= 1
	q = primes[j+1]
	while(p*q != n):
		if(p*q < n):
			i -= 1
		elif(p*q>n):
			j += 1
		p = primes[i]
		q = primes[j]
	return (p,q)
print(private_from_public(13155113))