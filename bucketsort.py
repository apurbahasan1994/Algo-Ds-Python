import math


def bucketsort(arr):
    number_of_buckets = round(math.sqrt(len(arr)))
    maxValue = max(arr)
    bucket = []
    for i in range(0, number_of_buckets):
        bucket.append([])

    for i in range(0, len(arr)):
        bucket_num = math.ceil((arr[i]*number_of_buckets)/maxValue)-1
        bucket[bucket_num].append(arr[i])

    for i in range(number_of_buckets):
        bucket[i].sort()

    arr = []
    for i in range(number_of_buckets):
        arr = [*arr, *bucket[i]]

    return arr


print(bucketsort([5, 4, 3, 7, 2, 8, 6, 9, 1, 11]))
