def main():
    arr = list(map(int,input().split()))
    srtd = 1
    for i in range(len(arr)-1,0,-1):
        if srtd == 0:
            break
        srtd = 0
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                srtd = 1
    print(arr)

main()