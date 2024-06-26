from case_MBPP_417 import remove_all_spaces


def check(candidate):
    assert candidate('python  program')==('pythonprogram')
    assert candidate('python   programming    language')==('pythonprogramminglanguage')
    assert candidate('python                     program')==('pythonprogram')
    assert candidate("ch xwmiditgqcqk") == "chxwmiditgqcqk"
    assert candidate("xbxdaphrzuyqlgyl") == "xbxdaphrzuyqlgyl"
    assert candidate("onvxwhogzidbnbmxckoy") == "onvxwhogzidbnbmxckoy"
    assert candidate("pngzhrzxyqvcanmmhgjjo") == "pngzhrzxyqvcanmmhgjjo"
    assert candidate(" hrakgarkdbpxrdzn ywb") == "hrakgarkdbpxrdznywb"
    assert candidate("kadktafspkhoatq ") == "kadktafspkhoatq"
    assert candidate("hrzjcpleoicisdvohbal") == "hrzjcpleoicisdvohbal"
    assert candidate("fgkkbwexacdbbbxyhd ") == "fgkkbwexacdbbbxyhd"
    assert candidate("cqjxs ppswhrak km") == "cqjxsppswhrakkm"
    assert candidate("jfggosodkklaclrhqf") == "jfggosodkklaclrhqf"
    assert candidate("jdyu niclasitcbttd") == "jdyuniclasitcbttd"
    assert candidate("qxoxxgjnxvttxg") == "qxoxxgjnxvttxg"
    assert candidate("hkzqhg kkctotwwp") == "hkzqhgkkctotwwp"
    assert candidate("gwauzdwvtgtkd") == "gwauzdwvtgtkd"
    assert candidate("rbeckrxitgvwvbzc") == "rbeckrxitgvwvbzc"
    assert candidate(" qknj xdswvw") == "qknjxdswvw"
    assert candidate("dejiivwpkglllde") == "dejiivwpkglllde"
    assert candidate("rdylfaebrgwxrpsunv") == "rdylfaebrgwxrpsunv"
    assert candidate("yaixryhidqga") == "yaixryhidqga"
    assert candidate("ryimuxhjvlocuw") == "ryimuxhjvlocuw"
    assert candidate("pjuevapnccii") == "pjuevapnccii"
    assert candidate("u mbojcwomwbsbtum") == "umbojcwomwbsbtum"
    assert candidate("lfxxtpnrdwfangrhgdx") == "lfxxtpnrdwfangrhgdx"
    assert candidate("ugtnl cutbrtu") == "ugtnlcutbrtu"
    assert candidate("gmtesbjvgukvnfib") == "gmtesbjvgukvnfib"
    assert candidate("t xztgffepkah") == "txztgffepkah"
    assert candidate(" dcxnsvbsafyj") == "dcxnsvbsafyj"
    assert candidate("hlhawxjapvaywtl") == "hlhawxjapvaywtl"
    assert candidate("ymdkgswrulpjeriz") == "ymdkgswrulpjeriz"
    assert candidate("tbdkkdcaswmhz") == "tbdkkdcaswmhz"
    assert candidate("erdyuenkcjwsrozhdfc") == "erdyuenkcjwsrozhdfc"
    assert candidate(" xbbdkvhsdgeccze s") == "xbbdkvhsdgecczes"
    assert candidate("fjcrqzrwygwsgvoxe") == "fjcrqzrwygwsgvoxe"
    assert candidate("owl yz mbsgej hf ossnqwhisf") == "owlyzmbsgejhfossnqwhisf"
    assert candidate("bjwocu vmiclfvflqxqjyrvofrrjt") == "bjwocuvmiclfvflqxqjyrvofrrjt"
    assert candidate("xskdn rceutfcwfnndguzsgwefujyqow") == "xskdnrceutfcwfnndguzsgwefujyqow"
    assert candidate("qhcifqsaovlccctvsaymakmltfpv") == "qhcifqsaovlccctvsaymakmltfpv"
    assert candidate("hbmfgnornhovyjufcgywqjbrdsnuwssoa") == "hbmfgnornhovyjufcgywqjbrdsnuwssoa"
    assert candidate("fuiqsruoqpsourqedmjldyfirqzi wul") == "fuiqsruoqpsourqedmjldyfirqziwul"
    assert candidate("aylckpiynjtadooyqnzzciqwgvkeusa") == "aylckpiynjtadooyqnzzciqwgvkeusa"
    assert candidate("fhqrnonqlksyjpbtrmlwzzu hezunumcvij") == "fhqrnonqlksyjpbtrmlwzzuhezunumcvij"
    assert candidate("lxhkuqdqsdpasrtgfvrpq gpjknbtfhf") == "lxhkuqdqsdpasrtgfvrpqgpjknbtfhf"
    assert candidate("akxeqn zhl pvldjxvonjhfrdpodt") == "akxeqnzhlpvldjxvonjhfrdpodt"
    assert candidate("opmrtzzfohvwvxzeovqeknwgewqphyocfup") == "opmrtzzfohvwvxzeovqeknwgewqphyocfup"
    assert candidate("cizaxyizadnblncpxwboqfjerozkocgis") == "cizaxyizadnblncpxwboqfjerozkocgis"
    assert candidate("dxhvairumqpvpfekwlxkbhyjeqz") == "dxhvairumqpvpfekwlxkbhyjeqz"
    assert candidate("rhklaxi yuw slzmrrvfrhteizmj") == "rhklaxiyuwslzmrrvfrhteizmj"
    assert candidate("mvl yktjrevzwhzsnhpjdoakkkhb") == "mvlyktjrevzwhzsnhpjdoakkkhb"
    assert candidate("ldrlsyfbaunxlvseexcaidpelgio") == "ldrlsyfbaunxlvseexcaidpelgio"
    assert candidate("xvcututii nndsmppgsmzpepaudo mn") == "xvcututiinndsmppgsmzpepaudomn"
    assert candidate("spqlaahzalrsuilklgebwepzft ") == "spqlaahzalrsuilklgebwepzft"
    assert candidate("ntleinqmnsyenrsooasmqeahg a") == "ntleinqmnsyenrsooasmqeahga"
    assert candidate("gdftoxhhnzvaebtdnumrjkxhywnowktino") == "gdftoxhhnzvaebtdnumrjkxhywnowktino"
    assert candidate("smnbwytxpymijraperntmjqoxc yswbkf") == "smnbwytxpymijraperntmjqoxcyswbkf"
    assert candidate("dcexivoesaumfw xyqmkmerihwpucf") == "dcexivoesaumfwxyqmkmerihwpucf"
    assert candidate("dqzmpqgdwuuckejivw mklqqhkpw ") == "dqzmpqgdwuuckejivwmklqqhkpw"
    assert candidate("izw qjrwswxoqkhdxcqpradawmtmkz") == "izwqjrwswxoqkhdxcqpradawmtmkz"
    assert candidate("tuiyrwao nyezjclfvvcvyisurxrkmnhdw") == "tuiyrwaonyezjclfvvcvyisurxrkmnhdw"
    assert candidate("afmgplmityujyjktkqmjkrdugznefxxgqjkc") == "afmgplmityujyjktkqmjkrdugznefxxgqjkc"
    assert candidate("z fduylurcsrzkajsvkpbqkbvmwdocg  ux") == "zfduylurcsrzkajsvkpbqkbvmwdocgux"
    assert candidate("dgrujfxokynsr umxcf dygmzlqfnbxatdqs") == "dgrujfxokynsrumxcfdygmzlqfnbxatdqs"
    assert candidate("jtthtzudl cortfimtcqnpstuuder") == "jtthtzudlcortfimtcqnpstuuder"
    assert candidate("ntcunuzlvqluffxgnujtadacxpuryqhdqif") == "ntcunuzlvqluffxgnujtadacxpuryqhdqif"
    assert candidate("lehfpdlzp oqdgebmfqoqnkzglgejhrltdaz") == "lehfpdlzpoqdgebmfqoqnkzglgejhrltdaz"
    assert candidate("ietcernlojdfoulxamogdgtkzluodujfgsm") == "ietcernlojdfoulxamogdgtkzluodujfgsm"
    assert candidate("vqjeei ccvhsvvrhwgqpumagjrkd") == "vqjeeiccvhsvvrhwgqpumagjrkd"
    assert candidate("wbofjatamou ncvhhsnhywngnhew xgjiyo") == "wbofjatamouncvhhsnhywngnhewxgjiyo"
    assert candidate("tbwuxgcyqojvjziajbhtpfbjflbzrvneludr") == "tbwuxgcyqojvjziajbhtpfbjflbzrvneludr"
    assert candidate("llcj nwgkaoxgfcq ymkzpztpmxhzwblafad") == "llcjnwgkaoxgfcqymkzpztpmxhzwblafad"
    assert candidate("mfoiivksudwnlq odpkbxelunkwehqsvmy qxb") == "mfoiivksudwnlqodpkbxelunkwehqsvmyqxb"
    assert candidate("wvcfawq edtugcxvdvxsixelbuygpmsviqks") == "wvcfawqedtugcxvdvxsixelbuygpmsviqks"
    assert candidate("gfshgiiiapnonazxniubrzyaqxghejn") == "gfshgiiiapnonazxniubrzyaqxghejn"
    assert candidate("xwclmqjoovwqikidpom wkppscrrnpvdrrlkhf") == "xwclmqjoovwqikidpomwkppscrrnpvdrrlkhf"
    assert candidate("srdegwszihyyqzojqyaocces rkl ny zqeous") == "srdegwszihyyqzojqyaoccesrklnyzqeous"
    assert candidate("xhxoqqapczsfjch czbqhkjlrrhlyw qhrnh") == "xhxoqqapczsfjchczbqhkjlrrhlywqhrnh"
    assert candidate("jguihoojsxxmrahutwouvjmwgmlgpsfdpjugojo") == "jguihoojsxxmrahutwouvjmwgmlgpsfdpjugojo"
    assert candidate("pibjmnarppymdiwknqtpomhhmmusntmnqkg sy") == "pibjmnarppymdiwknqtpomhhmmusntmnqkgsy"
    assert candidate("skjvg rnicmhfstmhhclahojrngcxzsprmxnyn") == "skjvgrnicmhfstmhhclahojrngcxzsprmxnyn"
    assert candidate("vdueyiuxsezwbzyfwrxtudzjprhfcc ihyt") == "vdueyiuxsezwbzyfwrxtudzjprhfccihyt"
    assert candidate("ntmhwalnvm zwodlwlsbrlhmdytloqjrysx") == "ntmhwalnvmzwodlwlsbrlhmdytloqjrysx"
    assert candidate("nfuhhurmiucmcxeicugmbsmmpczehqubyqi") == "nfuhhurmiucmcxeicugmbsmmpczehqubyqi"
    assert candidate("pyospgpgfiaxpexsftcmfwtovekyyunke") == "pyospgpgfiaxpexsftcmfwtovekyyunke"
    assert candidate("kmgeebcofkuaxvmktdxolklnkyb mhxnj") == "kmgeebcofkuaxvmktdxolklnkybmhxnj"
    assert candidate("djzpzscopc mflduelenxjpuwy f hplrma") == "djzpzscopcmflduelenxjpuwyfhplrma"
    assert candidate("joitkkbd belrhxwrxljgwameoameizr") == "joitkkbdbelrhxwrxljgwameoameizr"
    assert candidate("svvfxpflbhxvjf iszejeesncakeygaf") == "svvfxpflbhxvjfiszejeesncakeygaf"
    assert candidate("lswgvjnqtgielmirvapfzfowhjopmqot ar jvb") == "lswgvjnqtgielmirvapfzfowhjopmqotarjvb"
    assert candidate("xamsemveiqnypsyeuglcfqpqvkxpypz") == "xamsemveiqnypsyeuglcfqpqvkxpypz"
    assert candidate("iwhebcuipbmiadpeegimdotlbyqkqq") == "iwhebcuipbmiadpeegimdotlbyqkqq"
    assert candidate("oivkemphrimosdanatcedxo jtzjjxtpm") == "oivkemphrimosdanatcedxojtzjjxtpm"
    assert candidate("htncnjsooctrcclgoy epjszgxxvflgneysr") == "htncnjsooctrcclgoyepjszgxxvflgneysr"
    assert candidate("zygykinwtdyxxagyvmktgxddswyjybvub") == "zygykinwtdyxxagyvmktgxddswyjybvub"
    assert candidate("wwxdrnzxwwfuesduaybkytuavuqdyzmfli") == "wwxdrnzxwwfuesduaybkytuavuqdyzmfli"
    assert candidate("py gavntnlsozxyxi kapwgwifocdyelvi") == "pygavntnlsozxyxikapwgwifocdyelvi"
    assert candidate("bsozfkxnube e vovuciwqjqkhnbuvj") == "bsozfkxnubeevovuciwqjqkhnbuvj"
    assert candidate("knwhessfq wfefsxafcotokkikpxkpma retoih") == "knwhessfqwfefsxafcotokkikpxkpmaretoih"
    assert candidate("jrshx kctozlkmfchugsichntf cvvefnmhuz") == "jrshxkctozlkmfchugsichntfcvvefnmhuz"
    assert candidate("bmieldqdbjjnznrfdskrlvvesycilc") == "bmieldqdbjjnznrfdskrlvvesycilc"
    assert candidate("xecokwlwyvmvofbvqcfjju dpydkusjunzuh") == "xecokwlwyvmvofbvqcfjjudpydkusjunzuh"

if __name__ == '__main__':
    check(remove_all_spaces)