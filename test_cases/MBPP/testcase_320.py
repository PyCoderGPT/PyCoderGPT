from case_MBPP_320 import min_Jumps


def check(candidate):
    assert candidate((3,4),11)==3.5
    assert candidate((3,4),0)==0
    assert candidate((11,14),11)==1

if __name__ == '__main__':
    check(min_Jumps)