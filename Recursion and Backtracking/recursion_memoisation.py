def main():
    def fact(num):
        if num == 0:
            return 1
        else:
            f = 1
            for i in range(num):
                f = f * fact(num-1)
            return sum
    print(fact(5))
main()