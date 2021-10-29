def sub_sum(arr, s, n):
    table = [[False for _ in range(s+1)] for _ in range(len(arr)+1)]
    for i in range(len(arr)+1):
        for j in range(s+1):
            if(j == 0):
                table[i][j] = True
    for i in range(1, len(arr)+1):
        for j in range(1, s+1):
            if(arr[i-1] <= j):
                table[i][j] = table[i-1][j-arr[i-1]] or table[i-1][j]
            else:
                table[i][j] = table[i-1][j]
    return table[len(arr)][s]


def equal_sum_partition(nums):
    if sum(nums) % 2 > 0:
        return False
    n = len(nums)
    ans = sub_sum(nums, sum(nums)//2, n)
    if(ans):
        return True
    else:
        return False


print(equal_sum_partition([3, 2, 5]))
