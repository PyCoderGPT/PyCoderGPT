from case_MBPP_211 import find_Average_Of_Cube


def check(candidate):
    assert candidate(2) == 4.5
    assert candidate(3) == 12
    assert candidate(1) == 1

if __name__ == '__main__':
    check(find_Average_Of_Cube)