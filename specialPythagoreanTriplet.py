
for a in range(1000):
	b = a+1
	c = b+1
	while c <= 1000:
		while c*c < (a*a + b*b):
			c+=1
		if c*c == (a*a + b*b):
			#print('a:' + str(a) + ' b:' + str(b) + ' c:' + str(c))
			if a+b+c == 1000:
				print(a*b*c)
				break
		b+=1