def house_robber(arr, current_index):
    if current_index >= len(arr):
        return 0
    else:
        return max(arr[current_index]+house_robber(arr, current_index+2), house_robber(arr, current_index+1))


print(house_robber([6, 7, 1, 30, 8, 2, 4], 0))
