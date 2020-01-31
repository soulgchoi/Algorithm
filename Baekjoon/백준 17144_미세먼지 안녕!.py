import sys
sys.stdin = open('17144.txt', 'r')


R, C, T = map(int, input().split())
home = [list(map(int, input().split())) for _ in range(R)]
oa = []
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def iswall(x, y):
	return True if 0 <= x < R and 0 <= y < C else False

# def isair(x, y):
# 	return True if home[x][y] != -1 else False

for r in range(R):
	for c in range(C):
		if home[r][c] == -1:
			oa += [(r, c)]

print(oa)

def mise():
	misearr = []
	for m in range(R):
		for s in range(C):
			if home[m][s] > 0:
				misearr += [(m, s)]
	return misearr

mise_arr = mise()

def func1():
	temp = [[0]*C for _ in range(R)]
	for ms in mise_arr:
		r1, c1 = ms
		air = home[r1][c1]
		for dx, dy in dxdy:
			nr1, nc1 = r1 + dx, c1 + dy
			if iswall(nr1, nc1) and (nr1, nc1) not in oa:
				temp[nr1][nc1] += air // 5
				home[r1][c1] -= air // 5
	return temp

temp_arr = func1()
print(mise_arr)
print(*home, sep='\n')



def func2():
	for r2 in range(R):
		for c2 in range(C):
			if (r2, c2) not in oa:
				home[r2][c2] += temp_arr[r2][c2]

func2()


def func3():


