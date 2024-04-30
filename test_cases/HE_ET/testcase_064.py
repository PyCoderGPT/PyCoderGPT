from case_HE_064 import vowels_count


def check(candidate):
    assert candidate("WLKSXobNl") == 1
    assert candidate("dpC") == 0
    assert candidate("orafghw") == 2
    assert candidate("SvTf") == 0
    assert candidate("Rcr") == 0
    assert candidate("wtkaaiog") == 4
    assert candidate("jOGDc") == 1
    assert candidate("wAI") == 2
    assert candidate("zxey") == 2
    assert candidate("ACEDY") == 3, "Test 7"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("sxi") == 1
    assert candidate("IpxQpEdED") == 3
    assert candidate("chwi") == 1
    assert candidate("uisRpsKyZ") == 2
    assert candidate("YLisRX") == 1
    assert candidate("HksjnLrww") == 0
    assert candidate("iMmdG") == 1
    assert candidate("nVTx") == 0
    assert candidate("bzdyyst") == 0
    assert candidate("jcabto") == 2
    assert candidate("ezAsFRyO") == 3
    assert candidate("bye") == 1, "Test 4"
    assert candidate("qagoecrk") == 3
    assert candidate("htffm") == 0
    assert candidate("lUjeam") == 3
    assert candidate("dfe") == 1
    assert candidate("uraZwroZg") == 3
    assert candidate("bcrxedi") == 2
    assert candidate("fuoa") == 3
    assert candidate("vsup") == 1
    assert candidate("pkmive") == 2
    assert candidate("keY") == 2, "Test 5"
    assert candidate("LvVQtCdIS") == 1
    assert candidate("wzlmdYJFQ") == 0
    assert candidate("RdpTSCBxO") == 1
    assert candidate("bajxqza") == 2
    assert candidate("YUrSQAWp") == 2
    assert candidate("xenm") == 1
    assert candidate("Gsrlcd") == 0
    assert candidate("wplrjvkt") == 0
    assert candidate("yHLp") == 0
    assert candidate("PqT") == 0
    assert candidate("HsHUjl") == 1
    assert candidate("fzsen") == 1
    assert candidate("abcde") == 2, "Test 1"
    assert candidate("axf") == 1
    assert candidate("wvdvd") == 0
    assert candidate("EftkljPHH") == 1
    assert candidate("UeGm") == 2
    assert candidate("Cnd") == 0
    assert candidate("largjSFz") == 1
    assert candidate("Alone") == 3, "Test 2"
    assert candidate("opbbocbx") == 2
    assert candidate("qkbZfvFfG") == 0
    assert candidate("xgyeq") == 1
    assert candidate("Dlll") == 0
    assert candidate("yxdkra") == 1
    assert candidate("ThZJJ") == 0
    assert candidate("wftbmsp") == 0
    assert candidate("qtqu") == 1
    assert candidate("nnq") == 0
    assert candidate("SFLHyx") == 0
    assert candidate("eqvenle") == 3
    assert candidate("pfbuf") == 1
    assert candidate("nouzf") == 2
    assert candidate("qvt") == 0
    assert candidate("JRteFuBsm") == 2
    assert candidate("JdT") == 0
    assert candidate("iraTR") == 2
    assert candidate("xCpqwzZNO") == 1
    assert candidate("ZZpBY") == 1
    assert candidate("bYe") == 1, "Test 6"
    assert candidate("bprwrlz") == 0
    assert candidate("srezvdbi") == 2
    assert candidate("xmzjzfsd") == 0
    assert candidate("jder") == 1
    assert candidate("pFGheLS") == 1
    assert candidate("wkKhkykC") == 0
    assert candidate("pttuuh") == 2
    assert candidate("lknisac") == 2
    assert candidate("cukdnxkxw") == 1
    assert candidate("key") == 2, "Test 3"
    assert candidate("DgxnzsbRN") == 0
    assert candidate("VVdjTksh") == 0
    assert candidate("mgmstfzm") == 0
    assert candidate("fivkg") == 1
    assert candidate("aprpbhbva") == 2
    assert candidate("LBRPmeox") == 2
    assert candidate("aAboay") == 5
    assert candidate("gTfkWkL") == 0
    assert candidate("yxnk") == 0
    assert candidate("bajvbd") == 1
    assert candidate("czkp") == 0
    assert candidate("qSbxpNy") == 1
    assert candidate("dcsjaykkn") == 1
    assert candidate("xyichsbq") == 1
    assert candidate("jxglz") == 0
    assert candidate("hwlT") == 0
    assert candidate("kue") == 2
    assert candidate("Jxfs") == 0
    assert candidate("frw") == 0
    assert candidate("ofxgqm") == 1
    assert candidate("gqAOEgKW") == 3
    assert candidate("qwpllpe") == 1
    assert candidate("TtGtnDI") == 1
    assert candidate("knkdhm") == 0
    assert candidate("lNjkjaQ") == 1
    assert candidate("rBKaNrSZf") == 1
    assert candidate("ryll") == 0
    assert candidate("uiaTUA") == 5
    assert candidate("hlkaasqi") == 3
    assert candidate("bctkur") == 1
    assert candidate("QuzI") == 2
    assert candidate("EVsqd") == 1
    assert candidate("cmmacbu") == 2

if __name__ == '__main__':
    check(vowels_count)