from case_MBPP_007 import remove_Occ


def check(candidate):
    assert candidate("hello","l") == "heo"
    assert candidate("abcda","a") == "bcd"
    assert candidate("PHP","P") == "H"

if __name__ == '__main__':
    check(remove_Occ)