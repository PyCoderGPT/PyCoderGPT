from case_MBPP_196 import find_Parity


def check(candidate):
    assert candidate(12) == False
    assert candidate(7) == True
    assert candidate(10) == False

if __name__ == '__main__':
    check(find_Parity)