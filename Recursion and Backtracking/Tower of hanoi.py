def tower_of_hanoi(n, from_peg, to_peg, aux_peg):
    if n == 1:
        print("Shifting from peg {} to peg {}".format(from_peg, to_peg))
        return
    tower_of_hanoi(n - 1, from_peg, aux_peg, to_peg)
    print("Shifting from peg {} to peg {}".format(from_peg, to_peg))
    tower_of_hanoi(n - 1, aux_peg, to_peg, from_peg)


tower_of_hanoi(3, 'A', 'C', 'B')
