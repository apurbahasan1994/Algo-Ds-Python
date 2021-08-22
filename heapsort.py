def heapify(arr, n, i):
    smallest = i
    l = 2*i
    r = 2*i+1
    if l < n and arr[l] < arr[smallest]:
        smallest = l
    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def heap_sort(arr):
    n = len(arr)-1
    for i in range(int(n/2), -1, -1):
        heapify(arr, n, i)

    for i in range(n, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    arr.reverse()


a = [2, 1, 7, 6, 5, 3, 4, 9, 8]
heap_sort(a)
print(a)
