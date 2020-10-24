def miniMaxSum(arr):
    min_val, max_val = sum(arr[:-1]), sum(arr[:-1])
    for i in range(len(arr)-1):
        val = sum(arr[:i]) + sum(arr[i+1:])
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val
    print(min_val, max_val)
    return