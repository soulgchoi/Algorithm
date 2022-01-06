def switch_hand(cur_position, hand, phone, target):
    phone[target[0]][target[1]] = hand
    phone[cur_position[0]][cur_position[1]] = 0
    return phone


def solution(numbers, hand):
    answer = ''

    phone = [[0] * 3 for _ in range(4)]
    phone[3][0], phone[3][2] = 'L', 'R'

    cur_L = (3, 0)
    cur_R = (3, 2)
    for number in numbers:
        if number == 0: number = 11
        x = number // 3 if number % 3 else number // 3 - 1
        y = number % 3 - 1 if number % 3 else 2

        if y == 0:
            phone = switch_hand(cur_L, 'L', phone, (x, y))
            cur_L = (x, y)
            answer += 'L'
            continue
        if y == 2:
            phone = switch_hand(cur_R, 'R', phone, (x, y))
            cur_R = (x, y)
            answer += 'R'
            continue
        if y == 1:
            abs_L = abs(x - cur_L[0]) + abs(y - cur_L[1])
            abs_R = abs(x - cur_R[0]) + abs(y - cur_R[1])
            if abs_L == abs_R:
                if hand == 'left':
                    phone = switch_hand(cur_L, 'L', phone, (x, y))
                    cur_L = (x, y)
                    answer += 'L'
                else:
                    phone = switch_hand(cur_R, 'R', phone, (x, y))
                    cur_R = (x, y)
                    answer += 'R'
                    continue
            if abs_L < abs_R:
                phone = switch_hand(cur_L, 'L', phone, (x, y))
                cur_L = (x, y)
                answer += 'L'
                continue
            if abs_L > abs_R:
                phone = switch_hand(cur_R, 'R', phone, (x, y))
                cur_R = (x, y)
                answer += 'R'

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))  # "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))  # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))  # "LLRLLRLLRL"
