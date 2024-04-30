from case_MBPP_307 import first_repeated_char


def check(candidate):
    assert candidate("abcabc") == "a"
    assert candidate("abc") == "None"
    assert candidate("123123") == "1"
    assert candidate("gzcaabqoulds") == "a"
    assert candidate("usoflfgmrj") == f
    assert candidate("xigwtfzta") == "t"
    assert candidate("vqsvtdjrujt") == "v"
    assert candidate("mjlzfmkf") == "m"
    assert candidate("adrgdv") == "d"
    assert candidate("cpnig") == None
    assert candidate("vzbhqfs") == None
    assert candidate("lltrdsh") == "l"
    assert candidate("qyayopdsgxx") == "y"
    assert candidate("wiu") == None
    assert candidate("ihrkiyxcda") == i
    assert candidate("pflnso") == None
    assert candidate("hgumcx") == None
    assert candidate("txzherquxdfx") == "x"
    assert candidate("svcwfcjjpw") == "c"
    assert candidate("hqdxvex") == "x"
    assert candidate("ocrpqqjo") == "q"
    assert candidate("umlvn") == None
    assert candidate("tguvbbxb") == "b"
    assert candidate("uaqbhhkb") == "h"
    assert candidate("kxuydalotqlt") == "l"
    assert candidate("poscpmchz") == "p"
    assert candidate("yxyd") == "y"
    assert candidate("hnbrzelap") == None
    assert candidate("uueyvbz") == "u"
    assert candidate("pjdsts") == "s"
    assert candidate("wqyhluhh") == "h"
    assert candidate("viagi") == i
    assert candidate("ektgzxpudhbd") == "d"
    assert candidate("bazlt") == None
    assert candidate("mxpipf") == "p"
    assert candidate("xjccinlcz") == "c"
    assert candidate("ycgv") == None
    assert candidate("jvde") == None
    assert candidate("mcd") == None
    assert candidate("xum") == None
    assert candidate("hbn") == None
    assert candidate("cbgmdvx") == None
    assert candidate("bxscyd") == None
    assert candidate("ruzchv") == None
    assert candidate("khuajn") == None
    assert candidate("bwo") == None
    assert candidate("oan") == None
    assert candidate("nkyyoqlmt") == "y"
    assert candidate("tvyv") == "v"
    assert candidate("revykqcsr") == "r"
    assert candidate("iokf") == None
    assert candidate("devmbcvms") == "v"
    assert candidate("vna") == None
    assert candidate("ytqpyjsce") == "y"
    assert candidate("iaqt") == None
    assert candidate("evimmcaa") == "m"
    assert candidate("coniujgit") == i
    assert candidate("fzt") == None
    assert candidate("ytmstu") == "t"
    assert candidate("oofkuwbi") == "o"
    assert candidate("hpf") == None
    assert candidate("kvmc") == None
    assert candidate("fkmwmpye") == "m"
    assert candidate("yamjrz") == None
    assert candidate("auec") == None
    assert candidate("mjep") == None
    assert candidate("dxeri") == None
    assert candidate("oyuht") == None
    assert candidate("oulwxhba") == None
    assert candidate("748192381500") == 8
    assert candidate("268619") == 6
    assert candidate("86045885600") == 8
    assert candidate("341") == None
    assert candidate("3011") == 1
    assert candidate("63235") == 3
    assert candidate("34518524905") == 5
    assert candidate("3081745") == None
    assert candidate("88855083550") == 8
    assert candidate("587227") == 2
    assert candidate("264533365") == 3
    assert candidate("696") == 6
    assert candidate("5428693") == None
    assert candidate("98520729") == 2
    assert candidate("1368") == None
    assert candidate("765148306") == 6
    assert candidate("8640") == None
    assert candidate("10952181432") == 1
    assert candidate("017867001") == 7
    assert candidate("98742320") == 2
    assert candidate("783") == None
    assert candidate("6718463") == 6
    assert candidate("925523072") == 5
    assert candidate("26650003679") == 6
    assert candidate("18751842215") == 1
    assert candidate("2950265469") == 2
    assert candidate("49374") == 4
    assert candidate("302847") == None
    assert candidate("75437621") == 7
    assert candidate("926") == None
    assert candidate("45188") == 8
    assert candidate("5755") == 5
    assert candidate("85830262859") == 8

if __name__ == '__main__':
    check(first_repeated_char)