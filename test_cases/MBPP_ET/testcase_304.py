from case_MBPP_304 import armstrong_number


def check(candidate):
    assert candidate(153)==True
    assert candidate(259)==False
    assert candidate(4458)==False
    assert candidate(154) == False
    assert candidate(154) == False
    assert candidate(158) == False
    assert candidate(150) == False
    assert candidate(154) == False
    assert candidate(149) == False
    assert candidate(155) == False
    assert candidate(156) == False
    assert candidate(158) == False
    assert candidate(148) == False
    assert candidate(148) == False
    assert candidate(158) == False
    assert candidate(156) == False
    assert candidate(155) == False
    assert candidate(152) == False
    assert candidate(154) == False
    assert candidate(152) == False
    assert candidate(150) == False
    assert candidate(148) == False
    assert candidate(149) == False
    assert candidate(153) == True
    assert candidate(151) == False
    assert candidate(156) == False
    assert candidate(155) == False
    assert candidate(153) == True
    assert candidate(149) == False
    assert candidate(151) == False
    assert candidate(158) == False
    assert candidate(152) == False
    assert candidate(148) == False
    assert candidate(157) == False
    assert candidate(156) == False
    assert candidate(158) == False
    assert candidate(259) == False
    assert candidate(257) == False
    assert candidate(264) == False
    assert candidate(257) == False
    assert candidate(262) == False
    assert candidate(264) == False
    assert candidate(255) == False
    assert candidate(254) == False
    assert candidate(261) == False
    assert candidate(256) == False
    assert candidate(254) == False
    assert candidate(263) == False
    assert candidate(258) == False
    assert candidate(264) == False
    assert candidate(259) == False
    assert candidate(260) == False
    assert candidate(261) == False
    assert candidate(264) == False
    assert candidate(263) == False
    assert candidate(257) == False
    assert candidate(257) == False
    assert candidate(262) == False
    assert candidate(264) == False
    assert candidate(262) == False
    assert candidate(254) == False
    assert candidate(261) == False
    assert candidate(259) == False
    assert candidate(264) == False
    assert candidate(263) == False
    assert candidate(259) == False
    assert candidate(264) == False
    assert candidate(260) == False
    assert candidate(261) == False
    assert candidate(4596) == False
    assert candidate(5293) == False
    assert candidate(5283) == False
    assert candidate(4957) == False
    assert candidate(5147) == False
    assert candidate(5305) == False
    assert candidate(4695) == False
    assert candidate(3537) == False
    assert candidate(3958) == False
    assert candidate(5125) == False
    assert candidate(4028) == False
    assert candidate(5294) == False
    assert candidate(3414) == False
    assert candidate(4542) == False
    assert candidate(4868) == False
    assert candidate(3631) == False
    assert candidate(5354) == False
    assert candidate(5045) == False
    assert candidate(4376) == False
    assert candidate(4164) == False
    assert candidate(4813) == False
    assert candidate(4423) == False
    assert candidate(4169) == False
    assert candidate(3964) == False
    assert candidate(5160) == False
    assert candidate(4777) == False
    assert candidate(4100) == False
    assert candidate(4674) == False
    assert candidate(5054) == False
    assert candidate(4542) == False
    assert candidate(4452) == False
    assert candidate(4775) == False
    assert candidate(5399) == False

if __name__ == '__main__':
    check(armstrong_number)