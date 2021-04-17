import os
l = 0
for root, dirs, files in os.walk("../"):
    for name in files:
        print(os.path.join(root, name))
        l+= 1
print(l)
   # for name in dirs:
   #    print(os.path.join(root, name))
