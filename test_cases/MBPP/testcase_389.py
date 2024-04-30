from case_MBPP_389 import Diff


def check(candidate):
    assert (candidate([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
    assert (candidate([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]
    assert (candidate([1,2,3], [6,7,1])) == [2,3,6,7]

if __name__ == '__main__':
    check(Diff)