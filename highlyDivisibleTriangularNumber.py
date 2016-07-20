# Christopher Hsiao - 7/20/2016
# Problem 12: What is the value of the first triangle number to have over five hundred divisors?

# Naive approach to generating divisor count
import math
def divisorGenerator(n):
	count = 1
	sqrt = math.sqrt(n)
	for i in range(1,int(sqrt+1)):
		if n%i == 0:
			count += 2
	if pow(sqrt,2) == n:
		count-=1
	return count

runSum = 0
currNum = 1
currMax = 0
while True:
	# See you tomorrow 
	num = divisorGenerator(runSum)
	if num > currMax:
		currMax = num
	if num < 500:
		print(str(runSum) + ' - ' + str(currNum) + " - " + str(num) + " - " + str(currMax))
		runSum += currNum
		currNum += 1
	else:
		print(str(runSum) + ' - ' + str(currNum) + " - " + str(num) + " - " + str(currMax))
		break