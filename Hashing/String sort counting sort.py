def main():
    string = "qlh"
    MAX_LEN = 256
    h = {}
    for i in range(MAX_LEN):
        h[i] = 0
    for i in string:
        h[ord(i)] = h.get(ord(i), 0) + 1
    n = len(string)
    sorted_string_lst = [0]*n
    sum = 0
    for j in h.keys():
        sum += h.get(j)
        h[j] = sum
    for k in string:
        temp = h[ord(k)]
        sorted_string_lst[temp - 1] = k
        h[ord(k)] = h[ord(k)] - 1
    print(sorted_string_lst)
    print("".join(sorted_string_lst))


main()