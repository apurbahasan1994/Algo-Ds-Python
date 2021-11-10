def max_num_of_ways(coins, target):
    n = len(coins)
    table = [[0 for _ in range(target+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(target+1):
            if j == 0:
                table[i][j] = 1

    for i in range(1, n+1):
        for j in range(1, target+1):
            if(coins[i-1] <= j):
                table[i][j] = table[i][j-coins[i-1]]+table[i-1][j]
            else:
                table[i][j] = table[i-1][j]
    return table[-1][-1]


print(max_num_of_ways([1, 2, 3], 5))
