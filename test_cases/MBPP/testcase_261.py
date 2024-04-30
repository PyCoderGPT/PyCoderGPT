from case_MBPP_261 import is_lower


def check(candidate):
    assert candidate("InValid") == "invalid"
    assert candidate("TruE") == "true"
    assert candidate("SenTenCE") == "sentence"

if __name__ == '__main__':
    check(is_lower)