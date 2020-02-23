def main():
    t = int(input())
    for _ in range(t):
        s = input()
        a, b = 0, 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '1':
                    a += 1
                else:
                    b += 1
            else:
                if s[i] == '1':
                    b += 1
                else:
                    a += 1
        print(min(a, b))

main()