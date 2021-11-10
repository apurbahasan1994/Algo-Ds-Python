def palindromic_sub_seq(str_1, str_2, n):
    table = [['' for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if str_1[i-1] == str_2[j-1]:
                table[i][j] = str_1[i-1]+table[i-1][j-1]
            else:
                if len(table[i-1][j]) > len(table[i][j-1]):
                    table[i][j] = table[i-1][j]
                else:
                    table[i][j] = table[i][j-1]
    return table[-1][-1]


def main(sequence):
    n = len(sequence)
    rev_seq = ''.join(i for i in reversed(sequence))
    ans = palindromic_sub_seq(sequence, rev_seq, n)
    return ans


print(main('agbcba'))
