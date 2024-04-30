from case_HE_015 import string_sequence


def check(candidate):
    assert candidate(25) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'
    assert candidate(1) == '0 1'
    assert candidate(15) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
    assert candidate(13) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13'
    assert candidate(46) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46'
    assert candidate(37) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37'
    assert candidate(35) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35'
    assert candidate(0) == '0'
    assert candidate(34) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34'
    assert candidate(47) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47'
    assert candidate(48) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48'
    assert candidate(23) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23'
    assert candidate(29) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29'
    assert candidate(6) == '0 1 2 3 4 5 6'
    assert candidate(30) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30'
    assert candidate(44) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44'
    assert candidate(31) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31'
    assert candidate(22) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22'
    assert candidate(36) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36'
    assert candidate(5) == '0 1 2 3 4 5'
    assert candidate(26) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26'
    assert candidate(21) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21'
    assert candidate(33) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33'
    assert candidate(20) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'
    assert candidate(43) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43'
    assert candidate(8) == '0 1 2 3 4 5 6 7 8'
    assert candidate(27) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27'
    assert candidate(24) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24'
    assert candidate(38) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38'
    assert candidate(49) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49'
    assert candidate(45) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45'
    assert candidate(42) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42'
    assert candidate(18) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18'
    assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'
    assert candidate(28) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28'
    assert candidate(16) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'
    assert candidate(14) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14'
    assert candidate(12) == '0 1 2 3 4 5 6 7 8 9 10 11 12'
    assert candidate(39) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39'
    assert candidate(40) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40'
    assert candidate(4) == '0 1 2 3 4'
    assert candidate(3) == '0 1 2 3'
    assert candidate(50) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50'
    assert candidate(11) == '0 1 2 3 4 5 6 7 8 9 10 11'
    assert candidate(19) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19'
    assert candidate(41) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41'
    assert candidate(2) == '0 1 2'
    assert candidate(32) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32'

if __name__ == '__main__':
    check(string_sequence)