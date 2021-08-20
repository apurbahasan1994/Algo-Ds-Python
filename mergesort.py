
def merge(arr, l, r, mid):
    n1 = mid-l+1
    n2 = r-mid
    left = [0]*n1
    right = [0]*n2

    for i in range(0, n1):
        left[i] = arr[l+i]

    for j in range(0, n2):
        right[j] = arr[mid+1+j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = (left[i])
            i += 1
        else:
            arr[k] = (right[j])
            j += 1
        k += 1
    while i < n1:
        arr[k] = (left[i])
        i += 1
        k += 1
    while j < n2:
        arr[k] = (right[j])
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        mid = (l+r)//2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid+1, r)
        merge(arr, l, r, mid)


merge_sort([1, 3, 5, 2, 9], 0, 4)
