def main():
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        m = i
        k = i
        for j in range(i,len(arr)):
            if arr[j] < arr[m]:
                m = j
        arr[k],arr[m] = arr[m],arr[k]
    print(arr)

main()