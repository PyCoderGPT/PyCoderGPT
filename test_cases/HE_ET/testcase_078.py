from case_HE_078 import hex_key


def check(candidate):
    assert candidate("1079093") == 2
    assert candidate("CPFY") == 0
    assert candidate("J01") == 0
    assert candidate("CWC8QDL29") == 2
    assert candidate("DS4WECTHENH") == 1
    assert candidate("112233445566778899AABBCCDDEEFF00") == 12, "Sixth test error: " + str(candidate("112233445566778899AABBCCDDEEFF00"))  


    # Check some edge cases that are easy to work out by hand.
    assert candidate("IQ8AOUVSIH9") == 0
    assert candidate("3KV0") == 1
    assert candidate("717522626") == 6
    assert candidate("4425009") == 2
    assert candidate("WIJMZ") == 0
    assert candidate("H493EAK0T762ZR2ORDN7") == 6
    assert candidate("WSKHX2KOF3HV9618N3") == 3
    assert candidate("FBMAY") == 1
    assert candidate("310") == 1
    assert candidate("JSOLE") == 0
    assert candidate("OGWJ") == 0
    assert candidate("JCOAS9AO4VYU0LFAMIMD") == 1
    assert candidate("GBHUVMHNQV6G87") == 2
    assert candidate("091097") == 1
    assert candidate("V1I4X") == 0
    assert candidate("6OEO92R") == 1
    assert candidate("FZJA4EJIZUO0PN1VBOY1ZGJWQ3TPQNZ") == 2
    assert candidate("ZY1W7R8V7633Z9KQQY2ZKNLQOT0GFO") == 5
    assert candidate("V0D1") == 1
    assert candidate("ABED1A33") == 4, "Third test error: " + str(candidate("ABED1A33"))
    assert candidate("1077E") == 2, "Second test error: " + str(candidate("1077E"))
    assert candidate("4O0RNRFZXLSUIN9") == 0
    assert candidate("OQUG0K9WKM4") == 0
    assert candidate([]) == 0
    assert candidate("ZJPAM") == 0
    assert candidate("NFPPM") == 0
    assert candidate("VFZ") == 0
    assert candidate("JW8NS32P") == 2
    assert candidate("TQN6E4YN5YJS3RGTBVNREYMHA7TUXJR5DN") == 6
    assert candidate("O1V") == 0
    assert candidate("9CR3") == 1
    assert candidate("KQMDBB") == 3
    assert candidate("ZYICLQIIAO") == 0
    assert candidate("74U1P6CZG63S") == 2
    assert candidate("9S094T3CXGK61D1AG119ZI88J2626WR") == 4
    assert candidate("LIXZ3A7") == 2
    assert candidate("TE3MD9UP38LCIPFX3YK6C1S4G8P9GP0") == 4
    assert candidate("4037") == 2
    assert candidate("0161174") == 1
    assert candidate("8289") == 1
    assert candidate("K83SK5PK71ZMOD") == 4
    assert candidate("QMEFPST9TU8WLOZ76") == 1
    assert candidate("NMVT0TDKDYB2BP97") == 6
    assert candidate("EEW") == 0
    assert candidate("U1WUXK1XC07PT1U0") == 1
    assert candidate("MVT70UX") == 1
    assert candidate("270503003") == 5
    assert candidate("HD6I529K9506K6RH2M1XIGBRQVR") == 6
    assert candidate("K0Q5JFAOH8MDKS") == 2
    assert candidate("3507083") == 4
    assert candidate("008443") == 1
    assert candidate("NYRLKR") == 0
    assert candidate("AU417SX4BO20NJ6AIRUGL78G7621") == 6
    assert candidate("BF2YBGRXBOND") == 5
    assert candidate("4XX72U3L") == 3
    assert candidate("Z6PZN") == 0
    assert candidate("J6QTYRB0SHT05SGYG6SNKKH8MBLACVP3") == 4
    assert candidate("5WBJPUJAWRKQJECUBRVTVYFCLLG") == 3
    assert candidate("29980") == 1
    assert candidate("IHSCBC") == 1
    assert candidate("SPK6R6D43I0UXY80IIPK") == 2
    assert candidate("GIC") == 0
    assert candidate("UMNHPSNHD3QCB734Y18") == 5
    assert candidate("LDA1GEY8H") == 1
    assert candidate("83TYJWK8507K0AFJDZCJI") == 4
    assert candidate("WRRV") == 0
    assert candidate("DVVW") == 1
    assert candidate("FXX0IVOOC3U5RPUSB7085ACR72275R55VH0P") == 12
    assert candidate("2FJSEFZSO7K7BZ3X6WIGZBDCS1XAUF5A8E") == 8
    assert candidate("EU36FEMVO5YBKOYTG88R459OQOQ310Y") == 5
    assert candidate("123456789ABCDEF0") == 6, "Fifth test error: " + str(candidate("123456789ABCDEF0"))
    assert candidate("4XR9L4") == 0
    assert candidate("F87O3S2I8S") == 3
    assert candidate("NQZETQ") == 0
    assert candidate("RXZYRT") == 0
    assert candidate("DKJYW") == 1
    assert candidate("TNRCI") == 0
    assert candidate("2N0Q") == 1
    assert candidate("UEYMX") == 0
    assert candidate("Y3MEYDWLAAEWTSWZ3QFX") == 3
    assert candidate("846570637") == 4
    assert candidate("N0E") == 0
    assert candidate("1RYJ38YWMCKQWAI1TOJYRJ9O5U57XF1") == 4
    assert candidate("SD1RMVZD65YM68CF4XGNQSKBJCY3") == 5
    assert candidate("AKQ4WH1QGSABCO8Z7GHKRCWF746V0N82") == 4
    assert candidate("C4GJRK0VIOH11AW6I1TSIUR1BRGIIL31Z") == 2
    assert candidate("NSVF") == 0
    assert candidate("TMVF") == 0
    assert candidate("ZEP98JVE6GR02AR2VLOS") == 2
    assert candidate("277399763") == 6
    assert candidate("RJL9") == 0
    assert candidate("MMY6") == 0
    assert candidate("JPXCB0FW9M") == 1
    assert candidate("26399") == 2
    assert candidate("WNY2SA") == 1
    assert candidate("3JQ5LNQL0G23") == 4
    assert candidate("0916085") == 1
    assert candidate("2020") == 2, "Fourth test error: " + str(candidate("2020"))
    assert candidate("65H") == 1
    assert candidate("68YE") == 0
    assert candidate("PR3EKGPBN0V9NGGRC73G5WQJALDYMZR0") == 6
    assert candidate("82336") == 3
    assert candidate("V4D4N") == 1
    assert candidate("TTB") == 1
    assert candidate("YN076UBXXFLOAN2G2N8II") == 4
    assert candidate("5079031") == 3
    assert candidate("N12O2H6SHVDFAM7I1X99SWUE8TYVJUY0Z5E") == 5
    assert candidate("LWWT") == 0
    assert candidate("AB") == 1, "First test error: " + str(candidate("AB"))

if __name__ == '__main__':
    check(hex_key)