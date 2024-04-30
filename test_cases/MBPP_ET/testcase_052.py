from case_MBPP_052 import multiply_num


def check(candidate):
    assert candidate((8, 2, 3, -1, 7))==-67.2
    assert candidate((-10,-20,-30))==-2000.0
    assert candidate((19,15,18))==1710.0
    assert candidate((4, 1, 2, 1, 5)) == 8.0
    assert candidate((3, 7, 1, 4, 3)) == 50.4
    assert candidate((6, 2, 6, -6, 3)) == -259.2
    assert candidate((8, 2, 6, -2, 6)) == -230.4
    assert candidate((13, 4, 3, 1, 6)) == 187.2
    assert candidate((13, 7, 1, 1, 11)) == 200.2
    assert candidate((6, 2, 1, 3, 4)) == 28.8
    assert candidate((7, 1, 7, -4, 5)) == -196.0
    assert candidate((6, 2, 7, -1, 2)) == -33.6
    assert candidate((8, 3, 2, 2, 8)) == 153.6
    assert candidate((8, 2, 6, 0, 4)) == 0.0
    assert candidate((3, 5, 3, -3, 10)) == -270.0
    assert candidate((7, 6, 3, -6, 10)) == -1512.0
    assert candidate((12, 1, 6, 4, 10)) == 576.0
    assert candidate((6, 5, 5, -5, 8)) == -1200.0
    assert candidate((4, 4, 3, -3, 11)) == -316.8
    assert candidate((8, 4, 3, -6, 11)) == -1267.2
    assert candidate((5, 1, 1, -6, 4)) == -24.0
    assert candidate((11, 3, 3, -6, 10)) == -1188.0
    assert candidate((5, 7, 6, 2, 2)) == 168.0
    assert candidate((12, 2, 1, -6, 10)) == -288.0
    assert candidate((10, 3, 8, 3, 5)) == 720.0
    assert candidate((4, 1, 1, -3, 11)) == -26.4
    assert candidate((4, 2, 2, -5, 11)) == -176.0
    assert candidate((4, 7, 4, 0, 11)) == 0.0
    assert candidate((5, 2, 1, 1, 2)) == 4.0
    assert candidate((12, 6, 4, -5, 3)) == -864.0
    assert candidate((9, 6, 3, 2, 8)) == 518.4
    assert candidate((6, 1, 3, 4, 10)) == 144.0
    assert candidate((12, 7, 5, -5, 4)) == -1680.0
    assert candidate((12, 7, 1, -3, 12)) == -604.8
    assert candidate((12, 3, 6, -5, 12)) == -2592.0
    assert candidate((5, 6, 7, 2, 10)) == 840.0
    assert candidate((-15, -24, -35)) == -4200.0
    assert candidate((-8, -17, -28)) == -1269.3333333333333
    assert candidate((-14, -15, -33)) == -2310.0
    assert candidate((-7, -24, -27)) == -1512.0
    assert candidate((-12, -18, -31)) == -2232.0
    assert candidate((-6, -17, -25)) == -850.0
    assert candidate((-13, -22, -27)) == -2574.0
    assert candidate((-14, -23, -32)) == -3434.6666666666665
    assert candidate((-15, -20, -35)) == -3500.0
    assert candidate((-10, -16, -27)) == -1440.0
    assert candidate((-11, -25, -25)) == -2291.6666666666665
    assert candidate((-15, -17, -25)) == -2125.0
    assert candidate((-15, -24, -29)) == -3480.0
    assert candidate((-8, -22, -32)) == -1877.3333333333333
    assert candidate((-13, -22, -26)) == -2478.6666666666665
    assert candidate((-14, -21, -32)) == -3136.0
    assert candidate((-11, -23, -31)) == -2614.3333333333335
    assert candidate((-12, -15, -30)) == -1800.0
    assert candidate((-13, -16, -32)) == -2218.6666666666665
    assert candidate((-8, -21, -26)) == -1456.0
    assert candidate((-7, -19, -26)) == -1152.6666666666667
    assert candidate((-11, -19, -26)) == -1811.3333333333333
    assert candidate((-8, -18, -32)) == -1536.0
    assert candidate((-14, -19, -35)) == -3103.3333333333335
    assert candidate((-9, -16, -26)) == -1248.0
    assert candidate((-9, -24, -33)) == -2376.0
    assert candidate((-11, -22, -35)) == -2823.3333333333335
    assert candidate((-11, -25, -33)) == -3025.0
    assert candidate((-6, -22, -33)) == -1452.0
    assert candidate((-12, -25, -31)) == -3100.0
    assert candidate((-5, -24, -34)) == -1360.0
    assert candidate((-12, -19, -29)) == -2204.0
    assert candidate((-15, -16, -30)) == -2400.0
    assert candidate((14, 19, 17)) == 1507.3333333333333
    assert candidate((17, 17, 14)) == 1348.6666666666667
    assert candidate((16, 15, 23)) == 1840.0
    assert candidate((20, 13, 16)) == 1386.6666666666667
    assert candidate((15, 10, 23)) == 1150.0
    assert candidate((20, 19, 22)) == 2786.6666666666665
    assert candidate((14, 20, 18)) == 1680.0
    assert candidate((23, 11, 21)) == 1771.0
    assert candidate((22, 15, 23)) == 2530.0
    assert candidate((19, 17, 14)) == 1507.3333333333333
    assert candidate((14, 10, 19)) == 886.6666666666666
    assert candidate((19, 10, 23)) == 1456.6666666666667
    assert candidate((21, 18, 19)) == 2394.0
    assert candidate((14, 13, 22)) == 1334.6666666666667
    assert candidate((16, 10, 14)) == 746.6666666666666
    assert candidate((15, 16, 22)) == 1760.0
    assert candidate((17, 11, 19)) == 1184.3333333333333
    assert candidate((20, 12, 16)) == 1280.0
    assert candidate((16, 16, 14)) == 1194.6666666666667
    assert candidate((14, 10, 15)) == 700.0
    assert candidate((17, 14, 22)) == 1745.3333333333333
    assert candidate((14, 10, 13)) == 606.6666666666666
    assert candidate((20, 18, 16)) == 1920.0
    assert candidate((15, 13, 16)) == 1040.0
    assert candidate((20, 16, 16)) == 1706.6666666666667
    assert candidate((21, 17, 20)) == 2380.0
    assert candidate((17, 16, 20)) == 1813.3333333333333
    assert candidate((17, 17, 14)) == 1348.6666666666667
    assert candidate((20, 13, 22)) == 1906.6666666666667
    assert candidate((14, 11, 19)) == 975.3333333333334
    assert candidate((14, 19, 16)) == 1418.6666666666667
    assert candidate((19, 14, 21)) == 1862.0
    assert candidate((16, 12, 14)) == 896.0

if __name__ == '__main__':
    check(multiply_num)