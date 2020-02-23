import sys
sys.stdin = open('14890.txt', 'r')

for _ in range(4):
	N, L = map(int, input().split())
	data = [list(map(int, input().split())) for _ in range(N)]

	print(*data, sep='\n')