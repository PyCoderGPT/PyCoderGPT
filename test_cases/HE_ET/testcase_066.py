from case_HE_066 import digitSum


def check(candidate):
    assert candidate("SlpsVikY") == 258
    assert candidate("hjOOvh") == 158
    assert candidate(" How are yOu?") == 151, "Error"
    assert candidate("dcCIbm") == 140
    assert candidate("CFAIsWb") == 362
    assert candidate("You arE Very Smart") == 327, "Error"
    assert candidate("FcnUrbtEbh") == 224
    assert candidate("IjxaRUDNKD") == 529
    assert candidate("YASqCNUVI") == 626
    assert candidate("vTkrvqy~Go") == 155
    assert candidate("ZGPBVWjc") == 480
    assert candidate("dYpWa") == 176
    assert candidate("VOyVU") == 336
    assert candidate("WlN") == 165
    assert candidate("MJG@bRspAZS!") == 542
    assert candidate("CEL") == 212
    assert candidate("TlEyWf") == 240
    assert candidate("hzp") == 0
    assert candidate("EhSBZR") == 390
    assert candidate("AZraZRpgg=+IO~=!d") == 479
    assert candidate("uiYvRTtFqh") == 325
    assert candidate("jw") == 0
    assert candidate("BEUNDcwH") == 438
    assert candidate("CKhXCg") == 297
    assert candidate("mBOG") == 216
    assert candidate("n") == 0
    assert candidate("fh") == 0
    assert candidate("") == 0, "Error"
    assert candidate("uhmfZS") == 173
    assert candidate("ccgEINzKxx") == 295
    assert candidate("yoa") == 0
    assert candidate("kjs") == 0
    assert candidate("GHb") == 143
    assert candidate("oi") == 0
    assert candidate("rsiQXabiCaXw") == 324
    assert candidate("YyoGlqQt") == 241
    assert candidate("helloE") == 69, "Error"
    assert candidate("z") == 0
    assert candidate("mnsrAj RsmjPO|&") == 306
    assert candidate("aAaaaXa") == 153, "Error"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("Zew") == 90
    assert candidate("abAB") == 131, "Error"
    assert candidate("SGFQQcgwq") == 386
    assert candidate("VYtmw") == 175
    assert candidate("VsuDpc") == 154
    assert candidate("SMVzyF_V:/") == 402
    assert candidate("oPOrD") == 227
    assert candidate("EwQHkxceA") == 287
    assert candidate("ILYi") == 238
    assert candidate("FYNE") == 306
    assert candidate("gUfkeP") == 165
    assert candidate("XQiEhzZn") == 328
    assert candidate("f*QSgjaR$F^") == 316
    assert candidate("SBEzmo") == 218
    assert candidate("tIYEeRB") == 379
    assert candidate("mBaa!/EII@fbZMCqhh") == 515
    assert candidate("mw") == 0
    assert candidate("ldTHl") == 156
    assert candidate("AMhnWFw//tT xW!@D") == 538
    assert candidate("vrXvrfnHgp") == 160
    assert candidate("SVWNmWyY:i") == 510
    assert candidate("gdKFFPfWM") == 459
    assert candidate("NWdyY") == 254
    assert candidate("abcCd") == 67, "Error"
    assert candidate("NDi") == 146
    assert candidate("?wo&ZN|pXZ=wF") == 416
    assert candidate("eanJhjeU") == 159
    assert candidate("aVUNV") == 335
    assert candidate("IlJsGGN") == 367
    assert candidate("pkCuo") == 67
    assert candidate("UwNYt") == 252
    assert candidate("ssKsK") == 150
    assert candidate("oodz") == 0
    assert candidate("xgqhGuUX") == 244
    assert candidate("pOSrYv") == 251
    assert candidate("GcLF") == 217
    assert candidate("KIgugrKVhf") == 309
    assert candidate("wOdlzmDPB") == 293
    assert candidate("tviw*zg*qqoxukbj") == 0
    assert candidate("XpdJ") == 162
    assert candidate("lVMxHfkfC") == 302
    assert candidate("fBh") == 66
    assert candidate("qbb") == 0
    assert candidate("NrVBVvmFrmx") == 386
    assert candidate("arvbqFw") == 70
    assert candidate("jsy") == 0
    assert candidate("FdB") == 136
    assert candidate("DVkhHIzC faN~_Tn?") == 528
    assert candidate("EqDDxyNv") == 283
    assert candidate("efPfM") == 157
    assert candidate("xXgcSe") == 171
    assert candidate("DequwqRRq") == 232
    assert candidate("woDYq") == 157
    assert candidate("xoa") == 0
    assert candidate("IgkN") == 151
    assert candidate("%q^rg /iW-*") == 87
    assert candidate("wCDmTioUZ") == 394
    assert candidate("sGPvbJuRwR") == 389
    assert candidate("gm") == 0
    assert candidate("sicZcHqr") == 162
    assert candidate("DaXwt") == 156
    assert candidate("YRuYlSl") == 343
    assert candidate("e") == 0
    assert candidate("SbDPfIc") == 304
    assert candidate("woArBld") == 131, "Error"
    assert candidate("jdXa") == 88
    assert candidate("wbo") == 0
    assert candidate("FYXx") == 247
    assert candidate("zNjVlbJHdP") == 390
    assert candidate("VRvcAddACXCA") == 585
    assert candidate("+UEmCV??yaK+pMp/^C") == 526
    assert candidate("RprHOOFRUO") == 628
    assert candidate("sqe") == 0

if __name__ == '__main__':
    check(digitSum)