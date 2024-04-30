from case_MBPP_210 import concatenate_tuple


def check(candidate):
    assert candidate(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
    assert candidate(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
    assert candidate(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'

if __name__ == '__main__':
    check(concatenate_tuple)