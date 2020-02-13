import sys
sys.stdin = open('1953 [모의 SW 역량테스트] 탈주범 검거.txt', 'r')

T = int(input())
for tc in range(1, T+1):
	N, M, R, C, L = map(int, input().split())
	data = [list(map(int, input().split())) for _ in range(N)]

	print(*data, sep='\n')

	# 터널 타입
	temp = 0
