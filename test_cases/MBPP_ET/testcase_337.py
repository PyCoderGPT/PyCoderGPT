from case_MBPP_337 import noprofit_noloss


def check(candidate):
    assert candidate(1500,1200)==False
    assert candidate(100,100)==True
    assert candidate(2000,5000)==False
    assert candidate(1883, 2025) == False
    assert candidate(1774, 2019) == False
    assert candidate(998, 1512) == False
    assert candidate(634, 1855) == False
    assert candidate(1005, 2004) == False
    assert candidate(1094, 1510) == False
    assert candidate(644, 1556) == False
    assert candidate(1056, 1434) == False
    assert candidate(867, 256) == False
    assert candidate(948, 2063) == False
    assert candidate(1761, 1496) == False
    assert candidate(1447, 1148) == False
    assert candidate(828, 1244) == False
    assert candidate(2046, 2144) == False
    assert candidate(2022, 2167) == False
    assert candidate(819, 1157) == False
    assert candidate(1618, 1314) == False
    assert candidate(2100, 1009) == False
    assert candidate(1532, 1243) == False
    assert candidate(1136, 657) == False
    assert candidate(1378, 2105) == False
    assert candidate(2044, 686) == False
    assert candidate(1597, 532) == False
    assert candidate(728, 1519) == False
    assert candidate(1235, 396) == False
    assert candidate(1325, 532) == False
    assert candidate(2449, 1882) == False
    assert candidate(1166, 2064) == False
    assert candidate(1040, 780) == False
    assert candidate(925, 420) == False
    assert candidate(1627, 1786) == False
    assert candidate(882, 1568) == False
    assert candidate(1800, 2003) == False
    assert candidate(105, 99) == False
    assert candidate(100, 101) == False
    assert candidate(100, 102) == False
    assert candidate(98, 101) == False
    assert candidate(104, 98) == False
    assert candidate(98, 99) == False
    assert candidate(98, 97) == False
    assert candidate(95, 103) == False
    assert candidate(95, 103) == False
    assert candidate(104, 102) == False
    assert candidate(95, 99) == False
    assert candidate(98, 96) == False
    assert candidate(100, 95) == False
    assert candidate(96, 99) == False
    assert candidate(100, 104) == False
    assert candidate(98, 98) == True
    assert candidate(104, 97) == False
    assert candidate(98, 97) == False
    assert candidate(99, 103) == False
    assert candidate(97, 99) == False
    assert candidate(100, 97) == False
    assert candidate(98, 96) == False
    assert candidate(102, 103) == False
    assert candidate(98, 98) == True
    assert candidate(97, 103) == False
    assert candidate(96, 96) == True
    assert candidate(96, 95) == False
    assert candidate(100, 97) == False
    assert candidate(99, 101) == False
    assert candidate(99, 97) == False
    assert candidate(100, 97) == False
    assert candidate(100, 98) == False
    assert candidate(101, 96) == False
    assert candidate(1330, 4491) == False
    assert candidate(2175, 5335) == False
    assert candidate(1809, 5537) == False
    assert candidate(1282, 4947) == False
    assert candidate(2650, 4594) == False
    assert candidate(1927, 5125) == False
    assert candidate(1281, 4989) == False
    assert candidate(1219, 5208) == False
    assert candidate(2683, 5530) == False
    assert candidate(1695, 4881) == False
    assert candidate(2309, 4089) == False
    assert candidate(2724, 5077) == False
    assert candidate(2783, 5184) == False
    assert candidate(2221, 5547) == False
    assert candidate(1662, 4929) == False
    assert candidate(1303, 4446) == False
    assert candidate(1282, 5805) == False
    assert candidate(2817, 4044) == False
    assert candidate(2732, 5318) == False
    assert candidate(1951, 5192) == False
    assert candidate(2642, 4673) == False
    assert candidate(2167, 5342) == False
    assert candidate(2643, 5253) == False
    assert candidate(1459, 4632) == False
    assert candidate(2753, 5134) == False
    assert candidate(1491, 4991) == False
    assert candidate(2363, 4408) == False
    assert candidate(2197, 4388) == False
    assert candidate(1177, 4762) == False
    assert candidate(1028, 5607) == False
    assert candidate(2225, 5932) == False
    assert candidate(1589, 5527) == False
    assert candidate(1089, 4031) == False

if __name__ == '__main__':
    check(noprofit_noloss)