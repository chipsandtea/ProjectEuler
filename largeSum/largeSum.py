# Christopher Hsiao - 6/20/2016
# Problem 13: Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

data = []
with open("grid.dat") as grid:
	for num in grid:
		data.append(num)

sum = 0
for num in data:
	currNum = int(num[:15])
	sum += currNum
sum = str(sum)
print(sum[:10])