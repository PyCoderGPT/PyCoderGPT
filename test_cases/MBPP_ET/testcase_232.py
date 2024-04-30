from case_MBPP_232 import trim_tuple


def check(candidate):
    assert candidate([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1),(9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 2) == '[(2,), (9,), (2,), (2,)]'
    assert candidate([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1), (9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 1) == '[(3, 2, 1), (4, 9, 2), (1, 2, 3), (8, 2, 1)]'
    assert candidate([(7, 8, 4, 9), (11, 8, 12, 4),(4, 1, 7, 8), (3, 6, 9, 7)], 1) == '[(8, 4), (8, 12), (1, 7), (6, 9)]'
    assert candidate([(9, 8, 1, 2, 9), (7, 7, 9, 1, 6), (8, 3, 1, 2, 10), (9, 5, 3, 3, 5)], 5) == [(), (), (), ()]
    assert candidate([(10, 4, 4, 2, 5), (1, 1, 7, 2, 3), (11, 5, 6, 2, 8), (3, 10, 1, 3, 10)], 7) == [(), (), (), ()]
    assert candidate([(6, 5, 2, 3, 3), (3, 6, 7, 6, 1), (4, 3, 5, 7, 1), (2, 13, 7, 6, 8)], 7) == [(), (), (), ()]
    assert candidate([(7, 5, 3, 4, 1), (7, 8, 9, 7, 3), (5, 1, 2, 1, 3), (6, 9, 6, 1, 7)], 1) == [(5, 3, 4), (8, 9, 7), (1, 2, 1), (9, 6, 1)]
    assert candidate([(10, 3, 7, 1, 3), (1, 2, 9, 2, 2), (4, 3, 1, 8, 5), (9, 5, 7, 5, 9)], 5) == [(), (), (), ()]
    assert candidate([(7, 7, 7, 1, 9), (8, 9, 6, 4, 1), (6, 6, 5, 8, 4), (9, 5, 4, 3, 4)], 3) == [(), (), (), ()]
    assert candidate([(9, 4, 6, 2, 5), (6, 7, 13, 3, 4), (7, 2, 5, 2, 4), (3, 8, 7, 1, 5)], 3) == [(), (), (), ()]
    assert candidate([(1, 1, 6, 4, 6), (2, 1, 5, 4, 3), (4, 1, 5, 2, 3), (1, 4, 6, 1, 6)], 2) == [(6,), (5,), (5,), (6,)]
    assert candidate([(6, 1, 3, 1, 7), (6, 8, 4, 2, 5), (7, 2, 7, 1, 1), (6, 11, 2, 2, 2)], 6) == [(), (), (), ()]
    assert candidate([(4, 4, 7, 5, 6), (1, 2, 10, 7, 3), (9, 6, 5, 7, 2), (3, 9, 4, 5, 7)], 6) == [(), (), (), ()]
    assert candidate([(5, 3, 3, 6, 1), (5, 8, 8, 2, 5), (12, 2, 5, 1, 4), (3, 6, 4, 4, 12)], 5) == [(), (), (), ()]
    assert candidate([(6, 5, 4, 2, 1), (6, 8, 7, 1, 5), (12, 3, 1, 6, 4), (4, 7, 3, 5, 9)], 2) == [(4,), (7,), (1,), (3,)]
    assert candidate([(1, 3, 3, 2, 4), (7, 3, 6, 2, 3), (14, 2, 7, 8, 6), (2, 8, 5, 2, 9)], 5) == [(), (), (), ()]
    assert candidate([(4, 4, 7, 5, 4), (3, 7, 7, 3, 3), (12, 1, 4, 3, 7), (7, 9, 7, 1, 8)], 6) == [(), (), (), ()]
    assert candidate([(1, 1, 7, 5, 4), (8, 2, 9, 3, 5), (9, 1, 7, 2, 8), (3, 7, 2, 4, 8)], 5) == [(), (), (), ()]
    assert candidate([(7, 1, 2, 6, 1), (4, 6, 11, 1, 5), (7, 6, 7, 5, 3), (1, 7, 6, 1, 12)], 6) == [(), (), (), ()]
    assert candidate([(6, 6, 6, 1, 6), (8, 8, 10, 1, 4), (11, 3, 1, 4, 6), (1, 4, 3, 1, 2)], 6) == [(), (), (), ()]
    assert candidate([(1, 3, 1, 6, 1), (8, 6, 4, 1, 4), (12, 3, 2, 1, 4), (4, 8, 4, 5, 12)], 3) == [(), (), (), ()]
    assert candidate([(9, 6, 5, 3, 2), (2, 8, 5, 1, 1), (8, 5, 2, 8, 4), (5, 6, 6, 6, 11)], 1) == [(6, 5, 3), (8, 5, 1), (5, 2, 8), (6, 6, 6)]
    assert candidate([(4, 3, 1, 4, 2), (6, 5, 7, 6, 1), (10, 5, 2, 8, 5), (2, 3, 4, 1, 6)], 5) == [(), (), (), ()]
    assert candidate([(10, 8, 7, 6, 4), (2, 2, 8, 5, 4), (9, 4, 4, 2, 1), (5, 3, 3, 6, 5)], 6) == [(), (), (), ()]
    assert candidate([(7, 7, 1, 2, 5), (7, 3, 6, 6, 3), (11, 3, 5, 7, 3), (3, 12, 6, 4, 2)], 3) == [(), (), (), ()]
    assert candidate([(4, 5, 4, 6, 6), (4, 6, 7, 4, 3), (12, 2, 2, 1, 3), (9, 10, 1, 4, 6)], 1) == [(5, 4, 6), (6, 7, 4), (2, 2, 1), (10, 1, 4)]
    assert candidate([(6, 4, 6, 4, 6), (8, 6, 14, 4, 3), (6, 6, 1, 6, 9), (6, 5, 3, 4, 9)], 2) == [(6,), (14,), (1,), (3,)]
    assert candidate([(1, 1, 2, 6, 1), (8, 7, 12, 3, 1), (11, 2, 1, 2, 4), (9, 9, 6, 6, 7)], 7) == [(), (), (), ()]
    assert candidate([(4, 7, 4, 6, 5), (7, 2, 11, 4, 4), (5, 4, 4, 8, 5), (3, 7, 3, 6, 8)], 3) == [(), (), (), ()]
    assert candidate([(10, 2, 3, 3, 3), (5, 4, 5, 6, 2), (5, 5, 6, 1, 7), (7, 9, 3, 1, 11)], 6) == [(), (), (), ()]
    assert candidate([(10, 3, 7, 6, 6), (1, 7, 12, 1, 1), (8, 2, 1, 8, 10), (5, 4, 2, 1, 6)], 7) == [(), (), (), ()]
    assert candidate([(6, 8, 1, 4, 6), (5, 4, 8, 6, 1), (4, 5, 2, 5, 3), (8, 5, 2, 1, 10)], 6) == [(), (), (), ()]
    assert candidate([(7, 1, 6, 5, 3), (5, 1, 11, 4, 4), (14, 4, 6, 8, 4), (1, 9, 6, 4, 3)], 3) == [(), (), (), ()]
    assert candidate([(4, 4, 2, 3, 2), (3, 6, 5, 4, 6), (12, 5, 4, 1, 1), (7, 6, 3, 1, 5)], 4) == [(), (), (), ()]
    assert candidate([(3, 6, 7, 5, 4), (2, 8, 12, 4, 4), (9, 1, 7, 2, 6), (9, 11, 5, 6, 10)], 4) == [(), (), (), ()]
    assert candidate([(4, 8, 7, 2, 2), (7, 3, 12, 2, 1), (10, 5, 4, 4, 7), (7, 5, 3, 1, 4)], 6) == [(), (), (), ()]
    assert candidate([(3, 7, 1, 2, 2), (7, 6, 14, 2, 5), (6, 2, 3, 6, 2), (2, 10, 4, 2, 12)], 2) == [(1,), (14,), (3,), (4,)]
    assert candidate([(3, 4, 6, 3, 3), (3, 3, 8, 7, 2), (5, 2, 1, 2, 4), (9, 6, 5, 2, 9)], 4) == [(), (), (), ()]
    assert candidate([(7, 7, 6, 3, 5), (4, 3, 6, 7, 4), (11, 6, 6, 3, 2), (1, 11, 1, 6, 3)], 5) == [(), (), (), ()]
    assert candidate([(10, 3, 2, 1, 5), (1, 3, 7, 4, 1), (10, 6, 6, 1, 1), (4, 9, 2, 4, 11)], 5) == [(), (), (), ()]
    assert candidate([(9, 7, 1, 6, 7), (4, 6, 10, 3, 3), (10, 2, 3, 5, 3), (2, 9, 3, 5, 2)], 2) == [(1,), (10,), (3,), (3,)]
    assert candidate([(1, 5, 7, 1, 3), (7, 2, 9, 6, 2), (5, 2, 6, 5, 10), (7, 12, 2, 3, 7)], 4) == [(), (), (), ()]
    assert candidate([(1, 6, 7, 2, 8), (8, 2, 4, 1, 1), (6, 6, 2, 6, 4), (9, 12, 4, 2, 11)], 5) == [(), (), (), ()]
    assert candidate([(8, 3, 5, 1, 5), (3, 3, 7, 2, 5), (14, 6, 4, 4, 6), (3, 12, 1, 1, 11)], 2) == [(5,), (7,), (4,), (1,)]
    assert candidate([(9, 6, 1, 3, 7), (5, 4, 13, 6, 2), (13, 6, 5, 3, 2), (9, 5, 7, 5, 9)], 3) == [(), (), (), ()]
    assert candidate([(3, 1, 4, 4, 9), (5, 5, 6, 3, 2), (9, 5, 2, 8, 7), (9, 11, 7, 4, 11)], 4) == [(), (), (), ()]
    assert candidate([(8, 4, 3, 4, 3), (4, 8, 9, 5, 5), (13, 3, 4, 5, 1), (1, 4, 3, 6, 6)], 6) == [(), (), (), ()]
    assert candidate([(1, 4, 5, 5, 9), (4, 2, 13, 5, 5), (11, 4, 5, 4, 8), (2, 5, 5, 4, 3)], 4) == [(), (), (), ()]
    assert candidate([(8, 1, 3, 6, 6), (7, 2, 13, 6, 2), (10, 1, 6, 8, 3), (6, 9, 6, 5, 6)], 5) == [(), (), (), ()]
    assert candidate([(7, 6, 6, 1, 8), (3, 9, 9, 6, 3), (7, 2, 7, 7, 3), (2, 7, 4, 5, 9)], 5) == [(), (), (), ()]
    assert candidate([(6, 5, 7, 4, 1), (8, 7, 9, 6, 4), (7, 6, 6, 5, 6), (4, 9, 5, 5, 8)], 3) == [(), (), (), ()]
    assert candidate([(3, 3, 1, 2, 4), (3, 4, 13, 2, 4), (6, 6, 6, 3, 6), (7, 12, 2, 4, 9)], 3) == [(), (), (), ()]
    assert candidate([(1, 8, 6, 1, 8), (8, 3, 11, 2, 3), (10, 2, 2, 6, 6), (4, 8, 4, 6, 8)], 4) == [(), (), (), ()]
    assert candidate([(2, 4, 2, 1, 8), (8, 8, 9, 6, 5), (11, 6, 2, 4, 2), (4, 7, 1, 5, 7)], 4) == [(), (), (), ()]
    assert candidate([(10, 5, 1, 6, 6), (2, 3, 8, 7, 6), (10, 4, 5, 5, 6), (8, 6, 3, 5, 9)], 6) == [(), (), (), ()]
    assert candidate([(9, 6, 1, 4, 6), (2, 3, 8, 3, 5), (14, 1, 2, 7, 5), (2, 9, 4, 2, 7)], 3) == [(), (), (), ()]
    assert candidate([(5, 6, 6, 5, 4), (8, 2, 6, 4, 6), (8, 4, 2, 3, 9), (2, 13, 4, 4, 12)], 5) == [(), (), (), ()]
    assert candidate([(7, 2, 2, 5, 4), (5, 3, 8, 5, 4), (6, 6, 3, 7, 10), (7, 3, 2, 2, 7)], 2) == [(2,), (8,), (3,), (2,)]
    assert candidate([(6, 5, 1, 2, 5), (4, 9, 10, 2, 5), (8, 5, 6, 5, 8), (7, 8, 5, 2, 2)], 3) == [(), (), (), ()]
    assert candidate([(7, 6, 3, 4, 3), (8, 9, 11, 7, 1), (10, 6, 5, 2, 3), (2, 7, 6, 3, 7)], 5) == [(), (), (), ()]
    assert candidate([(9, 8, 5, 5, 9), (6, 9, 12, 1, 6), (13, 3, 3, 7, 6), (5, 3, 3, 1, 4)], 4) == [(), (), (), ()]
    assert candidate([(3, 7, 1, 4, 7), (7, 1, 11, 1, 2), (6, 2, 7, 1, 5), (6, 3, 5, 2, 6)], 4) == [(), (), (), ()]
    assert candidate([(4, 6, 6, 4, 5), (5, 1, 11, 5, 2), (8, 6, 2, 3, 1), (6, 6, 1, 2, 9)], 1) == [(6, 6, 4), (1, 11, 5), (6, 2, 3), (6, 1, 2)]
    assert candidate([(3, 4, 7, 2, 9), (3, 6, 5, 1, 5), (6, 4, 2, 2, 6), (4, 8, 5, 3, 2)], 3) == [(), (), (), ()]
    assert candidate([(8, 8, 1, 6, 9), (8, 4, 4, 2, 6), (4, 2, 1, 5, 4), (7, 11, 2, 4, 7)], 3) == [(), (), (), ()]
    assert candidate([(5, 6, 1, 3, 3), (1, 8, 11, 5, 4), (11, 2, 4, 5, 7), (3, 6, 4, 2, 12)], 1) == [(6, 1, 3), (8, 11, 5), (2, 4, 5), (6, 4, 2)]
    assert candidate([(4, 5, 1, 4, 4), (4, 5, 10, 6, 1), (12, 5, 1, 1, 8), (9, 5, 6, 5, 8)], 1) == [(5, 1, 4), (5, 10, 6), (5, 1, 1), (5, 6, 5)]
    assert candidate([(2, 7, 2, 4, 5), (3, 1, 6, 7, 1), (7, 2, 6, 2, 5), (2, 4, 4, 6, 5)], 6) == [(), (), (), ()]
    assert candidate([(5, 1, 4, 6, 3), (4, 5, 6, 6, 4), (11, 1, 5, 1, 5), (3, 10, 6, 6, 6)], 6) == [(), (), (), ()]
    assert candidate([(12, 7, 7, 11), (10, 12, 13, 8), (7, 1, 4, 5), (5, 3, 5, 4)], 1) == [(7, 7), (12, 13), (1, 4), (3, 5)]
    assert candidate([(9, 8, 3, 11), (9, 3, 13, 5), (9, 5, 3, 9), (6, 3, 12, 2)], 4) == [(), (), (), ()]
    assert candidate([(10, 3, 2, 5), (10, 8, 7, 7), (7, 3, 7, 9), (4, 4, 13, 3)], 1) == [(3, 2), (8, 7), (3, 7), (4, 13)]
    assert candidate([(8, 9, 3, 8), (8, 4, 13, 5), (3, 6, 5, 4), (7, 6, 10, 3)], 1) == [(9, 3), (4, 13), (6, 5), (6, 10)]
    assert candidate([(3, 6, 5, 13), (10, 3, 12, 9), (7, 1, 2, 3), (2, 7, 4, 2)], 2) == [(), (), (), ()]
    assert candidate([(6, 11, 8, 7), (10, 12, 8, 2), (5, 2, 11, 3), (6, 4, 14, 2)], 1) == [(11, 8), (12, 8), (2, 11), (4, 14)]
    assert candidate([(12, 5, 7, 12), (16, 8, 13, 9), (4, 1, 8, 6), (7, 1, 12, 4)], 5) == [(), (), (), ()]
    assert candidate([(5, 8, 2, 8), (6, 12, 10, 7), (8, 4, 7, 12), (6, 5, 12, 4)], 5) == [(), (), (), ()]
    assert candidate([(9, 12, 1, 6), (16, 11, 15, 8), (3, 1, 4, 10), (4, 6, 9, 6)], 5) == [(), (), (), ()]
    assert candidate([(8, 10, 9, 8), (8, 10, 12, 4), (8, 6, 10, 7), (4, 10, 8, 4)], 2) == [(), (), (), ()]
    assert candidate([(4, 4, 8, 14), (13, 11, 14, 1), (9, 6, 4, 9), (2, 6, 13, 3)], 3) == [(), (), (), ()]
    assert candidate([(12, 13, 2, 8), (10, 5, 17, 1), (3, 2, 4, 9), (8, 10, 11, 3)], 5) == [(), (), (), ()]
    assert candidate([(4, 11, 3, 5), (6, 9, 14, 6), (8, 5, 7, 13), (3, 7, 6, 5)], 6) == [(), (), (), ()]
    assert candidate([(8, 7, 7, 11), (8, 11, 9, 3), (6, 2, 5, 13), (2, 8, 4, 4)], 1) == [(7, 7), (11, 9), (2, 5), (8, 4)]
    assert candidate([(5, 10, 9, 11), (10, 13, 17, 2), (2, 4, 7, 4), (1, 1, 5, 12)], 2) == [(), (), (), ()]
    assert candidate([(6, 5, 8, 11), (16, 11, 10, 9), (2, 4, 6, 8), (6, 1, 4, 11)], 5) == [(), (), (), ()]
    assert candidate([(5, 8, 4, 11), (12, 13, 9, 6), (1, 1, 4, 7), (5, 2, 8, 9)], 1) == [(8, 4), (13, 9), (1, 4), (2, 8)]
    assert candidate([(8, 12, 2, 10), (10, 8, 12, 3), (2, 5, 3, 6), (7, 3, 6, 2)], 4) == [(), (), (), ()]
    assert candidate([(12, 12, 2, 4), (11, 3, 17, 7), (9, 4, 12, 10), (3, 11, 5, 3)], 6) == [(), (), (), ()]
    assert candidate([(7, 13, 7, 4), (7, 13, 17, 1), (5, 5, 4, 7), (4, 3, 12, 6)], 6) == [(), (), (), ()]
    assert candidate([(7, 8, 4, 12), (12, 3, 12, 4), (9, 5, 8, 6), (6, 8, 9, 2)], 2) == [(), (), (), ()]
    assert candidate([(6, 3, 6, 14), (9, 13, 10, 8), (1, 3, 6, 11), (1, 9, 13, 12)], 6) == [(), (), (), ()]
    assert candidate([(6, 8, 7, 5), (10, 8, 12, 8), (7, 1, 9, 8), (8, 4, 6, 8)], 4) == [(), (), (), ()]
    assert candidate([(2, 6, 7, 8), (9, 9, 9, 1), (8, 1, 11, 5), (3, 8, 5, 12)], 4) == [(), (), (), ()]
    assert candidate([(4, 12, 6, 11), (7, 3, 12, 2), (8, 4, 3, 11), (4, 6, 11, 8)], 4) == [(), (), (), ()]
    assert candidate([(2, 9, 5, 14), (9, 10, 9, 5), (2, 1, 8, 10), (1, 6, 7, 2)], 6) == [(), (), (), ()]
    assert candidate([(7, 12, 2, 9), (15, 3, 17, 4), (3, 1, 8, 9), (8, 4, 14, 10)], 2) == [(), (), (), ()]
    assert candidate([(3, 12, 7, 9), (6, 9, 10, 1), (7, 6, 9, 6), (1, 1, 7, 10)], 3) == [(), (), (), ()]
    assert candidate([(2, 3, 4, 7), (9, 4, 15, 1), (9, 5, 8, 12), (6, 9, 12, 9)], 4) == [(), (), (), ()]
    assert candidate([(3, 6, 8, 9), (10, 3, 12, 1), (6, 4, 4, 3), (4, 4, 6, 7)], 2) == [(), (), (), ()]
    assert candidate([(12, 8, 1, 8), (9, 3, 7, 3), (9, 5, 9, 9), (1, 6, 8, 5)], 1) == [(8, 1), (3, 7), (5, 9), (6, 8)]
    assert candidate([(11, 13, 6, 14), (13, 3, 13, 5), (2, 3, 10, 5), (8, 3, 14, 12)], 4) == [(), (), (), ()]
    assert candidate([(11, 11, 3, 7), (7, 9, 8, 3), (7, 6, 8, 9), (3, 4, 13, 10)], 4) == [(), (), (), ()]

if __name__ == '__main__':
    check(trim_tuple)