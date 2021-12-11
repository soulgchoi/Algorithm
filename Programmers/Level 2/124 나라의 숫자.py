# 시간초과
# def solution(n):
#     numbers = [''] * (n+1)
#     numbers[0] = '0'
#     rule = [4, 1, 2]
#
#     m = 1
#     while m <= n:
#         x, y = divmod(m, 3)
#         if y == 0:
#             x -= 1
#             y = 3
#
#         numbers[m] = str(numbers[x]) + str(rule[y % 3])
#         m += 1
#     return numbers[n][1:]

def solution(n):
    rule = [4, 1, 2]
    answer = ''
    while n > 0:
        m = n % 3
        answer = str(rule[m]) + answer
        if m == 0:
            n -= 1
        n = int(n / 3)
    return answer


print(solution(1))  # 1
print(solution(2))  # 2
print(solution(3))  # 4
print(solution(4))  # 11
print(solution(10))  # 41
