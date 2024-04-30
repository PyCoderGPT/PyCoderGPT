from case_HE_111 import histogram


def check(candidate):
    assert candidate("hqfrif u") == {'hqfrif': 1, 'u': 1}
    assert candidate("szngkijtjvzd") == {'szngkijtjvzd': 1}
    assert candidate("pkldcnocs cees") == {'pkldcnocs': 1, 'cees': 1}
    assert candidate("y") == {'y': 1}
    assert candidate("np") == {'np': 1}
    assert candidate("ipnqcovwflclbgf") == {'ipnqcovwflclbgf': 1}
    assert candidate("ssgeefwsznskwds") == {'ssgeefwsznskwds': 1}
    assert candidate("relsa") == {'relsa': 1}
    assert candidate("xnrwz") == {'xnrwz': 1}
    assert candidate("ebpzk") == {'ebpzk': 1}
    assert candidate("ucgouvpafay") == {'ucgouvpafay': 1}
    assert candidate("n rivtvpbjz") == {'n': 1, 'rivtvpbjz': 1}
    assert candidate('a b b a') == {'a':2,'b': 2}
    assert candidate("giu fdd qvgg") == {'giu': 1, 'fdd': 1, 'qvgg': 1}
    assert candidate("bpsdtkh") == {'bpsdtkh': 1}
    assert candidate("jmy") == {'jmy': 1}
    assert candidate("r") == {'r': 1}
    assert candidate('a b c a b') == {'a': 2, 'b': 2}
    assert candidate("ynszuyybemnm") == {'ynszuyybemnm': 1}
    assert candidate("qgbazuh") == {'qgbazuh': 1}
    assert candidate(" hgtjtrox") == {'': 1, 'hgtjtrox': 1}
    assert candidate("zjtokgrtx") == {'zjtokgrtx': 1}
    assert candidate("zncaaa") == {'zncaaa': 1}
    assert candidate("ofiqwtkvu") == {'ofiqwtkvu': 1}
    assert candidate("opy") == {'opy': 1}
    assert candidate("gu awuras nre") == {'gu': 1, 'awuras': 1, 'nre': 1}
    assert candidate("tibecrsz") == {'tibecrsz': 1}
    assert candidate("u") == {'u': 1}
    assert candidate("ukqdacqw") == {'ukqdacqw': 1}
    assert candidate("eorw") == {'eorw': 1}
    assert candidate("extoxsm") == {'extoxsm': 1}
    assert candidate("c") == {'c': 1}
    assert candidate("xpi") == {'xpi': 1}
    assert candidate("tqi") == {'tqi': 1}
    assert candidate("hflhqahunywguz") == {'hflhqahunywguz': 1}
    assert candidate("uxsylkbyigbm") == {'uxsylkbyigbm': 1}
    assert candidate("rs") == {'rs': 1}
    assert candidate("mfq") == {'mfq': 1}
    assert candidate("nppv") == {'nppv': 1}
    assert candidate("kjdvicwm") == {'kjdvicwm': 1}
    assert candidate("ajmwtkiery") == {'ajmwtkiery': 1}
    assert candidate("o") == {'o': 1}
    assert candidate("qrwnx") == {'qrwnx': 1}
    assert candidate("x") == {'x': 1}
    assert candidate("l") == {'l': 1}
    assert candidate("zgwj ti") == {'zgwj': 1, 'ti': 1}
    assert candidate('a b c d g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1}
    assert candidate("ebrlpsfs") == {'ebrlpsfs': 1}
    assert candidate("rg") == {'rg': 1}
    assert candidate("j") == {'j': 1}
    assert candidate("bfkxmcb") == {'bfkxmcb': 1}
    assert candidate("b") == {'b': 1}
    assert candidate("ovcbmobr") == {'ovcbmobr': 1}
    assert candidate("gerqufkk") == {'gerqufkk': 1}
    assert candidate("yidenuxbk pgr") == {'yidenuxbk': 1, 'pgr': 1}
    assert candidate("k") == {'k': 1}
    assert candidate("ksqehkbwj") == {'ksqehkbwj': 1}
    assert candidate("gfqwzilfe") == {'gfqwzilfe': 1}
    assert candidate("puacbltqysqo") == {'puacbltqysqo': 1}
    assert candidate("dedfr") == {'dedfr': 1}
    assert candidate("ixldvyly ejnz") == {'ixldvyly': 1, 'ejnz': 1}
    assert candidate("pwjum ocmuglne") == {'pwjum': 1, 'ocmuglne': 1}
    assert candidate("iagusf") == {'iagusf': 1}
    assert candidate("mfus") == {'mfus': 1}
    assert candidate("merfpzcloas") == {'merfpzcloas': 1}
    assert candidate("hrrbvgkbalkra") == {'hrrbvgkbalkra': 1}
    assert candidate('a') == {'a': 1}
    assert candidate("nopvee") == {'nopvee': 1}
    assert candidate("w") == {'w': 1}
    assert candidate("e") == {'e': 1}
    assert candidate("nd") == {'nd': 1}
    assert candidate("suh") == {'suh': 1}
    assert candidate("qwo vt") == {'qwo': 1, 'vt': 1}
    assert candidate("bofyxoswpalc") == {'bofyxoswpalc': 1}
    assert candidate("fxuesfdgjk ") == {'fxuesfdgjk': 1, '': 1}
    assert candidate(" clsersklwqd") == {'': 1, 'clsersklwqd': 1}
    assert candidate("qnvcehs") == {'qnvcehs': 1}
    assert candidate("oooudqv eywbx") == {'oooudqv': 1, 'eywbx': 1}
    assert candidate("dytvbkddxbb") == {'dytvbkddxbb': 1}
    assert candidate("vpthunm") == {'vpthunm': 1}
    assert candidate("oyrtsdmdudtafd") == {'oyrtsdmdudtafd': 1}
    assert candidate("waxgtdtlce") == {'waxgtdtlce': 1}
    assert candidate("kzn ouqqfz") == {'kzn': 1, 'ouqqfz': 1}
    assert candidate("ffs") == {'ffs': 1}
    assert candidate("ofk") == {'ofk': 1}
    assert candidate("rpzvizkuym") == {'rpzvizkuym': 1}
    assert candidate("jjmjpltkmmqa") == {'jjmjpltkmmqa': 1}
    assert candidate('') == {}
    assert candidate("kiyizlhs") == {'kiyizlhs': 1}
    assert candidate("uskutc") == {'uskutc': 1}
    assert candidate("alxzshsygrw") == {'alxzshsygrw': 1}
    assert candidate("tqlzsnbemvaudbs") == {'tqlzsnbemvaudbs': 1}
    assert candidate("zqmwhabyrgjygt") == {'zqmwhabyrgjygt': 1}
    assert candidate("t") == {'t': 1}
    assert candidate("uacomzq") == {'uacomzq': 1}
    assert candidate("pic") == {'pic': 1}
    assert candidate("xteoyzd") == {'xteoyzd': 1}
    assert candidate("vaagpoufagwwr") == {'vaagpoufagwwr': 1}
    assert candidate("ote") == {'ote': 1}
    assert candidate("fqrscrtr") == {'fqrscrtr': 1}
    assert candidate("a") == {'a': 1}
    assert candidate("n") == {'n': 1}
    assert candidate("q") == {'q': 1}
    assert candidate("qvarxoa") == {'qvarxoa': 1}
    assert candidate("lrmn") == {'lrmn': 1}
    assert candidate("jqqvzhh") == {'jqqvzhh': 1}
    assert candidate("nsg") == {'nsg': 1}
    assert candidate("mugytibcb") == {'mugytibcb': 1}
    assert candidate("comfnjz") == {'comfnjz': 1}
    assert candidate("pidc gx") == {'pidc': 1, 'gx': 1}
    assert candidate('b b b b a') == {'b': 4}
    assert candidate("vflxpn ") == {'vflxpn': 1, '': 1}
    assert candidate("vixitrb") == {'vixitrb': 1}
    assert candidate('r t g') == {'r': 1,'t': 1,'g': 1}
    assert candidate("akzmxaten") == {'akzmxaten': 1}
    assert candidate("un pjkbvq") == {'un': 1, 'pjkbvq': 1}
    assert candidate("nbw") == {'nbw': 1}
    assert candidate("zuqsdgrzu") == {'zuqsdgrzu': 1}
    assert candidate("xhsfxgka ") == {'xhsfxgka': 1, '': 1}
    assert candidate("ylpfxjytjxdubkk") == {'ylpfxjytjxdubkk': 1}
    assert candidate("mlclpljwxvnxv") == {'mlclpljwxvnxv': 1}
    assert candidate("pyjsqkszs") == {'pyjsqkszs': 1}
    assert candidate("s") == {'s': 1}
    assert candidate("sxaor") == {'sxaor': 1}

if __name__ == '__main__':
    check(histogram)