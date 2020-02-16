from collections import Counter,OrderedDict

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        sort_arr = sorted(arr)
        temp_arr = [i for i in range(1, n + 1)]
        no_in_list = -1
        cnt_h = Counter(sort_arr)
        key_arr = []
        for k in cnt_h.keys():
            key_arr.append(k)
        key_arr_sort = sorted(key_arr)
        for j in range(n):
            if temp_arr[j] != key_arr_sort[j]:
                no_in_list = temp_arr[j]
                break
        rep_item = -1
        for j in cnt_h.keys():
            if cnt_h[j] > 1:
                rep_item = j
                break
        print(rep_item,",",no_in_list)


main()