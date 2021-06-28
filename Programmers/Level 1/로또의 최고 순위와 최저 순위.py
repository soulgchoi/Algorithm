def solution(lottos, win_nums):
    win = [6, 6, 5, 4, 3, 2, 1]
    zero_cnt = lottos.count(0)
    win_cnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            win_cnt += 1
    return [win[win_cnt+zero_cnt], win[win_cnt]]


# print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3, 5]
# print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))  # [1, 6]
# print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))  # [1, 1]