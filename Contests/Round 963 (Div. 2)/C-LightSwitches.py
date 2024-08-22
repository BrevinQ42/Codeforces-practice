t = int(input())

for case in range(t):
	n,k = [int(x) for x in input().split()]
	a = sorted([int(a_i) for a_i in input().split()])

	latestInstallment = a[-1]
	timeBeforeEarliestClose = -1
	timeBeforeLatestOpen = -1
	isPossible = True

	for i in range(n-1):
		deltaTime = latestInstallment - a[i]
		timeBeforeSwitch = k - deltaTime % k

		if timeBeforeSwitch == k and (deltaTime // k) % 2 == 1:
			print(-1)
			isPossible = False
			break

		if (deltaTime // k) % 2 == 0: # on
			if timeBeforeEarliestClose == -1:
				timeBeforeEarliestClose = timeBeforeSwitch
			else:
				timeBeforeEarliestClose = min(timeBeforeEarliestClose, timeBeforeSwitch)

		else: # off
			if timeBeforeLatestOpen == -1:
				timeBeforeLatestOpen = timeBeforeSwitch
			else:
				timeBeforeLatestOpen = max(timeBeforeLatestOpen, timeBeforeSwitch)

	if isPossible:
		if timeBeforeLatestOpen == -1:
			print(latestInstallment)
		elif timeBeforeEarliestClose == -1 or timeBeforeLatestOpen < timeBeforeEarliestClose:
			print(latestInstallment + timeBeforeLatestOpen)
		else:
			print(-1)