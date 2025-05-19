log2 = {1: 0}

def calculateLog2(x):
	if x in log2:
		return log2[x]

	log2[x] = 1 + calculateLog2((x+1) // 2)
	return log2[x]

t = int(input())

for test in range(t):
	width, height, x, y = [int(i) for i in input().split()]
	UL_x = 1
	UL_y = 1

	if width == height == 1:
		print(0)
		continue

	# removing left side of Fouad's monster
	newWidth = width - (x - UL_x)
	newHeight = height
	minimumTurns = 1 + calculateLog2(newWidth) + calculateLog2(newHeight)

	# removing top side
	noOfTurns = 1 + calculateLog2(width) + calculateLog2(height - (y - UL_y))
	if minimumTurns > noOfTurns:
		newWidth = width
		newHeight = height - (y - UL_y)
		minimumTurns = noOfTurns

	# removing right side
	noOfTurns = 1 + calculateLog2(width - (UL_x + width-1 - x)) + calculateLog2(height)
	if minimumTurns > noOfTurns:
		newWidth = width - (UL_x + width-1 - x)
		newHeight = height
		minimumTurns = noOfTurns

	# removing bottom side
	noOfTurns = 1 + calculateLog2(width) + calculateLog2(height - (UL_y + height-1 - y))
	if minimumTurns > noOfTurns:
		newWidth = width
		newHeight = height - (UL_y + height-1 - y)
		minimumTurns = noOfTurns

	print(minimumTurns)