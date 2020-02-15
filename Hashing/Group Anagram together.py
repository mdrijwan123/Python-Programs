from collections import defaultdict


def main():
    arr = ['tac', 'toe', 'cat', 'eto']
    h = defaultdict(list)
    for i in range(len(arr)):
        h["".join(sorted(arr[i]))].append(arr[i])
    for j in h.keys():
        print(*h[j], end=" ")


main()
