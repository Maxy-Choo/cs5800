import random
import time
import matplotlib.pyplot as plt
import math

def split(arr, left, right, pivot):
    l = left
    r = right
    p = left
    while p <= r:
        if arr[p] < pivot:
            arr[l], arr[p] = arr[p], arr[l]
            l += 1
            p += 1
        elif arr[p] > pivot:
            arr[p], arr[r] = arr[r], arr[p]
            r -= 1
        else:
            p += 1
    return l, r


# 1. Random Pivot
def find_median_rand_pivot(arr, k):
    n = len(arr)
    left = 0
    right = n-1
    while left <= right:
        idx = random.randint(left, right)
        pivot = arr[idx]
        l, r = split(arr, left, right, pivot)

        if k < l:
            right = l - 1
        elif k > r:
            left = r + 1
        else:
            return arr[k]

    return arr[left]

# 2. Split always in the 25%-75% range
def quicksort(arr, left, right):
    stack = [(left, right)]
    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        pivot = arr[right]
        i, j = split(arr, left, right, pivot)
        stack.append((left, i-1))
        stack.append((j+1, right))

def median_of_median(arr, left, right):
    """
    Find a good pivot of an array by dividing it into groups of 5 and finding
    the median of each group, then finding the median of these medians.
    P = 1/5 + 1/25 + 1/125 + ... = 3/10, so the pivot is guaranteed to be in
    the 25%-75% range.
    """
    n = right - left + 1
    if n <= 5:
        sub = arr[left:right+1]
        quicksort(sub, 0, len(sub)-1)
        return sub[n // 2]

    group = []
    for i in range(left, right+1, 5):
        sub = arr[i:min(i+5, right+1)]
        quicksort(sub, 0, len(sub)-1)
        group.append(sub[len(sub)//2])

    return find_median_good_split(group, len(group)//2)

def find_median_good_split(arr, k):
    left = 0
    right = len(arr)-1
    while left <= right:
        pivot = median_of_median(arr, left, right)
        i, j = split(arr, left, right, pivot)
        if k < i:
            right = i - 1
        elif k > j:
            left = j + 1
        else:
            return arr[k]

    return arr[left]
        

if __name__ == "__main__":
    time_arr_rand = []
    time_arr_good = []
    time_arr_sort = []
    time_arr_sort2 = []
    size_arr = [pow(10, i) for i in range(1, 4)]
    for i in range(1, 4):
        arr1 = [random.randint(0, 100000) for _ in range(pow(10, i))]
        arr2 = arr1.copy()
        arr3 = arr1.copy()
        arr4 = arr1.copy()
        tmp = 0
        for _ in range(5):
            start = time.perf_counter()
            ans = find_median_rand_pivot(arr1, len(arr1)//2)
            end = time.perf_counter()
            tmp += end - start
        time_arr_rand.append(tmp / 5)

        tmp = 0
        for _ in range(5):
            start = time.perf_counter()
            ans = find_median_good_split(arr2, len(arr2)//2)
            end = time.perf_counter()
            tmp += end - start
        time_arr_good.append(tmp / 5)

        tmp = 0
        for _ in range(5):
            start = time.perf_counter()
            ans = sorted(arr3)[len(arr3)//2]
            end = time.perf_counter()
            tmp += end - start
        time_arr_sort.append(tmp / 5)

        tmp = 0
        for _ in range(5):
            start = time.perf_counter()
            quicksort(arr4, 0, len(arr4)-1)
            ans = arr4[len(arr4)//2]
            end = time.perf_counter()
            tmp += end - start
        time_arr_sort2.append(tmp / 5)

    plt.plot(size_arr, time_arr_rand, label="Random Pivot")
    plt.plot(size_arr, time_arr_good, label="Good Split")
    plt.plot(size_arr, time_arr_sort, label="Built-in Sort")
    plt.plot(size_arr, time_arr_sort2, label="Iterative Quick Sort")
    plt.xlabel("size")
    plt.ylabel("time(s)")
    plt.title("Performance of Median Finding")
    plt.legend()
    plt.show()
