from case_MBPP_076 import long_words


def check(candidate):
    assert candidate(3,"python is a programming language")==['python','programming','language']
    assert candidate(2,"writing a program")==['writing','program']
    assert candidate(5,"sorting list")==['sorting']
    assert candidate(4, 'gitgvj vggsxvfilzmfoazjjvujod') == ['gitgvj', 'vggsxvfilzmfoazjjvujod']
    assert candidate(4, 'awuvunvqdsshxfifcltdmmkklgcedc') == ['awuvunvqdsshxfifcltdmmkklgcedc']
    assert candidate(3, ' thtshzmjlpfohwpibozwfdxbktjsaz') == ['thtshzmjlpfohwpibozwfdxbktjsaz']
    assert candidate(1, 'hfotoubtzgqikrqfhenfkubvuinq') == ['hfotoubtzgqikrqfhenfkubvuinq']
    assert candidate(5, 'ronluxjfgn poqndobzemjdmdi bt') == ['ronluxjfgn', 'poqndobzemjdmdi']
    assert candidate(8, 'vifjihiaw bwsmjnullcjdxeekm') == ['vifjihiaw', 'bwsmjnullcjdxeekm']
    assert candidate(8, 'shqdphrngneaymmtgwokejusjvrmr') == ['shqdphrngneaymmtgwokejusjvrmr']
    assert candidate(8, 'du xzbuiqohsdwvzu kvvskhrqndoge') == ['xzbuiqohsdwvzu', 'kvvskhrqndoge']
    assert candidate(5, 'ipmsyidjwopchprwzjjmmgrbqmmbqdm nlcf') == ['ipmsyidjwopchprwzjjmmgrbqmmbqdm']
    assert candidate(7, 'cheqhmy ulvfnfbyggfsywalaxto') == ['ulvfnfbyggfsywalaxto']
    assert candidate(4, 'yocffktvgwsgbjldxzy lymrmipm oovgnht') == ['yocffktvgwsgbjldxzy', 'lymrmipm', 'oovgnht']
    assert candidate(5, 'jebjliistmagyzted hhuhkkdvnxbduypkuc') == ['jebjliistmagyzted', 'hhuhkkdvnxbduypkuc']
    assert candidate(8, 'qdlgyktcavryaurrjlrjbdqcgmntycxot') == ['qdlgyktcavryaurrjlrjbdqcgmntycxot']
    assert candidate(4, 'sxgxfnyy jbzjnknhprsuoo hwvxs') == ['sxgxfnyy', 'jbzjnknhprsuoo', 'hwvxs']
    assert candidate(3, ' rrdwomlqmjkdujeufsurdaqkivplxhsxaf') == ['rrdwomlqmjkdujeufsurdaqkivplxhsxaf']
    assert candidate(4, 'tibortqrsmzmcbputropwhzefuhbmhvcrjoc') == ['tibortqrsmzmcbputropwhzefuhbmhvcrjoc']
    assert candidate(6, 'mismiqltogclyalhrsepxtgutasmklr') == ['mismiqltogclyalhrsepxtgutasmklr']
    assert candidate(4, 'vanl fjgcdftkcgblrudwrhjymzu a') == ['fjgcdftkcgblrudwrhjymzu']
    assert candidate(8, 'apudxczqrhbarypxqusoyluqljff') == ['apudxczqrhbarypxqusoyluqljff']
    assert candidate(7, 'alflhpkvq wghfibfpyduszehzjykpxno') == ['alflhpkvq', 'wghfibfpyduszehzjykpxno']
    assert candidate(8, 'cgvpaggfsgvenelwhzpddrw wtrurnvzg') == ['cgvpaggfsgvenelwhzpddrw', 'wtrurnvzg']
    assert candidate(7, 'gdprnxyakuyvhgsbbvcrnjkzbxc') == ['gdprnxyakuyvhgsbbvcrnjkzbxc']
    assert candidate(3, 'cbzjcifribcgdfxbzom gqbdokarkqesygmk') == ['cbzjcifribcgdfxbzom', 'gqbdokarkqesygmk']
    assert candidate(2, 'tvccvmsdfiju muigkcs kalfaakfbvtzcht') == ['tvccvmsdfiju', 'muigkcs', 'kalfaakfbvtzcht']
    assert candidate(4, 'uiwpwkrolkueoput hukubzgeflughcbzkqx') == ['uiwpwkrolkueoput', 'hukubzgeflughcbzkqx']
    assert candidate(3, 'jo zknbxwyiuibxstgtsnntvefzlsp') == ['zknbxwyiuibxstgtsnntvefzlsp']
    assert candidate(2, ' xlp fjtjfhbhpodxj lussvplnksqj xpsk') == ['xlp', 'fjtjfhbhpodxj', 'lussvplnksqj', 'xpsk']
    assert candidate(3, 'alviofthjigabbmdkawvotsnrjmtoiallait') == ['alviofthjigabbmdkawvotsnrjmtoiallait']
    assert candidate(4, 'dxqxicvfczcxgkxwhdxvywadwehhyac') == ['dxqxicvfczcxgkxwhdxvywadwehhyac']
    assert candidate(5, 'nksbqskwlt lztawpwgifpjrrimcn') == ['nksbqskwlt', 'lztawpwgifpjrrimcn']
    assert candidate(4, 'pvourz lyjvzznqjtmzgbsnmhwnvrualbin') == ['pvourz', 'lyjvzznqjtmzgbsnmhwnvrualbin']
    assert candidate(3, 'chehuunyiqf tvlnsinpkfeqeiwplwhqd e') == ['chehuunyiqf', 'tvlnsinpkfeqeiwplwhqd']
    assert candidate(6, 'ejnsjckd mjnvtgnlwuhm riybetkycgbray') == ['ejnsjckd', 'mjnvtgnlwuhm', 'riybetkycgbray']
    assert candidate(2, 'kf tpzqjlr xhvmtk') == ['tpzqjlr', 'xhvmtk']
    assert candidate(7, 'ykopgcmqclemgvl lsmal') == ['ykopgcmqclemgvl']
    assert candidate(5, 'mgdo sabojzpja') == ['sabojzpja']
    assert candidate(7, 'gwemvklybdjfoggvblxqu') == ['gwemvklybdjfoggvblxqu']
    assert candidate(3, ' obnol zoiyufjpxwef') == ['obnol', 'zoiyufjpxwef']
    assert candidate(3, 'ohmyunofzbukh pnfc') == ['ohmyunofzbukh', 'pnfc']
    assert candidate(4, 'qqvvcnfcegruvoapwir') == ['qqvvcnfcegruvoapwir']
    assert candidate(6, 'qxtpetlzseckz') == ['qxtpetlzseckz']
    assert candidate(7, 'qevi gdahg egtriktmh') == ['egtriktmh']
    assert candidate(2, 'cwpg dw xakhsdbhnj') == ['cwpg', 'xakhsdbhnj']
    assert candidate(7, 'jktei zimgumqgre') == ['zimgumqgre']
    assert candidate(2, 'bdl beaalvfvdsm') == ['bdl', 'beaalvfvdsm']
    assert candidate(5, 'oyqi rskqtuhdy') == ['rskqtuhdy']
    assert candidate(4, 'sudkzayekfaurjbcohizm') == ['sudkzayekfaurjbcohizm']
    assert candidate(6, 'hdadiaux rratr ') == ['hdadiaux']
    assert candidate(7, 'qdlfwdjqlgfz') == ['qdlfwdjqlgfz']
    assert candidate(3, 'vzwfk svrdrqx') == ['vzwfk', 'svrdrqx']
    assert candidate(7, 'bm kwsvmybvlzj') == ['kwsvmybvlzj']
    assert candidate(6, ' i vwwbkzpmhucnxgb') == ['vwwbkzpmhucnxgb']
    assert candidate(1, 'ezigbiruzgvqgbtgcjhya') == ['ezigbiruzgvqgbtgcjhya']
    assert candidate(5, 'umuxe yo luysrikpg') == ['luysrikpg']
    assert candidate(4, 'zptkeufeqiblgyy') == ['zptkeufeqiblgyy']
    assert candidate(1, 'dztfcbhmtpnz') == ['dztfcbhmtpnz']
    assert candidate(2, 'oqiwxnwotdpsek') == ['oqiwxnwotdpsek']
    assert candidate(7, 'pcsgyta vohaucjws') == ['vohaucjws']
    assert candidate(3, 'lwvtvokwgpmgkxlin') == ['lwvtvokwgpmgkxlin']
    assert candidate(7, 'oyah rhgehmrv lfte') == ['rhgehmrv']
    assert candidate(5, 'ggugcxmeyoutb') == ['ggugcxmeyoutb']
    assert candidate(2, 'hkv  u lgpruzpxkhvu') == ['hkv', 'lgpruzpxkhvu']
    assert candidate(5, 'txkrzmgsvyxhyuqg') == ['txkrzmgsvyxhyuqg']
    assert candidate(7, 'xsyhcdiwknxztkdbqd') == ['xsyhcdiwknxztkdbqd']
    assert candidate(6, 'wuycutkblnnpksjfebv') == ['wuycutkblnnpksjfebv']
    assert candidate(5, 'wkrkjzhwssrd') == ['wkrkjzhwssrd']
    assert candidate(9, ' zeokfbfcaeg') == ['zeokfbfcaeg']
    assert candidate(7, ' pytplmkbsmt') == ['pytplmkbsmt']
    assert candidate(2, 'degmnladhspspylz') == ['degmnladhspspylz']
    assert candidate(2, 'zwriyqgfcidu') == ['zwriyqgfcidu']
    assert candidate(2, ' fijecrak') == ['fijecrak']
    assert candidate(7, 'wwgwcerawogqgkv') == ['wwgwcerawogqgkv']
    assert candidate(5, 'nrccugbjuu') == ['nrccugbjuu']
    assert candidate(10, 'odrzanxscxpsec') == ['odrzanxscxpsec']
    assert candidate(7, 'kwaamwsyw') == ['kwaamwsyw']
    assert candidate(4, 'iqfpvymgihjaiqog') == ['iqfpvymgihjaiqog']
    assert candidate(4, 'sqsxuqucbgd') == ['sqsxuqucbgd']
    assert candidate(2, 'gtspjlpvqjydwif') == ['gtspjlpvqjydwif']
    assert candidate(2, 'n szditfejpsukb') == ['szditfejpsukb']
    assert candidate(8, 'hipdstahc') == ['hipdstahc']
    assert candidate(5, 'wsyzldwtbeey') == ['wsyzldwtbeey']
    assert candidate(9, 'ulwtulnuffgumlz') == ['ulwtulnuffgumlz']
    assert candidate(10, 'aotmvtjrcuhvleavq') == ['aotmvtjrcuhvleavq']
    assert candidate(5, 'yfi knax ltql') == []
    assert candidate(1, 'jntnraaoo') == ['jntnraaoo']
    assert candidate(7, 'hfiajtckgqfqzvfp') == ['hfiajtckgqfqzvfp']
    assert candidate(7, 'gfsb scwwmac') == []
    assert candidate(6, 'xtvjeatvzav') == ['xtvjeatvzav']
    assert candidate(7, 'rcozjwkf poag') == ['rcozjwkf']
    assert candidate(10, 'decbvpzzwdsddsbt') == ['decbvpzzwdsddsbt']
    assert candidate(10, 'vmr gmzvrltlgicqz ') == ['gmzvrltlgicqz']
    assert candidate(10, 'kdrsjkiirpga') == ['kdrsjkiirpga']
    assert candidate(2, 'enbhxyuiog') == ['enbhxyuiog']
    assert candidate(8, 'cihwaqovuvaopy') == ['cihwaqovuvaopy']
    assert candidate(10, 'cfmxeklrgouaeklrki') == ['cfmxeklrgouaeklrki']
    assert candidate(6, 'llmbtwear') == ['llmbtwear']
    assert candidate(4, 'vazqqxuka') == ['vazqqxuka']
    assert candidate(1, 'uxymcqumqwohpzg mn') == ['uxymcqumqwohpzg', 'mn']
    assert candidate(8, 'lk nwzoqosyo') == ['nwzoqosyo']

if __name__ == '__main__':
    check(long_words)