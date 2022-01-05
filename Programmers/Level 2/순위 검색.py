from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []

    info_dict = {}
    for i in range(len(info)):
        _info = info[i].split()
        info_key = _info[:-1]
        info_score = int(_info[-1])

        for j in range(5):
            for comb in combinations(info_key, j):
                tmp = ''.join(comb)
                if tmp in info_dict:
                    info_dict[tmp].append(info_score)
                else:
                    info_dict[tmp] = [info_score]

    for k in info_dict:
        info_dict[k].sort()

    for q in query:
        _query = q.replace('and', '').replace('-', '').split()
        q_key = ''.join(_query[:-1])
        q_val = int(_query[-1])

        if q_key in info_dict:
            scores = info_dict[q_key]

            if scores:
                enter = bisect_left(scores, q_val)
                answer.append(len(scores) - enter)
            else:
                answer.append(0)
    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]
))  # [1, 1, 1, 1, 2, 4]
