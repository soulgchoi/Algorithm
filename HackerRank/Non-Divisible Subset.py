def nonDivisibleSubset(k, s):
	cnt = [0] * k
	for x in s:
		cnt[x % k] += 1

	ans = min(cnt[0], 1)
	for rem in range(1, (k + 1) // 2):
		ans += max(cnt[rem], cnt[k - rem])
	if k % 2 == 0:
		ans += min(cnt[k // 2], 1)
	return

nonDivisibleSubset(3, [1, 7, 2, 4])