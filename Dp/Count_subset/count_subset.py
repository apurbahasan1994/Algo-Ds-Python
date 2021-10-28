def sub_sum(arr, sum):
    table = [[0 for _ in range(sum+1)] for _ in range(len(arr)+1)]
    for i in range(len(arr)+1):
        for j in range(sum+1):
            if(j == 0):
                table[i][j] = 1
    for i in range(len(arr)+1):
        for j in range(sum+1):
            if(arr[i-1] <= j):
                table[i][j] = table[i-1][j-arr[i-1]] + table[i-1][j]
            else:
                table[i][j] = table[i-1][j]
    return table[len(arr)][sum]


print(sub_sum([2, 4, 1, 3, 5, 10], 5))
