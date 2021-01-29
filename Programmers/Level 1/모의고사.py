def solution(answers):
    answer = []
    grades = [0] * 3
    students = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    for idx, nums in enumerate(students):
        for i in range(len(answers)):
            if answers[i] == nums[i % len(nums)]:
                grades[idx] += 1
    _max = max(grades)
    for i, grade in enumerate(grades):
        if grade == _max:
            answer += [i+1]
    return answer


def solution2(answers):
    answer = []
    _max = 0
    students = {
        '1': [1, 2, 3, 4, 5],
        '2': [2, 1, 2, 3, 2, 4, 2, 5],
        '3': [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    for student, nums in students.items():
        cnt = 0
        for i in range(len(answers)):
            if answers[i] == nums[i % len(nums)]:
                cnt += 1
        answer += [(student, cnt)]
        if cnt > _max:
            _max = cnt
    answer = list(map(lambda y: int(y[0]), filter(lambda x: x[1] == _max, answer)))
    return answer


# print(solution([1, 2, 3, 4, 5]))  # [1]
# print(solution([1, 3, 2, 4, 2]))  # [1, 2, 3]
