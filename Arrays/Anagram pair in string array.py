arr = ["geeksquiz", "geeksforgeeks", "abcd", "forgeeksgeeks", "zuiqkeegs","pit","pro","aabb","bbdd"]
t = []


def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        i = 0
        str1_ord = 0
        str2_ord = 0
        while i < len(str1):
            str1_ord += ord(str1[i])
            str2_ord += ord(str2[i])
            i += 1
        if str2_ord != str1_ord:
            return False
        else:
            return True


for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if isAnagram(arr[i], arr[j]):
            t.append((arr[i], arr[j]))
            break
print(t)


