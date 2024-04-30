from case_MBPP_174 import colon_tuplex


def check(candidate):
    assert candidate(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True) 
    assert candidate(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert candidate(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)
    assert candidate(('EXIX', 4, [], 6), 2, 48) == ('EXIX', 4, [48], 6)
    assert candidate(('BNKZ', 8, [], 5), 2, 48) == ('BNKZ', 8, [48], 5)
    assert candidate(('FGNFWJXD', 10, [], 4), 2, 53) == ('FGNFWJXD', 10, [53], 4)
    assert candidate(('WJFDJAKSD', 9, [], 6), 2, 49) == ('WJFDJAKSD', 9, [49], 6)
    assert candidate(('FACLI', 8, [], 5), 2, 49) == ('FACLI', 8, [49], 5)
    assert candidate(('ZPIOB', 8, [], 3), 2, 45) == ('ZPIOB', 8, [45], 3)
    assert candidate(('KAPW', 1, [], 1), 2, 50) == ('KAPW', 1, [50], 1)
    assert candidate(('CWGDJ', 2, [], 6), 2, 47) == ('CWGDJ', 2, [47], 6)
    assert candidate(('CQBELMZ', 2, [], 3), 2, 45) == ('CQBELMZ', 2, [45], 3)
    assert candidate(('PEBPPM', 1, [], 5), 2, 54) == ('PEBPPM', 1, [54], 5)
    assert candidate(('AOD', 9, [], 3), 2, 51) == ('AOD', 9, [51], 3)
    assert candidate(('OQHLZFLH', 7, [], 5), 2, 53) == ('OQHLZFLH', 7, [53], 5)
    assert candidate(('EECYNCM', 5, [], 6), 2, 53) == ('EECYNCM', 5, [53], 6)
    assert candidate(('VYWJQY', 10, [], 5), 2, 48) == ('VYWJQY', 10, [48], 5)
    assert candidate(('WTBABHJV', 4, [], 2), 2, 51) == ('WTBABHJV', 4, [51], 2)
    assert candidate(('XPVIYIBP', 9, [], 1), 2, 49) == ('XPVIYIBP', 9, [49], 1)
    assert candidate(('ZAHSRAJ', 3, [], 2), 2, 48) == ('ZAHSRAJ', 3, [48], 2)
    assert candidate(('OEB', 3, [], 1), 2, 49) == ('OEB', 3, [49], 1)
    assert candidate(('ZWIV', 10, [], 2), 2, 47) == ('ZWIV', 10, [47], 2)
    assert candidate(('RUJOTRDLL', 5, [], 6), 2, 50) == ('RUJOTRDLL', 5, [50], 6)
    assert candidate(('KVJXSAV', 2, [], 3), 2, 45) == ('KVJXSAV', 2, [45], 3)
    assert candidate(('TAVBCWWNI', 6, [], 6), 2, 49) == ('TAVBCWWNI', 6, [49], 6)
    assert candidate(('RELRMEIR', 9, [], 2), 2, 52) == ('RELRMEIR', 9, [52], 2)
    assert candidate(('RIWWHSSKU', 5, [], 1), 2, 48) == ('RIWWHSSKU', 5, [48], 1)
    assert candidate(('GLLQBZDU', 1, [], 4), 2, 47) == ('GLLQBZDU', 1, [47], 4)
    assert candidate(('PAUWYGNY', 4, [], 2), 2, 50) == ('PAUWYGNY', 4, [50], 2)
    assert candidate(('IFZVY', 5, [], 5), 2, 45) == ('IFZVY', 5, [45], 5)
    assert candidate(('FDGTLUYT', 3, [], 5), 2, 47) == ('FDGTLUYT', 3, [47], 5)
    assert candidate(('GNDFIT', 4, [], 6), 2, 54) == ('GNDFIT', 4, [54], 6)
    assert candidate(('YWENUFVPH', 10, [], 5), 2, 48) == ('YWENUFVPH', 10, [48], 5)
    assert candidate(('JZZ', 5, [], 5), 2, 54) == ('JZZ', 5, [54], 5)
    assert candidate(('VMKB', 3, [], 2), 2, 48) == ('VMKB', 3, [48], 2)
    assert candidate(('UYRULW', 9, [], 5), 2, 51) == ('UYRULW', 9, [51], 5)
    assert candidate(('MFGWVFKQ', 7, [], 2), 2, 100) == ('MFGWVFKQ', 7, [100], 2)
    assert candidate(('ALMWNH', 5, [], 5), 2, 99) == ('ALMWNH', 5, [99], 5)
    assert candidate(('BPHSO', 6, [], 6), 2, 104) == ('BPHSO', 6, [104], 6)
    assert candidate(('ZFPHRNA', 5, [], 4), 2, 104) == ('ZFPHRNA', 5, [104], 4)
    assert candidate(('MQB', 5, [], 1), 2, 105) == ('MQB', 5, [105], 1)
    assert candidate(('CTAKDOO', 6, [], 1), 2, 99) == ('CTAKDOO', 6, [99], 1)
    assert candidate(('ZUAONMV', 9, [], 5), 2, 98) == ('ZUAONMV', 9, [98], 5)
    assert candidate(('NQOAJ', 4, [], 3), 2, 99) == ('NQOAJ', 4, [99], 3)
    assert candidate(('DDEPFD', 3, [], 6), 2, 95) == ('DDEPFD', 3, [95], 6)
    assert candidate(('QXHOMXK', 9, [], 5), 2, 102) == ('QXHOMXK', 9, [102], 5)
    assert candidate(('LIYNM', 4, [], 1), 2, 105) == ('LIYNM', 4, [105], 1)
    assert candidate(('HWXVU', 10, [], 1), 2, 96) == ('HWXVU', 10, [96], 1)
    assert candidate(('IBS', 10, [], 4), 2, 99) == ('IBS', 10, [99], 4)
    assert candidate(('PDJTEQMP', 8, [], 6), 2, 99) == ('PDJTEQMP', 8, [99], 6)
    assert candidate(('JMB', 8, [], 4), 2, 101) == ('JMB', 8, [101], 4)
    assert candidate(('YDMHUXXV', 7, [], 5), 2, 105) == ('YDMHUXXV', 7, [105], 5)
    assert candidate(('SBB', 1, [], 3), 2, 101) == ('SBB', 1, [101], 3)
    assert candidate(('DHPAMOVJW', 10, [], 2), 2, 98) == ('DHPAMOVJW', 10, [98], 2)
    assert candidate(('MHIGJT', 9, [], 2), 2, 101) == ('MHIGJT', 9, [101], 2)
    assert candidate(('GIIFFM', 4, [], 4), 2, 95) == ('GIIFFM', 4, [95], 4)
    assert candidate(('XFTCOLT', 5, [], 1), 2, 102) == ('XFTCOLT', 5, [102], 1)
    assert candidate(('AOLXX', 2, [], 4), 2, 102) == ('AOLXX', 2, [102], 4)
    assert candidate(('RTW', 2, [], 5), 2, 105) == ('RTW', 2, [105], 5)
    assert candidate(('PDPQCRWYI', 4, [], 6), 2, 95) == ('PDPQCRWYI', 4, [95], 6)
    assert candidate(('WYG', 1, [], 3), 2, 96) == ('WYG', 1, [96], 3)
    assert candidate(('XELUQGAG', 1, [], 2), 2, 102) == ('XELUQGAG', 1, [102], 2)
    assert candidate(('TEBU', 2, [], 4), 2, 105) == ('TEBU', 2, [105], 4)
    assert candidate(('HKXAHUS', 7, [], 3), 2, 102) == ('HKXAHUS', 7, [102], 3)
    assert candidate(('RCFCINKM', 4, [], 2), 2, 95) == ('RCFCINKM', 4, [95], 2)
    assert candidate(('ZGBQ', 6, [], 1), 2, 96) == ('ZGBQ', 6, [96], 1)
    assert candidate(('BDJKYSRRI', 10, [], 6), 2, 104) == ('BDJKYSRRI', 10, [104], 6)
    assert candidate(('SWPESA', 5, [], 1), 2, 105) == ('SWPESA', 5, [105], 1)
    assert candidate(('USJBL', 1, [], 2), 2, 96) == ('USJBL', 1, [96], 2)
    assert candidate(('WPU', 6, [], 5), 2, 503) == ('WPU', 6, [503], 5)
    assert candidate(('YEN', 9, [], 4), 2, 504) == ('YEN', 9, [504], 4)
    assert candidate(('UZVBZ', 7, [], 6), 2, 502) == ('UZVBZ', 7, [502], 6)
    assert candidate(('IWSPGZC', 9, [], 3), 2, 496) == ('IWSPGZC', 9, [496], 3)
    assert candidate(('XHMWZ', 5, [], 1), 2, 498) == ('XHMWZ', 5, [498], 1)
    assert candidate(('ZNIBYZKHB', 1, [], 4), 2, 496) == ('ZNIBYZKHB', 1, [496], 4)
    assert candidate(('FZIHPVDC', 5, [], 4), 2, 503) == ('FZIHPVDC', 5, [503], 4)
    assert candidate(('CHRPLEDEH', 10, [], 5), 2, 498) == ('CHRPLEDEH', 10, [498], 5)
    assert candidate(('VTKMN', 4, [], 3), 2, 501) == ('VTKMN', 4, [501], 3)
    assert candidate(('RRZDZ', 5, [], 4), 2, 498) == ('RRZDZ', 5, [498], 4)
    assert candidate(('JYLAS', 5, [], 3), 2, 499) == ('JYLAS', 5, [499], 3)
    assert candidate(('VUOSSQBRX', 2, [], 2), 2, 504) == ('VUOSSQBRX', 2, [504], 2)
    assert candidate(('HBQFTAPFV', 6, [], 1), 2, 500) == ('HBQFTAPFV', 6, [500], 1)
    assert candidate(('QUTTPM', 5, [], 4), 2, 502) == ('QUTTPM', 5, [502], 4)
    assert candidate(('BMQJJHEDE', 1, [], 5), 2, 501) == ('BMQJJHEDE', 1, [501], 5)
    assert candidate(('RHTWOZ', 2, [], 3), 2, 501) == ('RHTWOZ', 2, [501], 3)
    assert candidate(('JAJWQ', 3, [], 5), 2, 505) == ('JAJWQ', 3, [505], 5)
    assert candidate(('HFSGQ', 5, [], 5), 2, 501) == ('HFSGQ', 5, [501], 5)
    assert candidate(('CVULNZLT', 2, [], 5), 2, 498) == ('CVULNZLT', 2, [498], 5)
    assert candidate(('DAVWWNPUX', 4, [], 4), 2, 497) == ('DAVWWNPUX', 4, [497], 4)
    assert candidate(('AJFFYO', 10, [], 3), 2, 500) == ('AJFFYO', 10, [500], 3)
    assert candidate(('XQHCTS', 10, [], 4), 2, 499) == ('XQHCTS', 10, [499], 4)
    assert candidate(('SUVWIBL', 4, [], 4), 2, 501) == ('SUVWIBL', 4, [501], 4)
    assert candidate(('TCUTRAG', 7, [], 5), 2, 496) == ('TCUTRAG', 7, [496], 5)
    assert candidate(('KHANFCR', 3, [], 2), 2, 499) == ('KHANFCR', 3, [499], 2)
    assert candidate(('XBPN', 4, [], 1), 2, 505) == ('XBPN', 4, [505], 1)
    assert candidate(('TPZWNIZTX', 8, [], 5), 2, 504) == ('TPZWNIZTX', 8, [504], 5)
    assert candidate(('XHTYTU', 1, [], 2), 2, 497) == ('XHTYTU', 1, [497], 2)
    assert candidate(('KJAFFNG', 9, [], 4), 2, 503) == ('KJAFFNG', 9, [503], 4)
    assert candidate(('CPHCEZGL', 6, [], 1), 2, 504) == ('CPHCEZGL', 6, [504], 1)
    assert candidate(('LTA', 5, [], 6), 2, 505) == ('LTA', 5, [505], 6)
    assert candidate(('AWLFTG', 6, [], 1), 2, 496) == ('AWLFTG', 6, [496], 1)
    assert candidate(('YGF', 3, [], 2), 2, 502) == ('YGF', 3, [502], 2)

if __name__ == '__main__':
    check(colon_tuplex)