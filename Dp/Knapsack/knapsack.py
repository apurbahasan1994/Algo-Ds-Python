def knapsack(wt_arr, val_arr, weight, n):
    table = [[0 for _ in range(weight+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(weight+1):
            if(wt_arr[i-1] <= j):
                table[i][j] = max(val_arr[i-1]+table[i-1]
                                  [j-wt_arr[i-1]], table[i-1][j])
            elif wt_arr[i-1] > j:
                table[i-1][j]
    return table[-1][-1]


print(knapsack([4, 5, 1], [1, 2, 3], 4, 3))
