import sys


def sub_sum(nums, target, n):
    table = [[False for _ in range(target+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(target+1):
            if j == 0:
                table[i][j] = True

    for i in range(1, n+1):
        for j in range(1, target+1):
            if(nums[i-1] <= j):
                table[i][j] = table[i-1][j-nums[i-1]] or table[i-1][j]
            else:
                table[i][j] = table[i-1][j]
    return table


def min_sub_sum_diff(nums):
    n = len(nums)
    target = sum(nums)
    table = sub_sum(nums, target, n)
    target_table = table[-1]
    target_table = target_table[:len(target_table)//2]
    min_value = sys.maxsize
    for i in range(len(target_table)):
        if(target_table[i]):
            if(min_value > (target-(2*i))):
                min_value = target-(2*i)
    return min_value


print(min_sub_sum_diff([2, 4, 2, 3, 1]))
