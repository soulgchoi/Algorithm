from itertools import combinations


def solution(orders, course):
    comb_orders = {}
    for i in range(len(orders)):
        order = [x for x in orders[i]]
        for j in range(2, len(order)+1):
            combs = list(combinations(order, j))
            for comb in combs:
                comb = tuple(sorted(comb))
                if len(comb) in course:
                    if comb in comb_orders.keys():
                        comb_orders[comb] += 1
                    else:
                        comb_orders[comb] = 1

    candidates = {}
    for c in course:
        candidates[c] = [[], 2]
    for key, val in comb_orders.items():
        if val > candidates[len(key)][1]:
            candidates[len(key)][0] = ["".join(key)]
            candidates[len(key)][1] = val
        elif val == candidates[len(key)][1]:
            candidates[len(key)][0] += ["".join(key)]

    answer = []
    for cd in candidates.values():
        answer += cd[0]
    return sorted(answer)


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))  # ["AC", "ACDE", "BCFG", "CDE"]
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))  # ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))  # ["WX", "XY"]
