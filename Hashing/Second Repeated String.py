import sys
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(str,input().split()))
    h = {}
    for j in range(len(arr)):
        h[arr[j]] = h.get(arr[j],0)+1
    max_val = -sys.maxsize
    max_key = 0
    for i in h.keys():
        if h[i] > max_val:
            max_key = i
            max_val = h[i]
    h[max_key] = 0
    max_val = -sys.maxsize
    for i in h.keys():
        if h[i] > max_val:
            max_key = i
            max_val = h[i]
    print(max_key)