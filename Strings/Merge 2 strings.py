def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(str, input().split()))
        max_len = max(len(arr[0]), len(arr[1]))
        i = 0
        str_lst = []
        while i < max_len:
            if i < len(arr[0]) and i < len(arr[1]):
                str_lst.append(arr[0][i])
                str_lst.append(arr[1][i])
            elif len(arr[0]) > i >= len(arr[1]):
                str_lst.append(arr[0][i])
            elif len(arr[0]) <= i < len(arr[1]):
                str_lst.append(arr[1][i])
            i += 1
        print("".join(str_lst))


main()
