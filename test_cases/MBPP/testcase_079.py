from case_MBPP_079 import reverse_vowels


def check(candidate):
    assert candidate("Python") == "Python"
    assert candidate("USA") == "ASU"
    assert candidate("ab") == "ab"

if __name__ == '__main__':
    check(reverse_vowels)