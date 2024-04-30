from case_MBPP_224 import neg_nos


def check(candidate):
    assert candidate([-1,4,5,-6]) == [-1,-6]
    assert candidate([-1,-2,3,4]) == [-1,-2]
    assert candidate([-7,-6,8,9]) == [-7,-6]

if __name__ == '__main__':
    check(neg_nos)