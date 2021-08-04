def sign(boolean):
    return 1 if boolean else -1


def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer += absolutes[i] * sign(signs[i])
    return answer
