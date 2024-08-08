D = int(input())
M = int(input())
N = int(input())
K = int(input())

print("YES" if (M - N) % K == 0 and abs((M - N) // K) <= D and ((M - N) // K - D) % 2 == 0 else "NO")