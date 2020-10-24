def plusMinus(arr):
    length = len(arr)
    positive = len(list(filter(lambda x: x > 0, arr)))
    negative = len(list(filter(lambda y: y < 0, arr)))
    zero = arr.count(0)
    print('%0.6f' % float(positive/length))
    print('%0.6f' % float(negative/length))
    print('%0.6f' % float(zero/length))
    return


plusMinus([-4, 3, -9, 0, 4, 1])