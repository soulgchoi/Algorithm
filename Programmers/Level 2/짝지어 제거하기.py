# 효율성 통과 못함..
def solution(s):
    new_s = s[0]
    i = 1
    while i < len(s):
        if not new_s:
            new_s = s[i]
        elif new_s[-1] == s[i]:
            new_s = new_s[:-1]
        else:
            new_s += s[i]
        i += 1

    return 1 if not new_s else 0


# 리스트가 더 빠르구나!
def solution(s):
    new_s = [s[0]]
    i = 1
    while i < len(s):
        if not new_s:
            new_s = [s[i]]
        elif new_s[-1] == s[i]:
            new_s.pop(-1)
        else:
            new_s += [s[i]]
        i += 1

    return 1 if not new_s else 0
