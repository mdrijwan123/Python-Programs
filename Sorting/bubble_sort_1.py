ls = list(map(int, input().split()))
flag = 1
for i in range(len(ls)):
    if flag:
        flag = 0
        for j in range(len(ls)-i-1):
            if ls[j+1] < ls[j]:
                ls[j],ls[j+1] = ls[j + 1],ls[j]
                flag = 1

print(ls)