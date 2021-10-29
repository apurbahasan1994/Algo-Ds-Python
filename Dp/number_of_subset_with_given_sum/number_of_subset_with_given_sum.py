def sub_s(arr, s):
    table = [[0 for _ in range(s+1)] for _ in range(len(arr)+1)]
    for i in range(len(arr)+1):
        for j in range(s+1):
            if(j == 0):
                table[i][j] = 1
    for i in range(1, len(arr)+1):
        for j in range(1, s+1):
            if(arr[i-1] <= j):
                table[i][j] = table[i-1][j-arr[i-1]] + table[i-1][j]
            else:
                table[i][j] = table[i-1][j]
    return table[len(arr)][s]


def min_sub_s_diff(nums, diff):
    target = (sum(nums)+diff)//2
    count = sub_s(nums, target)
    return count


print(min_sub_s_diff([3, 1, 2, 3], 3))
