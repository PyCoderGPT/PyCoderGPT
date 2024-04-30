from case_MBPP_025 import bell_number


def check(candidate):
    assert candidate(2)==2
    assert candidate(10)==115975
    assert candidate(56)==6775685320645824322581483068371419745979053216268760300

if __name__ == '__main__':
    check(bell_number)