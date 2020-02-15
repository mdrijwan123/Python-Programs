class word:
    def __init__(self, string, index):
        self.string = string
        self.index = index


def dubArray(arr):
    dub = []
    for i in range(len(arr)):
        dub.append(word(arr[i], i))
    return dub


arr = ["cat", "tac", "dog"]
dub = dubArray(arr)
'''
for i in range(len(arr)):
    print(dub[i].index,dub[i].string, sep=" ", end="")
    print()
'''
sortarray = sorted(dub,key=lambda k:k.string)
for i in range(len(sortarray)):
    print(sortarray[i].index,sortarray[i].string, sep=" ", end="")
    print()
for j in sortarray:
	print(arr[j.index])
