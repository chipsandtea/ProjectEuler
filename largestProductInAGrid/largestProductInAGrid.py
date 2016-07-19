# Christopher Hsiao - 7/19/2016
# Problem 11: What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

# Data Structure: 2D Array
# Movement through 2D Array
# Up/Left: [i--][j++]  -  Up: [i--][j]  -  Up/Right: [i--][j++]
# Left: [i][j--]                           Right: [i][j++]
# Down/Left: [i++][j--] - Down: [i++][j] - Down/Right: [i++][j++]

# Read in the 20x20 Grid and store in a 2D Array
data = []
with open('grid.dat') as gridFile:
	for line in gridFile:
		currLine = [int(x) for x in line.split()]
		data.append(currLine)
		print(currLine)

# Function that crawls the data from a source node's index
def largestProd(x, y):
	products = []
	i,j = x,y
	# Crawl down (i++)
	downProd = 1
	count = 1
	while i < 20 and count <=4:
		downProd *= data[i][j]
		i+=1
		count+=1
	# If it failed to crawl 4 down
	if count < 4:
		downProd = 1
	products.append(downProd)
	i,j = x,y
	# Crawl right (j++)
	rightProd = 1
	count = 1
	while j < 20 and count <=4:
		rightProd *= data[i][j]
		j+=1
		count+=1
	# If it failed to crawl 4 down
	if count < 4:
		rightProd = 1
	products.append(rightProd)
	i,j = x,y
	# Crawl down left (i++)(j--)
	downLeftProd = 1
	count = 1
	while i < 20 and j >= 0 and count <=4:
		downLeftProd *= data[i][j]
		i+=1
		j-=1
		count+=1
	# If it failed to crawl 4 down
	if count < 4:
		downLeftProd = 1
	products.append(downLeftProd)
	i,j = x,y
	#Crawl down right (i++)(j++)
	downRightProd = 1
	count = 1
	while i < 20 and j < 20 and count <=4:
		downRightProd *= data[i][j]
		i+=1
		j+=1
		count+=1
	# If it failed to crawl 4 down
	if count < 4:
		downRightProd = 1
	products.append(downRightProd)
	return max(products)

maxVal = 0
for i in range(len(data)):
	for j in range(len(data)):
		tempNum = largestProd(i,j)
		if maxVal < tempNum:
			maxVal = tempNum

print(maxVal)



