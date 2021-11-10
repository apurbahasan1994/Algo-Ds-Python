def app(str_1, str_2, n, m):
    table = [['' for _ in range(m+1)]for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            a = str_1[i-1]
            b = str_2[j-1]
            if(str_1[i-1] == str_2[j-1]):
                table[i][j] = str_1[i-1]+table[i-1][j-1]
            else:
                if len(table[i-1][j]) > len(table[i][j-1]):
                    table[i][j] = table[i-1][j]
                else:
                    table[i][j] = table[i][j-1]
    return table[-1][-1]


def main(str_1, str_2):
    n = len(str_1)
    m = len(str_2)
    ans = ''.join(i for i in reversed(app(str_1, str_2, n, m)))
    print(ans)
    i = 0
    j = 0
    superseq = ''
    for char in ans:
        while(str_1[i] != char):
            superseq += str_1[i]
            i += 1
        while(str_2[j] != char):
            superseq += str_2[j]
            j += 1

        superseq += char
        i += 1
        j += 1
    superseq = superseq+str_1[i:]+str_2[j:]
    return superseq


print(main("bbbaaaba", "bbababbb"))
