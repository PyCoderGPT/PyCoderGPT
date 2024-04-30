from case_MBPP_193 import add_nested_tuples


def check(candidate):
    assert candidate(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((7, 10), (7, 14), (3, 10), (8, 13))
    assert candidate(((2, 4), (5, 6), (3, 10), (2, 11)), ((7, 8), (4, 10), (2, 2), (8, 4))) == ((9, 12), (9, 16), (5, 12), (10, 15))
    assert candidate(((3, 5), (6, 7), (4, 11), (3, 12)), ((8, 9), (5, 11), (3, 3), (9, 5))) == ((11, 14), (11, 18), (7, 14), (12, 17))
    assert candidate(((2, 7), (9, 3), (2, 6), (2, 6)), ((7, 4), (8, 14), (6, 6), (3, 7))) == ((9, 11), (17, 17), (8, 12), (5, 13))
    assert candidate(((1, 8), (4, 8), (4, 9), (3, 13)), ((7, 12), (3, 11), (1, 4), (10, 1))) == ((8, 20), (7, 19), (5, 13), (13, 14))
    assert candidate(((6, 4), (6, 5), (1, 8), (1, 12)), ((9, 7), (5, 13), (4, 6), (10, 1))) == ((15, 11), (11, 18), (5, 14), (11, 13))
    assert candidate(((3, 4), (6, 6), (1, 5), (5, 15)), ((10, 5), (6, 9), (6, 3), (9, 2))) == ((13, 9), (12, 15), (7, 8), (14, 17))
    assert candidate(((4, 5), (2, 1), (3, 10), (3, 12)), ((11, 6), (7, 12), (1, 1), (4, 6))) == ((15, 11), (9, 13), (4, 11), (7, 18))
    assert candidate(((1, 1), (2, 7), (2, 4), (5, 7)), ((11, 11), (5, 12), (2, 3), (12, 3))) == ((12, 12), (7, 19), (4, 7), (17, 10))
    assert candidate(((3, 8), (2, 8), (6, 8), (2, 9)), ((5, 9), (3, 11), (3, 3), (8, 2))) == ((8, 17), (5, 19), (9, 11), (10, 11))
    assert candidate(((6, 4), (2, 2), (3, 10), (2, 9)), ((7, 6), (8, 14), (6, 4), (10, 4))) == ((13, 10), (10, 16), (9, 14), (12, 13))
    assert candidate(((3, 3), (3, 1), (5, 6), (2, 12)), ((8, 9), (4, 14), (3, 6), (11, 7))) == ((11, 12), (7, 15), (8, 12), (13, 19))
    assert candidate(((5, 6), (3, 9), (6, 7), (3, 8)), ((6, 12), (2, 5), (2, 3), (9, 7))) == ((11, 18), (5, 14), (8, 10), (12, 15))
    assert candidate(((3, 4), (4, 9), (3, 10), (5, 8)), ((6, 12), (2, 13), (5, 1), (2, 1))) == ((9, 16), (6, 22), (8, 11), (7, 9))
    assert candidate(((6, 7), (4, 2), (6, 13), (4, 11)), ((11, 3), (2, 8), (1, 4), (8, 1))) == ((17, 10), (6, 10), (7, 17), (12, 12))
    assert candidate(((6, 3), (8, 7), (3, 9), (6, 15)), ((6, 6), (3, 9), (6, 2), (3, 1))) == ((12, 9), (11, 16), (9, 11), (9, 16))
    assert candidate(((2, 4), (2, 6), (3, 10), (6, 9)), ((2, 11), (6, 8), (3, 4), (8, 1))) == ((4, 15), (8, 14), (6, 14), (14, 10))
    assert candidate(((1, 4), (9, 4), (4, 7), (2, 11)), ((5, 2), (2, 5), (6, 5), (7, 2))) == ((6, 6), (11, 9), (10, 12), (9, 13))
    assert candidate(((3, 5), (2, 8), (3, 10), (1, 11)), ((7, 2), (4, 12), (4, 3), (6, 6))) == ((10, 7), (6, 20), (7, 13), (7, 17))
    assert candidate(((5, 3), (2, 2), (5, 5), (5, 11)), ((4, 3), (3, 14), (4, 2), (2, 2))) == ((9, 6), (5, 16), (9, 7), (7, 13))
    assert candidate(((5, 1), (2, 9), (3, 11), (3, 15)), ((2, 12), (7, 9), (4, 4), (11, 5))) == ((7, 13), (9, 18), (7, 15), (14, 20))
    assert candidate(((4, 5), (3, 9), (6, 13), (1, 14)), ((10, 2), (1, 11), (1, 4), (12, 5))) == ((14, 7), (4, 20), (7, 17), (13, 19))
    assert candidate(((3, 8), (6, 9), (5, 12), (6, 5)), ((9, 5), (2, 11), (5, 4), (9, 3))) == ((12, 13), (8, 20), (10, 16), (15, 8))
    assert candidate(((3, 8), (6, 2), (3, 9), (3, 10)), ((11, 3), (1, 7), (5, 5), (12, 6))) == ((14, 11), (7, 9), (8, 14), (15, 16))
    assert candidate(((2, 6), (5, 6), (1, 11), (4, 11)), ((6, 3), (1, 12), (2, 3), (6, 5))) == ((8, 9), (6, 18), (3, 14), (10, 16))
    assert candidate(((4, 2), (9, 1), (2, 4), (4, 9)), ((3, 8), (4, 9), (6, 1), (7, 2))) == ((7, 10), (13, 10), (8, 5), (11, 11))
    assert candidate(((1, 3), (2, 2), (6, 14), (4, 11)), ((7, 4), (5, 9), (1, 6), (12, 2))) == ((8, 7), (7, 11), (7, 20), (16, 13))
    assert candidate(((4, 5), (5, 5), (5, 10), (1, 13)), ((3, 7), (2, 14), (1, 1), (9, 6))) == ((7, 12), (7, 19), (6, 11), (10, 19))
    assert candidate(((5, 3), (4, 2), (7, 6), (1, 7)), ((9, 5), (6, 7), (5, 1), (10, 4))) == ((14, 8), (10, 9), (12, 7), (11, 11))
    assert candidate(((5, 3), (6, 10), (1, 10), (5, 9)), ((7, 4), (2, 11), (1, 5), (11, 4))) == ((12, 7), (8, 21), (2, 15), (16, 13))
    assert candidate(((2, 6), (7, 7), (2, 5), (4, 7)), ((7, 6), (8, 5), (5, 1), (5, 2))) == ((9, 12), (15, 12), (7, 6), (9, 9))
    assert candidate(((3, 8), (4, 10), (3, 5), (6, 14)), ((7, 7), (6, 5), (2, 5), (11, 5))) == ((10, 15), (10, 15), (5, 10), (17, 19))
    assert candidate(((3, 3), (6, 4), (2, 8), (3, 13)), ((11, 9), (2, 13), (2, 2), (10, 3))) == ((14, 12), (8, 17), (4, 10), (13, 16))
    assert candidate(((5, 2), (1, 10), (3, 8), (2, 13)), ((4, 5), (2, 12), (1, 3), (3, 7))) == ((9, 7), (3, 22), (4, 11), (5, 20))
    assert candidate(((4, 6), (7, 9), (2, 4), (6, 12)), ((7, 11), (7, 8), (3, 1), (4, 7))) == ((11, 17), (14, 17), (5, 5), (10, 19))
    assert candidate(((5, 5), (5, 3), (5, 6), (1, 9)), ((8, 12), (4, 9), (6, 5), (9, 2))) == ((13, 17), (9, 12), (11, 11), (10, 11))
    assert candidate(((2, 7), (1, 2), (8, 6), (7, 11)), ((2, 5), (8, 14), (7, 3), (6, 2))) == ((4, 12), (9, 16), (15, 9), (13, 13))
    assert candidate(((2, 2), (9, 3), (5, 14), (7, 9)), ((2, 12), (5, 5), (6, 1), (11, 6))) == ((4, 14), (14, 8), (11, 15), (18, 15))
    assert candidate(((1, 6), (7, 2), (8, 15), (1, 15)), ((6, 6), (8, 12), (4, 2), (6, 6))) == ((7, 12), (15, 14), (12, 17), (7, 21))
    assert candidate(((3, 3), (3, 10), (7, 6), (2, 11)), ((2, 5), (3, 12), (6, 5), (11, 8))) == ((5, 8), (6, 22), (13, 11), (13, 19))
    assert candidate(((6, 2), (5, 5), (4, 7), (3, 13)), ((11, 8), (3, 8), (1, 7), (4, 5))) == ((17, 10), (8, 13), (5, 14), (7, 18))
    assert candidate(((6, 4), (8, 5), (7, 7), (6, 10)), ((7, 13), (8, 7), (1, 4), (13, 6))) == ((13, 17), (16, 12), (8, 11), (19, 16))
    assert candidate(((7, 7), (5, 1), (8, 7), (3, 13)), ((7, 11), (9, 13), (6, 7), (4, 6))) == ((14, 18), (14, 14), (14, 14), (7, 19))
    assert candidate(((4, 6), (2, 2), (2, 13), (6, 8)), ((11, 10), (4, 10), (4, 1), (13, 4))) == ((15, 16), (6, 12), (6, 14), (19, 12))
    assert candidate(((4, 4), (4, 9), (8, 12), (4, 16)), ((7, 12), (7, 5), (5, 3), (6, 8))) == ((11, 16), (11, 14), (13, 15), (10, 24))
    assert candidate(((4, 3), (3, 10), (3, 14), (1, 9)), ((10, 11), (5, 8), (1, 3), (6, 2))) == ((14, 14), (8, 18), (4, 17), (7, 11))
    assert candidate(((7, 2), (10, 1), (1, 14), (7, 9)), ((6, 12), (1, 6), (3, 4), (12, 4))) == ((13, 14), (11, 7), (4, 18), (19, 13))
    assert candidate(((3, 7), (2, 5), (8, 14), (1, 6)), ((3, 7), (2, 12), (3, 1), (13, 8))) == ((6, 14), (4, 17), (11, 15), (14, 14))
    assert candidate(((3, 9), (6, 11), (8, 8), (6, 12)), ((2, 11), (6, 5), (7, 5), (4, 4))) == ((5, 20), (12, 16), (15, 13), (10, 16))
    assert candidate(((4, 6), (9, 5), (6, 12), (4, 11)), ((10, 10), (5, 8), (1, 7), (10, 4))) == ((14, 16), (14, 13), (7, 19), (14, 15))
    assert candidate(((5, 2), (9, 3), (6, 11), (7, 14)), ((5, 12), (1, 10), (1, 3), (9, 9))) == ((10, 14), (10, 13), (7, 14), (16, 23))
    assert candidate(((4, 7), (8, 7), (3, 10), (6, 7)), ((2, 10), (2, 11), (3, 1), (4, 3))) == ((6, 17), (10, 18), (6, 11), (10, 10))
    assert candidate(((4, 9), (1, 7), (8, 5), (1, 16)), ((8, 11), (7, 9), (4, 6), (4, 8))) == ((12, 20), (8, 16), (12, 11), (5, 24))
    assert candidate(((7, 1), (6, 6), (4, 14), (2, 9)), ((4, 4), (9, 8), (7, 4), (3, 6))) == ((11, 5), (15, 14), (11, 18), (5, 15))
    assert candidate(((4, 3), (5, 7), (5, 14), (2, 7)), ((10, 13), (6, 14), (1, 1), (6, 4))) == ((14, 16), (11, 21), (6, 15), (8, 11))
    assert candidate(((3, 2), (10, 2), (4, 8), (1, 7)), ((4, 6), (2, 14), (6, 1), (10, 7))) == ((7, 8), (12, 16), (10, 9), (11, 14))
    assert candidate(((3, 3), (3, 6), (1, 15), (1, 7)), ((10, 11), (4, 14), (1, 7), (10, 2))) == ((13, 14), (7, 20), (2, 22), (11, 9))
    assert candidate(((7, 6), (6, 2), (4, 13), (2, 11)), ((12, 8), (6, 5), (2, 4), (8, 9))) == ((19, 14), (12, 7), (6, 17), (10, 20))
    assert candidate(((3, 8), (7, 8), (5, 7), (4, 8)), ((8, 3), (4, 7), (6, 6), (13, 3))) == ((11, 11), (11, 15), (11, 13), (17, 11))
    assert candidate(((4, 7), (8, 9), (1, 9), (3, 10)), ((4, 11), (6, 12), (4, 5), (12, 3))) == ((8, 18), (14, 21), (5, 14), (15, 13))
    assert candidate(((5, 6), (2, 9), (5, 13), (2, 10)), ((12, 4), (5, 7), (1, 6), (5, 8))) == ((17, 10), (7, 16), (6, 19), (7, 18))
    assert candidate(((1, 4), (4, 1), (6, 11), (1, 14)), ((9, 4), (6, 12), (2, 2), (8, 1))) == ((10, 8), (10, 13), (8, 13), (9, 15))
    assert candidate(((4, 7), (4, 5), (7, 12), (5, 16)), ((11, 8), (6, 8), (5, 5), (6, 4))) == ((15, 15), (10, 13), (12, 17), (11, 20))
    assert candidate(((3, 3), (3, 6), (2, 13), (1, 10)), ((5, 11), (4, 11), (5, 6), (5, 9))) == ((8, 14), (7, 17), (7, 19), (6, 19))
    assert candidate(((1, 4), (9, 5), (1, 11), (3, 12)), ((11, 5), (1, 14), (7, 5), (11, 7))) == ((12, 9), (10, 19), (8, 16), (14, 19))
    assert candidate(((5, 2), (2, 6), (8, 6), (5, 10)), ((8, 5), (5, 6), (3, 4), (12, 4))) == ((13, 7), (7, 12), (11, 10), (17, 14))
    assert candidate(((4, 3), (1, 2), (7, 15), (4, 15)), ((2, 7), (7, 11), (6, 5), (10, 3))) == ((6, 10), (8, 13), (13, 20), (14, 18))
    assert candidate(((7, 9), (7, 10), (5, 14), (2, 14)), ((11, 7), (3, 13), (1, 2), (5, 2))) == ((18, 16), (10, 23), (6, 16), (7, 16))
    assert candidate(((6, 6), (3, 2), (8, 13), (3, 6)), ((8, 10), (9, 5), (4, 7), (7, 4))) == ((14, 16), (12, 7), (12, 20), (10, 10))
    assert candidate(((1, 7), (7, 12), (6, 11), (8, 16)), ((6, 10), (8, 9), (6, 7), (5, 8))) == ((7, 17), (15, 21), (12, 18), (13, 24))
    assert candidate(((4, 1), (8, 3), (2, 13), (3, 13)), ((6, 11), (8, 16), (3, 4), (7, 3))) == ((10, 12), (16, 19), (5, 17), (10, 16))
    assert candidate(((8, 2), (1, 2), (5, 13), (8, 14)), ((9, 4), (5, 14), (8, 4), (13, 9))) == ((17, 6), (6, 16), (13, 17), (21, 23))
    assert candidate(((8, 9), (6, 9), (5, 13), (5, 10)), ((7, 9), (1, 8), (6, 7), (6, 2))) == ((15, 18), (7, 17), (11, 20), (11, 12))
    assert candidate(((4, 1), (10, 11), (6, 11), (7, 13)), ((5, 5), (7, 9), (8, 5), (7, 6))) == ((9, 6), (17, 20), (14, 16), (14, 19))
    assert candidate(((1, 6), (6, 11), (3, 12), (1, 16)), ((11, 12), (2, 15), (2, 4), (7, 4))) == ((12, 18), (8, 26), (5, 16), (8, 20))
    assert candidate(((6, 5), (3, 4), (2, 9), (2, 7)), ((5, 13), (5, 13), (1, 1), (12, 5))) == ((11, 18), (8, 17), (3, 10), (14, 12))
    assert candidate(((5, 9), (4, 9), (1, 11), (5, 11)), ((7, 7), (6, 10), (8, 7), (9, 5))) == ((12, 16), (10, 19), (9, 18), (14, 16))
    assert candidate(((6, 1), (6, 6), (3, 8), (4, 14)), ((7, 5), (10, 14), (8, 4), (7, 7))) == ((13, 6), (16, 20), (11, 12), (11, 21))
    assert candidate(((4, 3), (9, 11), (7, 8), (7, 7)), ((7, 13), (9, 15), (7, 6), (11, 2))) == ((11, 16), (18, 26), (14, 14), (18, 9))
    assert candidate(((3, 5), (8, 6), (8, 14), (1, 10)), ((3, 12), (9, 8), (7, 7), (12, 6))) == ((6, 17), (17, 14), (15, 21), (13, 16))
    assert candidate(((5, 9), (5, 2), (9, 13), (2, 9)), ((6, 8), (2, 7), (8, 7), (14, 9))) == ((11, 17), (7, 9), (17, 20), (16, 18))
    assert candidate(((3, 10), (1, 2), (2, 10), (8, 8)), ((5, 8), (3, 11), (1, 7), (8, 6))) == ((8, 18), (4, 13), (3, 17), (16, 14))
    assert candidate(((5, 9), (4, 2), (2, 16), (1, 16)), ((6, 9), (7, 7), (6, 7), (9, 5))) == ((11, 18), (11, 9), (8, 23), (10, 21))
    assert candidate(((7, 1), (9, 10), (4, 12), (2, 14)), ((10, 12), (4, 16), (7, 8), (6, 2))) == ((17, 13), (13, 26), (11, 20), (8, 16))
    assert candidate(((1, 4), (2, 4), (2, 16), (1, 17)), ((11, 10), (7, 6), (5, 8), (5, 7))) == ((12, 14), (9, 10), (7, 24), (6, 24))
    assert candidate(((2, 10), (9, 11), (9, 6), (5, 17)), ((12, 7), (8, 14), (5, 5), (5, 4))) == ((14, 17), (17, 25), (14, 11), (10, 21))
    assert candidate(((2, 4), (6, 9), (4, 14), (2, 9)), ((13, 11), (1, 10), (6, 3), (7, 2))) == ((15, 15), (7, 19), (10, 17), (9, 11))
    assert candidate(((1, 3), (5, 12), (3, 11), (5, 16)), ((6, 11), (7, 10), (7, 7), (6, 1))) == ((7, 14), (12, 22), (10, 18), (11, 17))
    assert candidate(((8, 5), (5, 5), (1, 16), (4, 10)), ((6, 4), (2, 7), (5, 1), (7, 5))) == ((14, 9), (7, 12), (6, 17), (11, 15))
    assert candidate(((5, 9), (1, 6), (7, 7), (1, 11)), ((13, 6), (5, 9), (4, 8), (10, 9))) == ((18, 15), (6, 15), (11, 15), (11, 20))
    assert candidate(((4, 5), (3, 12), (2, 12), (5, 8)), ((11, 10), (3, 7), (6, 7), (5, 5))) == ((15, 15), (6, 19), (8, 19), (10, 13))
    assert candidate(((8, 8), (8, 2), (7, 15), (2, 17)), ((7, 8), (8, 15), (6, 6), (10, 6))) == ((15, 16), (16, 17), (13, 21), (12, 23))
    assert candidate(((5, 8), (2, 2), (8, 7), (8, 17)), ((5, 6), (7, 15), (1, 2), (8, 3))) == ((10, 14), (9, 17), (9, 9), (16, 20))
    assert candidate(((2, 1), (9, 5), (9, 11), (4, 15)), ((6, 12), (2, 11), (2, 5), (14, 3))) == ((8, 13), (11, 16), (11, 16), (18, 18))
    assert candidate(((7, 7), (5, 6), (7, 8), (1, 14)), ((4, 13), (2, 7), (7, 4), (14, 6))) == ((11, 20), (7, 13), (14, 12), (15, 20))
    assert candidate(((3, 2), (8, 3), (6, 11), (4, 10)), ((8, 9), (1, 8), (5, 1), (9, 2))) == ((11, 11), (9, 11), (11, 12), (13, 12))
    assert candidate(((8, 3), (6, 9), (4, 13), (7, 17)), ((5, 12), (8, 7), (5, 1), (10, 9))) == ((13, 15), (14, 16), (9, 14), (17, 26))
    assert candidate(((4, 3), (6, 7), (3, 15), (3, 9)), ((11, 10), (1, 12), (2, 2), (8, 5))) == ((15, 13), (7, 19), (5, 17), (11, 14))
    assert candidate(((8, 3), (8, 9), (8, 10), (4, 14)), ((8, 9), (4, 7), (5, 3), (6, 10))) == ((16, 12), (12, 16), (13, 13), (10, 24))
    assert candidate(((5, 3), (7, 9), (1, 15), (5, 10)), ((5, 13), (10, 12), (8, 7), (8, 4))) == ((10, 16), (17, 21), (9, 22), (13, 14))
    assert candidate(((1, 2), (6, 3), (6, 6), (5, 9)), ((3, 13), (8, 15), (5, 5), (8, 2))) == ((4, 15), (14, 18), (11, 11), (13, 11))
    assert candidate(((2, 3), (8, 7), (7, 13), (5, 8)), ((12, 6), (1, 8), (1, 5), (9, 7))) == ((14, 9), (9, 15), (8, 18), (14, 15))

if __name__ == '__main__':
    check(add_nested_tuples)