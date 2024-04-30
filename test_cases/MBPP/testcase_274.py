from case_MBPP_274 import split


def check(candidate):
    assert candidate('python') == ['p','y','t','h','o','n']
    assert candidate('Name') == ['N','a','m','e']
    assert candidate('program') == ['p','r','o','g','r','a','m']

if __name__ == '__main__':
    check(split)