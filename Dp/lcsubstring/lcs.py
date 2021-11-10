def lcs(str_1, str_2, n, m, ans):

    if n == 0:
        return ans
    if m == 0:
        return ans
    if str_1[n-1] == str_2[m-1]:
        ans = lcs(str_1, str_2, n-1, m-1, 1+ans)
    diff = max(lcs(str_1, str_2, n, m-1, 0), lcs(str_1, str_2, n-1, m, 0))
    return max(ans, diff)


def main(str_1, str_2):
    n = len(str_1)
    m = len(str_2)
    return lcs(str_1, str_2, n, m, 0)


# print(main('abcdxyz', 'xyzabcd'))
print(main('zxabcdezy', 'yzabcdezx'))
