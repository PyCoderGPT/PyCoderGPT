from case_MBPP_137 import dog_age


def check(candidate):
    assert candidate(12)==61
    assert candidate(15)==73
    assert candidate(24)==109

if __name__ == '__main__':
    check(dog_age)