for _ in range(int(input())):
    st = input()
    stack = []
    result = ""
    for i in range(len(st) + 1):
        stack.append(str(i + 1))
        if i == len(st) or st[i] == "I":
            while len(stack):
                result = result + stack[-1]
                stack.pop()
    print(result)
