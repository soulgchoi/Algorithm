def func(val, d):
    global answer, n, result
    if val == result:
        if d < answer:
            answer = d
    else:
        for a in range(1, 8-d+1):
            num = int(str(n) * a)
            func(val + num, d+len(str(num)))
            func(val - num, d+len(str(num)))
            func(val * num, d+len(str(num)))
            func(val // num, d+len(str(num)))


def solution(N, number):
    global answer, n, result
    answer = 9
    n, result = N, number
    func(0, 0)
    return answer if answer < 9 else -1

print(solution(5, 12))
print(solution(2, 11))