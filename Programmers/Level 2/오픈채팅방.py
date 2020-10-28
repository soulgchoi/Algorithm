def message(s, t):
    if t == 'Enter':
        return f'{s}님이 들어왔습니다.'
    elif t == 'Leave':
        return f'{s}님이 나갔습니다.'


def solution(record):
    answer = []
    chat = {}
    for r in record:
        r = r.split()
        if r[0] == 'Enter' or r[0] == 'Change':
            if r[1] in chat.keys():
                chat[r[1]] += [r[2]]
            else:
                chat[r[1]] = [r[2]]

    for c in record:
        tmp = c.split()
        if tmp[0] == 'Enter' or tmp[0] == 'Leave':
            answer.append(message(chat[tmp[1]][-1], tmp[0]))
    return answer
