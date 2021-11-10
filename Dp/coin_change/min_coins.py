import sys


def min_coins_recursive(coins, target):
    ans = sys.maxsize
    if target == 0:
        return 0
    if target < 0:
        return sys.maxsize
    for coin in coins:
        if(coin <= target):
            sub_ans = 1 + min_coins_recursive(coins, target-coin)
            if(sub_ans < ans):
                ans = sub_ans
    return ans


print(min_coins_recursive([1, 2, 3, 4, 5], 11))
