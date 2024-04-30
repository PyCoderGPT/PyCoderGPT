from case_MBPP_030 import dif_Square


def check(candidate):
    assert candidate(5) == True
    assert candidate(10) == False
    assert candidate(15) == True

if __name__ == '__main__':
    check(dif_Square)