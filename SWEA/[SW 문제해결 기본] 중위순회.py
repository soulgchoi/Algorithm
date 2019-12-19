import sys
sys.stdin = open('[SW 문제해결 기본] 중위순회.txt', 'r')


def traverse(T):
	if T:
		traverse(tree[T][1])
		print(tree[T][0], end='')
		traverse(tree[T][2])

for tc in range(1, 11):
	N = int(input())
	arr = [list(input().split()) for _ in range(N)]
	tree = [[0] * 3 for _ in range(N + 1)]

	for a in arr:
		tree[int(a[0])][0] = a[1]
		if len(a) >= 3:
			tree[int(a[0])][1] = int(a[2])
		if len(a) >= 4:
			tree[int(a[0])][2] = int(a[3])

	print('#%d' % tc, end=' ')
	traverse(1)
	print()