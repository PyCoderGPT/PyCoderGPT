from case_MBPP_023 import recursive_list_sum


def check(candidate):
    assert candidate(([1, 2, [3,4],[5,6]]))==21
    assert candidate(([7, 10, [15,14],[19,41]]))==106
    assert candidate(([10, 20, [30,40],[50,60]]))==210

if __name__ == '__main__':
    check(recursive_list_sum)