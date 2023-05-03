def quicksort(lst, low=0, high=-1):
    if high == -1:
        high = len(lst) - 1
    if low < high:
        pi = Partition(lst, low, high)
        quicksort(lst, low, pi - 1)
        quicksort(lst, pi + 1, high)
    return lst


def Partition(lst, low, high):
    pivot = lst[high]
    i = low - 1
    for j in range(low, high):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1
