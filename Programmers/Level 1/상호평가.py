def grade(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 50:
        return 'D'
    return 'F'


def solution(scores):
    scores = list(map(list, zip(*scores)))
    answer = ''
    for i in range(len(scores)):
        extra = scores[i][:i] + scores[i][i + 1:]
        if scores[i][i] == min(scores[i]) or scores[i][i] == max(scores[i]):
            if scores[i][i] not in extra:
                answer += str(grade(sum(extra) / (len(scores[i]) - 1)))
                continue
        answer += str(grade(sum(scores[i]) / len(scores[i])))

    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))