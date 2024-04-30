from case_HE_147 import get_max_triples


def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

if __name__ == '__main__':
    check(get_max_triples)