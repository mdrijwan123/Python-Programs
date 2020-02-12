def main():
    def sortedornot(arr, n):
        if n == 1:
            return 1
        else:
            if arr[n - 2] < arr[n - 1]:
                return sortedornot(arr, n - 1)
            else:
                return 0

    arr = [10, 3, 5, 9]
    print(bool(sortedornot(arr, len(arr))))


main()
