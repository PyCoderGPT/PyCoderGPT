from case_HE_125 import split_words


def check(candidate):
    assert candidate("nqovy") == 2
    assert candidate("aHVdlX|%fU=") == 3
    assert candidate("jg*~+urNr-E@A!qKRY") == 3
    assert candidate("tycdhmmyz") == 4
    assert candidate("i_scT:h~e") == 1
    assert candidate("p") == 1
    assert candidate("RmWjn%JLYnFgOT/Lc") == 3
    assert candidate("ZpV&@OBba@QgtsF") == 3
    assert candidate("k+@?:NANl&*Fre") == 2
    assert candidate("pnpmdbvxycpm") == 8
    assert candidate("hv") == 2
    assert candidate("rmatxyfcw") == 4
    assert candidate("Hello world,!") == ["Hello","world,!"]
    assert candidate("_nUUBN-tbtugLg") == 4
    assert candidate("Ej?@*zT_b@kdOSBJqRkW") == 4
    assert candidate("mvfzgdb") == 5
    assert candidate("OfrwN") == 2
    assert candidate("cxxxajg") == 4
    assert candidate("dkoat") == 2
    assert candidate("eqwsuz") == 1
    assert candidate("xp") == 2
    assert candidate("b") == 1
    assert candidate("U?MQ#|tNC") == 1
    assert candidate("bboRkIIkwEE") == 2
    assert candidate("!Nn^j_n%RCwU_m/s^nzrIT") == 6
    assert candidate("eGDrXSfC") == 2
    assert candidate("W#bov/?Thz?W") == 4
    assert candidate("NnEwAnlMVB=Wba|O?") == 4
    assert candidate("hohbth") == 5
    assert candidate("RvCBtA") == 2
    assert candidate("q") == 0
    assert candidate("KwiQw~-r_") == 1
    assert candidate("msvvbcgky") == 3
    assert candidate("uhxvybwbmh") == 6
    assert candidate("Hello,Hello,world !") == ["Hello,Hello,world","!"]
    assert candidate("hM/hRRo&SWoS&mF~|") == 2
    assert candidate("dpBtfxTsi:~") == 5
    assert candidate("njls") == 3
    assert candidate("anfcmzn") == 4
    assert candidate("zuh") == 2
    assert candidate(":jZdsTuwXB?") == 2
    assert candidate("w") == 0
    assert candidate("$|yu?&U_hCaMM!&") == 1
    assert candidate("") == 0
    assert candidate("al#PIP-QTpPLvox*") == 4
    assert candidate("wunr") == 2
    assert candidate("LqkZ,zL,~NeZg:wOm_h") == ['LqkZ', 'zL', '~NeZg:wOm_h']
    assert candidate("Hello world!") == ["Hello","world!"]
    assert candidate("AWp!@PZMYbS^z&I") == 3
    assert candidate("NJSTW O!@YrDw|pVGZ*?") == ['NJSTW', 'O!@YrDw|pVGZ*?']
    assert candidate("bdpyljovl") == 7
    assert candidate("d|po*:jWq&hhnNIHqx&eY@?") == 7
    assert candidate("abcdef") == 3
    assert candidate(",X*$Wump&HCJb%+As") == ['X*$Wump&HCJb%+As']
    assert candidate("ufiksfwi") == 2
    assert candidate("hpSGeTps") == 3
    assert candidate("GbQdw*vMBTePLWnvV") == 5
    assert candidate("Hello,world!") == ["Hello","world!"]
    assert candidate("aLmAGvwjl") == 3
    assert candidate("kvdmaav") == 3
    assert candidate("e_^sxp/fqMTYI:|") == 3
    assert candidate("UU-?rMWetRg&") == 2
    assert candidate("gS#RB,~cU-w:ZH_") == ['gS#RB', '~cU-w:ZH_']
    assert candidate("rKevoU") == 2
    assert candidate("bkp") == 2
    assert candidate("xnb") == 3
    assert candidate("QKG$HXnkw^ozxnWXEo") == 4
    assert candidate("XQXesS%p:UbMalngB") == 4
    assert candidate("oKRmE") == 0
    assert candidate("zzxs") == 3
    assert candidate("|sfihzOlhVcPN_eEh") == 6
    assert candidate("rcXPAxR") == 2
    assert candidate("fTtDWqiB~-") == 2
    assert candidate(":=K+at:~we") == 1
    assert candidate("aaabb") == 2
    assert candidate("CX!@@rhr,/-H:HgT") == ['CX!@@rhr', '/-H:HgT']
    assert candidate("nzo") == 2
    assert candidate("T/woQZAkIO|/EE") == 0
    assert candidate("zuve") == 2
    assert candidate("ckEaxwWfSiFqEQoeIw") == 2
    assert candidate("VkIPu=_zhMF C+!nfe-raB#?") == ['VkIPu=_zhMF', 'C+!nfe-raB#?']
    assert candidate("r -TnGH|hD%q%%_Z") == ['r', '-TnGH|hD%q%%_Z']
    assert candidate("dOTcSA") == 1
    assert candidate("lNv") == 2
    assert candidate("&TduYUyhbeXh") == 4
    assert candidate("y!fm#C:hKGj ") == ['y!fm#C:hKGj']
    assert candidate("apcyyq") == 1
    assert candidate("irg") == 1
    assert candidate("$JY_UYz,!iq") == ['$JY_UYz', '!iq']
    assert candidate("aB+lU+OnYF$PZO@NwU") == 2
    assert candidate("rzy") == 2
    assert candidate("+/oUxjmn~y-+ZPkyN,") == ['+/oUxjmn~y-+ZPkyN']
    assert candidate("wo") == 0
    assert candidate("oaIXYoFS") == 0
    assert candidate("~rUBcwdGrVT^!h&IH*") == 4
    assert candidate("gFrJQl") == 2
    assert candidate("goMGiS_MVr") == 1
    assert candidate("aaaBb") == 1
    assert candidate("WnTPRMoeKCP eY-i") == ['WnTPRMoeKCP', 'eY-i']
    assert candidate("Dgia~wiNNMRt-i") == 1
    assert candidate("Mv+pADUgje") == 3
    assert candidate("f") == 1
    assert candidate("omBjuAWlYq_N") == 2
    assert candidate("%TSp@orNumXB") == 2
    assert candidate("|U:s$UhWkK#ZSK") == 1
    assert candidate("ykzlzecy") == 3
    assert candidate("gq&xmYfWMBK#-NQYiNjAM*L") == 3
    assert candidate("hmytaseac") == 2
    assert candidate("$nw/P%QRfarwyOi|Q") == 3
    assert candidate("syoicmg") == 0
    assert candidate("fVglGtpJc") == 4
    assert candidate("xCcvykbBAKs@gJi") == 3
    assert candidate("rr") == 2
    assert candidate("K^=nzDBNH J%JTsrnL") == ['K^=nzDBNH', 'J%JTsrnL']
    assert candidate("=lHNHN+Y*~NUhK") == 2
    assert candidate("r!QzUIkvlpSV@iw,Js&xvIT") == ['r!QzUIkvlpSV@iw', 'Js&xvIT']
    assert candidate("r*&oaf-!aG*wgAFVp") == 3
    assert candidate("sqgy!ymCjd t:rln-^bIVz") == ['sqgy!ymCjd', 't:rln-^bIVz']
    assert candidate("asivgkx") == 2
    assert candidate("pied") == 2
    assert candidate("hbpsavk") == 4
    assert candidate("zJINZp") == 2
    assert candidate("plufdpelfsr") == 8
    assert candidate("xngtyezta") == 5
    assert candidate("~/Ttj*k_=") == 2
    assert candidate("kheNiYo") == 1

if __name__ == '__main__':
    check(split_words)