n = int(input())
if n < 4:
	print("NO")
else:
	print("YES")

	if n % 2 == 0:
		print("4 * 3 = 12")
		print("12 * 2 = 24")
		print("24 * 1 = 24")

		for i in range(5, n+1, 2):
			print(f"{i+1} - {i} = 1")
			print("24 * 1 = 24")

	else:
		print("5 * 4 = 20")
		print("20 + 3 = 23")
		print("23 + 2 = 25")
		print("25 - 1 = 24")

		for i in range(6, n+1, 2):
			print(f"{i+1} - {i} = 1")
			print("24 * 1 = 24")