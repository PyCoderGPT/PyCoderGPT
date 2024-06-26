from case_MBPP_239 import loss_amount


def check(candidate):
    assert candidate(1500,1200)==None
    assert candidate(100,200)==100
    assert candidate(2000,5000)==3000
    assert candidate(879, 1079) == 200
    assert candidate(1188, 1972) == 784
    assert candidate(669, 1323) == 654
    assert candidate(2324, 201) == None
    assert candidate(963, 385) == None
    assert candidate(1455, 724) == None
    assert candidate(1362, 1722) == 360
    assert candidate(543, 518) == None
    assert candidate(1032, 2041) == 1009
    assert candidate(969, 1726) == 757
    assert candidate(2396, 971) == None
    assert candidate(761, 1599) == 838
    assert candidate(1997, 1781) == None
    assert candidate(1698, 591) == None
    assert candidate(1843, 1374) == None
    assert candidate(1308, 1078) == None
    assert candidate(811, 1273) == 462
    assert candidate(607, 1880) == 1273
    assert candidate(1749, 391) == None
    assert candidate(1687, 2162) == 475
    assert candidate(674, 1929) == 1255
    assert candidate(1449, 943) == None
    assert candidate(1829, 229) == None
    assert candidate(2154, 412) == None
    assert candidate(770, 1054) == 284
    assert candidate(1859, 272) == None
    assert candidate(1742, 789) == None
    assert candidate(2002, 242) == None
    assert candidate(1159, 1216) == 57
    assert candidate(1897, 1386) == None
    assert candidate(1560, 342) == None
    assert candidate(1505, 559) == None
    assert candidate(2103, 389) == None
    assert candidate(104, 203) == 99
    assert candidate(104, 200) == 96
    assert candidate(103, 200) == 97
    assert candidate(96, 197) == 101
    assert candidate(104, 196) == 92
    assert candidate(99, 202) == 103
    assert candidate(95, 202) == 107
    assert candidate(102, 203) == 101
    assert candidate(95, 202) == 107
    assert candidate(100, 201) == 101
    assert candidate(102, 199) == 97
    assert candidate(105, 198) == 93
    assert candidate(105, 200) == 95
    assert candidate(101, 195) == 94
    assert candidate(99, 198) == 99
    assert candidate(95, 205) == 110
    assert candidate(104, 205) == 101
    assert candidate(100, 205) == 105
    assert candidate(102, 200) == 98
    assert candidate(104, 203) == 99
    assert candidate(100, 196) == 96
    assert candidate(102, 195) == 93
    assert candidate(104, 202) == 98
    assert candidate(95, 198) == 103
    assert candidate(98, 200) == 102
    assert candidate(105, 196) == 91
    assert candidate(105, 200) == 95
    assert candidate(102, 205) == 103
    assert candidate(101, 198) == 97
    assert candidate(104, 196) == 92
    assert candidate(99, 204) == 105
    assert candidate(105, 200) == 95
    assert candidate(97, 202) == 105
    assert candidate(2794, 4558) == 1764
    assert candidate(2607, 5662) == 3055
    assert candidate(1793, 4065) == 2272
    assert candidate(1414, 4934) == 3520
    assert candidate(2855, 5766) == 2911
    assert candidate(1178, 5597) == 4419
    assert candidate(2240, 5162) == 2922
    assert candidate(2196, 5074) == 2878
    assert candidate(2456, 4200) == 1744
    assert candidate(1992, 5857) == 3865
    assert candidate(2869, 4257) == 1388
    assert candidate(2643, 4019) == 1376
    assert candidate(1603, 4234) == 2631
    assert candidate(1592, 4665) == 3073
    assert candidate(2928, 4228) == 1300
    assert candidate(1275, 4864) == 3589
    assert candidate(2452, 5021) == 2569
    assert candidate(1807, 4716) == 2909
    assert candidate(1276, 5101) == 3825
    assert candidate(1068, 4312) == 3244
    assert candidate(2813, 5433) == 2620
    assert candidate(1392, 4286) == 2894
    assert candidate(1217, 4027) == 2810
    assert candidate(2594, 4825) == 2231
    assert candidate(2216, 5531) == 3315
    assert candidate(2064, 5633) == 3569
    assert candidate(1143, 4275) == 3132
    assert candidate(1425, 5373) == 3948
    assert candidate(1645, 5346) == 3701
    assert candidate(2543, 5554) == 3011
    assert candidate(2039, 4290) == 2251
    assert candidate(2737, 5892) == 3155
    assert candidate(2312, 4931) == 2619

if __name__ == '__main__':
    check(loss_amount)