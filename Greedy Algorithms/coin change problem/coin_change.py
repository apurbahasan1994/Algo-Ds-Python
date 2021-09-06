def coin_change(coins, total_sum):
    visited = []

    def max_coin(coins):
        maximum = -1
        for coin in coins:
            if coin not in visited:
                if coin > maximum:
                    maximum = coin
        return maximum
    min_coins = 0
    while total_sum != 0:
        max_num = max_coin(coins)
        if max_num <= total_sum:
            total_sum = total_sum-max_num
            min_coins += 1
        else:
            visited.append(max_num)

    print(min_coins)


coins = [1, 2, 5, 10, 20, 50, 100, 1000]
total_sum = 2035
coin_change(coins, total_sum)
