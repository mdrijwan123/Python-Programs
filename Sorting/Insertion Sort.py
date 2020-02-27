def main():
    arr = list(map(int,input().split()))
    for i in range(1,len(arr)):
        j = i
        val = arr[j]
        while arr[j-1] > val and j >= 1:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = val
    print(arr)

main()