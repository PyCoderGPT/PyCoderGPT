from case_MBPP_086 import extract_singly


def check(candidate):
    assert candidate([(3, 4, 5), (4, 5, 7), (1, 4)]) == [3, 4, 5, 7, 1]
    assert candidate([(1, 2, 3), (4, 2, 3), (7, 8)]) == [1, 2, 3, 4, 7, 8]
    assert candidate([(7, 8, 9), (10, 11, 12), (10, 11)]) == [7, 8, 9, 10, 11, 12]
    assert candidate([(3, 7, 5), (7, 7, 9), (5, 2)]) == [3, 7, 5, 9, 2]
    assert candidate([(3, 9, 6), (1, 6, 6), (4, 3)]) == [3, 9, 6, 1, 4]
    assert candidate([(1, 7, 2), (5, 10, 5), (2, 6)]) == [1, 7, 2, 5, 10, 6]
    assert candidate([(6, 8, 9), (5, 8, 11), (4, 1)]) == [6, 8, 9, 5, 11, 4, 1]
    assert candidate([(6, 9, 4), (3, 9, 10), (3, 3)]) == [6, 9, 4, 3, 10]
    assert candidate([(2, 4, 9), (1, 3, 12), (2, 5)]) == [2, 4, 9, 1, 3, 12, 5]
    assert candidate([(8, 9, 4), (4, 6, 2), (2, 6)]) == [8, 9, 4, 6, 2]
    assert candidate([(6, 4, 2), (2, 5, 12), (5, 8)]) == [6, 4, 2, 5, 12, 8]
    assert candidate([(2, 6, 6), (3, 4, 2), (3, 4)]) == [2, 6, 3, 4]
    assert candidate([(4, 6, 5), (8, 3, 5), (6, 9)]) == [4, 6, 5, 8, 3, 9]
    assert candidate([(3, 9, 1), (4, 7, 7), (6, 4)]) == [3, 9, 1, 4, 7, 6]
    assert candidate([(4, 9, 2), (6, 8, 5), (5, 1)]) == [4, 9, 2, 6, 8, 5, 1]
    assert candidate([(6, 8, 10), (5, 5, 7), (4, 9)]) == [6, 8, 10, 5, 7, 4, 9]
    assert candidate([(8, 1, 5), (8, 9, 6), (2, 6)]) == [8, 1, 5, 9, 6, 2]
    assert candidate([(6, 1, 1), (9, 8, 6), (1, 7)]) == [6, 1, 9, 8, 7]
    assert candidate([(4, 5, 5), (8, 10, 2), (5, 6)]) == [4, 5, 8, 10, 2, 6]
    assert candidate([(6, 2, 8), (8, 5, 8), (6, 7)]) == [6, 2, 8, 5, 7]
    assert candidate([(5, 8, 9), (2, 3, 6), (5, 6)]) == [5, 8, 9, 2, 3, 6]
    assert candidate([(7, 4, 1), (6, 3, 11), (2, 1)]) == [7, 4, 1, 6, 3, 11, 2]
    assert candidate([(1, 4, 2), (8, 8, 3), (4, 6)]) == [1, 4, 2, 8, 3, 6]
    assert candidate([(3, 1, 2), (2, 3, 10), (5, 5)]) == [3, 1, 2, 10, 5]
    assert candidate([(6, 5, 10), (7, 3, 12), (4, 1)]) == [6, 5, 10, 7, 3, 12, 4, 1]
    assert candidate([(2, 6, 8), (9, 5, 4), (1, 5)]) == [2, 6, 8, 9, 5, 4, 1]
    assert candidate([(4, 5, 2), (1, 1, 11), (4, 1)]) == [4, 5, 2, 1, 11]
    assert candidate([(2, 4, 7), (7, 9, 4), (6, 3)]) == [2, 4, 7, 9, 6, 3]
    assert candidate([(4, 8, 7), (5, 10, 11), (3, 2)]) == [4, 8, 7, 5, 10, 11, 3, 2]
    assert candidate([(5, 4, 10), (7, 3, 11), (4, 4)]) == [5, 4, 10, 7, 3, 11]
    assert candidate([(6, 5, 2), (8, 10, 5), (1, 1)]) == [6, 5, 2, 8, 10, 1]
    assert candidate([(5, 5, 10), (5, 3, 11), (3, 9)]) == [5, 10, 3, 11, 9]
    assert candidate([(2, 5, 9), (7, 5, 6), (3, 6)]) == [2, 5, 9, 7, 6, 3]
    assert candidate([(2, 6, 5), (8, 2, 11), (6, 1)]) == [2, 6, 5, 8, 11, 1]
    assert candidate([(1, 2, 10), (4, 2, 5), (3, 2)]) == [1, 2, 10, 4, 5, 3]
    assert candidate([(8, 1, 10), (8, 3, 2), (1, 3)]) == [8, 1, 10, 3, 2]
    assert candidate([(3, 7, 4), (1, 1, 5), (5, 5)]) == [3, 7, 4, 1, 5]
    assert candidate([(6, 7, 1), (6, 5, 3), (11, 3)]) == [6, 7, 1, 5, 3, 11]
    assert candidate([(1, 7, 4), (2, 2, 7), (2, 7)]) == [1, 7, 4, 2]
    assert candidate([(4, 2, 3), (3, 7, 7), (2, 5)]) == [4, 2, 3, 7, 5]
    assert candidate([(5, 6, 1), (7, 4, 3), (6, 4)]) == [5, 6, 1, 7, 4, 3]
    assert candidate([(4, 1, 4), (8, 2, 5), (10, 12)]) == [4, 1, 8, 2, 5, 10, 12]
    assert candidate([(6, 1, 2), (8, 2, 5), (4, 9)]) == [6, 1, 2, 8, 5, 4, 9]
    assert candidate([(1, 5, 3), (9, 2, 6), (10, 4)]) == [1, 5, 3, 9, 2, 6, 10, 4]
    assert candidate([(4, 3, 8), (6, 1, 6), (12, 12)]) == [4, 3, 8, 6, 1, 12]
    assert candidate([(4, 7, 5), (9, 5, 3), (11, 11)]) == [4, 7, 5, 9, 3, 11]
    assert candidate([(5, 3, 6), (4, 6, 3), (2, 7)]) == [5, 3, 6, 4, 2, 7]
    assert candidate([(5, 1, 8), (1, 7, 8), (7, 9)]) == [5, 1, 8, 7, 9]
    assert candidate([(4, 7, 1), (3, 2, 1), (11, 3)]) == [4, 7, 1, 3, 2, 11]
    assert candidate([(6, 3, 6), (1, 2, 2), (8, 9)]) == [6, 3, 1, 2, 8, 9]
    assert candidate([(5, 1, 4), (5, 3, 1), (2, 9)]) == [5, 1, 4, 3, 2, 9]
    assert candidate([(2, 2, 2), (6, 5, 8), (12, 3)]) == [2, 6, 5, 8, 12, 3]
    assert candidate([(5, 4, 3), (1, 5, 2), (12, 5)]) == [5, 4, 3, 1, 2, 12]
    assert candidate([(4, 3, 4), (7, 2, 3), (8, 10)]) == [4, 3, 7, 2, 8, 10]
    assert candidate([(3, 3, 4), (4, 1, 4), (4, 9)]) == [3, 4, 1, 9]
    assert candidate([(5, 4, 3), (3, 5, 1), (3, 10)]) == [5, 4, 3, 1, 10]
    assert candidate([(3, 7, 1), (6, 4, 8), (8, 8)]) == [3, 7, 1, 6, 4, 8]
    assert candidate([(6, 3, 8), (3, 1, 1), (9, 13)]) == [6, 3, 8, 1, 9, 13]
    assert candidate([(6, 2, 1), (2, 3, 6), (4, 13)]) == [6, 2, 1, 3, 4, 13]
    assert candidate([(3, 7, 2), (8, 4, 1), (2, 10)]) == [3, 7, 2, 8, 4, 1, 10]
    assert candidate([(5, 7, 4), (4, 7, 1), (11, 5)]) == [5, 7, 4, 1, 11]
    assert candidate([(3, 3, 3), (4, 1, 7), (8, 12)]) == [3, 4, 1, 7, 8, 12]
    assert candidate([(3, 5, 7), (6, 1, 8), (4, 7)]) == [3, 5, 7, 6, 1, 8, 4]
    assert candidate([(2, 2, 2), (6, 4, 8), (12, 6)]) == [2, 6, 4, 8, 12]
    assert candidate([(1, 2, 3), (8, 2, 7), (6, 4)]) == [1, 2, 3, 8, 7, 6, 4]
    assert candidate([(5, 4, 1), (9, 6, 3), (6, 3)]) == [5, 4, 1, 9, 6, 3]
    assert candidate([(6, 3, 4), (3, 1, 4), (6, 6)]) == [6, 3, 4, 1]
    assert candidate([(1, 4, 1), (6, 3, 2), (10, 3)]) == [1, 4, 6, 3, 2, 10]
    assert candidate([(2, 5, 7), (3, 2, 8), (12, 7)]) == [2, 5, 7, 3, 8, 12]
    assert candidate([(6, 3, 8), (7, 9, 7), (10, 12)]) == [6, 3, 8, 7, 9, 10, 12]
    assert candidate([(7, 9, 7), (13, 11, 8), (14, 6)]) == [7, 9, 13, 11, 8, 14, 6]
    assert candidate([(3, 7, 11), (11, 14, 8), (11, 8)]) == [3, 7, 11, 14, 8]
    assert candidate([(12, 12, 5), (15, 14, 13), (15, 13)]) == [12, 5, 15, 14, 13]
    assert candidate([(6, 7, 13), (5, 12, 10), (14, 7)]) == [6, 7, 13, 5, 12, 10, 14]
    assert candidate([(10, 10, 4), (14, 6, 8), (9, 9)]) == [10, 4, 14, 6, 8, 9]
    assert candidate([(3, 11, 9), (12, 10, 12), (5, 16)]) == [3, 11, 9, 12, 10, 5, 16]
    assert candidate([(4, 11, 10), (8, 10, 12), (14, 8)]) == [4, 11, 10, 8, 12, 14]
    assert candidate([(5, 11, 9), (13, 15, 8), (9, 13)]) == [5, 11, 9, 13, 15, 8]
    assert candidate([(7, 8, 5), (8, 14, 12), (13, 9)]) == [7, 8, 5, 14, 12, 13, 9]
    assert candidate([(5, 13, 10), (7, 11, 13), (5, 7)]) == [5, 13, 10, 7, 11]
    assert candidate([(12, 4, 12), (7, 16, 8), (7, 12)]) == [12, 4, 7, 16, 8]
    assert candidate([(9, 10, 6), (7, 7, 8), (14, 16)]) == [9, 10, 6, 7, 8, 14, 16]
    assert candidate([(3, 3, 9), (6, 8, 13), (7, 14)]) == [3, 9, 6, 8, 13, 7, 14]
    assert candidate([(9, 7, 6), (9, 8, 9), (8, 6)]) == [9, 7, 6, 8]
    assert candidate([(9, 13, 4), (13, 6, 15), (11, 13)]) == [9, 13, 4, 6, 15, 11]
    assert candidate([(10, 4, 10), (7, 14, 9), (10, 15)]) == [10, 4, 7, 14, 9, 15]
    assert candidate([(7, 11, 9), (10, 9, 15), (8, 12)]) == [7, 11, 9, 10, 15, 8, 12]
    assert candidate([(8, 7, 10), (8, 10, 13), (6, 7)]) == [8, 7, 10, 13, 6]
    assert candidate([(6, 8, 9), (7, 15, 11), (5, 12)]) == [6, 8, 9, 7, 15, 11, 5, 12]
    assert candidate([(4, 7, 7), (8, 13, 17), (11, 13)]) == [4, 7, 8, 13, 17, 11]
    assert candidate([(8, 7, 14), (8, 14, 7), (15, 7)]) == [8, 7, 14, 15]
    assert candidate([(7, 7, 11), (13, 16, 9), (15, 7)]) == [7, 11, 13, 16, 9, 15]
    assert candidate([(5, 8, 13), (12, 16, 9), (10, 6)]) == [5, 8, 13, 12, 16, 9, 10, 6]
    assert candidate([(9, 3, 5), (11, 12, 8), (9, 8)]) == [9, 3, 5, 11, 12, 8]
    assert candidate([(11, 12, 10), (13, 9, 12), (5, 15)]) == [11, 12, 10, 13, 9, 5, 15]
    assert candidate([(4, 6, 14), (6, 8, 10), (11, 11)]) == [4, 6, 14, 8, 10, 11]
    assert candidate([(10, 6, 7), (8, 13, 16), (14, 13)]) == [10, 6, 7, 8, 13, 16, 14]
    assert candidate([(12, 12, 5), (6, 14, 15), (9, 16)]) == [12, 5, 6, 14, 15, 9, 16]
    assert candidate([(5, 5, 6), (14, 7, 7), (9, 13)]) == [5, 6, 14, 7, 9, 13]
    assert candidate([(11, 8, 8), (13, 12, 15), (12, 6)]) == [11, 8, 13, 12, 15, 6]
    assert candidate([(9, 3, 5), (12, 13, 15), (8, 14)]) == [9, 3, 5, 12, 13, 15, 8, 14]
    assert candidate([(7, 4, 5), (7, 14, 10), (14, 7)]) == [7, 4, 5, 14, 10]

if __name__ == '__main__':
    check(extract_singly)