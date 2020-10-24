def timeConversion(s):
    tm = s[:-2].split(':')
    st = s[-2:]
    if st == 'PM':
        if int(tm[0]) < 12:
            tm[0] = str(int(tm[0]) + 12)
    if st == 'AM':
        if int(tm[0]) == 12:
            tm[0] = '0' + str(int(tm[0]) - 12)
    return ':'.join(tm)

timeConversion('12:40:22AM')
timeConversion('12:45:54PM')