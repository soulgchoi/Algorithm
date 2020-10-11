import itertools


# 이것은 시간초과
def solution(nums):
    ponketmon = len(nums) // 2
    combs = list(set(itertools.combinations(nums, ponketmon)))
    combs = list(map(list, map(set, combs)))
    combs.sort(key=len)
    return len(combs[-1])


# 이것은 정답
def solution(nums):
    n = len(nums) // 2
    ponketmon = list(set(nums))
    return len(ponketmon) if len(ponketmon) < n else n
