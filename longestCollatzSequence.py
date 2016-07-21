# Christopher Hsiao - 7/21/2016
# Problem 14: Which starting number, under one million, produces the longest chain?

n = 999999
currMax = (0,0)

# Returns size of chain of Collatz sequence
def collatzSequence(n):
	count = 0
	while n != 1:
		if n%2 == 0:
			count +=1
			n /= 2
		else:
			count += 1
			n = (3*n)+1
	return count

# Runs through all values and stores a running max chain length.
while n >= 1:
	count = collatzSequence(n)
	if count > currMax[1]:
		currMax = (n, count)
	else:
		n-=1

print(currMax)

