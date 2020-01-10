from itertools import combinations
import sys
sys.stdin = open('2629.txt', 'r')

N = int(input())
choo = list(map(int, input().split()))
goo = int(input())
weight = list(map(int, input().split()))

pws = []
for j in range(N+1):
    pws += list(combinations(choo, j))

sum_choo = []
for p in range(len(pws)//2):
    sum1 = [abs(sum(pws[p]) - sum(pws[-1-p]))]
    sum2 = [sum(pws[p])]
    sum3 = [sum(pws[-1-p])]
    for s in [sum1, sum2, sum3]:
        if s not in sum_choo:
            sum_choo += s

for i in weight:
    if i in sum_choo:
        print('Y', end=' ')
    else:
        print('N', end=' ')