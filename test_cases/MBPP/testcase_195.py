from case_MBPP_195 import check_tuplex


def check(candidate):
    assert candidate(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
    assert candidate(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'5')==False
    assert candidate(("w", 3, "r", "e", "s", "o", "u", "r", "c","e"),3)==True

if __name__ == '__main__':
    check(check_tuplex)