N, K = [int(i) for i in input().split()]
a = [int(a_i) for a_i in input().split()]

freq_counter = [0 for num in range(100000)]
sub_sums = [0 for num in range(100000)]

max_value = 0
previous_sum = 0

for i in range(N-K+1):
	currrent_value = previous_sum

	if i > 0:
		previous_value = a[i-1]-1
		freq_counter[previous_value] -= 1
		currrent_value -= sub_sums[previous_value]

		if freq_counter[previous_value] != 0:
			sub_sums[previous_value] = freq_counter[previous_value] * freq_counter[previous_value] * (previous_value+1)
			currrent_value += sub_sums[previous_value]
		else:
			sub_sums[previous_value] = 0

		next_value = a[i+K-1]-1
		freq_counter[next_value] += 1

		currrent_value -= sub_sums[next_value]
		sub_sums[next_value] = freq_counter[next_value] * freq_counter[next_value] * (next_value+1)
		currrent_value += sub_sums[next_value]
	else:
		value_set = set()
		
		for j in range(K):
			freq_counter[a[i+j]-1] += 1
			value_set.add(a[i+j]-1)

		for value in value_set:
			sub_sums[value] = freq_counter[value] * freq_counter[value] * (value+1)
			currrent_value += sub_sums[value]

	max_value = max(max_value, currrent_value)
	previous_sum = currrent_value
	
print(max_value)