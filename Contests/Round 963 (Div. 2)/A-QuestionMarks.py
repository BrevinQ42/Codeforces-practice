t = int(input())

for case in range(t):
	n = int(input())
	answers = input()

	freq_count = [0 for option in ['A','B','C','D']]
	max_score = 0

	for i in range(4*n):
		answer = answers[i]
		if answer != '?':
			if freq_count[ord(answer)-ord('A')] < n:
				freq_count[ord(answer)-ord('A')] += 1
				max_score += 1

	print(max_score)