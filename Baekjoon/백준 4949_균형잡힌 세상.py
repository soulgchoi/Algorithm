import sys
sys.stdin = open('4949.txt', 'r')

while True:
    N = input()
    if N == '.':
        break

    stack = []
    prths1 = ['(', '[']
    prths2 = [')', ']']
    for n in N:
        if n == '(' or n =='[':
            stack += [n]
            continue
        if n == ')' or n == ']':
            if stack:
                if (stack[-1] == '(' and n == ')') or (stack[-1] == '[' and n == ']'):
                    stack.pop()
                    continue
            stack += [n]
            break

    print('no') if len(stack) else print('yes')
