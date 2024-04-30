from case_MBPP_076 import long_words


def check(candidate):
    assert candidate(3,"python is a programming language")==['python','programming','language']
    assert candidate(2,"writing a program")==['writing','program']
    assert candidate(5,"sorting list")==['sorting']

if __name__ == '__main__':
    check(long_words)