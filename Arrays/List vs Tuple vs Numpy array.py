import numpy as np

a = [[[1, 2, 3], [4, 5, 6], [6, 7, 8]], 9, 0]
na = np.array([[[1, 2, 3], [4, 5, 6], [6, 7, 8]], 9, 0])
ta = ([[1, 2, 3], [4, 5, 6], [6, 7, 8]], 9, 0)
print(a)
print(na)
print(ta)
print(na.shape)
print(np.shape(a))
print(np.shape(ta))
print(a[0][1][1])
print(na[0][1][1])
print(type(na))
a = np.reshape(a,(1,3))
print(np.shape(a))
print(a)
print("The list is {}".format(a[0][2]))
'''
[[[1, 2, 3], [4, 5, 6], [6, 7, 8]], 9, 0]
[list([[1, 2, 3], [4, 5, 6], [6, 7, 8]]) 9 0]
([[1, 2, 3], [4, 5, 6], [6, 7, 8]], 9, 0)
(3,)
(3,)
(3,)
5
5
<class 'numpy.ndarray'>
'''