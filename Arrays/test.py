arr = [5,4,3,2]
b = iter(arr)
print(b)
while True:
    try:
        e = next(b)
        print(e)
    except StopIteration:
        break
