from case_HE_157 import right_angle_triangle


def check(candidate):
    assert candidate(273, 936, 975) == True
    assert candidate(285, 380, 475) == True
    assert candidate(705, 376, 799) == True
    assert candidate(870, 464, 986) == True
    assert candidate(3504, 4015, 5329) == True
    assert candidate(525, 280, 595) == True
    assert candidate(1536, 1760, 2336) == True
    assert candidate(175, 600, 625) == True
    assert candidate(455, 1560, 1625) == True
    assert candidate(48, 55, 73) == True

    # Check some edge cases that are easy to work out by hand.
    assert candidate(3, 2, 5) == False
    assert candidate(259, 888, 925) == True
    assert candidate(490, 1680, 1750) == True
    assert candidate(1185, 632, 1343) == True
    assert candidate(6, 1, 9) == False
    assert candidate(2256, 2585, 3431) == True
    assert candidate(1155, 616, 1309) == True
    assert candidate(4, 5, 5) == False
    assert candidate(5, 7, 1) == False
    assert candidate(5, 1, 2) == False
    assert candidate(54, 72, 90) == True
    assert candidate(20, 12, 16) == True
    assert candidate(5, 5, 2) == False
    assert candidate(2736, 3135, 4161) == True
    assert candidate(518, 1776, 1850) == True
    assert candidate(3, 6, 11) == False
    assert candidate(7, 7, 5) == False
    assert candidate(15, 2, 10) == False
    assert candidate(10, 6, 8) == True
    assert candidate(15, 5, 11) == False
    assert candidate(1, 1, 2) == False
    assert candidate(1, 3, 15) == False
    assert candidate(280, 960, 1000) == True
    assert candidate(6, 1, 7) == False
    assert candidate(10, 9, 3) == False
    assert candidate(2, 7, 6) == False
    assert candidate(1, 7, 4) == False
    assert candidate(765, 408, 867) == True
    assert candidate(69, 92, 115) == True
    assert candidate(140, 336, 364) == True
    assert candidate(240, 144, 192) == True
    assert candidate(2, 4, 6) == False
    assert candidate(780, 468, 624) == True
    assert candidate(6, 7, 6) == False
    assert candidate(3888, 4455, 5913) == True
    assert candidate(6, 7, 7) == False
    assert candidate(2, 2, 2) == False
    assert candidate(14, 8, 10) == False
    assert candidate(204, 272, 340) == True
    assert candidate(3, 7, 2) == False
    assert candidate(1035, 552, 1173) == True
    assert candidate(243, 324, 405) == True
    assert candidate(581, 1992, 2075) == True
    assert candidate(11, 5, 8) == False
    assert candidate(820, 492, 656) == True
    assert candidate(5, 4, 4) == False
    assert candidate(4, 4, 4) == False
    assert candidate(4, 5, 4) == False
    assert candidate(12, 1, 2) == False
    assert candidate(900, 480, 1020) == True
    assert candidate(3, 3, 4) == False
    assert candidate(360, 864, 936) == True
    assert candidate(7, 1, 6) == False
    assert candidate(5, 3, 2) == False
    assert candidate(210, 112, 238) == True
    assert candidate(1000, 600, 800) == True
    assert candidate(285, 684, 741) == True
    assert candidate(65, 156, 169) == True
    assert candidate(960, 576, 768) == True
    assert candidate(3792, 4345, 5767) == True
    assert candidate(5, 5, 6) == False
    assert candidate(3, 3, 3) == False
    assert candidate(3, 2, 3) == False
    assert candidate(1, 2, 1) == False
    assert candidate(12, 4, 2) == False
    assert candidate(6, 4, 1) == False
    assert candidate(5, 12, 13) == True
    assert candidate(2, 6, 9) == False
    assert candidate(160, 384, 416) == True
    assert candidate(3, 6, 3) == False
    assert candidate(2, 4, 11) == False
    assert candidate(2880, 3300, 4380) == True
    assert candidate(10, 5, 7) == False
    assert candidate(7, 24, 25) == True
    assert candidate(15, 8, 17) == True
    assert candidate(4752, 5445, 7227) == True
    assert candidate(4656, 5335, 7081) == True
    assert candidate(380, 912, 988) == True
    assert candidate(350, 840, 910) == True
    assert candidate(3, 4, 5) == True
    assert candidate(2, 4, 8) == False
    assert candidate(1, 4, 4) == False
    assert candidate(70, 42, 56) == True
    assert candidate(15, 9, 11) == False
    assert candidate(201, 268, 335) == True
    assert candidate(170, 408, 442) == True
    assert candidate(12, 16, 20) == True
    assert candidate(305, 732, 793) == True
    assert candidate(2, 2, 10) == False
    assert candidate(1, 3, 4) == False
    assert candidate(230, 552, 598) == True
    assert candidate(1, 1, 1) == False
    assert candidate(3, 3, 9) == False
    assert candidate(6, 5, 3) == False
    assert candidate(235, 564, 611) == True
    assert candidate(3, 1, 4) == False
    assert candidate(81, 108, 135) == True
    assert candidate(1, 2, 3) == False
    assert candidate(5, 5, 4) == False
    assert candidate(21, 28, 35) == True
    assert candidate(234, 312, 390) == True
    assert candidate(3, 1, 7) == False
    assert candidate(230, 138, 184) == True
    assert candidate(168, 576, 600) == True
    assert candidate(1095, 584, 1241) == True
    assert candidate(320, 192, 256) == True
    assert candidate(8, 5, 6) == False
    assert candidate(5, 2, 4) == False
    assert candidate(6, 4, 4) == False
    assert candidate(4, 1, 4) == False
    assert candidate(528, 605, 803) == True
    assert candidate(5, 4, 10) == False
    assert candidate(15, 8, 3) == False
    assert candidate(1455, 776, 1649) == True
    assert candidate(21, 72, 75) == True
    assert candidate(2544, 2915, 3869) == True
    assert candidate(610, 366, 488) == True
    assert candidate(8, 10, 10) == False
    assert candidate(2, 4, 5) == False
    assert candidate(2, 3, 1) == False
    assert candidate(3, 3, 1) == False
    assert candidate(219, 292, 365) == True
    assert candidate(1, 5, 5) == False
    assert candidate(192, 220, 292) == True

if __name__ == '__main__':
    check(right_angle_triangle)