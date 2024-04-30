from case_HE_134 import check_if_last_char_is_a_letter


def check(candidate):
    assert candidate("VqqRDdbPXFl") == False
    assert candidate("tzhnsddx") == False
    assert candidate("oz2NZNzFFrjV") == False
    assert candidate("U U") == True
    assert candidate("meNICdgPjavi") == False
    assert candidate("") == False
    assert candidate("jskamxw") == False
    assert candidate("I I") == True
    assert candidate("vaydkcvogjoijl") == False
    assert candidate("ZPoNzXdigZ") == False
    assert candidate("4Pn7oVnJN3cnhocGQ5") == False
    assert candidate("dma") == False
    assert candidate("eFKpmJKEnSxuJOYd") == False
    assert candidate("gqh") == False
    assert candidate("lcowzv tlmmbz k") == True
    assert candidate("tndhrdo d") == True
    assert candidate("zhsqjuucwlfrk") == False
    assert candidate("VvxZYkkesE") == False
    assert candidate("eeeee") == False
    assert candidate("igqjtp irtb") == False
    assert candidate("f") == True
    assert candidate("jgxielroew fr i") == True
    assert candidate("keatrbvt") == False
    assert candidate("MINKNHyQXjAsWBUisE") == False
    assert candidate("apple") == False
    assert candidate("wj") == False
    assert candidate("k  elw") == False
    assert candidate("kldxco") == False
    assert candidate("jf") == False
    assert candidate("jbrvtastnkkn") == False
    assert candidate("gqvow") == False
    assert candidate("Pumpkin pie 1") == False
    assert candidate("h hxkixyjalb") == False
    assert candidate("ujzenjmemkxpo p") == True
    assert candidate("jumhxk") == False
    assert candidate("i") == True
    assert candidate("gmkzyzq") == False
    assert candidate("apple pi e") == True
    assert candidate(" qwzduxia") == False
    assert candidate("gnjjq") == False
    assert candidate("TBZWphoYT jHncGdbE") == False
    assert candidate("J J") == True
    assert candidate("oardedkxp") == False
    assert candidate("8 e5HJ17rErk") == False
    assert candidate("tqmuft") == False
    assert candidate("ztqfd ptii  ") == False
    assert candidate("j") == True
    assert candidate("apple pie") == False
    assert candidate("ita") == False
    assert candidate("xyITwFd PJCihQ") == False
    assert candidate("aeikqu") == False
    assert candidate("okz") == False
    assert candidate("h3F5gkLi8gUPskIK") == False
    assert candidate("ggiblyzgoa") == False
    assert candidate("szbbwhbkiunz") == False
    assert candidate("ziy") == False
    assert candidate("S S") == True
    assert candidate("llsyqzmbfforar") == False
    assert candidate("pngv") == False
    assert candidate("zyneryxm") == False
    assert candidate("hlywrkczii") == False
    assert candidate("rlnpc") == False
    assert candidate("apple pi e ") == False

    # Check some edge cases that are easy to work out by hand.
    assert candidate("ocLursbxHZ dL") == False
    assert candidate("E E") == True
    assert candidate("ypggzkgeiofhapw") == False
    assert candidate("uyxohyw w") == True
    assert candidate("xyhxquubibt") == False
    assert candidate("J4nbcFY7pN11Dh") == False
    assert candidate("uxuonfira") == False
    assert candidate("L0JKz3DXQuqx") == False
    assert candidate("rbbvx") == False
    assert candidate("swm") == False
    assert candidate("onljsdvhfqoj") == False
    assert candidate("ugjevxw x") == True
    assert candidate("dlpzjmckdt") == False
    assert candidate("ggoxbwuagae") == False
    assert candidate("M M") == True
    assert candidate("vrqcmjkaey y") == True
    assert candidate("Z6oxaGqpFnUp") == False
    assert candidate("obrainbxbavwgbh n") == True
    assert candidate("fzfbr") == False
    assert candidate("zwfwmlij w") == True
    assert candidate("ppsttwqztpx") == False
    assert candidate("t  bfgakod") == False
    assert candidate("sm") == False
    assert candidate("tVF ogIlrx") == False
    assert candidate("nnncfGftbYDEhnjY") == False
    assert candidate("ycbihdu") == False
    assert candidate("tqlserzwaabvlh") == False
    assert candidate("kcforfkqxw") == False
    assert candidate("fN6Sel7c6kPHSH6inZ") == False
    assert candidate("zlvh") == False
    assert candidate("royv") == False
    assert candidate("vl") == False
    assert candidate("ddhbwm") == False
    assert candidate("xdswbkjo") == False
    assert candidate("nwdk") == False
    assert candidate("V") == True
    assert candidate("E") == True
    assert candidate("Pumpkin pie ") == False
    assert candidate("e acin g  ") == False
    assert candidate("wgymztk ") == False
    assert candidate("pczmh") == False
    assert candidate("ybgesnuj b") == True
    assert candidate("A") == True
    assert candidate("coqeqx") == False
    assert candidate("gxlev") == False
    assert candidate("dpmudl") == False
    assert candidate("nhmjoivdi") == False
    assert candidate("Sl42QA5NU") == False
    assert candidate("reuuw") == False
    assert candidate("vclpghngvb fm") == False
    assert candidate("MmcPNDZggEkzPuw") == False
    assert candidate("N N") == True
    assert candidate("o") == True
    assert candidate("eqtgt") == False
    assert candidate("rmgwowjgogkl v") == True
    assert candidate("cygjyebnztqqf") == False
    assert candidate("RwHkpkFdd") == False
    assert candidate("yHvvPn6E  gnWl") == False
    assert candidate("eeeee e ") == False
    assert candidate("vrvnucaigurvzfi") == False
    assert candidate("V V") == True
    assert candidate("y") == True
    assert candidate("vbu") == False
    assert candidate("l6Np geHEs") == False
    assert candidate("ycyjlluh wet") == False
    assert candidate("nky") == False
    assert candidate("btsPADWGt") == False
    assert candidate("EtacRnVlXjTwP") == False
    assert candidate("kqzcpqd") == False
    assert candidate("elamqcarez") == False
    assert candidate("Z Z") == True
    assert candidate("hpjy") == False
    assert candidate("qqefzbzzskqqc") == False
    assert candidate("iyiboej") == False

if __name__ == '__main__':
    check(check_if_last_char_is_a_letter)