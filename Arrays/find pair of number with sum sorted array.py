def binary_search(arr, num):
    n = len(arr)
    l = 0
    r = n - 1
    mid = (l + r) // 2
    while l <= r:
        if arr[mid] == num:
            return True
        else:
            if num > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        mid = (l + r) // 2
    else:
        return False


def main():
    arr = [1,2,4,4]
    sum_val = 8
    not_found = 0
    for i in range(len(arr)):
        to_search = sum_val - arr[i]
        if binary_search(arr[i:], to_search):
            not_found = 1
    if not_found == 0:
        print("Not Found")
    else:
        print("Found")


if __name__ == '__main__':
    main()
