N, K = [int(i) for i in input().split()] # songCount, minimumDistance
songs = [song for song in input().split()]

if K > N // 2:
	print("NO")
else:
	print("YES")
	print(*(songs[N//2:] + songs[:N//2]))