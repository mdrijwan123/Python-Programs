import sys
def main():
    cost = []
    for i in range(3):
        temp = list(map(int, input().split()))
        cost.append(temp)

    def minCost(cost, m, n):
        if n < 0 or m < 0:
            return sys.maxsize
        elif n == 0 and m == 0:
            return cost[m][n]
        else:
            return cost[m][n] + min(minCost(cost, m - 1, n - 1), minCost(cost, m - 1, n), minCost(cost, m, n - 1))

    def min(x, y, z):
        if x < y:
            return x if (x < z) else z
        else:
            return y if (y < z) else z
    print(minCost(cost, 2, 2))


if __name__ == '__main__':
    main()
