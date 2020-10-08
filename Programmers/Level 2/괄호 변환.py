# 어렵다고 생각했는데.. 문제에 있는대로만 구현하면 답이 나온다
def func1(s):
    cnt = 0
    for idx, val in enumerate(s):
        if val == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return idx


def func2(s):
    cnt = 0
    for val in s:
        if val == '(':
            cnt += 1
        if val == ')':
            if cnt == 0:
                return False
            else:
                cnt -= 1
    return False if cnt > 0 else True


def solution(p):
    if p == '' or func2(p):
        return p
    u_idx = func1(p)
    u, v = p[:u_idx+1], p[u_idx+1:]
    if func2(u):
        return u + solution(v)
    else:
        tmp = '(' + solution(v) + ')'
        u = u[1:-1]
        for val in u:
            if val == '(':
                tmp += ')'
            else:
                tmp += '('
        return tmp


# def solution(p):
#     answer = ''
#     l_cnt, r_cnt = 0, 0
#     for q in p:
#         if q == '(':
#             if r_cnt > 0:
#                 r_cnt -= 1
#                 answer += ')'
#             else:
#                 l_cnt += 1
#                 answer += '('
#         elif q == ')':
#             if l_cnt > 0:
#                 l_cnt -= 1
#                 answer += ')'
#             else:
#                 r_cnt += 1
#                 answer += '('
#     return answer
