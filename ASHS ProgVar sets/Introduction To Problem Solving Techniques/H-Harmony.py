n = int(input())

print("YES")

for i in range(n):
	print('B' + '.' * (3*n-1))
	print('N' + '.' * (3*n-1))

index = 1
for i in range(n):
	print('.' * index + 'R' + '.' * (3*n-index-1))
	index += 1