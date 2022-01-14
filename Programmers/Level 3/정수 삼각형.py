def solution(triangle):
    dp = [triangle[0]]
    for i in range(1, len(triangle)):
        cur = dp[-1]
        nxt = [0] * (len(cur) + 1)
        for j in range(len(cur)):
            a, b = cur[j] + triangle[i][j], cur[j] + triangle[i][j+1]
            nxt[j] = a if a > nxt[j] else nxt[j]
            nxt[j+1] = b if b > nxt[j+1] else nxt[j+1]
        dp.append(nxt)

    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))