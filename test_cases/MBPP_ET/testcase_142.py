from case_MBPP_142 import ascii_value


def check(candidate):
    assert candidate('A')==65
    assert candidate('R')==82
    assert candidate('S')==83
    assert candidate("V") == 86
    assert candidate("D") == 68
    assert candidate("O") == 79
    assert candidate("V") == 86
    assert candidate("X") == 88
    assert candidate("N") == 78
    assert candidate("G") == 71
    assert candidate("G") == 71
    assert candidate("S") == 83
    assert candidate("V") == 86
    assert candidate("R") == 82
    assert candidate("K") == 75
    assert candidate("Z") == 90
    assert candidate("M") == 77
    assert candidate("R") == 82
    assert candidate("A") == 65
    assert candidate("H") == 72
    assert candidate("S") == 83
    assert candidate("I") == 73
    assert candidate("M") == 77
    assert candidate("L") == 76
    assert candidate("B") == 66
    assert candidate("H") == 72
    assert candidate("V") == 86
    assert candidate("I") == 73
    assert candidate("M") == 77
    assert candidate("C") == 67
    assert candidate("G") == 71
    assert candidate("F") == 70
    assert candidate("A") == 65
    assert candidate("I") == 73
    assert candidate("C") == 67
    assert candidate("J") == 74
    assert candidate("N") == 78
    assert candidate("N") == 78
    assert candidate("D") == 68
    assert candidate("D") == 68
    assert candidate("C") == 67
    assert candidate("J") == 74
    assert candidate("A") == 65
    assert candidate("I") == 73
    assert candidate("F") == 70
    assert candidate("F") == 70
    assert candidate("G") == 71
    assert candidate("M") == 77
    assert candidate("Y") == 89
    assert candidate("Q") == 81
    assert candidate("U") == 85
    assert candidate("P") == 80
    assert candidate("D") == 68
    assert candidate("T") == 84
    assert candidate("L") == 76
    assert candidate("S") == 83
    assert candidate("Q") == 81
    assert candidate("E") == 69
    assert candidate("U") == 85
    assert candidate("P") == 80
    assert candidate("E") == 69
    assert candidate("E") == 69
    assert candidate("K") == 75
    assert candidate("J") == 74
    assert candidate("F") == 70
    assert candidate("A") == 65
    assert candidate("O") == 79
    assert candidate("H") == 72
    assert candidate("J") == 74
    assert candidate("J") == 74
    assert candidate("I") == 73
    assert candidate("D") == 68
    assert candidate("U") == 85
    assert candidate("P") == 80
    assert candidate("Z") == 90
    assert candidate("V") == 86
    assert candidate("Y") == 89
    assert candidate("H") == 72
    assert candidate("W") == 87
    assert candidate("Q") == 81
    assert candidate("K") == 75
    assert candidate("M") == 77
    assert candidate("P") == 80
    assert candidate("J") == 74
    assert candidate("N") == 78
    assert candidate("F") == 70
    assert candidate("V") == 86
    assert candidate("O") == 79
    assert candidate("N") == 78
    assert candidate("J") == 74
    assert candidate("Y") == 89
    assert candidate("K") == 75
    assert candidate("Q") == 81
    assert candidate("L") == 76
    assert candidate("O") == 79
    assert candidate("V") == 86
    assert candidate("F") == 70
    assert candidate("D") == 68
    assert candidate("G") == 71
    assert candidate("J") == 74
    assert candidate("L") == 76
    assert candidate("P") == 80

if __name__ == '__main__':
    check(ascii_value)