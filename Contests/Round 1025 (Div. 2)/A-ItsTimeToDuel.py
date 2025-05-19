t = int(input())

for test in range(t):
	playerCount = int(input())
	results = [int(a) for a in input().split()]

	zeroFound = False
	oneFound = False

	if results[0] == 0:
		zeroFound = True
	else:
		oneFound = True

	# print(0, zeroFound, oneFound)
	verdictPrinted = False

	for i in range(1, playerCount):
		# print(i, zeroFound, oneFound)
		if results[i] == 0:
			if results[i-1] == 0:
				print("YES")
				verdictPrinted = True
				break
			else:
				zeroFound = True
		else:
			oneFound = True

	if not verdictPrinted:
		print("NO" if (zeroFound and oneFound) else "YES")