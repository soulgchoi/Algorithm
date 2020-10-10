import itertools


def prime_list(n):
	arr = [0, 0] + [1] * (n - 1)
	for i in range(2, int(n**0.5)+1):
		if arr[i]:
			for j in range(i+i, n+1, i):
				arr[j] = 0
	return [idx for idx in range(n+1) if arr[idx]]


def solution(nums):
	answer = 0

	combs = list(itertools.combinations(nums, 3))
	combs = list(map(sum, combs))
	primes = prime_list(max(combs))

	for comb in combs:
		if comb in primes:
			answer += 1

	return answer
