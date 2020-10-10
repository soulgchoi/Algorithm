def solution(s):
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:].lower()
    return ' '.join(s)


"""
문제 조건과는 맞지 않지만,
string.title() 이라는 메서드가 있다.
'for the last week'.title() => 'For The Last Week'
"""