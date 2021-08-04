import sys
import itertools

sys.stdin = open('1182.txt', 'r')

#
# def func(idx, k):
#     global answer
#
#     if k == S:
#         answer += 1
#
#     if idx >= N:
#         return
#
#     func(idx + 1, k + numbers[idx])
#     func(idx + 1, k)


N, S = list(map(int, input().split()))
numbers = list(map(int, input().split()))

answer = 0

for i in range(1, N + 1):
    combs = itertools.combinations(numbers, i)
    for c in combs:
        if sum(c) == S:
            answer += 1

print(answer)
