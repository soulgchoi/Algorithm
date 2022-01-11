def solution(n, times):
    min_time = 1
    max_time = max(times) * n

    low, high = min_time, max_time
    while low <= high:
        mid = (low + high) // 2

        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break

        if people >= n:
            low, high = low, mid - 1
        else:
            low, high = mid + 1, high

    return low


print(solution(6, [7, 10]))


print(solution(6, [7, 10]))
