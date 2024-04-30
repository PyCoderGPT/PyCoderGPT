from case_MBPP_123 import lps


def check(candidate):
    assert candidate("TENS FOR TENS") == 5
    assert candidate("CARDIO FOR CARDS") == 7
    assert candidate("PART OF THE JOURNEY IS PART") == 9

if __name__ == '__main__':
    check(lps)