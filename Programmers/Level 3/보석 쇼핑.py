def solution(gems):
    answer = []
    gem_number = len(set(gems))
    gem_dict = {}

    left, right = 0, 0
    while right < len(gems):
        if gems[right] in gem_dict:
            gem_dict[gems[right]] += 1
        else:
            gem_dict[gems[right]] = 1

        while len(gem_dict.keys()) >= gem_number:
            answer += [(left + 1, right + 1)]

            gem_dict[gems[left]] -= 1
            if gem_dict[gems[left]] == 0:
                gem_dict.pop(gems[left])

            left += 1

        else:
            right += 1

    return sorted(answer, key=lambda x: x[1] - x[0])[0]


print(solution(["DIA", "EM", "EM", "RUB", "DIA"]))  # [3, 5]
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))  # [3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"]))  # [1, 3]
print(solution(["XYZ", "XYZ", "XYZ"]))  # [1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))  # [1, 5]
