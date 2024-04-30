from case_MBPP_393 import occurance_substring


def check(candidate):
    assert candidate('python programming, python language','python')==('python', 0, 6)
    assert candidate('python programming,programming language','programming')==('programming', 7, 18)
    assert candidate('python programming,programming language','language')==('language', 31, 39)
    assert candidate('c++ programming, c++ language','python')==None

if __name__ == '__main__':
    check(occurance_substring)