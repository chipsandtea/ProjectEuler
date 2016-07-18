count = 1
n = 2
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
while count <= 10003:
	if isPrime(n):
		print(str(count) + " " + str(n))
		count+=1
	n+=1
print(str(count) + " " + str(n))