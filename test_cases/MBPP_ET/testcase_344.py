from case_MBPP_344 import add_dict_to_tuple


def check(candidate):
    assert candidate((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
    assert candidate((1, 2, 3), {"UTS" : 2, "is" : 3, "Worst" : 4} ) == (1, 2, 3, {'UTS': 2, 'is': 3, 'Worst': 4})
    assert candidate((8, 9, 10), {"POS" : 3, "is" : 4, "Okay" : 5} ) == (8, 9, 10, {'POS': 3, 'is': 4, 'Okay': 5})
    assert candidate((8, 10, 3), {'YKLBKVEQS': 5, 'zfyo': 1, 'uwdapfrhs': 2}) == (8, 10, 3, {'YKLBKVEQS': 5, 'zfyo': 1, 'uwdapfrhs': 2})
    assert candidate((1, 5, 4), {'UFAPNY': 1, 'hwko': 1, 'xtdeilps': 6}) == (1, 5, 4, {'UFAPNY': 1, 'hwko': 1, 'xtdeilps': 6})
    assert candidate((4, 2, 2), {'RYU': 2, 'noaji': 4, 'jbiqrkims': 5}) == (4, 2, 2, {'RYU': 2, 'noaji': 4, 'jbiqrkims': 5})
    assert candidate((7, 3, 4), {'JPDUPHY': 6, 'rauhrw': 1, 'qrcz': 7}) == (7, 3, 4, {'JPDUPHY': 6, 'rauhrw': 1, 'qrcz': 7})
    assert candidate((4, 1, 1), {'AUFNPZDZM': 5, 'dbya': 4, 'enpkswjw': 6}) == (4, 1, 1, {'AUFNPZDZM': 5, 'dbya': 4, 'enpkswjw': 6})
    assert candidate((2, 2, 5), {'EPN': 5, 'ydy': 7, 'mqoquy': 3}) == (2, 2, 5, {'EPN': 5, 'ydy': 7, 'mqoquy': 3})
    assert candidate((4, 2, 3), {'WCPWL': 2, 'ahr': 4, 'fabbysfl': 5}) == (4, 2, 3, {'WCPWL': 2, 'ahr': 4, 'fabbysfl': 5})
    assert candidate((5, 10, 2), {'NGEWHAQ': 5, 'vpptkb': 2, 'tzesmw': 6}) == (5, 10, 2, {'NGEWHAQ': 5, 'vpptkb': 2, 'tzesmw': 6})
    assert candidate((1, 7, 7), {'FPJQHV': 1, 'ejfloy': 2, 'vzcjc': 2}) == (1, 7, 7, {'FPJQHV': 1, 'ejfloy': 2, 'vzcjc': 2})
    assert candidate((6, 5, 2), {'GPPAU': 6, 'airvl': 3, 'fkrvhfn': 8}) == (6, 5, 2, {'GPPAU': 6, 'airvl': 3, 'fkrvhfn': 8})
    assert candidate((2, 7, 1), {'UEGGOUWH': 6, 'jnueiw': 3, 'gpvgjzdb': 5}) == (2, 7, 1, {'UEGGOUWH': 6, 'jnueiw': 3, 'gpvgjzdb': 5})
    assert candidate((5, 1, 7), {'KRUKIU': 6, 'oaxg': 6, 'thatndce': 2}) == (5, 1, 7, {'KRUKIU': 6, 'oaxg': 6, 'thatndce': 2})
    assert candidate((3, 3, 10), {'LEOEJWJFN': 6, 'cuhiy': 2, 'tdtr': 2}) == (3, 3, 10, {'LEOEJWJFN': 6, 'cuhiy': 2, 'tdtr': 2})
    assert candidate((9, 1, 3), {'HBH': 6, 'xhc': 3, 'rvchopi': 2}) == (9, 1, 3, {'HBH': 6, 'xhc': 3, 'rvchopi': 2})
    assert candidate((9, 10, 1), {'YJRJ': 3, 'meygn': 6, 'elmrokzip': 4}) == (9, 10, 1, {'YJRJ': 3, 'meygn': 6, 'elmrokzip': 4})
    assert candidate((5, 2, 2), {'HSE': 6, 'ovy': 2, 'dnuw': 5}) == (5, 2, 2, {'HSE': 6, 'ovy': 2, 'dnuw': 5})
    assert candidate((8, 4, 4), {'DOPB': 6, 'bcr': 2, 'jzmlojnxp': 3}) == (8, 4, 4, {'DOPB': 6, 'bcr': 2, 'jzmlojnxp': 3})
    assert candidate((3, 9, 5), {'LVSMIGR': 6, 'ectg': 3, 'glwmurhr': 8}) == (3, 9, 5, {'LVSMIGR': 6, 'ectg': 3, 'glwmurhr': 8})
    assert candidate((8, 6, 6), {'KSJYCOGP': 6, 'xjwn': 4, 'lozrf': 7}) == (8, 6, 6, {'KSJYCOGP': 6, 'xjwn': 4, 'lozrf': 7})
    assert candidate((5, 4, 11), {'GBEOTIH': 2, 'demjo': 3, 'fpjrr': 2}) == (5, 4, 11, {'GBEOTIH': 2, 'demjo': 3, 'fpjrr': 2})
    assert candidate((8, 2, 2), {'KBSGLADKA': 6, 'mwc': 6, 'hnsbm': 4}) == (8, 2, 2, {'KBSGLADKA': 6, 'mwc': 6, 'hnsbm': 4})
    assert candidate((9, 5, 7), {'BNDFKIEZ': 4, 'uuj': 3, 'iwkalcuk': 2}) == (9, 5, 7, {'BNDFKIEZ': 4, 'uuj': 3, 'iwkalcuk': 2})
    assert candidate((3, 10, 1), {'TSGOE': 5, 'cbmtn': 2, 'kaerxhblv': 3}) == (3, 10, 1, {'TSGOE': 5, 'cbmtn': 2, 'kaerxhblv': 3})
    assert candidate((5, 9, 1), {'ZCHBFQ': 5, 'hfj': 7, 'qoxkxbtb': 5}) == (5, 9, 1, {'ZCHBFQ': 5, 'hfj': 7, 'qoxkxbtb': 5})
    assert candidate((7, 2, 1), {'ISA': 4, 'atfw': 4, 'jhui': 8}) == (7, 2, 1, {'ISA': 4, 'atfw': 4, 'jhui': 8})
    assert candidate((6, 4, 8), {'EOGHC': 2, 'zsrkct': 3, 'owegcaa': 5}) == (6, 4, 8, {'EOGHC': 2, 'zsrkct': 3, 'owegcaa': 5})
    assert candidate((4, 3, 8), {'EHR': 2, 'vsbr': 5, 'ryapc': 3}) == (4, 3, 8, {'EHR': 2, 'vsbr': 5, 'ryapc': 3})
    assert candidate((3, 2, 9), {'TFOTNTZIS': 1, 'qoe': 3, 'thwdsln': 8}) == (3, 2, 9, {'TFOTNTZIS': 1, 'qoe': 3, 'thwdsln': 8})
    assert candidate((6, 6, 4), {'QGOAEDQCQ': 1, 'zculx': 5, 'cggw': 5}) == (6, 6, 4, {'QGOAEDQCQ': 1, 'zculx': 5, 'cggw': 5})
    assert candidate((6, 8, 2), {'ZOU': 4, 'hzzk': 5, 'fbdsgkaw': 1}) == (6, 8, 2, {'ZOU': 4, 'hzzk': 5, 'fbdsgkaw': 1})
    assert candidate((1, 7, 10), {'QTNISLMMS': 5, 'afndo': 3, 'qibjck': 3}) == (1, 7, 10, {'QTNISLMMS': 5, 'afndo': 3, 'qibjck': 3})
    assert candidate((6, 3, 11), {'PVPXI': 5, 'dvkl': 4, 'iugh': 3}) == (6, 3, 11, {'PVPXI': 5, 'dvkl': 4, 'iugh': 3})
    assert candidate((3, 4, 7), {'ULHTVJXDD': 5, 'kzhxxv': 2, 'jgyeiamk': 4}) == (3, 4, 7, {'ULHTVJXDD': 5, 'kzhxxv': 2, 'jgyeiamk': 4})
    assert candidate((1, 1, 4), {'NKEBNG': 5, 'jloarg': 6, 'hKNnoxVN': 4}) == (1, 1, 4, {'NKEBNG': 5, 'jloarg': 6, 'hKNnoxVN': 4})
    assert candidate((3, 7, 5), {'PISR': 5, 'knk': 1, 'xEXDeC': 3}) == (3, 7, 5, {'PISR': 5, 'knk': 1, 'xEXDeC': 3})
    assert candidate((1, 2, 1), {'FEPUISKBH': 2, 'tgkpv': 2, 'JLSHW': 5}) == (1, 2, 1, {'FEPUISKBH': 2, 'tgkpv': 2, 'JLSHW': 5})
    assert candidate((1, 4, 2), {'XRESSFU': 6, 'yudj': 2, 'kVvbeZ': 5}) == (1, 4, 2, {'XRESSFU': 6, 'yudj': 2, 'kVvbeZ': 5})
    assert candidate((4, 6, 1), {'FQUEGUV': 3, 'xegf': 4, 'DEfNbIJb': 2}) == (4, 6, 1, {'FQUEGUV': 3, 'xegf': 4, 'DEfNbIJb': 2})
    assert candidate((3, 5, 2), {'RGFS': 5, 'vsya': 8, 'waAoPYDJ': 5}) == (3, 5, 2, {'RGFS': 5, 'vsya': 8, 'waAoPYDJ': 5})
    assert candidate((5, 2, 8), {'FWHB': 3, 'eenu': 7, 'JuhnwM': 2}) == (5, 2, 8, {'FWHB': 3, 'eenu': 7, 'JuhnwM': 2})
    assert candidate((4, 2, 8), {'RAFQXXDBA': 2, 'eze': 5, 'tKifMhb': 7}) == (4, 2, 8, {'RAFQXXDBA': 2, 'eze': 5, 'tKifMhb': 7})
    assert candidate((4, 1, 2), {'XINNOBP': 5, 'pkzmo': 4, 'HuBfmnj': 6}) == (4, 1, 2, {'XINNOBP': 5, 'pkzmo': 4, 'HuBfmnj': 6})
    assert candidate((4, 5, 8), {'HZSEVTGMG': 4, 'jkrngm': 1, 'rIHAw': 7}) == (4, 5, 8, {'HZSEVTGMG': 4, 'jkrngm': 1, 'rIHAw': 7})
    assert candidate((3, 3, 2), {'NJHCWC': 3, 'swvpk': 5, 'YFPMfmEh': 8}) == (3, 3, 2, {'NJHCWC': 3, 'swvpk': 5, 'YFPMfmEh': 8})
    assert candidate((6, 5, 2), {'FVNMENM': 5, 'izopt': 2, 'ogLTfMatX': 9}) == (6, 5, 2, {'FVNMENM': 5, 'izopt': 2, 'ogLTfMatX': 9})
    assert candidate((5, 3, 4), {'POQLLL': 1, 'qgbamd': 1, 'eDZGQmPZA': 1}) == (5, 3, 4, {'POQLLL': 1, 'qgbamd': 1, 'eDZGQmPZA': 1})
    assert candidate((4, 5, 5), {'GYYYRPNXE': 3, 'oljx': 8, 'NHR': 6}) == (4, 5, 5, {'GYYYRPNXE': 3, 'oljx': 8, 'NHR': 6})
    assert candidate((3, 3, 1), {'ETL': 1, 'hkt': 1, 'GQNZDCdv': 5}) == (3, 3, 1, {'ETL': 1, 'hkt': 1, 'GQNZDCdv': 5})
    assert candidate((2, 3, 1), {'GAFPZ': 1, 'gwz': 3, 'ULEhC': 6}) == (2, 3, 1, {'GAFPZ': 1, 'gwz': 3, 'ULEhC': 6})
    assert candidate((3, 5, 3), {'BPZI': 2, 'uxhtz': 7, 'ABOTu': 9}) == (3, 5, 3, {'BPZI': 2, 'uxhtz': 7, 'ABOTu': 9})
    assert candidate((1, 4, 7), {'DZGQT': 4, 'enl': 1, 'Hdjl': 2}) == (1, 4, 7, {'DZGQT': 4, 'enl': 1, 'Hdjl': 2})
    assert candidate((6, 7, 3), {'HXZBCVLZS': 5, 'jlqydn': 5, 'RMPz': 8}) == (6, 7, 3, {'HXZBCVLZS': 5, 'jlqydn': 5, 'RMPz': 8})
    assert candidate((1, 4, 3), {'HTNW': 3, 'yqrllj': 1, 'MgUiBBkF': 6}) == (1, 4, 3, {'HTNW': 3, 'yqrllj': 1, 'MgUiBBkF': 6})
    assert candidate((3, 5, 7), {'NFF': 5, 'szmjby': 6, 'WsPmzIqp': 3}) == (3, 5, 7, {'NFF': 5, 'szmjby': 6, 'WsPmzIqp': 3})
    assert candidate((1, 3, 8), {'VKAOO': 4, 'orza': 1, 'lBnfe': 5}) == (1, 3, 8, {'VKAOO': 4, 'orza': 1, 'lBnfe': 5})
    assert candidate((5, 4, 6), {'XSRTEAICE': 3, 'sjaqmj': 2, 'mvJLsO': 1}) == (5, 4, 6, {'XSRTEAICE': 3, 'sjaqmj': 2, 'mvJLsO': 1})
    assert candidate((5, 3, 6), {'KOIY': 7, 'kzngnk': 5, 'hncWQsSiC': 4}) == (5, 3, 6, {'KOIY': 7, 'kzngnk': 5, 'hncWQsSiC': 4})
    assert candidate((3, 5, 1), {'CWLCI': 4, 'jcrxuu': 2, 'uFNsMazX': 1}) == (3, 5, 1, {'CWLCI': 4, 'jcrxuu': 2, 'uFNsMazX': 1})
    assert candidate((2, 7, 7), {'YOGAZ': 7, 'siba': 4, 'WGX': 6}) == (2, 7, 7, {'YOGAZ': 7, 'siba': 4, 'WGX': 6})
    assert candidate((2, 7, 2), {'UTAN': 2, 'nfc': 8, 'wNhWbx': 8}) == (2, 7, 2, {'UTAN': 2, 'nfc': 8, 'wNhWbx': 8})
    assert candidate((1, 5, 3), {'HRXCIS': 6, 'zapp': 3, 'BXMjO': 5}) == (1, 5, 3, {'HRXCIS': 6, 'zapp': 3, 'BXMjO': 5})
    assert candidate((2, 2, 7), {'NYQ': 2, 'nlid': 2, 'kiBOg': 2}) == (2, 2, 7, {'NYQ': 2, 'nlid': 2, 'kiBOg': 2})
    assert candidate((5, 1, 7), {'XZQDNJWE': 7, 'ncqwa': 1, 'lMPAX': 5}) == (5, 1, 7, {'XZQDNJWE': 7, 'ncqwa': 1, 'lMPAX': 5})
    assert candidate((6, 4, 1), {'QYEVZHW': 1, 'ajqd': 6, 'Rhcki': 4}) == (6, 4, 1, {'QYEVZHW': 1, 'ajqd': 6, 'Rhcki': 4})
    assert candidate((1, 3, 8), {'MTLR': 7, 'kpeku': 2, 'eWGBCrC': 3}) == (1, 3, 8, {'MTLR': 7, 'kpeku': 2, 'eWGBCrC': 3})
    assert candidate((1, 2, 1), {'NAAQ': 4, 'jcx': 5, 'wmDmmaC': 8}) == (1, 2, 1, {'NAAQ': 4, 'jcx': 5, 'wmDmmaC': 8})
    assert candidate((6, 4, 9), {'HSHKNGV': 4, 'gukz': 2, 'QrlhAciFK': 2}) == (6, 4, 9, {'HSHKNGV': 4, 'gukz': 2, 'QrlhAciFK': 2})
    assert candidate((3, 13, 14), {'ZPVTBRRRM': 1, 'fqwf': 5, 'zYy': 3}) == (3, 13, 14, {'ZPVTBRRRM': 1, 'fqwf': 5, 'zYy': 3})
    assert candidate((7, 11, 7), {'KBSODR': 8, 'uypx': 8, 'zDjmKbd': 9}) == (7, 11, 7, {'KBSODR': 8, 'uypx': 8, 'zDjmKbd': 9})
    assert candidate((6, 10, 7), {'WZO': 6, 'zarxy': 9, 'nfnuXUP': 5}) == (6, 10, 7, {'WZO': 6, 'zarxy': 9, 'nfnuXUP': 5})
    assert candidate((8, 11, 12), {'GMM': 7, 'vazf': 4, 'oENYtxfI': 5}) == (8, 11, 12, {'GMM': 7, 'vazf': 4, 'oENYtxfI': 5})
    assert candidate((3, 8, 5), {'EWDRD': 5, 'fqyi': 7, 'xUJ': 4}) == (3, 8, 5, {'EWDRD': 5, 'fqyi': 7, 'xUJ': 4})
    assert candidate((10, 11, 14), {'TJG': 6, 'tyopt': 1, 'TWNhd': 2}) == (10, 11, 14, {'TJG': 6, 'tyopt': 1, 'TWNhd': 2})
    assert candidate((6, 13, 8), {'VLNCDXUTM': 8, 'rzpu': 9, 'jHu': 1}) == (6, 13, 8, {'VLNCDXUTM': 8, 'rzpu': 9, 'jHu': 1})
    assert candidate((6, 13, 14), {'BRRNMAWPR': 4, 'kjl': 7, 'dPDLsPBCz': 8}) == (6, 13, 14, {'BRRNMAWPR': 4, 'kjl': 7, 'dPDLsPBCz': 8})
    assert candidate((7, 8, 6), {'LGWVCTOX': 6, 'qzcfqc': 6, 'fBtMyZEzl': 2}) == (7, 8, 6, {'LGWVCTOX': 6, 'qzcfqc': 6, 'fBtMyZEzl': 2})
    assert candidate((9, 9, 14), {'YADI': 3, 'ryek': 1, 'lkssPKymi': 5}) == (9, 9, 14, {'YADI': 3, 'ryek': 1, 'lkssPKymi': 5})
    assert candidate((10, 9, 11), {'QLHZIW': 8, 'uuj': 2, 'fSCmIenKI': 9}) == (10, 9, 11, {'QLHZIW': 8, 'uuj': 2, 'fSCmIenKI': 9})
    assert candidate((9, 12, 11), {'UTI': 1, 'pvkse': 7, 'yAxOruYX': 10}) == (9, 12, 11, {'UTI': 1, 'pvkse': 7, 'yAxOruYX': 10})
    assert candidate((3, 9, 12), {'EHOIHBRG': 3, 'zozjw': 3, 'eEnts': 6}) == (3, 9, 12, {'EHOIHBRG': 3, 'zozjw': 3, 'eEnts': 6})
    assert candidate((3, 4, 14), {'JPQE': 1, 'ckqb': 6, 'TmLfMzCV': 1}) == (3, 4, 14, {'JPQE': 1, 'ckqb': 6, 'TmLfMzCV': 1})
    assert candidate((11, 12, 14), {'NZPL': 2, 'wuhxk': 1, 'hdmFn': 10}) == (11, 12, 14, {'NZPL': 2, 'wuhxk': 1, 'hdmFn': 10})
    assert candidate((8, 7, 8), {'MDVKKEVCM': 8, 'ekzwd': 4, 'szQgI': 2}) == (8, 7, 8, {'MDVKKEVCM': 8, 'ekzwd': 4, 'szQgI': 2})
    assert candidate((9, 5, 13), {'WUHETRJAI': 8, 'uhga': 2, 'VHLi': 7}) == (9, 5, 13, {'WUHETRJAI': 8, 'uhga': 2, 'VHLi': 7})
    assert candidate((8, 4, 6), {'DMZYGNPJ': 1, 'tnm': 3, 'oMPeoiEon': 10}) == (8, 4, 6, {'DMZYGNPJ': 1, 'tnm': 3, 'oMPeoiEon': 10})
    assert candidate((10, 6, 6), {'HBKF': 3, 'qvoe': 6, 'fpFNWcp': 5}) == (10, 6, 6, {'HBKF': 3, 'qvoe': 6, 'fpFNWcp': 5})
    assert candidate((7, 11, 10), {'XKVFBWEX': 6, 'papd': 3, 'WcPBi': 5}) == (7, 11, 10, {'XKVFBWEX': 6, 'papd': 3, 'WcPBi': 5})
    assert candidate((13, 7, 5), {'JBE': 1, 'iwzz': 3, 'WieDvukXi': 6}) == (13, 7, 5, {'JBE': 1, 'iwzz': 3, 'WieDvukXi': 6})
    assert candidate((12, 10, 7), {'NSPTVFZJJ': 6, 'giysmz': 5, 'TFhNLFEe': 5}) == (12, 10, 7, {'NSPTVFZJJ': 6, 'giysmz': 5, 'TFhNLFEe': 5})
    assert candidate((4, 9, 7), {'RQSZVR': 6, 'yhscnv': 6, 'SRlzXN': 9}) == (4, 9, 7, {'RQSZVR': 6, 'yhscnv': 6, 'SRlzXN': 9})
    assert candidate((7, 9, 10), {'SOOHC': 2, 'rkhuz': 2, 'Gzfd': 7}) == (7, 9, 10, {'SOOHC': 2, 'rkhuz': 2, 'Gzfd': 7})
    assert candidate((4, 7, 11), {'DEXJPJQXG': 4, 'ifjis': 9, 'bWagu': 10}) == (4, 7, 11, {'DEXJPJQXG': 4, 'ifjis': 9, 'bWagu': 10})
    assert candidate((5, 9, 14), {'SYSX': 2, 'mil': 7, 'qxe': 1}) == (5, 9, 14, {'SYSX': 2, 'mil': 7, 'qxe': 1})
    assert candidate((12, 13, 12), {'AMIT': 3, 'wwhvl': 1, 'oQWBtxTn': 6}) == (12, 13, 12, {'AMIT': 3, 'wwhvl': 1, 'oQWBtxTn': 6})
    assert candidate((10, 11, 5), {'FHKRWHXF': 2, 'ikwupk': 2, 'fMMwNvB': 6}) == (10, 11, 5, {'FHKRWHXF': 2, 'ikwupk': 2, 'fMMwNvB': 6})
    assert candidate((13, 7, 10), {'PDGV': 3, 'yxo': 2, 'GzXlm': 4}) == (13, 7, 10, {'PDGV': 3, 'yxo': 2, 'GzXlm': 4})
    assert candidate((9, 5, 6), {'ALCTMRJ': 8, 'qidyz': 4, 'EzDCxP': 5}) == (9, 5, 6, {'ALCTMRJ': 8, 'qidyz': 4, 'EzDCxP': 5})
    assert candidate((6, 14, 7), {'HLDBTSOJ': 7, 'ere': 2, 'WaIaT': 6}) == (6, 14, 7, {'HLDBTSOJ': 7, 'ere': 2, 'WaIaT': 6})
    assert candidate((8, 12, 5), {'EFMSUUP': 3, 'umilo': 7, 'GCPGlM': 9}) == (8, 12, 5, {'EFMSUUP': 3, 'umilo': 7, 'GCPGlM': 9})

if __name__ == '__main__':
    check(add_dict_to_tuple)