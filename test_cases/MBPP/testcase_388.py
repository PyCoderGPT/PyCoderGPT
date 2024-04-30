from case_MBPP_388 import get_pairs_count


def check(candidate):
    assert candidate([1,1,1,1],2) == 6
    assert candidate([1,5,7,-1,5],6) == 3
    assert candidate([1,-2,3],1) == 1
    assert candidate([-1,-2,3],-3) == 1

if __name__ == '__main__':
    check(get_pairs_count)