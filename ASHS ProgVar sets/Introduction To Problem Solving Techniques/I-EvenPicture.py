n = int(input())

print(7 + (n-1)*3)

offset = -(n // 2)
print((-1 + offset), (-1 + offset))
print((0 + offset), (-1 + offset))
print((-1 + offset), (0 + offset))
print((0 + offset), (0 + offset))

for i in range(1, n+1):
	print((0 + offset + i), (0 + offset + i-1))
	print((0 + offset + i-1), (0 + offset + i))
	print((0 + offset + i), (0 + offset + i))