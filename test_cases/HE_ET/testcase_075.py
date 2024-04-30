from case_HE_075 import is_multiply_prime


def check(candidate):
    assert candidate(121) == False
    assert candidate(890) == True
    assert candidate(894) == False
    assert candidate(734) == False
    assert candidate(122) == False
    assert candidate(32) == False
    assert candidate(130) == True
    assert candidate(106) == False
    assert candidate(109) == False
    assert candidate(728) == False
    assert candidate(893) == False
    assert candidate(889) == False
    assert candidate(31) == False
    assert candidate(729) == False
    assert candidate(25) == False
    assert candidate(8) == True
    assert candidate(127) == False
    assert candidate(7) == False
    assert candidate(125) == True
    assert candidate(104) == False
    assert candidate(724) == False
    assert candidate(131) == False
    assert candidate(887) == False
    assert candidate(3) == False
    assert candidate(895) == False
    assert candidate(725) == True
    assert candidate(9 * 9 * 9) == False
    assert candidate(10) == False
    assert candidate(128) == False
    assert candidate(891) == False
    assert candidate(1) == False
    assert candidate(6) == False
    assert candidate(727) == False
    assert candidate(14) == False
    assert candidate(3 * 6 * 7) == False
    assert candidate(9) == False
    assert candidate(124) == True
    assert candidate(126) == False
    assert candidate(27) == True
    assert candidate(26) == False
    assert candidate(726) == False
    assert candidate(2) == False
    assert candidate(30) == True
    assert candidate(13) == False
    assert candidate(5) == False
    assert candidate(11 * 9 * 9) == False
    assert candidate(129) == False
    assert candidate(12) == True
    assert candidate(11) == False
    assert candidate(107) == False
    assert candidate(3 * 5 * 7) == True
    assert candidate(101) == False
    assert candidate(28) == True
    assert candidate(11 * 13 * 7) == True
    assert candidate(730) == True
    assert candidate(110) == True

if __name__ == '__main__':
    check(is_multiply_prime)