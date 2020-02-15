def main():
    def max_square(n):
        if n == 0:
            return 0
        else:
            return n * n + max_square(n - 1)

    t = int(input())
    for i in range(t):
        n = int(input())
        print(max_square(n))

main()
