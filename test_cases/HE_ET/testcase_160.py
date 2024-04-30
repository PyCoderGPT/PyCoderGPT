from case_HE_160 import do_algebra


def check(candidate):
    assert candidate(['**', '//', '-'], [5, 6, 6, 1]) == 2603
    assert candidate(['**', '-', '-'], [7, 1, 4, 9]) == -6
    assert candidate(['+', '**', '*'], [6, 2, 1, 1]) == 8
    assert candidate(['+', '+', '+'], [1, 4, 9, 9]) == 23
    assert candidate(['//', '-', '-'], [3, 3, 3, 6]) == -8
    assert candidate(['-', '*', '-'], [1, 1, 2, 3]) == -4
    assert candidate(['//', '-', '*'], [7, 2, 7, 5]) == -32
    assert candidate(['//', '*', '+'], [3, 5, 2, 3]) == 3
    assert candidate(['//', '**', '+'], [3, 7, 9, 3]) == 3
    assert candidate(['*', '//', '//'], [5, 2, 7, 9]) == 0
    assert candidate(['-', '//', '-'], [6, 8, 1, 10]) == -12
    assert candidate(['//', '**', '-'], [3, 7, 7, 1]) == -1
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['//', '//'], [8, 8, 7]) == 0
    assert candidate(['//', '//', '*'], [2, 1, 7, 6]) == 0
    assert candidate(['//', '//', '+'], [5, 2, 8, 2]) == 2
    assert candidate(['*', '+', '+'], [3, 2, 6, 5]) == 17
    assert candidate(['*', '**'], [5, 1, 6]) == 5
    assert candidate(['-', '+', '**'], [5, 3, 5, 6]) == 15627
    assert candidate(['-', '**', '//'], [1, 8, 3, 3]) == -169
    assert candidate(['**', '+', '-'], [3, 8, 1, 2]) == 6560
    assert candidate(['**', '//'], [12, 1, 6]) == 2
    assert candidate(['*', '+', '-'], [2, 2, 9, 6]) == 7
    assert candidate(['*', '+'], [2, 5, 7]) == 17
    assert candidate(['**', '*'], [2, 3, 1]) == 8
    assert candidate(['**', '//'], [7, 8, 8]) == 720600
    assert candidate(['-', '+', '-'], [3, 5, 9, 7]) == 0
    assert candidate(['**', '+'], [8, 4, 1]) == 4097
    assert candidate(['**', '*', '+'], [5, 2, 1, 9]) == 34
    assert candidate(['//', '-', '*'], [5, 4, 7, 1]) == -6
    assert candidate(['-', '**'], [6, 2, 2]) == 2
    assert candidate(['*', '+', '+'], [6, 3, 5, 5]) == 28
    assert candidate(['-', '**'], [8, 2, 7]) == -120
    assert candidate(['//', '**'], [4, 4, 4]) == 0
    assert candidate(['-', '//'], [5, 3, 8]) == 5
    assert candidate(['//', '**', '-'], [7, 2, 9, 3]) == -3
    assert candidate(['**', '-', '//'], [6, 1, 6, 7]) == 6
    assert candidate(['*', '//', '-'], [7, 1, 5, 10]) == -9
    assert candidate(['//', '*', '**'], [7, 6, 2, 1]) == 2
    assert candidate(['*', '*', '-'], [7, 8, 1, 9]) == 47
    assert candidate(['**', '+'], [8, 2, 7]) == 71
    assert candidate(['**', '//'], [9, 5, 9]) == 6561
    assert candidate(['**', '-', '*'], [5, 1, 2, 3]) == -1
    assert candidate(['*', '//', '+'], [7, 1, 8, 9]) == 9
    assert candidate(['//', '//', '+'], [2, 5, 8, 8]) == 8
    assert candidate(['*', '-', '+'], [6, 7, 4, 4]) == 42
    assert candidate(['-', '**', '-'], [7, 4, 1, 8]) == -5
    assert candidate(['+', '**', '+'], [4, 2, 7, 1]) == 133
    assert candidate(['*', '+'], [9, 3, 8]) == 35
    assert candidate(['*', '-', '//'], [4, 4, 2, 6]) == 16
    assert candidate(['*', '//', '//'], [7, 7, 6, 6]) == 1
    assert candidate(['**', '//', '//'], [1, 7, 6, 2]) == 0
    assert candidate(['*', '-', '**'], [2, 7, 7, 1]) == 7
    assert candidate(['+', '*', '**'], [6, 8, 1, 2]) == 14
    assert candidate(['**', '//', '+'], [5, 8, 3, 3]) == 130211
    assert candidate(['*', '-'], [6, 5, 7]) == 23
    assert candidate(['*', '*', '+'], [1, 3, 2, 9]) == 15
    assert candidate(['-', '*'], [3, 3, 6]) == -15
    assert candidate(['//', '-', '**'], [4, 8, 2, 2]) == -4
    assert candidate(['-', '**', '-'], [4, 5, 5, 9]) == -3130
    assert candidate(['**', '+', '*'], [1, 5, 5, 1]) == 6
    assert candidate(['-', '**'], [3, 5, 2]) == -22
    assert candidate(['+', '*'], [7, 3, 6]) == 25
    assert candidate(['*', '-', '**'], [5, 5, 2, 8]) == -231
    assert candidate(['+', '-', '**'], [6, 8, 4, 10]) == -1048562
    assert candidate(['+', '//', '*'], [7, 3, 7, 1]) == 7
    assert candidate(['**', '-', '//'], [7, 8, 1, 10]) == 5764801
    assert candidate(['//', '//', '+'], [1, 2, 8, 10]) == 10
    assert candidate(['*', '*', '-'], [3, 4, 1, 4]) == 8
    assert candidate(['//', '+', '**'], [7, 1, 5, 1]) == 12
    assert candidate(['*', '**'], [3, 2, 8]) == 768
    assert candidate(['*', '**'], [7, 3, 3]) == 189
    assert candidate(['+', '**', '-'], [5, 2, 5, 9]) == 28
    assert candidate(['-', '**', '*'], [5, 2, 7, 8]) == -1019
    assert candidate(['-', '+'], [8, 4, 3]) == 7
    assert candidate(['+', '-', '//'], [5, 4, 6, 2]) == 6
    assert candidate(['//', '+', '//'], [5, 1, 9, 4]) == 7
    assert candidate(['*', '**', '+'], [7, 1, 5, 1]) == 8
    assert candidate(['*', '+', '//'], [4, 6, 7, 10]) == 24
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['**', '*'], [8, 2, 2]) == 128
    assert candidate(['**', '-', '*'], [6, 4, 5, 1]) == 1291
    assert candidate(['-', '+'], [3, 4, 4]) == 3
    assert candidate(['+', '-'], [10, 3, 8]) == 5
    assert candidate(['//', '*'], [7, 3, 4]) == 8
    assert candidate(['//', '-'], [6, 1, 2]) == 4
    assert candidate(['**', '+'], [10, 3, 5]) == 1005
    assert candidate(['+', '-'], [3, 7, 6]) == 4
    assert candidate(['**', '//'], [9, 5, 2]) == 29524
    assert candidate(['*', '*'], [5, 2, 7]) == 70
    assert candidate(['*', '+', '**'], [5, 5, 2, 9]) == 537
    assert candidate(['-', '**'], [3, 3, 4]) == -78
    assert candidate(['**', '*', '*'], [7, 2, 4, 7]) == 1372
    assert candidate(['**', '*', '-'], [7, 6, 4, 6]) == 470590
    assert candidate(['//', '//'], [2, 7, 1]) == 0
    assert candidate(['+', '**', '+'], [6, 6, 4, 7]) == 1309
    assert candidate(['**', '*'], [10, 2, 8]) == 800
    assert candidate(['+', '//'], [3, 6, 4]) == 4
    assert candidate(['**', '+', '-'], [1, 5, 1, 1]) == 1
    assert candidate(['+', '-', '*'], [6, 8, 6, 1]) == 8
    assert candidate(['+', '**'], [7, 3, 5]) == 250
    assert candidate(['-', '//'], [7, 3, 2]) == 6
    assert candidate(['//', '+', '*'], [2, 6, 4, 4]) == 16
    assert candidate(['//', '//', '**'], [7, 1, 9, 1]) == 0
    assert candidate(['+', '*', '//'], [6, 5, 1, 3]) == 7
    assert candidate(['+', '**'], [3, 2, 4]) == 19
    assert candidate(['-', '*', '-'], [2, 7, 3, 9]) == -28
    assert candidate(['*', '*', '-'], [2, 1, 8, 4]) == 12
    assert candidate(['+', '**'], [7, 6, 6]) == 46663
    assert candidate(['**', '-', '-'], [1, 7, 7, 10]) == -16
    assert candidate(['**', '//', '//'], [1, 7, 4, 8]) == 0
    assert candidate(['-', '*', '*'], [7, 4, 7, 8]) == -217
    assert candidate(['**', '-'], [3, 2, 9]) == 0
    assert candidate(['-', '+', '**'], [5, 4, 2, 3]) == 9
    assert candidate(['+', '+'], [4, 4, 1]) == 9
    assert candidate(['-', '+'], [10, 7, 1]) == 4
    assert candidate(['-', '+', '*'], [5, 5, 4, 8]) == 32
    assert candidate(['//', '//', '*'], [4, 8, 9, 6]) == 0
    assert candidate(['+', '**', '-'], [1, 1, 9, 4]) == -2
    assert candidate(['+', '//', '+'], [5, 8, 2, 1]) == 10
    assert candidate(['-', '//', '**'], [4, 5, 8, 3]) == 4
    assert candidate(['+', '//', '*'], [5, 4, 8, 10]) == 5
    assert candidate(['**', '-', '+'], [2, 1, 7, 9]) == 4
    assert candidate(['//', '*'], [8, 4, 2]) == 4
    assert candidate(['//', '-', '*'], [4, 3, 3, 1]) == -2
    assert candidate(['-', '+', '+'], [1, 1, 9, 9]) == 18
    assert candidate(['-', '+', '**'], [1, 4, 2, 7]) == 125
    assert candidate(['*', '+'], [4, 8, 4]) == 36
    assert candidate(['*', '//', '*'], [7, 3, 1, 10]) == 210

if __name__ == '__main__':
    check(do_algebra)