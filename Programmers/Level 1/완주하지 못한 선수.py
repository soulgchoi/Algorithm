def solution(participant, completion):
    answer = {}
    for p in participant:
        if p in answer.keys():
            answer[p] += 1
        else:
            answer[p] = 1
    for c in completion:
        answer[c] -= 1
    answer = list(filter(lambda x: x[1] == 1, answer.items()))
    return answer[0][0]