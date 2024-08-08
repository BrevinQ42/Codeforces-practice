N = int(input())
K = int(input())

if N % (K+1) == 0:
	print("UNWINNABLE")
else:
	print("WINNABLE")
	print(N % (K+1))