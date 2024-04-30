from case_MBPP_101 import perimeter_pentagon


def check(candidate):
    assert candidate(5) == 25
    assert candidate(10) == 50
    assert candidate(15) == 75

if __name__ == '__main__':
    check(perimeter_pentagon)