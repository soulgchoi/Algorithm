import sys
sys.stdin = open('2383 [모의 SW 역량테스트] 점심 식사시간.txt', 'r')

T = int(input())
for tc in range(1, 2):
	N = int(input())
	data = [list(map(int, input().split())) for _ in range(N)]

	print(*data, sep='\n')
	"""
	① 계단 입구까지 이동 시간
		- 사람이 현재 위치에서 계단의 입구까지 이동하는데 걸리는 시간으로 다음과 같이 계산한다.
		- 이동 시간(분) = | PR - SR | + | PC - SC |
	  (PR, PC : 사람 P의 세로위치, 가로위치, SR, SC : 계단 입구 S의 세로위치, 가로위치)
    ② 계단을 내려가는 시간
        - 계단을 내려가는 시간은 계단 입구에 도착한 후부터 계단을 완전히 내려갈 때까지의 시간이다.
        - 계단 입구에 도착하면, 1분 후 아래칸으로 내려 갈 수 있다.
        - 계단 위에는 동시에 최대 3명까지만 올라가 있을 수 있다.
        - 이미 계단을 3명이 내려가고 있는 경우, 그 중 한 명이 계단을 완전히 내려갈 때까지 계단 입구에서 대기해야 한다.
        - 계단마다 길이 K가 주어지며, 계단에 올라간 후 완전히 내려가는데 K 분이 걸린다.
        
    지도 내에 1 은 사람을 나타내고, 2 이상 10 이하의 숫자는 계단의 입구를 나타내며 해당 숫자는 계단의 길이를 의미한다.
    """
	sarams = []
	stairs = []

	for row in range(N):
		for col in range(N):
			if data[row][col] == 1:
				sarams += [(row, col, 0)]
			elif data[row][col] not in [0, 1]:
				stairs += [(row, col, data[row][col])]

	print(stairs)
	print(sarams)