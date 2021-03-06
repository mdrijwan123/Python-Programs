def checkPanagram(s):
    h = [0] * 256
    for i in s:
        h[ord(i.upper())] += 1
    for j in range(65, 91):
        if h[j] == 0:
            return 0
    return 1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        if checkPanagram(s):
            print(1)
        else:
            print(0)