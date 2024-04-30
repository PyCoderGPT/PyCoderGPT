from case_MBPP_362 import tuple_to_dict


def check(candidate):
    assert candidate((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
    assert candidate((1, 2, 3, 4, 5, 6)) == {1: 2, 3: 4, 5: 6}
    assert candidate((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}

if __name__ == '__main__':
    check(tuple_to_dict)