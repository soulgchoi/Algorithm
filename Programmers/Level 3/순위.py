def solution(n, results):
    answer = 0
    lose = {}
    win = {}
    for winner, loser in results:
        if loser in lose:
            lose[loser] += [winner]
        else:
            lose[loser] = [winner]

        if winner in win:
            win[winner] += [loser]
        else:
            win[winner] = [loser]

    for i in range(1, n+1):
        total_win, total_lose = [i], [i]
        x = 0
        while x < len(total_win):
            if total_win[x] in win:
                for y in win[total_win[x]]:
                    if y in total_win: continue
                    total_win += [y]
            x += 1
        a = 0
        while a < len(total_lose):
            if total_lose[a] in lose:
                for b in lose[total_lose[a]]:
                    if b in total_lose: continue
                    total_lose += [b]
            a += 1

        if len(set(total_win + total_lose)) == n:
            answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))  # 2
