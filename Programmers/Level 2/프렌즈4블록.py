import copy


def del_block(arr, x, y, val):
	c = (val, val.lower(), val.upper())
	if x < len(arr) - 1 and y < len(arr[x]) - 1:
		if arr[x + 1][y] in c and arr[x + 1][y + 1] in c and arr[x][y + 1] in c:
			arr[x][y] = arr[x + 1][y] = arr[x + 1][y + 1] = arr[x][y + 1] = val.lower()
	return arr


def set_block(arr, x, y):
	for i in range(x-1, 1, -1):
		if arr[i][y] == '0':
			j = i
			while j > 0 and arr[j][y] == '0':
				j -= 1
			arr[i][y] = arr[j][y]
			arr[j][y] = '0'
	return arr


def solution(m, n, board):
	board = list(list(s for s in b) for b in board)
	# print(*board, sep='\n')
	# print()
	while True:
		check = copy.deepcopy(board)
		for r in range(m):
			for c in range(n):
				if board[r][c] != '0':
					del_block(board, r, c, board[r][c])
		for r2 in range(m):
			for c2 in range(n):
				if board[r2][c2].islower():
					board[r2][c2] = '0'
		for i in range(n):
			board = set_block(board, m, i)
		if board == check:
			break
	# print(*board, sep='\n')
	return sum(board, []).count('0')


# solution(6, 6, ["IIIIOO", "IIIOOO", "IIIOOI", "IOOIII", "OOOIII", "OOIIII"])
# print()
# solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
# print()
# solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
