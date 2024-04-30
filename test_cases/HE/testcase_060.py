from case_HE_060 import sum_to_n


def check(candidate):
    assert candidate(1) == 1
    assert candidate(6) == 21
    assert candidate(11) == 66
    assert candidate(30) == 465
    assert candidate(100) == 5050


if __name__ == '__main__':
    check(sum_to_n)