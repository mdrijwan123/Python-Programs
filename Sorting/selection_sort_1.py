ls = list(map(int, input().split()))

for i in range(len(ls)):
    mn = i
    j = i
    while j < len(ls):
        if ls[j] < ls[mn]:
            mn = j
        j += 1
    ls[i],ls[mn] = ls[mn],ls[i]

print(ls)