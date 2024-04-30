from case_MBPP_090 import max_Abs_Diff


def check(candidate):
    assert candidate((2,1,5,3),4) == 4
    assert candidate((9,3,2,5,1),5) == 8
    assert candidate((3,2,1),3) == 2
    assert candidate((1, 6, 1, 3), 4) == 5
    assert candidate((6, 6, 1, 6), 4) == 5
    assert candidate((1, 4, 10, 8), 1) == 0
    assert candidate((2, 5, 9, 2), 2) == 3
    assert candidate((3, 1, 5, 3), 2) == 2
    assert candidate((4, 4, 9, 8), 4) == 5
    assert candidate((7, 4, 9, 1), 4) == 8
    assert candidate((7, 3, 7, 5), 3) == 4
    assert candidate((6, 1, 6, 1), 2) == 5
    assert candidate((4, 5, 4, 1), 4) == 4
    assert candidate((2, 5, 7, 3), 3) == 5
    assert candidate((2, 2, 2, 7), 3) == 0
    assert candidate((2, 4, 10, 3), 4) == 8
    assert candidate((6, 1, 7, 8), 3) == 6
    assert candidate((2, 4, 10, 1), 2) == 2
    assert candidate((3, 1, 8, 2), 3) == 7
    assert candidate((7, 3, 3, 8), 4) == 5
    assert candidate((3, 5, 10, 2), 3) == 7
    assert candidate((7, 3, 1, 4), 1) == 0
    assert candidate((5, 6, 3, 2), 1) == 0
    assert candidate((2, 4, 9, 4), 4) == 7
    assert candidate((3, 1, 1, 7), 3) == 2
    assert candidate((2, 4, 6, 7), 4) == 5
    assert candidate((4, 1, 8, 8), 4) == 7
    assert candidate((4, 2, 3, 6), 3) == 2
    assert candidate((7, 5, 7, 7), 3) == 2
    assert candidate((2, 2, 4, 6), 2) == 0
    assert candidate((3, 5, 7, 8), 4) == 5
    assert candidate((2, 4, 5, 5), 2) == 2
    assert candidate((1, 6, 5, 6), 4) == 5
    assert candidate((5, 2, 9, 1), 2) == 3
    assert candidate((5, 2, 3, 3), 2) == 3
    assert candidate((3, 1, 3, 8), 4) == 7
    assert candidate((10, 2, 5, 7, 6), 2) == 8
    assert candidate((11, 4, 5, 3, 2), 2) == 7
    assert candidate((6, 5, 7, 2, 3), 4) == 5
    assert candidate((13, 3, 1, 9, 4), 4) == 12
    assert candidate((14, 8, 5, 10, 1), 5) == 13
    assert candidate((7, 2, 1, 2, 5), 2) == 5
    assert candidate((9, 1, 5, 6, 3), 1) == 0
    assert candidate((7, 2, 3, 5, 6), 5) == 5
    assert candidate((13, 5, 4, 9, 2), 1) == 0
    assert candidate((12, 8, 3, 6, 3), 3) == 9
    assert candidate((14, 4, 5, 4, 1), 2) == 10
    assert candidate((11, 8, 6, 1, 2), 2) == 3
    assert candidate((6, 1, 1, 3, 3), 5) == 5
    assert candidate((9, 5, 5, 1, 1), 2) == 4
    assert candidate((8, 3, 1, 10, 5), 4) == 9
    assert candidate((5, 8, 2, 8, 3), 3) == 6
    assert candidate((13, 1, 7, 7, 3), 3) == 12
    assert candidate((11, 3, 7, 8, 5), 4) == 8
    assert candidate((11, 7, 2, 1, 6), 3) == 9
    assert candidate((4, 3, 3, 3, 1), 2) == 1
    assert candidate((13, 4, 6, 6, 4), 1) == 0
    assert candidate((6, 8, 6, 4, 4), 3) == 2
    assert candidate((12, 1, 3, 8, 3), 1) == 0
    assert candidate((10, 5, 6, 10, 3), 2) == 5
    assert candidate((9, 2, 4, 9, 3), 4) == 7
    assert candidate((6, 2, 7, 8, 5), 5) == 6
    assert candidate((4, 6, 3, 8, 6), 1) == 0
    assert candidate((12, 6, 1, 4, 1), 4) == 11
    assert candidate((8, 3, 6, 10, 4), 2) == 5
    assert candidate((9, 5, 7, 2, 4), 3) == 4
    assert candidate((8, 5, 5, 4, 3), 5) == 5
    assert candidate((9, 8, 2, 7, 6), 5) == 7
    assert candidate((10, 1, 2, 4, 4), 2) == 9
    assert candidate((1, 5, 6), 1) == 0
    assert candidate((2, 7, 4), 1) == 0
    assert candidate((1, 5, 5), 3) == 4
    assert candidate((2, 7, 2), 3) == 5
    assert candidate((2, 2, 2), 2) == 0
    assert candidate((5, 4, 2), 2) == 1
    assert candidate((4, 7, 1), 3) == 6
    assert candidate((8, 4, 6), 3) == 4
    assert candidate((4, 5, 4), 2) == 1
    assert candidate((2, 4, 2), 1) == 0
    assert candidate((2, 3, 3), 3) == 1
    assert candidate((7, 4, 1), 1) == 0
    assert candidate((3, 3, 3), 1) == 0
    assert candidate((5, 4, 4), 3) == 1
    assert candidate((8, 5, 6), 1) == 0
    assert candidate((4, 2, 6), 2) == 2
    assert candidate((8, 7, 6), 1) == 0
    assert candidate((8, 2, 4), 2) == 6
    assert candidate((8, 2, 4), 2) == 6
    assert candidate((5, 6, 1), 2) == 1
    assert candidate((2, 2, 6), 1) == 0
    assert candidate((2, 4, 1), 1) == 0
    assert candidate((4, 4, 2), 1) == 0
    assert candidate((4, 6, 1), 1) == 0
    assert candidate((8, 1, 4), 2) == 7
    assert candidate((5, 2, 3), 1) == 0
    assert candidate((3, 7, 1), 2) == 4
    assert candidate((2, 3, 1), 2) == 1
    assert candidate((6, 7, 6), 1) == 0
    assert candidate((4, 6, 4), 2) == 2
    assert candidate((1, 6, 3), 3) == 5
    assert candidate((7, 5, 5), 3) == 2
    assert candidate((2, 4, 2), 1) == 0

if __name__ == '__main__':
    check(max_Abs_Diff)