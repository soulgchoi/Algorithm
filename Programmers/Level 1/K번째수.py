def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# def solution(array, commands):
#     answer = []
#     for command in commands:
#         x, y, z = command
#         temp = array[x-1:y]
#         temp.sort()
#         answer += [temp[z-1]]
#     return answer


# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
