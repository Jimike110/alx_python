def fibonacci_sequence(n):
    result = []
    num = 0
    if n == 1:
        result.append(0)
        return result
    elif n <= 0:
        return result
    result.append(num)
    result.append(1)
    for i in range(2, n):
        num = result[i-2] + result[i-1]
        result.append(num)
    return result