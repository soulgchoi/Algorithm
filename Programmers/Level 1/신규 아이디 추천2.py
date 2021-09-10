def solution(new_id):
    new_id = new_id.lower()
    char = ['-', '_', '.'] + list(map(str, list(range(10))))
    valid_id = []
    for n in new_id:
        if n in char or n.isalpha():
            valid_id += [n]

    i = 1
    while i < len(valid_id):
        if valid_id[i-1] == '.' and valid_id[i] == '.':
            valid_id = valid_id[:i] + valid_id[i+1:]
        else:
            i += 1

    valid_id = ''.join(valid_id).strip('.')
    valid_id = valid_id[:15].strip('.')
    if valid_id == '':
        valid_id = 'a'
    if len(valid_id) < 3:
        valid_id = valid_id + valid_id[-1] * (3 - len(valid_id))

    return valid_id


print(solution("...!@BaT#*..y.abcdefghijklm"))  # "bat.y.abcdefghi"
print(solution("z-+.^."	))  # "z--"
print(solution("=.="))  # "aaa"
print(solution("123_.def"))  # "123_.def"
print(solution("abcdefghijklmn.p"))  # "abcdefghijklmn"
print(solution("................b"))  # "bbb"
print(solution("~!@#$%&*()=+[{]}:?,<>/"))  # aaa
print(solution(".1."))  # 111