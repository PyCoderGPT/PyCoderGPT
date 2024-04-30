from case_MBPP_241 import text_match_wordz


def check(candidate):
    assert candidate("pythonz.")==('Found a match!')
    assert candidate("xyz.")==('Found a match!')
    assert candidate("  lang  .")==('Not matched!')
    assert candidate("tbwjkzofhdm") == "Found a match!"
    assert candidate("kmwsstbjo") == "Not matched!"
    assert candidate("edeiqgczj") == "Found a match!"
    assert candidate("ohw.") == "Not matched!"
    assert candidate("icjzjx") == "Found a match!"
    assert candidate("vjo") == "Not matched!"
    assert candidate("q.wegchzo") == "Found a match!"
    assert candidate("geztdruorkiy") == "Found a match!"
    assert candidate("wle.nnfho") == "Not matched!"
    assert candidate("mytdymj") == "Not matched!"
    assert candidate("trkxiluxfmjv") == "Not matched!"
    assert candidate("wwitztwh.") == "Found a match!"
    assert candidate("nnpbquvp") == "Not matched!"
    assert candidate("ggkdqh") == "Not matched!"
    assert candidate("hzejxqn") == "Found a match!"
    assert candidate("gj.u") == "Not matched!"
    assert candidate("syk") == "Not matched!"
    assert candidate("lbzdyq") == "Found a match!"
    assert candidate("kelj") == "Not matched!"
    assert candidate("jnmkksmrdzgg") == "Found a match!"
    assert candidate("ikfcf") == "Not matched!"
    assert candidate("puah.y.k") == "Not matched!"
    assert candidate("ecifczjwevu") == "Found a match!"
    assert candidate("gjccpnucvnv") == "Not matched!"
    assert candidate("kmjskv") == "Not matched!"
    assert candidate("aq.euz") == "Not matched!"
    assert candidate("lclno") == "Not matched!"
    assert candidate("zxef") == "Found a match!"
    assert candidate("rjisygcii") == "Not matched!"
    assert candidate("v.xcavb") == "Not matched!"
    assert candidate("wdp") == "Not matched!"
    assert candidate("wpaazuffknj") == "Found a match!"
    assert candidate("jnsm.otctedn") == "Not matched!"
    assert candidate("lnvqrh") == "Not matched!"
    assert candidate("afksw") == "Not matched!"
    assert candidate("ojzwri") == "Found a match!"
    assert candidate("fbylbtahi") == "Not matched!"
    assert candidate("ddcf") == "Not matched!"
    assert candidate("scmfbijkq") == "Not matched!"
    assert candidate("hhlrdyrbf") == "Not matched!"
    assert candidate("rsrsnajld") == "Not matched!"
    assert candidate(".vrntskdh") == "Not matched!"
    assert candidate("nmii") == "Not matched!"
    assert candidate("sppvqpw") == "Not matched!"
    assert candidate(".monxhdc") == "Not matched!"
    assert candidate("ldtn") == "Not matched!"
    assert candidate("yxzz") == "Found a match!"
    assert candidate("wnsaofsh") == "Not matched!"
    assert candidate("frzvkuklb") == "Found a match!"
    assert candidate("gczlhco") == "Found a match!"
    assert candidate("ufbxm") == "Not matched!"
    assert candidate("dwli") == "Not matched!"
    assert candidate("jcriiiwwv") == "Not matched!"
    assert candidate("mhftwm") == "Not matched!"
    assert candidate("ltrhsedsc") == "Not matched!"
    assert candidate("hag") == "Not matched!"
    assert candidate("oava") == "Not matched!"
    assert candidate("eqqcsqo") == "Not matched!"
    assert candidate(".fugqw") == "Not matched!"
    assert candidate("ktr") == "Not matched!"
    assert candidate("cdcicoo") == "Not matched!"
    assert candidate("tbbiybklg") == "Not matched!"
    assert candidate("n.y") == "Not matched!"
    assert candidate("scts.bv") == "Not matched!"
    assert candidate("jfmngjxi") == "Not matched!"
    assert candidate(".ohwevyeg") == "Not matched!"
    assert candidate("htcvkjm go qnnd") == "Not matched!"
    assert candidate("rvlpxqksi") == "Not matched!"
    assert candidate("mmywwllkdxwizcl") == "Found a match!"
    assert candidate("hq.fxghds") == "Not matched!"
    assert candidate("ogoxu.ryonh") == "Not matched!"
    assert candidate("ce.ecyuijizt. k") == "Found a match!"
    assert candidate("wfp frrbrkvf") == "Not matched!"
    assert candidate("czqkovwpd") == "Found a match!"
    assert candidate(" jaeqabmx") == "Not matched!"
    assert candidate("qacpmmhektfsqf") == "Not matched!"
    assert candidate("sjwrzkoewmwthw") == "Found a match!"
    assert candidate(" lqt are") == "Not matched!"
    assert candidate("oc. .qox") == "Not matched!"
    assert candidate("rkitbkmyqqvyrm") == "Not matched!"
    assert candidate("dkonuww") == "Not matched!"
    assert candidate("pxolxtk ytwkidi") == "Not matched!"
    assert candidate("ajbvoudsjaohv") == "Not matched!"
    assert candidate("tknvzlaa") == "Found a match!"
    assert candidate("zfrcojt") == "Found a match!"
    assert candidate("jdscsdskpklheng") == "Not matched!"
    assert candidate("hqhevvelggxbw") == "Not matched!"
    assert candidate(".fb.zji.pxikx") == "Found a match!"
    assert candidate("cyhulgccul") == "Not matched!"
    assert candidate("izcycryuwunnj") == "Found a match!"
    assert candidate("hnqgolqybcta ia") == "Not matched!"
    assert candidate("nayrbdzcqmtijt") == "Found a match!"
    assert candidate(".uahwdhbyzh") == "Found a match!"
    assert candidate("ugesbnwuncbh ") == "Not matched!"
    assert candidate("qxwhkirnqrjog") == "Not matched!"
    assert candidate("h.tjehdbpznlv") == "Found a match!"
    assert candidate("jtwybh") == "Not matched!"
    assert candidate("pivuxfcx..mrl.") == "Not matched!"
    assert candidate("hzkbpyk") == "Found a match!"

if __name__ == '__main__':
    check(text_match_wordz)