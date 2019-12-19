def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        if i & (1 << j):
            output += '1'
        else:
            output += '0'
    print(output)

a = 0x86
key = 0xAA

print('a      ==> ', end='')
Bbit_print(a)

print('a^=key ==> ', end='')
a ^= key
Bbit_print(a)

print('a^=key ==> ', end='')
a ^= key
Bbit_print(a)