def binary_search(arr, num):
    n = len(arr)
    l = 0
    r = n - 1
    mid = int(l - (l - r) / 2)
    while l <= r:
        if arr[mid] == num:
            return True
        else:
            if num > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        mid = int(l - (l - r) / 2)
    else:
        return False


def main():
    arr = [1,2,4,4,6,8]
    sum_val = 7
    not_found = True
    for i in range(len(arr)):
        to_search = sum_val - arr[i]
        if binary_search(arr[i:], to_search):
            not_found = False
    if not_found is True:
        print("Not Found")
    else:
        print("Found")


if __name__ == '__main__':
    main()
