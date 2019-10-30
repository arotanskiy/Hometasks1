import numpy as np
from array import array


def array_gen(n, m):
    """
    This is an zero array n x m elements generator.
    :return: array n x m elements
    """
    arr = np.zeros(n * m).reshape(n, m)
    # arr = np.random.rand(n, n)
    # print("\nUsed array with size N x M and N = {} M = {}:\n{}".format(n, m, arr))
    return (arr)


def spirale_array_fill(b, n, m):
    """
    This function allow to fill N x M array by spiral
    :return: spiral filled array
    """
    b = b  # begin from this number
    n = n  # horizontal size
    m = m  # vertical size
    spiral = array_gen(n, m)
    bp = 0  # point of a beginning cycle
    while bp < round(n/2):
        # horizontal high line
        curr = bp
        start = bp
        end = n - bp - 1
        step = 1
        for j in range(start, end, step):
            spiral[curr, j] = b
            b += 1

        # vertical left line
        curr = j + 1
        start = bp
        end = m - bp - 1
        for i in range(start, end, step):
            spiral[i, curr] = b
            b += 1

        # horizontal low line
        curr = i + 1
        start = -(bp + 1)  # add +1 to compensate beginning of a negative indexes (start from -1, not 0)
        end = -(n - bp)
        step = -1
        for j in range(start, end, step):
            spiral[curr, j] = b
            b += 1

        # vertical left line
        curr = j - 1
        start = -(bp + 1)  # add +1 to compensate beginning of a negative indexes (start from -1, not 0)
        end = -(m - bp)
        step = -1
        for i in range(start, end, step):
            spiral[i, curr] = b
            b += 1
        bp += 1
    if n % 2 != 0 or m % 2 != 0:
        spiral[(n // 2), (m // 2)] = b
    return (spiral)

print(spirale_array_fill(1, 7, 7))