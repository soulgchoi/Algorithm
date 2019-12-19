import sys, pprint, itertools
sys.stdin = open('3752.txt', 'r')

T = int(input())
for tc in range(1, T+1):
	N = int(input())
	data = list(map(int, input().split()))

	pwset = [[]]
	for d in data:
		tmp = [x + [d] for x in pwset]
		pwset += tmp

	ans = [0]
	cnt = 1
	for pw in pwset:
		sump = sum(pw)
		if sump not in ans:
			ans += [sump]
			cnt += 1
	print('#%d %d' % (tc, cnt))