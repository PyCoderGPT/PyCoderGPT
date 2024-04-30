from case_HE_031 import is_prime


def check(candidate):
    assert candidate(255520) == False
    assert candidate(6) == False
    assert candidate(85) == False
    assert candidate(83) == True
    assert candidate(82) == False
    assert candidate(7) == True
    assert candidate(13) == True
    assert candidate(57) == False
    assert candidate(81) == False
    assert candidate(3) == True
    assert candidate(104) == False
    assert candidate(90) == False
    assert candidate(88) == False
    assert candidate(255344) == False
    assert candidate(12) == False
    assert candidate(14316) == False
    assert candidate(12938) == False
    assert candidate(8) == False
    assert candidate(102) == False
    assert candidate(12628) == False
    assert candidate(61) == True
    assert candidate(5 * 17) == False
    assert candidate(98) == False
    assert candidate(63) == False
    assert candidate(19) == True
    assert candidate(12884) == False
    assert candidate(87) == False
    assert candidate(89) == True
    assert candidate(255139) == False
    assert candidate(12897) == False
    assert candidate(73) == True
    assert candidate(1) == False
    assert candidate(15) == False
    assert candidate(75) == False
    assert candidate(18) == False
    assert candidate(96) == False
    assert candidate(5) == True
    assert candidate(9) == False
    assert candidate(255046) == False
    assert candidate(14) == False
    assert candidate(78) == False
    assert candidate(255214) == False
    assert candidate(76) == False
    assert candidate(2) == True
    assert candidate(254873) == True
    assert candidate(13441 * 19) == False
    assert candidate(13796) == False
    assert candidate(11) == True
    assert candidate(14253) == False
    assert candidate(100) == False
    assert candidate(20) == False
    assert candidate(58) == False
    assert candidate(22) == False
    assert candidate(17) == True
    assert candidate(13481) == False
    assert candidate(12832) == False
    assert candidate(254513) == False
    assert candidate(106) == False
    assert candidate(16) == False
    assert candidate(13441) == True
    assert candidate(66) == False
    assert candidate(65) == False
    assert candidate(80) == False
    assert candidate(11 * 7) == False
    assert candidate(101) == True
    assert candidate(103) == True
    assert candidate(56) == False
    assert candidate(254423) == False
    assert candidate(254790) == False
    assert candidate(4) == False

if __name__ == '__main__':
    check(is_prime)