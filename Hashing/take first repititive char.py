from collections import Counter
def main():
    t = int(input())
    for _ in range(t):
        arr = input()
        h = Counter(arr)
        cnt = 0
        for j in arr:
            if h[j] > 1:
                cnt += 1
                break
        if cnt == 0:
            print(-1)
        else:
            for i in arr:
                if h[i] > 1:
                    print(i)
                    break


main()

