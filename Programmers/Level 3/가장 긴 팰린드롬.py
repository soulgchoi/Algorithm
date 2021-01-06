def isPalindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-1-i]:
            return False
    return True

def solution(s):
    length = len(s)
    if isPalindrome(s):
        return len(s)
    while length > 1:
        for i in range(len(s)-length):
            if isPalindrome(s[i:i+length+1]):
                return len(s[i:i+length+1])
        length -= 1
    return 1