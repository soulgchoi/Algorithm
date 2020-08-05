def solution(citations):
    citations.sort(reverse=True)
    i = 0
    while i < len(citations) and i+1 <= citations[i]:  # 조건문 순서 바꾸면 틀림
        i += 1
    return i