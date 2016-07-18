def isPalindrome(n):
	return str(n) == str(n)[::-1]
def findLargest(bot, top):
	z = 0
	for x in range(top, bot, -1):
		for y in range(top, bot, -1):
			if isPalindrome(x*y):
				if x*y > z:
					z = x*y
	return z

print(findLargest(100, 999))