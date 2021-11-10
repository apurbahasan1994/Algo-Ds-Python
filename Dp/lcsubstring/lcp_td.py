def lcs(str_1, str_2, n, m, ans):
    table = [[0 for _ in range(m+1)] for _ in range(n+1)]
    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str_1[i-1] == str_2[j-1]:
                table[i][j] = 1+table[i-1][j-1]
                ans = max(ans, table[i][j])
            else:
                table[i][j] = 0
    for i in table:
        print(i)
    return ans


def main(str_1, str_2):
    n = len(str_1)
    m = len(str_2)
    return lcs(str_1, str_2, n, m, 0)


# print(main('abcdxyz', 'xyzabcd'))
print(main('zxabcdezy', 'yzabcdezx'))
