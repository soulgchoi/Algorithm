# 틀린 답
def solution(board):
	answer = 0
	square = []
	for row in range(len(board)):
		for col in range(len(board[0])):
			if board[row][col] == 1:
				x, y = row, col
				tmp = [x, y]
				for i in range(5):
					while board[x][y] == 1:
						if i == 0:
							if y == len(board[0])-1:
								break
							else:
								y += 1
						elif i == 1:
							if x == len(board)-1:
								break
							else:
								x += 1
						elif i == 2:
							tx, ty = x - tmp[0], y - tmp[1]
							if tx > ty:
								x -= tx - ty
							elif ty > tx:
								y -= ty - tx
							square = [x - tmp[0], y - tmp[1]]
							break
						elif i == 3:
							if y == tmp[1]:
								break
							else:
								y -= 1
						elif i == 4:
							if x == tmp[0]:
								break
							else:
								x -= 1
					if i in [0, 2] and board[x][y] != 1:
						y -= 1
					elif i in [1, 3] and board[x][y] != 1:
						x -= 1
				if [x, y] == tmp:
					if (square[0]+1) * (square[1]+1) > answer:
						answer = (square[0]+1) * (square[1]+1)
			else: continue
			break
	return answer


solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])