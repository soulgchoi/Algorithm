import itertools


def solution(numbers):
    answer = 0
    numbers = list(sum(map(lambda x: x.split(), numbers), []))

    _combs = []
    for i in range(2, len(numbers)+1):
        temp = list(itertools.combinations(numbers, i))
        _combs += temp

    _set = []
    for _comb in _combs:
        temp = list(map(list, list(itertools.permutations(_comb))))
        _set += temp
    _set = list(map(''.join, _set))

    numbers += _set
    numbers = list(set(map(int, numbers)))
    for number in numbers:
        if number < 2:
            continue
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            answer += 1

    return answer


# print(solution("17"))  # 3
# print(solution("011"))  # 2
