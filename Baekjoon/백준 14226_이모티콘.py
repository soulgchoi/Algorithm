import sys
sys.stdin = open('14226.txt', 'r')


def func1():
	return

def func2():
	return

for _ in range(4):
	S = int(input())
	print(S)

	ans = 0
	res = 1
	temp = 0
	while res != S:
		if res < S:
			func1()
			func2()

		else:
			res -= 1
			ans += 1