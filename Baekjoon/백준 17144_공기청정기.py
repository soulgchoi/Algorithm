import sys
sys.stdin = open('17144.txt', 'r')


R, C, T = map(int, input().split())
home = [list(map(int, input().split())) for _ in range(R)]

print(*home, sep='\n')
def iswall(x, y):
	return True if 0 <= x < R and 0 <= y < R else False

def isair(x, y):
	return True if home[x][y] != -1 else False
