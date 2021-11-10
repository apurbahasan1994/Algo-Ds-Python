def lcs_reursive(str_1, str_2, n, m):
    if n == 0 or m == 0:
        return 0

    if(str_1[n-1] == str_2[m-1]):
        return 1+lcs_reursive(str_1, str_2, n-1, m-1)
    else:
        return max(lcs_reursive(str_1, str_2, n, m-1), lcs_reursive(str_1, str_2, n-1, m))


def lcs_tabulation(str_1, str_2, n, m, table):
    if table[n][m] != -1:
        return table[n][m]
    if n == 0 or m == 0:
        return 0

    if(str_1[n-1] == str_2[m-1]):
        table[n][m] = 1+lcs_tabulation(str_1, str_2, n-1, m-1, table)
        return table[n][m]
    else:
        table[n][m] = max(lcs_tabulation(str_1, str_2, n, m-1, table),
                          lcs_tabulation(str_1, str_2, n-1, m, table))
        return table[n][m]


def main(str_1, str_2, n, m):
    table = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    return lcs_tabulation(str_1, str_2, n, m, table)


def lcs_tabulation(str_1, str_2, n, m, table):
    if table[n][m] != -1:
        return table[n][m]
    if n == 0 or m == 0:
        return 0

    if(str_1[n-1] == str_2[m-1]):
        table[n][m] = 1+lcs_tabulation(str_1, str_2, n-1, m-1, table)
        return table[n][m]
    else:
        table[n][m] = max(lcs_tabulation(str_1, str_2, n, m-1, table),
                          lcs_tabulation(str_1, str_2, n-1, m, table))
        return table[n][m]


def bottom_up(str_1, str_2, n, m):
    table = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                table[i][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if(str_1[i-1] == str_2[j-1]):
                table[i][j] = 1+table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    return table[n][m]


def bottom_up_print(str_1, str_2, n, m):
    if n == 0 or m == 0:
        return []

    if(str_1[n-1] == str_2[m-1]):
        ans = bottom_up_print(str_1, str_2, n-1, m-1)
        ans.append(str_1[n-1])
        return ans
    else:
        ans1 = bottom_up_print(str_1, str_2, n, m-1)
        ans2 = bottom_up_print(str_1, str_2, n-1, m)
        if(len(ans1) > len(ans2)):
            return [*ans1]
        else:
            return [*ans2]


def bottom_up_2(str_1, str_2, n, m):
    table = [[[] for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                table[i][j] = []

    for i in range(1, n+1):
        for j in range(1, m+1):
            if(str_1[i-1] == str_2[j-1]):
                table[i][j] = [*table[i-1][j-1], str_1[i-1]]
            else:
                ans1 = table[i-1][j]
                ans2 = table[i][j-1]
                if(len(ans1) > len(ans2)):
                    table[i][j] = [*table[i-1][j]]
                else:
                    table[i][j] = [*table[i][j-1]]

    return table[n][m]


def main(str_1, str_2, n, m):
    table = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    tab_ans = lcs_tabulation(str_1, str_2, n, m, table)
    return tab_ans


print(lcs_reursive('ABCDGH', 'AEDFHR', 6, 6))
# print(main('ABC', 'AC', 3, 2))
print(bottom_up_2('ABC', 'AC', 3, 2))
