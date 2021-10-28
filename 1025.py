def func(n, d={}):
    if n in d:
        return d[n]
    ans = 0
    if n == 0:
        return 1
    if n < 0:
        return 0
    ans = func(n-1)+func(n-2)
    d[n] = ans
    return d[n]


print(func(3))
