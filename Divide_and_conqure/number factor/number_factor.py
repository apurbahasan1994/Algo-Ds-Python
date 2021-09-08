def number_factor(n):
    if n in [0, 1, 2]:
        return 1
    elif n == 3:
        return 2
    else:
        s1 = number_factor(n-1)
        s2 = number_factor(n-3)
        s3 = number_factor(n-4)
        return s1+s2+s3


print(number_factor(5))
