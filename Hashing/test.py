s = 'abcdeab'
h = {}
for i in s:
    h[i] = h.get(i, 0) + 1
for i in h.keys():
    if h[i] > 1:
        print(i)
        break
