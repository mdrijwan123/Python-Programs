def main():
    arr = [1, 4, 1, 2, 7, 5, 2]
    n = len(arr)
    h = {}
    for i in arr:
        h[i] = h.get(i, 0) + 1
    sum = 0
    for j in h.keys():
        sum += h[j]
        h[j] = sum
    sorted_arr = [0] * n
    for i in arr:
        temp = h.get(i)
        sorted_arr[temp - 1] = i
        h[i] = h.get(i, 0) - 1
    print(sorted_arr)


main()
