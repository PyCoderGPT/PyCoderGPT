from case_MBPP_136 import split_two_parts


def check(candidate):
    assert candidate([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
    assert candidate(['a', 'b', 'c', 'd'],2)==(['a', 'b'], ['c', 'd'])
    assert candidate(['p', 'y', 't', 'h', 'o', 'n'],4)==(['p', 'y', 't', 'h'], ['o', 'n'])

if __name__ == '__main__':
    check(split_two_parts)