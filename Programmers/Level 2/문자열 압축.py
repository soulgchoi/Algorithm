def solution(s):
    if len(s) < 2:
        return 1
    answer = len(s)
    for i in range(len(s) // 2, 0, -1):
        l = len(s) // i + 1 if len(s) % i else len(s) // i
        words = [s[j:j + i] for j in range(0, len(s), i)]
        cnt = 1
        strings = []
        a, b = 0, 1
        while a < l:
            if a == l - 1:
                strings += [str(cnt) + words[a]] if cnt > 1 else [words[a]]
                break
            if words[a] == words[b]:
                cnt += 1
            else:
                strings += [str(cnt) + words[a]] if cnt > 1 else [words[a]]
                cnt = 1
            a = b
            b = a + 1
        strings = ''.join(strings)
        if len(strings) < answer:
            answer = len(strings)
    return answer


print(solution("aabbaccc"))  # 7
print(solution("ababcdcdababcdcd"))  # 9
print(solution("abcabcdede"))  # 8
print(solution("abcabcabcabcdededededede"))  # 14
print(solution("xababcdcdababcdcd"))  # 17
