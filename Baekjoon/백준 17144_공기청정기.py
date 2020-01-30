import sys
sys.stdin = open('17144.txt', 'r')

R, C, T = map(int, input().split())
home = [list(map(int, input().split())) for _ in range(R)]

print(*home, sep='\n')