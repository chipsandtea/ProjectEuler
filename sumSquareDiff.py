sumOfSquares = 0
squareOfSums = 0
for i in range(101):
	print(pow(i,2))
	sumOfSquares+=pow(i,2)

squareOfSums = pow(((100)*(101))/2,2)
print(squareOfSums-sumOfSquares)