def rod_cutting(length, price, n):
    table = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if length[i-1] <= j:
                table[i][j] = max(price[i-1]+table[i]
                                  [j-i], table[i-1][j])
            else:
                table[i][j] = table[i-1][j]
    return table[-1][-1]


print(rod_cutting([1, 2, 3, 4, 5, 6, 7, 8], [3, 5, 8, 9, 10, 17, 17, 20], 8))
