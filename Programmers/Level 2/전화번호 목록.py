def solution(phone_book):
    phone_book = sorted(phone_book, key=len)
    i = 0
    while i < len(phone_book) - 1:
        temp = phone_book[i]
        for j in range(i+1, len(phone_book)):
            if phone_book[j][:len(temp)] == temp:
                return False
        i += 1
    return True
