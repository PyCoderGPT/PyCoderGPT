from case_HE_103 import rounded_avg


def check(candidate):
    assert candidate(7, 1) == -1
    assert candidate(201, 228) == '0b11010110'
    assert candidate(565, 856) == '0b1011000110'
    assert candidate(3, 3) == '0b11'
    assert candidate(2, 5) == '0b100'
    assert candidate(7, 2) == -1
    assert candidate(2, 3) == '0b10'
    assert candidate(361, 495) == '0b110101100'
    assert candidate(187, 545) == '0b101101110'
    assert candidate(2, 2) == '0b10'
    assert candidate(10, 7) == -1
    assert candidate(969, 973) == '0b1111001011'
    assert candidate(10, 2) == -1
    assert candidate(1000, 992) == -1
    assert candidate(9, 12) == '0b1010'
    assert candidate(1000, 997) == -1
    assert candidate(350,902) == "0b1001110010"
    assert candidate(3, 5) == '0b100'
    assert candidate(5, 5) == "0b101"
    assert candidate(365, 492) == '0b110101100'
    assert candidate(357, 500) == '0b110101100'
    assert candidate(6, 10) == '0b1000'
    assert candidate(1, 5) == "0b11"
    assert candidate(5, 17) == '0b1011'
    assert candidate(4, 8) == '0b110'
    assert candidate(194, 238) == '0b11011000'
    assert candidate(348, 904) == '0b1001110010'
    assert candidate(198, 229) == '0b11010110'
    assert candidate(2, 6) == '0b100'
    assert candidate(959, 976) == '0b1111001000'
    assert candidate(7, 13) == "0b1010"
    assert candidate(555, 849) == '0b1010111110'
    assert candidate(5, 5) == '0b101'
    assert candidate(349, 902) == '0b1001110010'
    assert candidate(966, 977) == '0b1111001100'
    assert candidate(965, 980) == '0b1111001100'
    assert candidate(193, 237) == '0b11010111'
    assert candidate(960, 972) == '0b1111000110'
    assert candidate(992, 1001) == '0b1111100100'
    assert candidate(186, 549) == '0b101110000'
    assert candidate(367, 500) == '0b110110010'
    assert candidate(5, 3) == -1
    assert candidate(362,496) == "0b110101101"
    assert candidate(6, 4) == -1
    assert candidate(357, 498) == '0b110101100'
    assert candidate(1, 1) == '0b1'
    assert candidate(197, 237) == '0b11011001'
    assert candidate(365, 501) == '0b110110001'
    assert candidate(3, 6) == '0b100'
    assert candidate(7, 9) == '0b1000'
    assert candidate(359, 491) == '0b110101001'
    assert candidate(11, 18) == '0b1110'
    assert candidate(197, 232) == '0b11010110'
    assert candidate(189, 544) == '0b101101110'
    assert candidate(4, 5) == '0b100'
    assert candidate(347, 905) == '0b1001110010'
    assert candidate(183, 546) == '0b101101100'
    assert candidate(359, 495) == '0b110101011'
    assert candidate(364, 498) == '0b110101111'
    assert candidate(564, 847) == '0b1011000010'
    assert candidate(4, 2) == -1
    assert candidate(964, 973) == '0b1111001000'
    assert candidate(562, 847) == '0b1011000000'
    assert candidate(11, 11) == '0b1011'
    assert candidate(192, 231) == '0b11010100'
    assert candidate(12, 15) == '0b1110'
    assert candidate(185, 542) == '0b101101100'
    assert candidate(8, 10) == '0b1001'
    assert candidate(3, 7) == '0b101'
    assert candidate(992, 998) == '0b1111100011'
    assert candidate(10, 13) == '0b1100'
    assert candidate(194, 237) == '0b11011000'
    assert candidate(355, 907) == '0b1001110111'
    assert candidate(6, 6) == '0b110'
    assert candidate(7, 5) == -1
    assert candidate(994, 992) == -1
    assert candidate(964,977) == "0b1111001010"
    assert candidate(185,546) == "0b101101110"
    assert candidate(197,233) == "0b11010111"


    # Check some edge cases that are easy to work out by hand.
    assert candidate(197, 238) == '0b11011010'
    assert candidate(9, 5) == -1
    assert candidate(6, 2) == -1
    assert candidate(180, 541) == '0b101101000'
    assert candidate(969, 972) == '0b1111001010'
    assert candidate(348, 902) == '0b1001110001'
    assert candidate(187, 548) == '0b101110000'
    assert candidate(4, 6) == '0b101'
    assert candidate(993, 992) == -1
    assert candidate(563, 852) == '0b1011000100'
    assert candidate(3, 10) == '0b110'
    assert candidate(11, 15) == '0b1101'
    assert candidate(185, 546) == '0b101101110'
    assert candidate(961, 980) == '0b1111001010'
    assert candidate(180, 543) == '0b101101010'
    assert candidate(5, 1) == -1
    assert candidate(561, 849) == '0b1011000001'
    assert candidate(995, 993) == -1
    assert candidate(4, 15) == '0b1010'
    assert candidate(8, 1) == -1
    assert candidate(8, 3) == -1
    assert candidate(4, 7) == '0b110'
    assert candidate(964, 974) == '0b1111001001'
    assert candidate(564, 850) == '0b1011000011'
    assert candidate(555, 852) == '0b1011000000'
    assert candidate(350, 903) == '0b1001110010'
    assert candidate(355, 900) == '0b1001110100'
    assert candidate(558, 852) == '0b1011000001'
    assert candidate(996,997) == "0b1111100100"
    assert candidate(968, 972) == '0b1111001010'
    assert candidate(180, 546) == '0b101101011'
    assert candidate(352, 900) == '0b1001110010'
    assert candidate(352, 897) == '0b1001110000'
    assert candidate(10, 15) == '0b1100'
    assert candidate(991, 996) == '0b1111100010'
    assert candidate(560,851) == "0b1011000010"
    assert candidate(995, 999) == '0b1111100101'
    assert candidate(991, 994) == '0b1111100000'
    assert candidate(564, 848) == '0b1011000010'
    assert candidate(6, 1) == -1

if __name__ == '__main__':
    check(rounded_avg)