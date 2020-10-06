def solution(s):
    arr = list(map(int, s.split(' ')))
    return '%d %d' % (min(arr), max(arr))
