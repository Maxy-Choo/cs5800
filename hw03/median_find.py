import random
import time
import matplotlib.pyplot as plt
import math


def find_median_rand_pivot(arr):
    n = len(arr)
    left = 0
    right = n
    while left < right:
        idx = random.randint(left, right)
        pivot = arr[idx]
        l = left
        r = right-1
        while l <= r:
            if arr[l] < pivot:
                l += 1
            else:
                arr[l], arr[r] = arr[r], arr[l]
                r -= 1
        if l < r-l+1:
            left = l
        else:
            right = l

    return arr[left] if n % 2 == 1 else (arr[left]+arr[left+1])/2.0

def good_split(arr):
    n = len(arr)
    if n <= 5:
        a.sort()
    return a[n//2]

    group = []
    for i in range(0, n, 5):
        sub = a[i:i+5]
        sub.sort()
        group.append(sub[2])

    return find_median_good_split(group, len(group)//2)

def split(arr, pivot):
    i = 0
    r = 0
    j = len(arr)-1
    while r <= j:
        if arr[r] < pivot:
            arr[i], arr[r] = arr[r], arr[i]
            i += 1
            r += 1
        elif arr[r] > pivot:
            arr[r], arr[j] = arr[j], arr[r]
            j -= 1
        else:
            r += 1
    return i, r, j
        

def find_median_good_split(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = good_split(arr)
    i, r, j = split(arr, pivot)
    if k < i:
        return find_median_good_split(arr[:i], k)
    elif i <= k <= j:
        return arr[k]
    else:
        return find_median_good_split(arr[j+1:], k-j-1)
        

if "__name__" == "__main__":
    time_arr = []
    size_arr = [pow(10, i) for i in range(1, 7)]
    for i in range(1, 7):
        arr = [random.randint(0, 100000) for _ in range(pow(10, i))]
        start = time.performance_t()
        ans = find_median_rand_pivot(arr)
        end = time.performance_t()
        time_arr.append(end-start)

    plt(size_arr, time_arr)
    plt.xlabel("size")
    plt.ylabel("time(s)")
    plt.title("Performance of Median Finding using Random Pivot Sorting")
    plt.show()
