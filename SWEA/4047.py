import sys
sys.stdin = open('solvingclub1.txt', 'r')

for tc in range(1, int(input())+1):
    data = list(input())
    card = [data[i:i+3] for i in range(0, len(data)-2, 3)]
    flag = 1
    S = D = H = C = 13
    for i in card:
        if card.count(i) < 2:
            if 'S' in i:
                S -= 1
            elif 'D' in i:
                D -= 1
            elif 'H' in i:
                H -= 1
            elif 'C' in i:
                C -= 1
        else:
            flag = 0
            break
    if flag == 1:
        print('#{} {} {} {} {}'.format(tc, S, D, H, C))
    else:
        print('#{} {}'.format(tc, 'ERROR'))

