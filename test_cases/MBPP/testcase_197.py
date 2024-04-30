from case_MBPP_197 import rearrange_bigger


def check(candidate):
    assert candidate(12)==21
    assert candidate(10)==False
    assert candidate(102)==120

if __name__ == '__main__':
    check(rearrange_bigger)