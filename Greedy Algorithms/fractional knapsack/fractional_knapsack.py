def fractional_knapsack(weights, values, limit):
    w_to_v_ratio = []
    ans = 0
    usedCapacity = 0
    for w, v in zip(weights, values):
        w_to_v_ratio.append(v/w)
    w_to_v_ratio.sort(reverse=True)
    weights = [x for x, _, _ in sorted(
        zip(weights, values, w_to_v_ratio), key=lambda x:x[2])]
    values = [x for _, x, _ in sorted(
        zip(weights, values, w_to_v_ratio), key=lambda x:x[2])]

    for i in range(len(weights)):
        if weights[i]+usedCapacity <= limit:
            usedCapacity += weights[i]
            ans += values[i]
        else:
            unUsedWeight = limit-usedCapacity
            ans += values[0]*(unUsedWeight/weights[0])
            break
    print(ans)


fractional_knapsack([20, 30, 10], [100, 120, 60], 50)
