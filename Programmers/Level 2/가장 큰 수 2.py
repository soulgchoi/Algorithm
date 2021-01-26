def solution(numbers):
    import functools
    numbers = list(map(str, numbers))
    numbers.sort(key=functools.cmp_to_key(lambda x, y: int(x+y)-int(y+x)), reverse=True)
    return str(int(''.join(numbers)))


# print(solution([6, 10, 2]))  # "6210"
# print(solution([3, 30, 34, 5, 9]))  # "9534330"
