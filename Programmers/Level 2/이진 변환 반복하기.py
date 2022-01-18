def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[0] += 1

        tmp = ''
        for x in s:
            if x == '0':
                answer[1] += 1
                continue
            tmp += x

        s = str(bin(len(tmp)))[2:]

    return answer


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))