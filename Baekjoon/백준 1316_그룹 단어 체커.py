import sys
sys.stdin = open('1316.txt', 'r')

T = 2
for tc in range(T):
    print(f'------ tc: {tc}')

    N = int(input())
    words = [input() for _ in range(N)]

    ans = 0
    for word in words:
        li = []
        i = 0
        while i < len(word):
            if word[i] in li:
                break

            temp = word[i]
            j = i + 1
            while j < len(word) and word[j] == temp:
                j += 1
            li += [temp]
            i = j

        if i == len(word):
            ans += 1

    print(ans)
