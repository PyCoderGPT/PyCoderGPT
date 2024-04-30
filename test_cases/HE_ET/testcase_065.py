from case_HE_065 import circular_shift


def check(candidate):
    assert candidate(100, 2) == '001'
    assert candidate(93, 13) == '39'
    assert candidate(98, 6) == '89'
    assert candidate(11, 2) == '11'
    assert candidate(8, 7) == '8'
    assert candidate(12, 105) == '21'
    assert candidate(96, 10) == '69'
    assert candidate(11, 101) == "11"
    assert candidate(15, 2) == '15'
    assert candidate(12, 5) == '21'
    assert candidate(98, 3) == '89'
    assert candidate(17, 6) == '71'
    assert candidate(96, 9) == '69'
    assert candidate(97, 9) == '79'
    assert candidate(103, 6) == '301'
    assert candidate(14, 3) == '41'
    assert candidate(9, 97) == '9'
    assert candidate(97, 2) == '97'
    assert candidate(102, 6) == '201'
    assert candidate(6, 96) == '6'
    assert candidate(17, 2) == '17'
    assert candidate(14, 4) == '41'
    assert candidate(99, 11) == '99'
    assert candidate(93, 12) == '39'
    assert candidate(95, 7) == '59'
    assert candidate(97, 11) == '79'
    assert candidate(13, 101) == '31'
    assert candidate(9, 101) == '9'
    assert candidate(92, 5) == '29'
    assert candidate(9, 4) == '9'
    assert candidate(96, 4) == '69'
    assert candidate(8, 1) == '8'
    assert candidate(12, 3) == '21'
    assert candidate(105, 1) == '510'
    assert candidate(99, 4) == '99'
    assert candidate(8, 2) == '8'
    assert candidate(11, 99) == '11'
    assert candidate(10, 6) == '01'
    assert candidate(101, 5) == '101'
    assert candidate(105, 6) == '501'
    assert candidate(10, 97) == '01'
    assert candidate(12, 1) == "21"
    assert candidate(12, 1) == '21'
    assert candidate(7, 4) == '7'
    assert candidate(101, 13) == '101'
    assert candidate(97, 3) == '79'
    assert candidate(101, 3) == '101'
    assert candidate(8, 97) == '8'
    assert candidate(16, 96) == '61'
    assert candidate(7, 5) == '7'
    assert candidate(8, 105) == '8'
    assert candidate(105, 2) == '051'
    assert candidate(16, 98) == '61'
    assert candidate(15, 3) == '51'
    assert candidate(11, 7) == '11'
    assert candidate(12, 100) == '21'
    assert candidate(94, 8) == '49'
    assert candidate(101, 7) == '101'
    assert candidate(101, 4) == '101'
    assert candidate(99, 3) == '99'
    assert candidate(14, 2) == '14'
    assert candidate(9, 1) == '9'
    assert candidate(102, 7) == '201'
    assert candidate(16, 7) == '61'
    assert candidate(12, 2) == "12"
    assert candidate(102, 2) == '021'
    assert candidate(7, 106) == '7'
    assert candidate(14, 102) == '41'
    assert candidate(13, 104) == '31'
    assert candidate(12, 4) == '21'
    assert candidate(14, 7) == '41'
    assert candidate(100, 2) == "001"
    assert candidate(100, 5) == '001'
    assert candidate(6, 97) == '6'
    assert candidate(14, 6) == '41'
    assert candidate(13, 6) == '31'
    assert candidate(13, 1) == '31'
    assert candidate(16, 3) == '61'
    assert candidate(97, 8) == "79"

if __name__ == '__main__':
    check(circular_shift)