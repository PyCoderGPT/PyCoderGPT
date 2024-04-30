from case_MBPP_150 import count_first_elements


def check(candidate):
    assert candidate((1, 5, 7, (4, 6), 10) ) == 3
    assert candidate((2, 9, (5, 7), 11) ) == 2
    assert candidate((11, 15, 5, 8, (2, 3), 8) ) == 4
    assert candidate((6, 1, 7, (5, 10), 6)) == 3
    assert candidate((6, 2, 4, (7, 8), 7)) == 3
    assert candidate((5, 5, 3, (1, 5), 14)) == 3
    assert candidate((1, 3, 7, (5, 3), 15)) == 3
    assert candidate((1, 1, 2, (5, 3), 6)) == 3
    assert candidate((4, 4, 4, (2, 2), 12)) == 3
    assert candidate((6, 6, 9, (5, 10), 13)) == 3
    assert candidate((4, 6, 4, (9, 2), 15)) == 3
    assert candidate((2, 4, 9, (7, 7), 7)) == 3
    assert candidate((3, 8, 6, (8, 7), 8)) == 3
    assert candidate((6, 1, 7, (2, 2), 6)) == 3
    assert candidate((1, 5, 2, (3, 10), 9)) == 3
    assert candidate((1, 6, 11, (4, 2), 9)) == 3
    assert candidate((1, 6, 6, (4, 7), 5)) == 3
    assert candidate((6, 10, 6, (9, 8), 5)) == 3
    assert candidate((5, 1, 7, (3, 8), 7)) == 3
    assert candidate((6, 6, 8, (6, 10), 14)) == 3
    assert candidate((3, 6, 6, (9, 6), 10)) == 3
    assert candidate((3, 4, 9, (9, 7), 6)) == 3
    assert candidate((1, 8, 2, (9, 8), 5)) == 3
    assert candidate((4, 4, 8, (4, 9), 7)) == 3
    assert candidate((6, 2, 2, (2, 8), 10)) == 3
    assert candidate((1, 8, 12, (1, 5), 9)) == 3
    assert candidate((1, 9, 10, (4, 6), 14)) == 3
    assert candidate((5, 2, 7, (4, 8), 8)) == 3
    assert candidate((2, 3, 3, (3, 11), 11)) == 3
    assert candidate((4, 3, 7, (1, 7), 10)) == 3
    assert candidate((3, 10, 10, (7, 8), 11)) == 3
    assert candidate((3, 2, 6, (9, 1), 8)) == 3
    assert candidate((6, 10, 4, (3, 11), 5)) == 3
    assert candidate((4, 5, 8, (8, 3), 7)) == 3
    assert candidate((3, 8, 8, (7, 5), 7)) == 3
    assert candidate((6, 5, 9, (1, 10), 15)) == 3
    assert candidate((1, 7, (6, 8), 7)) == 2
    assert candidate((2, 5, (10, 5), 15)) == 2
    assert candidate((1, 8, (1, 4), 6)) == 2
    assert candidate((7, 4, (10, 12), 9)) == 2
    assert candidate((6, 8, (8, 9), 9)) == 2
    assert candidate((2, 6, (6, 11), 8)) == 2
    assert candidate((3, 13, (1, 11), 12)) == 2
    assert candidate((1, 12, (8, 5), 13)) == 2
    assert candidate((6, 12, (4, 8), 14)) == 2
    assert candidate((1, 13, (2, 8), 15)) == 2
    assert candidate((5, 4, (9, 7), 7)) == 2
    assert candidate((3, 5, (9, 8), 7)) == 2
    assert candidate((2, 10, (4, 7), 9)) == 2
    assert candidate((3, 4, (6, 12), 8)) == 2
    assert candidate((2, 6, (10, 10), 10)) == 2
    assert candidate((7, 7, (8, 10), 12)) == 2
    assert candidate((4, 13, (4, 6), 8)) == 2
    assert candidate((2, 13, (9, 6), 10)) == 2
    assert candidate((3, 7, (9, 9), 11)) == 2
    assert candidate((3, 14, (10, 10), 8)) == 2
    assert candidate((6, 7, (8, 7), 12)) == 2
    assert candidate((7, 9, (10, 3), 14)) == 2
    assert candidate((3, 9, (4, 8), 12)) == 2
    assert candidate((7, 7, (5, 2), 12)) == 2
    assert candidate((6, 12, (9, 6), 9)) == 2
    assert candidate((4, 7, (1, 5), 6)) == 2
    assert candidate((6, 5, (7, 3), 16)) == 2
    assert candidate((6, 13, (5, 12), 6)) == 2
    assert candidate((1, 6, (5, 4), 11)) == 2
    assert candidate((3, 9, (4, 4), 8)) == 2
    assert candidate((6, 7, (3, 12), 16)) == 2
    assert candidate((2, 5, (3, 3), 9)) == 2
    assert candidate((5, 6, (2, 9), 12)) == 2
    assert candidate((7, 16, 4, 9, (3, 3), 10)) == 4
    assert candidate((6, 15, 8, 7, (3, 3), 9)) == 4
    assert candidate((15, 13, 9, 8, (3, 4), 13)) == 4
    assert candidate((10, 18, 10, 5, (6, 6), 7)) == 4
    assert candidate((11, 13, 8, 5, (6, 6), 6)) == 4
    assert candidate((12, 16, 10, 13, (6, 3), 3)) == 4
    assert candidate((9, 13, 7, 8, (5, 4), 9)) == 4
    assert candidate((11, 10, 10, 10, (7, 8), 4)) == 4
    assert candidate((7, 17, 4, 8, (4, 2), 9)) == 4
    assert candidate((7, 17, 6, 9, (2, 3), 8)) == 4
    assert candidate((16, 17, 3, 7, (3, 1), 13)) == 4
    assert candidate((12, 19, 10, 5, (3, 6), 12)) == 4
    assert candidate((10, 13, 6, 13, (5, 7), 10)) == 4
    assert candidate((15, 15, 3, 11, (2, 6), 6)) == 4
    assert candidate((8, 20, 9, 8, (2, 6), 9)) == 4
    assert candidate((13, 16, 3, 10, (7, 5), 12)) == 4
    assert candidate((15, 13, 5, 10, (5, 6), 6)) == 4
    assert candidate((9, 13, 7, 4, (3, 6), 7)) == 4
    assert candidate((12, 15, 4, 9, (1, 5), 12)) == 4
    assert candidate((14, 20, 1, 10, (2, 1), 10)) == 4
    assert candidate((16, 10, 2, 7, (2, 3), 7)) == 4
    assert candidate((9, 10, 4, 11, (7, 3), 13)) == 4
    assert candidate((8, 17, 10, 8, (5, 3), 4)) == 4
    assert candidate((13, 12, 3, 10, (7, 8), 9)) == 4
    assert candidate((10, 13, 7, 7, (7, 4), 6)) == 4
    assert candidate((13, 18, 10, 12, (6, 1), 8)) == 4
    assert candidate((10, 19, 10, 7, (2, 4), 10)) == 4
    assert candidate((9, 10, 2, 11, (4, 4), 8)) == 4
    assert candidate((12, 10, 4, 13, (3, 1), 6)) == 4
    assert candidate((15, 19, 5, 13, (1, 5), 4)) == 4
    assert candidate((7, 18, 7, 3, (7, 8), 4)) == 4
    assert candidate((6, 17, 1, 5, (7, 1), 3)) == 4
    assert candidate((11, 10, 8, 11, (3, 4), 12)) == 4

if __name__ == '__main__':
    check(count_first_elements)