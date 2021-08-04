# def solution(k, room_number):
#     answer = []
#     rooms = list(range(k))
#
#     room_number = [x-1 for x in room_number]
#
#     num = room_number.pop(0)
#     while True:
#         if rooms[num] == num:
#             answer += [num]
#             rooms[num] += 1
#             if room_number:
#                 num = room_number.pop(0)
#             else:
#                 break
#         else:
#             num = rooms[num]
#
#     return [ans + 1 for ans in answer]


def solution(k, room_number):
# answer = []
# rooms = dict()
# for l in range(1, k + 1):
#     rooms[l] = l
# print(rooms)
#
# num = room_number.pop(0)
# while True:
#     print(rooms)
#     if rooms[num] == num:
#         answer += [num]
#         rooms[num] += 1
#         if room_number:
#             num = room_number.pop(0)
#         else:
#             break
#     else:
#         num = rooms[num]
#
# return answer
    answer = []
    rooms = dict()
    for l in range(1, k + 1):
        rooms[l] = l

    num = room_number[0]
    i = 0
    l = len(room_number)
    while i < l:
        if rooms[num] == num:
            answer += [num]
            rooms[num] += 1
            i += 1
            if i == l:
                break
            num = room_number[i]
        else:
            num = rooms[num]

    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))  # [1, 3, 4, 2, 5, 6]
