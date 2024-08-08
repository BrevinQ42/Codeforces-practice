s = int(input()) # startIndex
e = int(input()) # endIndex
t = int(input()) # timeInSeconds

print("YES" if t - abs(s-e) >= 0 and (t - abs(s-e)) % 2 == 0 else "NO")