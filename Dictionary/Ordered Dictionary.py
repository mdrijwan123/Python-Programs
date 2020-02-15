from collections import OrderedDict

h = OrderedDict()
h[1] = 'one'
h[0] = 'zeros'

k = {}

k['a'] = 'A'
k['b'] = 'B'
k['c'] = 'C'
k['d'] = 'D'
print(k)
print(h)

h.pop(0)
print(h)