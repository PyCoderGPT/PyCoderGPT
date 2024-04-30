from case_HE_082 import prime_length


def check(candidate):
    assert candidate("jbmqdwtvhggs") == False
    assert candidate('') == False
    assert candidate("nvyptlgbqohuyzhxa") == True
    assert candidate("jyqqpdapyzeytzzeg") == True
    assert candidate("hspswo") == False
    assert candidate("dxn") == True
    assert candidate("ZNGakV") == False
    assert candidate("rgToy") == True
    assert candidate("ihngswanrco") == True
    assert candidate("tjrAO") == True
    assert candidate("KKZUZ") == True
    assert candidate('M') == False
    assert candidate('0') == False
    assert candidate("qyfrfqfrk") == False
    assert candidate('wow') == True
    assert candidate("K") == False
    assert candidate("bvapxjkbeidr") == False
    assert candidate("wwIQdHJO") == False
    assert candidate("FFFHK") == True
    assert candidate("ker") == True
    assert candidate("jxrsid") == False
    assert candidate("RzcKTUMY") == False
    assert candidate("LhMKFpz") == True
    assert candidate("qchjyep") == True
    assert candidate("xCOH") == False
    assert candidate("qfymul") == False
    assert candidate("RXWYQ") == True
    assert candidate("dvqzd") == True
    assert candidate("t") == False
    assert candidate("sjaprrmn") == False
    assert candidate("iirpz") == True
    assert candidate("npprtgh") == True
    assert candidate("O") == False
    assert candidate("QOQbMgiYa") == False
    assert candidate("ovdreywuo") == False
    assert candidate("nntrracrwmohj") == True
    assert candidate('HI') == True
    assert candidate("opumjzxrrcgwsktjnivm") == False
    assert candidate("hnsfqprypsu") == True
    assert candidate("eli") == True
    assert candidate("dqv") == True
    assert candidate("QHC") == True
    assert candidate("aQW") == True
    assert candidate("gfnDFP") == False
    assert candidate("vPlgFeox") == False
    assert candidate("woj") == True
    assert candidate("pivnccob") == False
    assert candidate("ACwrd") == True
    assert candidate('gogo') == False
    assert candidate("pfdybfcv") == False
    assert candidate("imP") == True
    assert candidate("shx") == True
    assert candidate("agrox") == True
    assert candidate("xbZflKTlX") == False
    assert candidate("cmqpqfydpvzwnsxewhzf") == False
    assert candidate("sskt") == False
    assert candidate("xlvxscr") == True
    assert candidate("njttx") == True
    assert candidate("cjIfCschr") == False
    assert candidate("slden") == True
    assert candidate("rtwofnjpq") == False
    assert candidate('Wow') == True
    assert candidate("tu") == True
    assert candidate('MadaM') == True
    assert candidate('world') == True
    assert candidate("tEvHnl") == False
    assert candidate("fmvpwsnmexejwelfzrwd") == False
    assert candidate("U") == False
    assert candidate("ols") == True
    assert candidate("M") == False
    assert candidate("ynslwx") == False
    assert candidate("ipuadvzafio") == True
    assert candidate("tzivbr") == False
    assert candidate("HGXWQ") == True
    assert candidate("A") == False
    assert candidate("tXx") == True
    assert candidate('Hello') == True
    assert candidate("mlgjcwr") == True
    assert candidate("ouu") == True
    assert candidate("thmdu") == True
    assert candidate("rlqmycut") == False
    assert candidate("bokic") == True
    assert candidate("rpbojn") == False
    assert candidate("bZlkvUQw") == False
    assert candidate("wZQhHpZ") == True
    assert candidate("franuetws") == False
    assert candidate("jeie") == False
    assert candidate('go') == True
    assert candidate("lqv") == True
    assert candidate("UrDBLbeLu") == False
    assert candidate("jJpkg") == True
    assert candidate("ftfaho") == False
    assert candidate("T") == False
    assert candidate("czxkhyfbyrqq") == False
    assert candidate("Q") == False
    assert candidate("ltok") == False
    assert candidate("jnln") == False
    assert candidate("Z") == False
    assert candidate("GJT") == True
    assert candidate("nktpxkp") == True
    assert candidate("qqeutcwkaubezglnynmo") == False
    assert candidate("CLkWVAy") == True
    assert candidate("flvsizus") == False
    assert candidate("ojj") == True
    assert candidate("z") == False
    assert candidate("epfrnej") == True
    assert candidate('kittens') == True
    assert candidate("czwX") == False
    assert candidate("fuc") == True
    assert candidate("abxzTRAvy") == False
    assert candidate("OXLRMH") == False
    assert candidate("lgtybs") == False
    assert candidate("ZJmxcsrY") == False
    assert candidate("l") == False
    assert candidate("uYCFavt") == True
    assert candidate("RGBbsrmp") == False
    assert candidate("jkgGmgN") == True
    assert candidate("juuknp") == False
    assert candidate("TYB") == True
    assert candidate("glho") == False
    assert candidate('aaaaaaaaaaaaaaa') == False

    # Check some edge cases that are easy to work out by hand.
    assert candidate("kajdcplp") == False
    assert candidate("hsidwvp") == True
    assert candidate("EMwCiT") == False
    assert candidate("PcaJIZ") == False
    assert candidate("diwb") == False
    assert candidate("cSvovfhBl") == False
    assert candidate('orange') == False
    assert candidate("gamrlrwjxat") == True
    assert candidate("tmuyfsz") == True
    assert candidate('Madam') == True
    assert candidate("aqvfw") == True
    assert candidate('abcdcba') == True
    assert candidate("iwekhb") == False
    assert candidate("qdfzqf") == False
    assert candidate("dirdF") == True

if __name__ == '__main__':
    check(prime_length)