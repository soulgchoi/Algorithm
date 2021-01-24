import heapq


def solution(operations):
    queue = []
    for operation in operations:
        operation = operation.split()

        if operation[0] == 'I':
            heapq.heappush(queue, int(operation[1]))
        if operation[0] == 'D':
            if operation[1] == '1':
                if not queue:
                    continue
                queue.pop()
            if operation[1] == '-1':
                if not queue:
                    continue
                heapq.heappop(queue)

    if not queue:
        return [0, 0]

    # _max = heapq.nlargest(1, queue)
    # _min = heapq.nsmallest(1, queue)
    # return [_max[0], _min[0]]
    return [max(queue), min(queue)]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))  # [0, 0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))  # [7, 5]
