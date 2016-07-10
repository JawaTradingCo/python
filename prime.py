# python prime number generator

def isNotPrime(p,i):
	return p % i == 0 and i != p and i != 1

def findPrimes(many):
	many = int(many)
	count = 0
	p = 2;
	while count < many:
		prime = True
		
		for i in range(1,10):
			#print(str(p) + " % " + str(i) + " = " + str(p%i))
			if isNotPrime(p,i):
				
				prime = False
				break
		if prime == True:
			count += 1
			print("#%d) %d is a prime number."%(count,p))
			
		p += 1

	print("Done counting.")

	
		
if __name__ == "__main__":
	many = raw_input('How many primes?')
	findPrimes(many)
