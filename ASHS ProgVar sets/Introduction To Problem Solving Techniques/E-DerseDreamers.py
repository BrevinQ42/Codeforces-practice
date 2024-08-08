a = int(input()) # initialXCoordinate
b = int(input()) # initialYCoordinate
c = int(input()) # targetXCoordinate
d = int(input()) # targetYCoordinate

if (c-a + d-b) % 2 == 0:
	print("YES")
	print(max(abs(c-a), abs(d-b)))
else:
	print("NO")