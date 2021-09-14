def single(score):
    return score


def double(score):
    return score ** 2


def triple(score):
    return score ** 3


def cal_bonus(char, score):
    if char == 'S':
        return single(score)
    if char == 'D':
        return double(score)
    if char == 'T':
        return triple(score)


def solution(dartResult):
    answer = []
    temp = ''
    i = 0
    while i < len(dartResult):
        if dartResult[i].isdecimal():
            while dartResult[i].isdecimal():
                temp += dartResult[i]
                i += 1
            temp = int(temp)
        if dartResult[i].isalpha():
            temp = cal_bonus(dartResult[i], temp)
        if dartResult[i] == '*':
            if answer: answer[-1] *= 2
            temp *= 2
        if dartResult[i] == '#':
            temp *= -1

        if i != (len(dartResult) - 1):
            if dartResult[i + 1].isdecimal():
                answer += [temp]
                temp = ''

        i += 1
    return sum(answer) + temp


print(solution("1S2D*3T"))  # 37
print(solution("1D2S#10S"))  # 9
print(solution("1D2S0T"))  # 3
print(solution("1S*2T*3S"))  # 23
print(solution("1D#2S*3S"))  # 5
print(solution("1T2D3D#"))  # -4
print(solution("1D2S3T*"))  # 59
