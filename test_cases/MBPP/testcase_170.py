from case_MBPP_170 import dict_depth


def check(candidate):
    assert candidate({'a':1, 'b': {'c': {'d': {}}}})==4
    assert candidate({'a':1, 'b': {'c':'python'}})==2
    assert candidate({1: 'Sun', 2: {3: {4:'Mon'}}})==3

if __name__ == '__main__':
    check(dict_depth)