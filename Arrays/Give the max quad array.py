def main():
    def givemaxquadsum(arr):
        max_sum = arr[0] + arr[1] + arr[2] + arr[3]
        for i in range(1, len(arr) - 3):
            if arr[i] + arr[i + 1] + arr[i + 2] + arr[i + 3] > max_sum:
                max_sum = arr[i] + arr[i + 1] + arr[i + 2] + arr[i + 3]
        print(max_sum)

    givemaxquadsum([2,3,4,5,6,7,8,2])


main()