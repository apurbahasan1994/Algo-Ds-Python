def partition(arr, start, end):
    pivot = arr[start]
    i = start
    j = end
    while(i < j):
        while arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[start], arr[j] = arr[j], arr[start]
    return j


def quicksort(arr, start, end):
    if start < end:
        p_index = partition(arr, start, end)
        quicksort(arr, start, p_index)
        quicksort(arr, p_index+1, end)


a = [7, 6, 1, 4, 2, 3, 9, 10, 15]
quicksort(a, 0, 6)
