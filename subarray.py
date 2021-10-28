import sys


def sub_array(nums):
    max_sum = -999
    for i in range(0, len(nums)):
        sums = 0
        for j in range(1, len(nums)+1):
            if(i+j <= len(nums)):
                sums += nums[i+j-1]
            max_sum = max(sums, max_sum)
    print(max_sum)


def sub(nums):
    if(len(nums) == 1):
        return nums[0]
    mid = len(nums)//2
    lss = sub(nums[:mid])
    rss = sub(nums[mid:])
    l_sum = -sys.maxsize-1
    r_sum = -sys.maxsize-1
    sums = 0
    for i in range(mid-1, -1, -1):
        sums += nums[i]
        l_sum = max(sums, l_sum)
    sums = 0
    for j in range(mid, len(nums)):
        sums += nums[j]
        r_sum = max(sums, r_sum)
    ans = max(lss, rss)
    return max(ans, r_sum+l_sum)


print(sub([1, 2]))
# sub_array([0, 1])
# print(sub([0, 1, -2, ]))
