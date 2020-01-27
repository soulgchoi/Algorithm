import sys
sys.stdin = open('17406.txt', 'r')

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
bingle = [tuple(map(int, input().split())) for _ in range(K)]

print(arr)
print(bingle)

k = 0
while k < K:
	r, c, s = K[k]
	edges = [(r-s-1, c-s-1), (r-s-1, c+s-1), (r+s-1, c+s-1), (r+s-1, c-s-1)]
	if ((c+s)-(r-s)) % 2:  # 홀수면 가운데 있음

	else:  # 짝수면 가운데 없음

