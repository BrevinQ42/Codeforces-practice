t = int(input())

for case in range(t):
	n = int(input())
	a = [int(a_i) for a_i in input().split()]

	evens = []
	biggest_odd = 0
	for a_i in a:
		if a_i % 2 == 0:
			evens.append(a_i)
		else:
			biggest_odd = max(biggest_odd, a_i)

	if biggest_odd == 0 or not evens:
		print(0)
		continue

	evens.sort(reverse=True)

	operations_count = 0
	while evens:
		smallest_even = evens[-1]
		if smallest_even < biggest_odd:
			evens.pop()
			biggest_odd += smallest_even
		else:
			biggest_odd += evens[0]
			
		operations_count += 1

	print(operations_count)