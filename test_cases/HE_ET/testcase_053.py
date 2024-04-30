from case_HE_053 import add


def check(candidate):
    assert candidate(376, 7043) == 7419
    assert candidate(4146, 2825) == 6971
    assert candidate(791, 5387) == 6178
    assert candidate(4649, 1608) == 6257
    assert candidate(5018, 466) == 5484
    assert candidate(6117, 272) == 6389
    assert candidate(1357, 2487) == 3844
    assert candidate(x, y) == x + y
    assert candidate(8006, 8709) == 16715
    assert candidate(9796, 1174) == 10970
    assert candidate(7870, 7360) == 15230
    assert candidate(732, 3143) == 3875
    assert candidate(7935, 5949) == 13884
    assert candidate(5454, 7869) == 13323
    assert candidate(1126, 6742) == 7868
    assert candidate(8849, 8347) == 17196
    assert candidate(9515, 166) == 9681
    assert candidate(4503, 9969) == 14472
    assert candidate(2059, 4780) == 6839
    assert candidate(7879, 324) == 8203
    assert candidate(9811, 8213) == 18024
    assert candidate(3740, 5624) == 9364
    assert candidate(8914, 1540) == 10454
    assert candidate(746, 8724) == 9470
    assert candidate(3136, 4547) == 7683
    assert candidate(7961, 3114) == 11075
    assert candidate(3677, 7658) == 11335
    assert candidate(1790, 1852) == 3642
    assert candidate(9282, 7108) == 16390
    assert candidate(1302, 452) == 1754
    assert candidate(4327, 7636) == 11963
    assert candidate(364, 3749) == 4113
    assert candidate(5121, 8664) == 13785
    assert candidate(9165, 5702) == 14867
    assert candidate(7008, 2731) == 9739
    assert candidate(6585, 9545) == 16130
    assert candidate(5310, 1992) == 7302
    assert candidate(1225, 9125) == 10350
    assert candidate(5941, 2669) == 8610
    assert candidate(7037, 324) == 7361
    assert candidate(4788, 386) == 5174
    assert candidate(6945, 904) == 7849
    assert candidate(248, 7823) == 8071
    assert candidate(3060, 5657) == 8717
    assert candidate(2263, 9847) == 12110
    assert candidate(368, 2797) == 3165
    assert candidate(4107, 5540) == 9647
    assert candidate(8296, 1811) == 10107
    assert candidate(5276, 8660) == 13936
    assert candidate(5680, 7464) == 13144
    assert candidate(8345, 5607) == 13952
    assert candidate(1901, 127) == 2028
    assert candidate(4458, 1677) == 6135
    assert candidate(2222, 8205) == 10427
    assert candidate(1584, 818) == 2402
    assert candidate(5278, 2081) == 7359
    assert candidate(3006, 5) == 3011
    assert candidate(5635, 8779) == 14414
    assert candidate(1, 0) == 1
    assert candidate(9383, 8066) == 17449
    assert candidate(3518, 6494) == 10012
    assert candidate(0, 1) == 1
    assert candidate(2675, 9912) == 12587
    assert candidate(3555, 1782) == 5337
    assert candidate(3683, 7981) == 11664
    assert candidate(8333, 509) == 8842
    assert candidate(7, 5) == 12
    assert candidate(2008, 5033) == 7041
    assert candidate(514, 5170) == 5684
    assert candidate(2759, 668) == 3427
    assert candidate(690, 1142) == 1832
    assert candidate(3359, 9746) == 13105
    assert candidate(9566, 6478) == 16044
    assert candidate(2, 3) == 5
    assert candidate(3204, 9768) == 12972
    assert candidate(712, 4175) == 4887
    assert candidate(162, 2906) == 3068
    assert candidate(6205, 6624) == 12829
    assert candidate(5388, 9547) == 14935
    assert candidate(9129, 5617) == 14746
    assert candidate(5741, 9160) == 14901
    assert candidate(1791, 3916) == 5707
    assert candidate(3227, 9778) == 13005
    assert candidate(6199, 4771) == 10970
    assert candidate(5, 7) == 12
    assert candidate(4900, 8980) == 13880
    assert candidate(7789, 2308) == 10097
    assert candidate(3067, 3000) == 6067
    assert candidate(7773, 1016) == 8789
    assert candidate(3745, 1622) == 5367
    assert candidate(9412, 4209) == 13621
    assert candidate(9816, 4210) == 14026
    assert candidate(2141, 379) == 2520
    assert candidate(7655, 1186) == 8841
    assert candidate(8167, 3551) == 11718
    assert candidate(1589, 6268) == 7857
    assert candidate(8547, 6845) == 15392
    assert candidate(7631, 5609) == 13240
    assert candidate(7522, 8477) == 15999
    assert candidate(1528, 6738) == 8266
    assert candidate(5692, 7583) == 13275
    assert candidate(8263, 466) == 8729
    assert candidate(5559, 1830) == 7389
    assert candidate(804, 2620) == 3424
    assert candidate(5002, 5678) == 10680
    assert candidate(4986, 3544) == 8530

if __name__ == '__main__':
    check(add)