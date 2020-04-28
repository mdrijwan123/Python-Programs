import math


def isPrime(num):
    prime = True
    if num == 1 or num < 1:
        prime = False
    else:
        short_num = int(math.sqrt(num))
        for i in range(2, short_num + 1):
            if num % i == 0:
                prime = False
                break
    if prime:
        print("Prime")
    else:
        print("Not prime")


n = int(input())
for _ in range(n):
    isPrime(int(input()))
