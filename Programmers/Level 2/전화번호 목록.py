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


def solution2(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = []
        temp = ""
        for number in phone_number:
            temp += number
            hash_map[phone_number] += [temp]

    for phone_number in phone_book:
        for key, val in hash_map.items():
            if phone_number != key and phone_number in val:
                return False
    return True


def solution3(phone_book):
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if phone_number != temp and temp in phone_book:
                return False
    return True


# print(solution(["119", "97674223", "1195524421"]))
# print(solution(	["123", "456", "789"]))
# print(solution(	["12", "123", "1235", "567", "88"]))
