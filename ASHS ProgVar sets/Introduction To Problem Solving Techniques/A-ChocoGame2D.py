M = int(input()) # rows
N = int(input()) # columns

if M == N:
	print("UNWINNABLE")
else:
	print("WINNABLE")

	if M > N:
		print(f"H {N}")
	else:
		print(f"V {M}")