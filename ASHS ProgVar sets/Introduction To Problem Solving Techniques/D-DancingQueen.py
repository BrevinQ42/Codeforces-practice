N = int(input()) # verseCount
print(1 if N%4 == 1 or N%4 == 2 else 0)
print("ABBA"[4-N%4:] + "ABBA" * (N//4))