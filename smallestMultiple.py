num = 20

def checkDivisibility(n):
	if n%20 == 0: #10, 5, 4, 2, 1
		if n%18 == 0: # 9, 6, 3
			if n%16 == 0: #8
				if n%19 == 0 and n%17 == 0 and n%15 == 0 and n%14 == 0 and n%13 == 0 and n%12 == 0 and n%11 == 0:
					return True
	return False


while True:
	if checkDivisibility(num):
		print(num)
		break
	num+=1