from case_HE_067 import fruit_distribution


def check(candidate):
    assert candidate('2 apples and 3 oranges', 525) == 520
    assert candidate('2 apples and 3 oranges', 794) == 789
    assert candidate('2 apples and 3 oranges', 489) == 484
    assert candidate('2 apples and 3 oranges', 758) == 753
    assert candidate('5 apples and 6 oranges', 982) == 971
    assert candidate('2 apples and 3 oranges', 24) == 19
    assert candidate('2 apples and 3 oranges', 786) == 781
    assert candidate('2 apples and 3 oranges', 351) == 346
    assert candidate('5 apples and 6 oranges', 426) == 415
    assert candidate("1 apples and 100 oranges",120) == 19
    assert candidate('0 apples and 1 oranges', 477) == 476
    assert candidate('0 apples and 1 oranges', 390) == 389
    assert candidate('5 apples and 6 oranges', 497) == 486
    assert candidate("5 apples and 6 oranges",21) == 10
    assert candidate('2 apples and 3 oranges', 827) == 822
    assert candidate('0 apples and 1 oranges', 95) == 94
    assert candidate('1 apples and 0 oranges', 136) == 135
    assert candidate('1 apples and 0 oranges', 871) == 870
    assert candidate('0 apples and 1 oranges', 604) == 603
    assert candidate('2 apples and 3 oranges', 588) == 583
    assert candidate('5 apples and 6 oranges', 185) == 174
    assert candidate('5 apples and 6 oranges', 861) == 850
    assert candidate('2 apples and 3 oranges', 595) == 590
    assert candidate('5 apples and 6 oranges', 261) == 250
    assert candidate('0 apples and 1 oranges', 894) == 893
    assert candidate('2 apples and 3 oranges', 949) == 944
    assert candidate('1 apples and 0 oranges', 228) == 227
    assert candidate('5 apples and 6 oranges', 899) == 888
    assert candidate('5 apples and 6 oranges', 269) == 258
    assert candidate('0 apples and 1 oranges', 618) == 617
    assert candidate('5 apples and 6 oranges', 83) == 72
    assert candidate('5 apples and 6 oranges', 955) == 944
    assert candidate('2 apples and 3 oranges', 449) == 444
    assert candidate('5 apples and 6 oranges', 996) == 985
    assert candidate('2 apples and 3 oranges', 230) == 225
    assert candidate('5 apples and 6 oranges', 124) == 113
    assert candidate('5 apples and 6 oranges', 817) == 806
    assert candidate("2 apples and 3 oranges",5) == 0
    assert candidate('5 apples and 6 oranges', 193) == 182
    assert candidate('2 apples and 3 oranges', 322) == 317
    assert candidate('5 apples and 6 oranges', 553) == 542
    assert candidate('0 apples and 1 oranges', 738) == 737
    assert candidate('5 apples and 6 oranges', 771) == 760
    assert candidate('5 apples and 6 oranges', 869) == 858
    assert candidate('2 apples and 3 oranges', 839) == 834
    assert candidate("1 apples and 0 oranges",3) == 2
    assert candidate('5 apples and 6 oranges', 633) == 622
    assert candidate('1 apples and 0 oranges', 409) == 408
    assert candidate('2 apples and 3 oranges', 103) == 98
    assert candidate('2 apples and 3 oranges', 629) == 624
    assert candidate('2 apples and 3 oranges', 433) == 428
    assert candidate('2 apples and 3 oranges', 302) == 297
    assert candidate('2 apples and 3 oranges', 124) == 119
    assert candidate('0 apples and 1 oranges', 767) == 766
    assert candidate('5 apples and 6 oranges', 270) == 259
    assert candidate('0 apples and 1 oranges', 760) == 759
    assert candidate('5 apples and 6 oranges', 231) == 220
    assert candidate('5 apples and 6 oranges', 574) == 563
    assert candidate('2 apples and 3 oranges', 550) == 545
    assert candidate('2 apples and 3 oranges', 628) == 623
    assert candidate('0 apples and 1 oranges', 415) == 414
    assert candidate('2 apples and 3 oranges', 282) == 277
    assert candidate('2 apples and 3 oranges', 342) == 337
    assert candidate('5 apples and 6 oranges', 991) == 980
    assert candidate('1 apples and 0 oranges', 244) == 243
    assert candidate('1 apples and 0 oranges', 952) == 951
    assert candidate('5 apples and 6 oranges', 204) == 193
    assert candidate('1 apples and 0 oranges', 177) == 176
    assert candidate('2 apples and 3 oranges', 298) == 293
    assert candidate('1 apples and 0 oranges', 127) == 126
    assert candidate('5 apples and 6 oranges', 723) == 712
    assert candidate("0 apples and 1 oranges",3) == 2
    assert candidate('1 apples and 0 oranges', 444) == 443
    assert candidate('5 apples and 6 oranges', 271) == 260
    assert candidate('2 apples and 3 oranges', 522) == 517
    assert candidate('5 apples and 6 oranges', 728) == 717
    assert candidate('0 apples and 1 oranges', 888) == 887
    assert candidate('5 apples and 6 oranges', 616) == 605
    assert candidate('2 apples and 3 oranges', 756) == 751
    assert candidate('0 apples and 1 oranges', 291) == 290
    assert candidate('5 apples and 6 oranges', 740) == 729
    assert candidate('2 apples and 3 oranges', 67) == 62
    assert candidate("5 apples and 6 oranges",19) == 8
    assert candidate('0 apples and 1 oranges', 588) == 587
    assert candidate('5 apples and 6 oranges', 554) == 543
    assert candidate('1 apples and 0 oranges', 421) == 420
    assert candidate('1 apples and 0 oranges', 283) == 282
    assert candidate('5 apples and 6 oranges', 979) == 968
    assert candidate('2 apples and 3 oranges', 669) == 664
    assert candidate('5 apples and 6 oranges', 285) == 274
    assert candidate('0 apples and 1 oranges', 748) == 747
    assert candidate('2 apples and 3 oranges', 945) == 940
    assert candidate('2 apples and 3 oranges', 288) == 283
    assert candidate('1 apples and 0 oranges', 832) == 831
    assert candidate("2 apples and 3 oranges",100) == 95
    assert candidate('2 apples and 3 oranges', 274) == 269
    assert candidate('0 apples and 1 oranges', 377) == 376
    assert candidate('2 apples and 3 oranges', 491) == 486
    assert candidate('0 apples and 1 oranges', 640) == 639
    assert candidate('1 apples and 0 oranges', 852) == 851
    assert candidate('5 apples and 6 oranges', 640) == 629
    assert candidate('1 apples and 0 oranges', 555) == 554
    assert candidate('5 apples and 6 oranges', 987) == 976
    assert candidate('5 apples and 6 oranges', 197) == 186
    assert candidate('2 apples and 3 oranges', 715) == 710
    assert candidate('0 apples and 1 oranges', 659) == 658
    assert candidate('0 apples and 1 oranges', 878) == 877
    assert candidate('1 apples and 0 oranges', 964) == 963
    assert candidate('1 apples and 0 oranges', 861) == 860
    assert candidate('1 apples and 0 oranges', 578) == 577
    assert candidate('5 apples and 6 oranges', 733) == 722
    assert candidate('2 apples and 3 oranges', 607) == 602
    assert candidate('2 apples and 3 oranges', 150) == 145
    assert candidate('5 apples and 6 oranges', 221) == 210
    assert candidate('1 apples and 0 oranges', 640) == 639

if __name__ == '__main__':
    check(fruit_distribution)