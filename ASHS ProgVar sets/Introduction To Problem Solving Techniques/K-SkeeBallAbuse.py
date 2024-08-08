P = int(input())
X = int(input())
Y = int(input())
M = int(input())

if X * M > Y:
	token_count = (P // M) * Y

	if P % M > 0:
		token_count += min(X * (P%M), Y)

	print(token_count)

else:
	print(X * P)