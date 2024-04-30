from case_MBPP_305 import sum_average


def check(candidate):
    assert candidate(10)==(55, 5.5)
    assert candidate(15)==(120, 8.0)
    assert candidate(20)==(210, 10.5)

if __name__ == '__main__':
    check(sum_average)