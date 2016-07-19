# Christopher Hsiao - 7/19/2016
# Problem 10:The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# NOTE: Reusing code from my 10001prime.py 

n = 2
sum = 0
# Determines if the number n is prime
def isPrime(n):
	if n <= 1:
		return False
	elif n <= 3:
		return True
	elif n%2 == 0 or n%3 == 0:
		return False
	i = 5
	while pow(i,2) <= n:
		if n%i == 0 or n%(i+2) == 0:
			return False
		i+=6
	return True
# while the number if less than 2 million
while n < 2000000:
	# check if it is prime
	if isPrime(n):
		# print it out if it is
		print(str(n))
		# add the number to the running sum
		sum += n
	n+=1
# print out the sum
print("Sum: " + str(sum))