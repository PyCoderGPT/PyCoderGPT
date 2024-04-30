from case_MBPP_362 import tuple_to_dict


def check(candidate):
    assert candidate((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
    assert candidate((1, 2, 3, 4, 5, 6)) == {1: 2, 3: 4, 5: 6}
    assert candidate((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}
    assert candidate((4, 6, 9, 6, 8, 1)) == {4: 6, 9: 6, 8: 1}
    assert candidate((2, 10, 11, 5, 14, 4)) == {2: 10, 11: 5, 14: 4}
    assert candidate((5, 8, 10, 8, 10, 1)) == {5: 8, 10: 1}
    assert candidate((3, 1, 5, 5, 13, 3)) == {3: 1, 5: 5, 13: 3}
    assert candidate((5, 1, 6, 10, 18, 3)) == {5: 1, 6: 10, 18: 3}
    assert candidate((5, 3, 6, 8, 9, 10)) == {5: 3, 6: 8, 9: 10}
    assert candidate((2, 3, 4, 11, 8, 2)) == {2: 3, 4: 11, 8: 2}
    assert candidate((3, 9, 2, 15, 10, 2)) == {3: 9, 2: 15, 10: 2}
    assert candidate((1, 7, 3, 7, 16, 2)) == {1: 7, 3: 7, 16: 2}
    assert candidate((1, 9, 11, 12, 11, 8)) == {1: 9, 11: 8}
    assert candidate((2, 7, 11, 11, 14, 1)) == {2: 7, 11: 11, 14: 1}
    assert candidate((4, 7, 9, 7, 18, 9)) == {4: 7, 9: 7, 18: 9}
    assert candidate((6, 8, 4, 5, 11, 4)) == {6: 8, 4: 5, 11: 4}
    assert candidate((1, 6, 6, 7, 14, 1)) == {1: 6, 6: 7, 14: 1}
    assert candidate((6, 1, 7, 9, 12, 6)) == {6: 1, 7: 9, 12: 6}
    assert candidate((6, 5, 5, 13, 9, 6)) == {6: 5, 5: 13, 9: 6}
    assert candidate((6, 7, 2, 13, 18, 8)) == {6: 7, 2: 13, 18: 8}
    assert candidate((1, 1, 6, 9, 11, 3)) == {1: 1, 6: 9, 11: 3}
    assert candidate((5, 8, 9, 9, 13, 7)) == {5: 8, 9: 9, 13: 7}
    assert candidate((4, 3, 3, 10, 13, 8)) == {4: 3, 3: 10, 13: 8}
    assert candidate((2, 6, 3, 9, 18, 6)) == {2: 6, 3: 9, 18: 6}
    assert candidate((2, 7, 6, 14, 12, 4)) == {2: 7, 6: 14, 12: 4}
    assert candidate((5, 5, 12, 8, 13, 9)) == {5: 5, 12: 8, 13: 9}
    assert candidate((6, 8, 4, 6, 11, 5)) == {6: 8, 4: 6, 11: 5}
    assert candidate((5, 4, 10, 9, 16, 5)) == {5: 4, 10: 9, 16: 5}
    assert candidate((5, 5, 11, 11, 14, 2)) == {5: 5, 11: 11, 14: 2}
    assert candidate((6, 5, 4, 12, 13, 1)) == {6: 5, 4: 12, 13: 1}
    assert candidate((2, 2, 2, 9, 11, 5)) == {2: 9, 11: 5}
    assert candidate((4, 3, 10, 5, 17, 3)) == {4: 3, 10: 5, 17: 3}
    assert candidate((3, 9, 7, 11, 12, 1)) == {3: 9, 7: 11, 12: 1}
    assert candidate((5, 8, 4, 15, 12, 3)) == {5: 8, 4: 15, 12: 3}
    assert candidate((3, 4, 6, 14, 13, 7)) == {3: 4, 6: 14, 13: 7}
    assert candidate((4, 1, 8, 5, 12, 9)) == {4: 1, 8: 5, 12: 9}
    assert candidate((4, 5, 4, 5, 5, 3)) == {4: 5, 5: 3}
    assert candidate((2, 3, 3, 6, 9, 11)) == {2: 3, 3: 6, 9: 11}
    assert candidate((4, 1, 2, 8, 6, 5)) == {4: 1, 2: 8, 6: 5}
    assert candidate((6, 6, 5, 1, 2, 6)) == {6: 6, 5: 1, 2: 6}
    assert candidate((1, 5, 1, 9, 2, 5)) == {1: 9, 2: 5}
    assert candidate((1, 4, 1, 9, 10, 1)) == {1: 9, 10: 1}
    assert candidate((5, 2, 2, 8, 9, 1)) == {5: 2, 2: 8, 9: 1}
    assert candidate((1, 6, 3, 5, 4, 6)) == {1: 6, 3: 5, 4: 6}
    assert candidate((6, 3, 5, 2, 5, 2)) == {6: 3, 5: 2}
    assert candidate((1, 3, 2, 2, 1, 9)) == {1: 9, 2: 2}
    assert candidate((6, 7, 1, 2, 9, 10)) == {6: 7, 1: 2, 9: 10}
    assert candidate((6, 7, 6, 8, 10, 1)) == {6: 8, 10: 1}
    assert candidate((5, 2, 4, 6, 4, 11)) == {5: 2, 4: 11}
    assert candidate((1, 6, 8, 2, 4, 1)) == {1: 6, 8: 2, 4: 1}
    assert candidate((3, 2, 8, 8, 9, 2)) == {3: 2, 8: 8, 9: 2}
    assert candidate((1, 5, 6, 3, 4, 6)) == {1: 5, 6: 3, 4: 6}
    assert candidate((2, 3, 7, 1, 1, 8)) == {2: 3, 7: 1, 1: 8}
    assert candidate((1, 3, 5, 5, 1, 7)) == {1: 7, 5: 5}
    assert candidate((1, 1, 4, 2, 4, 1)) == {1: 1, 4: 1}
    assert candidate((3, 7, 1, 2, 7, 9)) == {3: 7, 1: 2, 7: 9}
    assert candidate((4, 6, 2, 1, 1, 10)) == {4: 6, 2: 1, 1: 10}
    assert candidate((4, 4, 5, 3, 4, 1)) == {4: 1, 5: 3}
    assert candidate((5, 7, 4, 3, 2, 7)) == {5: 7, 4: 3, 2: 7}
    assert candidate((4, 4, 5, 3, 4, 5)) == {4: 5, 5: 3}
    assert candidate((4, 2, 8, 8, 9, 11)) == {4: 2, 8: 8, 9: 11}
    assert candidate((3, 2, 7, 8, 10, 8)) == {3: 2, 7: 8, 10: 8}
    assert candidate((6, 5, 3, 7, 5, 7)) == {6: 5, 3: 7, 5: 7}
    assert candidate((4, 2, 4, 6, 2, 9)) == {4: 6, 2: 9}
    assert candidate((6, 6, 8, 8, 1, 9)) == {6: 6, 8: 8, 1: 9}
    assert candidate((6, 5, 6, 5, 6, 7)) == {6: 7}
    assert candidate((1, 2, 5, 6, 8, 6)) == {1: 2, 5: 6, 8: 6}
    assert candidate((4, 3, 8, 6, 4, 4)) == {4: 4, 8: 6}
    assert candidate((4, 2, 8, 4, 10, 3)) == {4: 2, 8: 4, 10: 3}
    assert candidate((3, 8, 14, 10, 6, 11)) == {3: 8, 14: 10, 6: 11}
    assert candidate((3, 3, 11, 14, 9, 16)) == {3: 3, 11: 14, 9: 16}
    assert candidate((10, 3, 12, 14, 10, 10)) == {10: 10, 12: 14}
    assert candidate((8, 5, 11, 12, 14, 11)) == {8: 5, 11: 12, 14: 11}
    assert candidate((7, 4, 4, 7, 11, 17)) == {7: 4, 4: 7, 11: 17}
    assert candidate((2, 3, 8, 12, 6, 13)) == {2: 3, 8: 12, 6: 13}
    assert candidate((7, 5, 4, 9, 7, 13)) == {7: 13, 4: 9}
    assert candidate((8, 7, 8, 12, 6, 15)) == {8: 12, 6: 15}
    assert candidate((2, 3, 14, 14, 9, 12)) == {2: 3, 14: 14, 9: 12}
    assert candidate((9, 5, 4, 6, 9, 10)) == {9: 10, 4: 6}
    assert candidate((6, 3, 4, 7, 8, 8)) == {6: 3, 4: 7, 8: 8}
    assert candidate((7, 4, 5, 14, 15, 11)) == {7: 4, 5: 14, 15: 11}
    assert candidate((7, 13, 4, 13, 13, 14)) == {7: 13, 4: 13, 13: 14}
    assert candidate((10, 8, 4, 6, 16, 12)) == {10: 8, 4: 6, 16: 12}
    assert candidate((9, 8, 9, 11, 10, 15)) == {9: 11, 10: 15}
    assert candidate((12, 12, 4, 12, 16, 9)) == {12: 12, 4: 12, 16: 9}
    assert candidate((3, 6, 11, 9, 8, 17)) == {3: 6, 11: 9, 8: 17}
    assert candidate((12, 12, 14, 9, 6, 8)) == {12: 12, 14: 9, 6: 8}
    assert candidate((8, 3, 5, 5, 12, 10)) == {8: 3, 5: 5, 12: 10}
    assert candidate((11, 11, 5, 5, 7, 10)) == {11: 11, 5: 5, 7: 10}
    assert candidate((4, 13, 10, 12, 13, 7)) == {4: 13, 10: 12, 13: 7}
    assert candidate((2, 5, 6, 10, 15, 15)) == {2: 5, 6: 10, 15: 15}
    assert candidate((4, 4, 7, 11, 8, 17)) == {4: 4, 7: 11, 8: 17}
    assert candidate((9, 8, 12, 14, 15, 8)) == {9: 8, 12: 14, 15: 8}
    assert candidate((10, 10, 11, 6, 16, 13)) == {10: 10, 11: 6, 16: 13}
    assert candidate((9, 8, 8, 7, 11, 14)) == {9: 8, 8: 7, 11: 14}
    assert candidate((10, 4, 9, 12, 15, 14)) == {10: 4, 9: 12, 15: 14}
    assert candidate((10, 9, 6, 12, 6, 13)) == {10: 9, 6: 13}
    assert candidate((9, 4, 5, 13, 6, 13)) == {9: 4, 5: 13, 6: 13}
    assert candidate((11, 5, 5, 13, 6, 14)) == {11: 5, 5: 13, 6: 14}
    assert candidate((2, 13, 4, 15, 15, 14)) == {2: 13, 4: 15, 15: 14}
    assert candidate((9, 9, 8, 8, 13, 14)) == {9: 9, 8: 8, 13: 14}
    assert candidate((5, 4, 13, 8, 7, 7)) == {5: 4, 13: 8, 7: 7}

if __name__ == '__main__':
    check(tuple_to_dict)