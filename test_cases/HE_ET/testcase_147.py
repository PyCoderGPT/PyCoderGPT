from case_HE_147 import get_max_triples


def check(candidate):
    assert candidate(148) == 175273
    assert candidate(84) == 30996
    assert candidate(74) == 20724
    assert candidate(126) == 106764
    assert candidate(166) == 248050
    assert candidate(58) == 10108
    assert candidate(5) == 1
    assert candidate(29) == 1089
    assert candidate(43) == 4018
    assert candidate(169) == 261856
    assert candidate(136) == 135675
    assert candidate(19) == 306
    assert candidate(39) == 2886
    assert candidate(178) == 306328
    assert candidate(75) == 21900
    assert candidate(46) == 4950
    assert candidate(187) == 355570
    assert candidate(98) == 49136
    assert candidate(173) == 277761
    assert candidate(108) == 66780
    assert candidate(153) == 192525
    assert candidate(134) == 127754
    assert candidate(48) == 5520
    assert candidate(38) == 2586
    assert candidate(124) == 102541
    assert candidate(17) == 185
    assert candidate(93) == 42315
    assert candidate(18) == 240
    assert candidate(41) == 3289
    assert candidate(51) == 6664
    assert candidate(135) == 131670
    assert candidate(177) == 299425
    assert candidate(186) == 347944
    assert candidate(16) == 175
    assert candidate(185) == 340441
    assert candidate(61) == 11800
    assert candidate(13) == 88
    assert candidate(30) == 1260
    assert candidate(130) == 118336
    assert candidate(9) == 21
    assert candidate(82) == 29160
    assert candidate(164) == 236169
    assert candidate(158) == 210886
    assert candidate(21) == 399
    assert candidate(12) == 60
    assert candidate(91) == 40050
    assert candidate(40) == 3211
    assert candidate(142) == 154630
    assert candidate(190) == 373086
    assert candidate(167) == 249535
    assert candidate(168) == 255640
    assert candidate(34) == 1936
    assert candidate(50) == 6136
    assert candidate(171) == 269724
    assert candidate(188) == 357461
    assert candidate(60) == 11020
    assert candidate(80) == 26351
    assert candidate(112) == 75295
    assert candidate(195) == 401440
    assert candidate(64) == 13671
    assert candidate(200) == 431211
    assert candidate(191) == 375039
    assert candidate(102) == 56100
    assert candidate(79) == 26026
    assert candidate(27) == 900
    assert candidate(176) == 292639
    assert candidate(76) == 23125
    assert candidate(63) == 12810
    assert candidate(97) == 48640
    assert candidate(71) == 18239
    assert candidate(196) == 409825
    assert candidate(26) == 764
    assert candidate(192) == 383040
    assert candidate(15) == 130
    assert candidate(42) == 3640
    assert candidate(96) == 46624
    assert candidate(62) == 11990
    assert candidate(137) == 136665
    assert candidate(106) == 63700
    assert candidate(127) == 110250
    assert candidate(54) == 7956
    assert candidate(109) == 69336
    assert candidate(6) == 4
    assert candidate(47) == 5055
    assert candidate(149) == 176449
    assert candidate(150) == 181300
    assert candidate(67) == 15730
    assert candidate(2) == 0
    assert candidate(129) == 114681
    assert candidate(189) == 365211
    assert candidate(114) == 78736
    assert candidate(181) == 322200
    assert candidate(155) == 198951
    assert candidate(36) == 2244
    assert candidate(53) == 7361
    assert candidate(107) == 64295
    assert candidate(10) == 36
    assert candidate(100) == 53361

if __name__ == '__main__':
    check(get_max_triples)