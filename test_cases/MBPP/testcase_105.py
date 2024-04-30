from case_MBPP_105 import count_Set_Bits


def check(candidate):
    assert candidate(2) == 1
    assert candidate(4) == 1
    assert candidate(6) == 2

if __name__ == '__main__':
    check(count_Set_Bits)