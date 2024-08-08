# credits to Ahia

N = int(input())

if N % 2 == 0 and N >= 8:
	print("YES")
	print(f"4 {N-4}")
elif N % 2 == 1 and N >= 13:
	print("YES")
	print(f"9 {N-9}")
else:
	print("NO")