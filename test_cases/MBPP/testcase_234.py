from case_MBPP_234 import count_Occurrence


def check(candidate):
    assert candidate(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
    assert candidate((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6
    assert candidate((1,2,3,4,5,6),[1,2]) == 2

if __name__ == '__main__':
    check(count_Occurrence)