def min_heapify(arr, i, N):
    left = 2 * i
    right = 2 * i + 1
    least = i
    if left < N and arr[left] < arr[i]:
        least = left
    if right < N and arr[right] < arr[least]:
        least = right
    if i != least:
        arr[i], arr[least] = arr[least], arr[i]
        min_heapify(arr, least, N)


def max_heapify(arr, i, N):
    left = 2 * i
    right = 2 * i + 1
    most = i
    if left < N and arr[left] > arr[i]:
        most = left
    if right < N and arr[right] > arr[most]:
        most = right
    if i != most:
        arr[i], arr[most] = arr[most], arr[i]
        min_heapify(arr, most, N)


def make_min_heapify(arr):
    N = len(arr)
    for i in range(N // 2, -1, -1):
        min_heapify(arr, i, N)


def make_max_heapify(arr):
    N = len(arr)
    for i in range(N // 2, -1, -1):
        max_heapify(arr, i, N)


arr = [5, 7, 2, 4, 9, 0]
make_min_heapify(arr)
print(arr)
make_max_heapify(arr)
print(arr)
