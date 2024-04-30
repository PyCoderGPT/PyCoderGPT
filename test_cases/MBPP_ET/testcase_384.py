from case_MBPP_384 import find_Min_Diff


def check(candidate):
    assert candidate((1,5,3,19,18,25),6) == 1
    assert candidate((4,3,2,6),4) == 1
    assert candidate((30,5,20,9),4) == 4
    assert candidate((2, 7, 5, 16, 23, 26), 6) == 2
    assert candidate((2, 6, 6, 20, 18, 27), 5) == 0
    assert candidate((1, 4, 1, 14, 23, 25), 4) == 0
    assert candidate((2, 7, 5, 24, 17, 28), 2) == 3
    assert candidate((5, 7, 4, 15, 19, 26), 6) == 1
    assert candidate((5, 1, 7, 22, 15, 25), 2) == 4
    assert candidate((2, 8, 6, 21, 18, 22), 2) == 4
    assert candidate((1, 10, 1, 24, 13, 27), 5) == 0
    assert candidate((5, 8, 4, 15, 17, 21), 3) == 1
    assert candidate((5, 4, 4, 18, 15, 22), 2) == 0
    assert candidate((6, 5, 7, 19, 13, 24), 2) == 1
    assert candidate((3, 4, 8, 21, 18, 27), 1) == 100000000000000000000
    assert candidate((4, 10, 6, 24, 21, 26), 3) == 2
    assert candidate((5, 5, 1, 24, 21, 28), 5) == 0
    assert candidate((4, 9, 5, 14, 14, 28), 1) == 100000000000000000000
    assert candidate((2, 4, 1, 15, 17, 22), 6) == 1
    assert candidate((1, 2, 8, 14, 15, 24), 6) == 1
    assert candidate((4, 4, 5, 15, 20, 27), 3) == 0
    assert candidate((5, 6, 8, 16, 18, 28), 5) == 1
    assert candidate((4, 4, 1, 19, 14, 28), 5) == 0
    assert candidate((5, 5, 2, 24, 19, 28), 2) == 3
    assert candidate((5, 1, 4, 24, 18, 20), 5) == 1
    assert candidate((1, 3, 7, 20, 14, 23), 6) == 2
    assert candidate((6, 10, 6, 18, 16, 25), 4) == 0
    assert candidate((1, 4, 8, 19, 16, 20), 3) == 3
    assert candidate((2, 5, 4, 16, 23, 24), 1) == 100000000000000000000
    assert candidate((6, 9, 1, 19, 17, 25), 6) == 2
    assert candidate((1, 6, 1, 16, 22, 29), 5) == 0
    assert candidate((6, 9, 5, 17, 19, 21), 1) == 100000000000000000000
    assert candidate((2, 6, 2, 22, 14, 29), 3) == 0
    assert candidate((2, 10, 2, 14, 16, 22), 6) == 0
    assert candidate((3, 6, 7, 17, 16, 27), 6) == 1
    assert candidate((2, 4, 8, 18, 15, 28), 1) == 100000000000000000000
    assert candidate((6, 8, 6, 4), 4) == 0
    assert candidate((4, 6, 7, 8), 4) == 1
    assert candidate((7, 8, 1, 10), 4) == 1
    assert candidate((2, 1, 6, 10), 2) == 1
    assert candidate((7, 7, 4, 2), 2) == 2
    assert candidate((6, 7, 2, 2), 3) == 0
    assert candidate((1, 8, 4, 2), 2) == 1
    assert candidate((1, 4, 6, 10), 1) == 100000000000000000000
    assert candidate((1, 7, 4, 10), 1) == 100000000000000000000
    assert candidate((7, 4, 4, 6), 1) == 100000000000000000000
    assert candidate((3, 2, 6, 4), 3) == 1
    assert candidate((1, 7, 3, 2), 1) == 100000000000000000000
    assert candidate((7, 4, 2, 6), 3) == 2
    assert candidate((1, 8, 5, 2), 1) == 100000000000000000000
    assert candidate((6, 5, 7, 1), 4) == 1
    assert candidate((5, 4, 5, 7), 3) == 0
    assert candidate((7, 1, 5, 2), 3) == 1
    assert candidate((7, 7, 7, 8), 1) == 100000000000000000000
    assert candidate((2, 2, 3, 5), 2) == 0
    assert candidate((4, 5, 1, 5), 3) == 1
    assert candidate((7, 4, 4, 3), 4) == 0
    assert candidate((8, 7, 5, 5), 4) == 0
    assert candidate((2, 3, 3, 8), 3) == 0
    assert candidate((7, 7, 2, 6), 3) == 1
    assert candidate((5, 4, 5, 8), 1) == 100000000000000000000
    assert candidate((3, 7, 3, 7), 3) == 0
    assert candidate((6, 5, 3, 7), 2) == 2
    assert candidate((8, 8, 6, 9), 1) == 100000000000000000000
    assert candidate((1, 3, 4, 8), 1) == 100000000000000000000
    assert candidate((7, 8, 4, 1), 3) == 3
    assert candidate((6, 4, 6, 6), 3) == 0
    assert candidate((6, 1, 2, 7), 3) == 1
    assert candidate((1, 5, 4, 3), 3) == 1
    assert candidate((25, 4, 23, 9), 4) == 2
    assert candidate((35, 8, 24, 14), 4) == 6
    assert candidate((29, 5, 17, 5), 3) == 0
    assert candidate((25, 3, 16, 11), 2) == 8
    assert candidate((27, 7, 22, 11), 4) == 4
    assert candidate((29, 7, 15, 4), 4) == 3
    assert candidate((31, 10, 15, 12), 2) == 2
    assert candidate((29, 2, 17, 10), 1) == 100000000000000000000
    assert candidate((31, 2, 15, 14), 2) == 12
    assert candidate((35, 1, 18, 8), 1) == 100000000000000000000
    assert candidate((28, 7, 19, 7), 4) == 0
    assert candidate((32, 10, 22, 7), 1) == 100000000000000000000
    assert candidate((29, 9, 16, 5), 1) == 100000000000000000000
    assert candidate((32, 5, 23, 11), 4) == 6
    assert candidate((26, 4, 20, 7), 2) == 3
    assert candidate((28, 3, 20, 10), 3) == 7
    assert candidate((28, 4, 20, 14), 3) == 6
    assert candidate((32, 1, 23, 8), 1) == 100000000000000000000
    assert candidate((26, 7, 16, 9), 2) == 2
    assert candidate((30, 9, 20, 12), 1) == 100000000000000000000
    assert candidate((28, 4, 25, 11), 2) == 7
    assert candidate((27, 7, 17, 14), 4) == 3
    assert candidate((34, 6, 20, 4), 1) == 100000000000000000000
    assert candidate((31, 10, 21, 12), 3) == 2
    assert candidate((30, 4, 16, 14), 3) == 2
    assert candidate((35, 10, 18, 12), 3) == 2
    assert candidate((30, 9, 16, 4), 3) == 5
    assert candidate((26, 10, 18, 12), 3) == 2
    assert candidate((25, 2, 21, 11), 4) == 4
    assert candidate((35, 1, 15, 8), 4) == 7
    assert candidate((30, 6, 15, 10), 3) == 4
    assert candidate((31, 9, 20, 8), 2) == 1
    assert candidate((31, 7, 24, 8), 3) == 1

if __name__ == '__main__':
    check(find_Min_Diff)