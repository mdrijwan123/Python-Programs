import time
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)

def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)


def partition(arr, low, high):
    left = low
    right = high
    pivot = arr[left]
    p = left
    while left < right:
        while arr[left] <= pivot:
            if left + 1 <= len(arr) - 1:
                left += 1
            else:
                break
        while arr[right] > pivot:
            if right - 1 >= 0:
                right -= 1
            else:
                break
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[p], arr[right] = arr[right], pivot
    return right


#A = [n for n in range(0, 990)]
A = [n for n in range(999, 0, -1)]
#print(A)
start = time.time()
quickSort(A, 0, len(A) - 1)
print(time.time() - start)
#print(A)
