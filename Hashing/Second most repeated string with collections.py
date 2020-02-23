from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(str,input().split()))
    h = {}
    h = Counter(arr)
    print(h.most_common()[1][0])