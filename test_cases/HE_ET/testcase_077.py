from case_HE_077 import iscube


def check(candidate):
    assert candidate(68921) == True
    assert candidate(1000000) == True
    assert candidate(205379) == True
    assert candidate(216) == True
    assert candidate(314432) == True
    assert candidate(274625) == True
    assert candidate(157464) == True
    assert candidate(941192) == True
    assert candidate(178) == False
    assert candidate(250047) == True
    assert candidate(3) == False
    assert candidate(179) == False
    assert candidate(857375) == True
    assert candidate(512) == True
    assert candidate(405224) == True
    assert candidate(176) == False
    assert candidate(238328) == True
    assert candidate(1) == True, "First test error: " + str(candidate(1))
    assert candidate(1000) == True
    assert candidate(4913) == True
    assert candidate(373248) == True
    assert candidate(262144) == True
    assert candidate(2) == False, "Second test error: " + str(candidate(2))
    assert candidate(0) == True, "1st edge test error: " + str(candidate(0))
    assert candidate(2197) == True
    assert candidate(2744) == True
    assert candidate(175) == False
    assert candidate(103823) == True
    assert candidate(13824) == True
    assert candidate(474552) == True
    assert candidate(658503) == True
    assert candidate(636056) == True
    assert candidate(5) == False
    assert candidate(4) == False
    assert candidate(21952) == True
    assert candidate(42875) == True
    assert candidate(681472) == True
    assert candidate(1) == True
    assert candidate(884736) == True
    assert candidate(12167) == True
    assert candidate(180) == False, "Fifth test error: " + str(candidate(180))
    assert candidate(1000) == True, "Sixth test error: " + str(candidate(1000))


    # Check some edge cases that are easy to work out by hand.
    assert candidate(729) == True
    assert candidate(753571) == True
    assert candidate(54872) == True
    assert candidate(1331) == True
    assert candidate(185193) == True
    assert candidate(438976) == True
    assert candidate(180) == False
    assert candidate(7) == False
    assert candidate(8) == True
    assert candidate(2) == False
    assert candidate(1729) == False, "2nd edge test error: " + str(candidate(1728))
    assert candidate(493039) == True
    assert candidate(729000) == True
    assert candidate(328509) == True
    assert candidate(85184) == True
    assert candidate(704969) == True
    assert candidate(287496) == True
    assert candidate(15625) == True
    assert candidate(3375) == True
    assert candidate(226981) == True
    assert candidate(19683) == True
    assert candidate(64) == True, "Fourth test error: " + str(candidate(64))
    assert candidate(571787) == True
    assert candidate(181) == False
    assert candidate(185) == False
    assert candidate(551368) == True
    assert candidate(64) == True
    assert candidate(-1) == True, "Third test error: " + str(candidate(-1))
    assert candidate(74088) == True
    assert candidate(8000) == True

if __name__ == '__main__':
    check(iscube)