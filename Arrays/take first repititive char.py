def main():
    t = int(input())
    for _ in range(t):
        arr = input()
        for j in arr:
            if arr.count(j) > 1:
                print(j)
                break
        else:
            print(-1)

main()
