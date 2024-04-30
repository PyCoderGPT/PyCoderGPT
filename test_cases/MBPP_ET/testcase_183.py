from case_MBPP_183 import convert_list_dictionary


def check(candidate):
    assert candidate(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] ,[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
    assert candidate(["abc","def","ghi","jkl"],["python","program","language","programs"],[100,200,300,400])==[{'abc':{'python':100}},{'def':{'program':200}},{'ghi':{'language':300}},{'jkl':{'programs':400}}]
    assert candidate(["A1","A2","A3","A4"],["java","C","C++","DBMS"],[10,20,30,40])==[{'A1':{'java':10}},{'A2':{'C':20}},{'A3':{'C++':30}},{'A4':{'DBMS':40}}]
    assert candidate(['4MUE81Q4', 'F24OAE', 'OYUSALHP', 'WOEG'], ['RrSXwun', 'JJBkXUwyL', 'pyFQdOpDDOYIcyM', 'SXYBcsIEgkx'], [81, 99, 84, 90]) == [{'4MUE81Q4': {'RrSXwun': 81}}, {'F24OAE': {'JJBkXUwyL': 99}}, {'OYUSALHP': {'pyFQdOpDDOYIcyM': 84}}, {'WOEG': {'SXYBcsIEgkx': 90}}]
    assert candidate(['N5W9TXB8', 'Y4G8Q', '7DMFP1', 'OM6D5VA'], ['PrMptZ', 'RYNYkvywwa GeZQvo', 'MuMShtNYWMf', 'XwoFbOrSu'], [81, 95, 85, 96]) == [{'N5W9TXB8': {'PrMptZ': 81}}, {'Y4G8Q': {'RYNYkvywwa GeZQvo': 95}}, {'7DMFP1': {'MuMShtNYWMf': 85}}, {'OM6D5VA': {'XwoFbOrSu': 96}}]
    assert candidate(['9YE3Z', '9CRK9UJ', '1PZGV2Z97', 'TR6NIFH'], ['Tqcpb TR', 'owlCbexzoSRKfMZuWF', 'qYmKTXFKQTyMtW', 'LJAsmJhk wACGPBCK'], [87, 101, 90, 96]) == [{'9YE3Z': {'Tqcpb TR': 87}}, {'9CRK9UJ': {'owlCbexzoSRKfMZuWF': 101}}, {'1PZGV2Z97': {'qYmKTXFKQTyMtW': 90}}, {'TR6NIFH': {'LJAsmJhk wACGPBCK': 96}}]
    assert candidate(['LKP2UA', 'CKY', 'Z6DKP', 'N89N'], ['GpVXzPx', 'UggJWkgf Z', 'WTsKEDJeTaAEjhqD ', 'yKgzNQGhraL'], [89, 97, 88, 87]) == [{'LKP2UA': {'GpVXzPx': 89}}, {'CKY': {'UggJWkgf Z': 97}}, {'Z6DKP': {'WTsKEDJeTaAEjhqD ': 88}}, {'N89N': {'yKgzNQGhraL': 87}}]
    assert candidate(['XG4QZQO0', 'Z9VDOD', '4JDT16M', 'GY5WYG7'], ['lBkpezpOrg', 'DfigVhWSUpRL', 'paSAZfTLDh', 'jPDgzSisbJRkO'], [86, 98, 84, 94]) == [{'XG4QZQO0': {'lBkpezpOrg': 86}}, {'Z9VDOD': {'DfigVhWSUpRL': 98}}, {'4JDT16M': {'paSAZfTLDh': 84}}, {'GY5WYG7': {'jPDgzSisbJRkO': 94}}]
    assert candidate(['3DHH', '5L2Y9UYM', '06AMGWPU', 'WV3Q'], ['SHPrYBDVIfCzU', 'eGiJKDvsF', 'TQ TKWnyXhs', 'jNeBOzyY ZlEP'], [82, 94, 92, 96]) == [{'3DHH': {'SHPrYBDVIfCzU': 82}}, {'5L2Y9UYM': {'eGiJKDvsF': 94}}, {'06AMGWPU': {'TQ TKWnyXhs': 92}}, {'WV3Q': {'jNeBOzyY ZlEP': 96}}]
    assert candidate(['GWPIGVD', '9W8M', 'L4H', '6W7'], ['CCHHLprxuEcdEi', 'HjLtXK PXXAbbBDf', 'nvJvySPxONrWgkAKs', 'TjOKixdxJAo MX'], [89, 96, 84, 90]) == [{'GWPIGVD': {'CCHHLprxuEcdEi': 89}}, {'9W8M': {'HjLtXK PXXAbbBDf': 96}}, {'L4H': {'nvJvySPxONrWgkAKs': 84}}, {'6W7': {'TjOKixdxJAo MX': 90}}]
    assert candidate(['A6R9F', 'X2CA6W6Q6', 'OPZNPJO', '6E75QJXE2'], ['kWNMBW uyK', 'HfBIaYVHCUynhiMnYu', 'ODUAuOoWZs', 'aoscgNfoe'], [82, 99, 86, 92]) == [{'A6R9F': {'kWNMBW uyK': 82}}, {'X2CA6W6Q6': {'HfBIaYVHCUynhiMnYu': 99}}, {'OPZNPJO': {'ODUAuOoWZs': 86}}, {'6E75QJXE2': {'aoscgNfoe': 92}}]
    assert candidate(['K8HB2N', 'QNJ2FXRTP', 'HGY6U2G4N', 'DAD'], ['BAAZCYjhiX', 'bnliSOHHTksmSS C', 'pikHsnnEtFmr', 'emOlIvqdnY '], [82, 93, 90, 95]) == [{'K8HB2N': {'BAAZCYjhiX': 82}}, {'QNJ2FXRTP': {'bnliSOHHTksmSS C': 93}}, {'HGY6U2G4N': {'pikHsnnEtFmr': 90}}, {'DAD': {'emOlIvqdnY ': 95}}]
    assert candidate(['UCJ8DLP', '8WFFL', '1HUQSVBD', 'JEHXRP79'], ['XWsCGfhE', 'AYehFECSoOaLE', 've FWZqhIHkFQUqPF', 'tDJLcVCqdvWFHpXKJY'], [89, 100, 88, 89]) == [{'UCJ8DLP': {'XWsCGfhE': 89}}, {'8WFFL': {'AYehFECSoOaLE': 100}}, {'1HUQSVBD': {'ve FWZqhIHkFQUqPF': 88}}, {'JEHXRP79': {'tDJLcVCqdvWFHpXKJY': 89}}]
    assert candidate(['L126WST', 'DP8', 'XMX', 'FGJ2'], ['dXoOSFpwHv UbW', 'qiVXttwUMPjY', 'ZwSFGJRZoUvJF', 'WjAhMhiLDCnBIYBevF'], [81, 101, 86, 91]) == [{'L126WST': {'dXoOSFpwHv UbW': 81}}, {'DP8': {'qiVXttwUMPjY': 101}}, {'XMX': {'ZwSFGJRZoUvJF': 86}}, {'FGJ2': {'WjAhMhiLDCnBIYBevF': 91}}]
    assert candidate(['NJJI', 'E2FD7SSH1', '184WJ', '6EYSSJ3VC'], ['j tJ rqAjPIuhqa', 'ysCMeDeLAfegntY', 'yaNzNhVOsy', 'iYrWirUFnfZYAkutQ'], [83, 96, 89, 91]) == [{'NJJI': {'j tJ rqAjPIuhqa': 83}}, {'E2FD7SSH1': {'ysCMeDeLAfegntY': 96}}, {'184WJ': {'yaNzNhVOsy': 89}}, {'6EYSSJ3VC': {'iYrWirUFnfZYAkutQ': 91}}]
    assert candidate(['CZQ', 'IF6NOTQ', 'K2AO', '2VAUR'], ['wZQdpQlR', 'SnAplLEWKyMbCUBp', 'QruusuJSDAH', 'RbExfAerK'], [81, 102, 92, 95]) == [{'CZQ': {'wZQdpQlR': 81}}, {'IF6NOTQ': {'SnAplLEWKyMbCUBp': 102}}, {'K2AO': {'QruusuJSDAH': 92}}, {'2VAUR': {'RbExfAerK': 95}}]
    assert candidate(['N8W23G7XB', 'F65I', '8CXAPF6E', 'MK2O85C3'], ['OZdudcMe', 'EmhyqRiTWnpEMcbdqi', 'wfkKwI srWt', 'rRQzYfXWBYtdsMJ'], [90, 99, 92, 87]) == [{'N8W23G7XB': {'OZdudcMe': 90}}, {'F65I': {'EmhyqRiTWnpEMcbdqi': 99}}, {'8CXAPF6E': {'wfkKwI srWt': 92}}, {'MK2O85C3': {'rRQzYfXWBYtdsMJ': 87}}]
    assert candidate(['1DOBT0HQZ', '3PRD', 'IFLP3QKYQ', 'CYXVSGU'], ['NqhTsVZAIBxurC', 'DfIigZESrO', 'yIJmPwlZP', 'JjKlylzcIZcOGzN'], [88, 101, 91, 92]) == [{'1DOBT0HQZ': {'NqhTsVZAIBxurC': 88}}, {'3PRD': {'DfIigZESrO': 101}}, {'IFLP3QKYQ': {'yIJmPwlZP': 91}}, {'CYXVSGU': {'JjKlylzcIZcOGzN': 92}}]
    assert candidate(['57ZV4R78O', '1R9L9JA0', '8X1Z3', '9EF'], ['raeVni', 'SGErIFiivmFPGTYha', 'msiTirCPRubbpIt', ' lpSSFKuufpErKQ'], [85, 93, 86, 94]) == [{'57ZV4R78O': {'raeVni': 85}}, {'1R9L9JA0': {'SGErIFiivmFPGTYha': 93}}, {'8X1Z3': {'msiTirCPRubbpIt': 86}}, {'9EF': {' lpSSFKuufpErKQ': 94}}]
    assert candidate(['IQ4K1IT4', 'VC1DH', 'RNH', '2QBRGFN'], ['sBdykp', 'rtDUdLGffqzI', 'rmAbTZioIUgDhFcsVm', 'OyBmVOeeNpirKKVFVg'], [82, 100, 85, 95]) == [{'IQ4K1IT4': {'sBdykp': 82}}, {'VC1DH': {'rtDUdLGffqzI': 100}}, {'RNH': {'rmAbTZioIUgDhFcsVm': 85}}, {'2QBRGFN': {'OyBmVOeeNpirKKVFVg': 95}}]
    assert candidate(['YCLA8P2A', 'HXR263', 'KUZ79WR', '3ZEPT'], ['ZbGKUsBxx', 'gWMTvJcnOvovLG', 'jdVsPMDuxLFNsrCD', 'cnQRZcVSjbTUNtMooN'], [90, 101, 90, 88]) == [{'YCLA8P2A': {'ZbGKUsBxx': 90}}, {'HXR263': {'gWMTvJcnOvovLG': 101}}, {'KUZ79WR': {'jdVsPMDuxLFNsrCD': 90}}, {'3ZEPT': {'cnQRZcVSjbTUNtMooN': 88}}]
    assert candidate(['0QWZIO6N', '5YX', '7SE7ZNI', '8K78SG'], ['oyqdLeEO', 'TPihydBiDbY', 'YlkcmUJxqyhgFrx', 'mBVOXEirXMUgmp'], [88, 95, 84, 87]) == [{'0QWZIO6N': {'oyqdLeEO': 88}}, {'5YX': {'TPihydBiDbY': 95}}, {'7SE7ZNI': {'YlkcmUJxqyhgFrx': 84}}, {'8K78SG': {'mBVOXEirXMUgmp': 87}}]
    assert candidate(['U919', 'F8BSCXE', 'NYSKIDF', 'UT9SWC7Q'], ['MbMhIzPeQAWZ', 'jqZVWhjglO', 'nqmQSgqVW', 'GcwzXBejY qDDarah'], [86, 94, 84, 87]) == [{'U919': {'MbMhIzPeQAWZ': 86}}, {'F8BSCXE': {'jqZVWhjglO': 94}}, {'NYSKIDF': {'nqmQSgqVW': 84}}, {'UT9SWC7Q': {'GcwzXBejY qDDarah': 87}}]
    assert candidate(['3L2P9', 'NI6CXWVHM', 'JF8U', 'F072O0'], ['sILOSz', 'FaWCVVSJHu tJDj', 'SgEINfuEw', 'zvQsBgRwsGMv'], [87, 93, 86, 90]) == [{'3L2P9': {'sILOSz': 87}}, {'NI6CXWVHM': {'FaWCVVSJHu tJDj': 93}}, {'JF8U': {'SgEINfuEw': 86}}, {'F072O0': {'zvQsBgRwsGMv': 90}}]
    assert candidate(['RUL7WH', 'T6Y', '2NZA0', 'CJYQGKA'], ['xsFHXbPhaomNuj', 'BFdtLsxnBPEK', 'krExgWQUbYxOKYa', 'ZZMMXTassZIfJO'], [84, 93, 94, 94]) == [{'RUL7WH': {'xsFHXbPhaomNuj': 84}}, {'T6Y': {'BFdtLsxnBPEK': 93}}, {'2NZA0': {'krExgWQUbYxOKYa': 94}}, {'CJYQGKA': {'ZZMMXTassZIfJO': 94}}]
    assert candidate(['V2V54', '4GHA90C', '36KNJLX', '98XQTU45A'], ['QfKkrGwRMoI', 'xCsYSQvZC', 'UckUqSYlit TuxQ ', 'NIqvcBghUbW'], [81, 93, 94, 89]) == [{'V2V54': {'QfKkrGwRMoI': 81}}, {'4GHA90C': {'xCsYSQvZC': 93}}, {'36KNJLX': {'UckUqSYlit TuxQ ': 94}}, {'98XQTU45A': {'NIqvcBghUbW': 89}}]
    assert candidate(['DPEJ', 'KCB6GAX6', 'WTP', 'LAF4SQ'], ['o NcvrGgxR', 'GmOgTgqOHgSaP', 'QsPsTufwGuq', 'vprssZFvIKRz G'], [88, 100, 88, 93]) == [{'DPEJ': {'o NcvrGgxR': 88}}, {'KCB6GAX6': {'GmOgTgqOHgSaP': 100}}, {'WTP': {'QsPsTufwGuq': 88}}, {'LAF4SQ': {'vprssZFvIKRz G': 93}}]
    assert candidate(['8DD', 'TO92BR', 'W0SPTL8', 'O3D'], ['ZrTWtq UMev', 'uuXpCBNpzHkXWSHhm', 'tSPJjCBgqlLCsWd', 'LvvOjcWbuO'], [80, 94, 87, 95]) == [{'8DD': {'ZrTWtq UMev': 80}}, {'TO92BR': {'uuXpCBNpzHkXWSHhm': 94}}, {'W0SPTL8': {'tSPJjCBgqlLCsWd': 87}}, {'O3D': {'LvvOjcWbuO': 95}}]
    assert candidate(['ICP8FVV1T', 'ANJ', 'YGI89', '28W1SC5LY'], ['aCsiBSpvWrGmqd', 'Ty tjaITeSeYntCr', 'xPbZlvSlRxT', 'ikIIEUFCNqgSoFV'], [85, 95, 89, 92]) == [{'ICP8FVV1T': {'aCsiBSpvWrGmqd': 85}}, {'ANJ': {'Ty tjaITeSeYntCr': 95}}, {'YGI89': {'xPbZlvSlRxT': 89}}, {'28W1SC5LY': {'ikIIEUFCNqgSoFV': 92}}]
    assert candidate(['88N363MN', 'ZPQ41', 'DHQ9GQ3', 'T8JB6VFK'], ['KegEliqp', 'mqHgNtHVklOfp vn', 'iWjUKkmWtMRDtedi', 'VqCshqHzBabMReVj'], [82, 97, 92, 92]) == [{'88N363MN': {'KegEliqp': 82}}, {'ZPQ41': {'mqHgNtHVklOfp vn': 97}}, {'DHQ9GQ3': {'iWjUKkmWtMRDtedi': 92}}, {'T8JB6VFK': {'VqCshqHzBabMReVj': 92}}]
    assert candidate(['2G2ND3J91', 'IGX1F2B', 'XKAZ6T3', 'ZO3JPICFL'], ['acLkWwmcSQgFK', 'sIwrBjuIc', 'rSuSKsfwdU', 'uuEyurQHBHEesutxe'], [89, 95, 84, 95]) == [{'2G2ND3J91': {'acLkWwmcSQgFK': 89}}, {'IGX1F2B': {'sIwrBjuIc': 95}}, {'XKAZ6T3': {'rSuSKsfwdU': 84}}, {'ZO3JPICFL': {'uuEyurQHBHEesutxe': 95}}]
    assert candidate(['ZMV7Q', '40SL', 'MXLA', 'KIY'], ['RFeRnsXIehzXOn', 'WZlzbY H GCQBONq', 'jDGRruXrCDgsBBFZ', 'brJEekhbgGq'], [87, 96, 90, 96]) == [{'ZMV7Q': {'RFeRnsXIehzXOn': 87}}, {'40SL': {'WZlzbY H GCQBONq': 96}}, {'MXLA': {'jDGRruXrCDgsBBFZ': 90}}, {'KIY': {'brJEekhbgGq': 96}}]
    assert candidate(['9S6Q', 'KCVZG', 'J03NPK', '8KLXW'], ['dnehZNFnftS', 'THPGzqqNlf', 'xjUzrvmlHTdHegs', 'eCfjBuRaAN'], [85, 103, 90, 87]) == [{'9S6Q': {'dnehZNFnftS': 85}}, {'KCVZG': {'THPGzqqNlf': 103}}, {'J03NPK': {'xjUzrvmlHTdHegs': 90}}, {'8KLXW': {'eCfjBuRaAN': 87}}]
    assert candidate(['PHK18XKPL', 'HK5DGCE05', 'TLP', '3WD'], ['ReDfXBPM', 'nrjiuoxeKG', 'UWJIPygNM', 'CIcUtWkmASxg'], [81, 97, 94, 92]) == [{'PHK18XKPL': {'ReDfXBPM': 81}}, {'HK5DGCE05': {'nrjiuoxeKG': 97}}, {'TLP': {'UWJIPygNM': 94}}, {'3WD': {'CIcUtWkmASxg': 92}}]
    assert candidate(['KY559', 'X0M', 'P0GGDB5M', 'S0DAB489Z'], ['zkuAFOHfErMMTq', 'eaQhPlYRNj', 'IdEpdsP cRSQ', 'WGrFHLNEfbJOuYM'], [89, 100, 88, 88]) == [{'KY559': {'zkuAFOHfErMMTq': 89}}, {'X0M': {'eaQhPlYRNj': 100}}, {'P0GGDB5M': {'IdEpdsP cRSQ': 88}}, {'S0DAB489Z': {'WGrFHLNEfbJOuYM': 88}}]
    assert candidate(['CDJ', 'SCU698P', '91V32T5J', 'OW4Z6'], ['OovjSFIwCjwAmb', 'SfjzSjoszXRz ', 'wyGcCRoHFBrCoIfY', 'd WMnPuHYKXZay'], [88, 97, 84, 94]) == [{'CDJ': {'OovjSFIwCjwAmb': 88}}, {'SCU698P': {'SfjzSjoszXRz ': 97}}, {'91V32T5J': {'wyGcCRoHFBrCoIfY': 84}}, {'OW4Z6': {'d WMnPuHYKXZay': 94}}]
    assert candidate(['jvpxeeim', 'snikeese', 'bbkhwnu', 'rhmqcd'], ['nqnjo', 'cchdirrj', 'qifyc', 'ylzy'], [97, 203, 302, 404]) == [{'jvpxeeim': {'nqnjo': 97}}, {'snikeese': {'cchdirrj': 203}}, {'bbkhwnu': {'qifyc': 302}}, {'rhmqcd': {'ylzy': 404}}]
    assert candidate(['oluakadn', 'piwno', 'ycasucp', 'ouxnwbhd'], ['spjnurhdma', 'rmyoan', 'kfyattsso', 'rlqxpwpez'], [100, 205, 302, 398]) == [{'oluakadn': {'spjnurhdma': 100}}, {'piwno': {'rmyoan': 205}}, {'ycasucp': {'kfyattsso': 302}}, {'ouxnwbhd': {'rlqxpwpez': 398}}]
    assert candidate(['dpvowdgcr', 'opuil', 'idhdxpziq', 'khe'], ['tbotari', 'saddod', 'bypgrorgejn', 'cyfd'], [101, 200, 296, 396]) == [{'dpvowdgcr': {'tbotari': 101}}, {'opuil': {'saddod': 200}}, {'idhdxpziq': {'bypgrorgejn': 296}}, {'khe': {'cyfd': 396}}]
    assert candidate(['hrctv', 'tlyvf', 'njw', 'cowjgzsl'], ['cuvbzis', 'whzwotcf', 'wsvnry', 'hah'], [97, 195, 305, 397]) == [{'hrctv': {'cuvbzis': 97}}, {'tlyvf': {'whzwotcf': 195}}, {'njw': {'wsvnry': 305}}, {'cowjgzsl': {'hah': 397}}]
    assert candidate(['orjs', 'cre', 'ewzkgn', 'cwoljgmci'], ['jco', 'pox', 'zsdnjbcn', 'mtjolbekdro'], [97, 197, 304, 402]) == [{'orjs': {'jco': 97}}, {'cre': {'pox': 197}}, {'ewzkgn': {'zsdnjbcn': 304}}, {'cwoljgmci': {'mtjolbekdro': 402}}]
    assert candidate(['ndizq', 'orongs', 'svegrjesf', 'erflnt'], ['dgrt', 'hgnpduqij', 'djwegisht', 'rge'], [102, 203, 305, 404]) == [{'ndizq': {'dgrt': 102}}, {'orongs': {'hgnpduqij': 203}}, {'svegrjesf': {'djwegisht': 305}}, {'erflnt': {'rge': 404}}]
    assert candidate(['tgpf', 'inkmntvs', 'oudm', 'xmgemdbmh'], ['hqmritzsz', 'tgn', 'fslsokex', 'vgwzetsx'], [103, 202, 297, 403]) == [{'tgpf': {'hqmritzsz': 103}}, {'inkmntvs': {'tgn': 202}}, {'oudm': {'fslsokex': 297}}, {'xmgemdbmh': {'vgwzetsx': 403}}]
    assert candidate(['iaousqu', 'ipyeygubt', 'quzd', 'depgzizv'], ['bikebkclqby', 'vwoku', 'ahhc', 'vefe'], [104, 199, 305, 403]) == [{'iaousqu': {'bikebkclqby': 104}}, {'ipyeygubt': {'vwoku': 199}}, {'quzd': {'ahhc': 305}}, {'depgzizv': {'vefe': 403}}]
    assert candidate(['jeis', 'gtee', 'pamulewc', 'flnc'], ['tzmhvsclvvg', 'cbdsgtois', 'yvjh', 'ziiclkab'], [96, 197, 302, 403]) == [{'jeis': {'tzmhvsclvvg': 96}}, {'gtee': {'cbdsgtois': 197}}, {'pamulewc': {'yvjh': 302}}, {'flnc': {'ziiclkab': 403}}]
    assert candidate(['gkgcxli', 'kvdljlxx', 'serfxklbr', 'pabk'], ['wxujweiy', 'utzipxstzkf', 'ypqoqpxn', 'ubcorcon'], [104, 195, 303, 395]) == [{'gkgcxli': {'wxujweiy': 104}}, {'kvdljlxx': {'utzipxstzkf': 195}}, {'serfxklbr': {'ypqoqpxn': 303}}, {'pabk': {'ubcorcon': 395}}]
    assert candidate(['pbem', 'scqociq', 'gbhuax', 'gmpbrsk'], ['gdfcezmefk', 'ggibv', 'llakademkw', 'jint'], [100, 200, 301, 404]) == [{'pbem': {'gdfcezmefk': 100}}, {'scqociq': {'ggibv': 200}}, {'gbhuax': {'llakademkw': 301}}, {'gmpbrsk': {'jint': 404}}]
    assert candidate(['qen', 'awqodbq', 'fts', 'klgaah'], ['rckyjoooykl', 'djhhugxxykdt', 'rieteq', 'mgfgu'], [101, 205, 298, 397]) == [{'qen': {'rckyjoooykl': 101}}, {'awqodbq': {'djhhugxxykdt': 205}}, {'fts': {'rieteq': 298}}, {'klgaah': {'mgfgu': 397}}]
    assert candidate(['hdoaztva', 'evk', 'wolnretm', 'jlgvgp'], ['awqfk', 'btzpzg', 'zdikvtndcoj', 'wgidrr'], [99, 199, 300, 397]) == [{'hdoaztva': {'awqfk': 99}}, {'evk': {'btzpzg': 199}}, {'wolnretm': {'zdikvtndcoj': 300}}, {'jlgvgp': {'wgidrr': 397}}]
    assert candidate(['jdu', 'xfgmb', 'iuyrlwkgg', 'xhu'], ['apmpunqivagv', 'cvprcstog', 'cgcdbiwlws', 'nzbbuyyzbp'], [101, 200, 299, 400]) == [{'jdu': {'apmpunqivagv': 101}}, {'xfgmb': {'cvprcstog': 200}}, {'iuyrlwkgg': {'cgcdbiwlws': 299}}, {'xhu': {'nzbbuyyzbp': 400}}]
    assert candidate(['ylupsys', 'wbfdey', 'gigzs', 'gmsx'], ['rcavavqara', 'xzoyvdmutrut', 'zyczxgoxqw', 'ixsbybtvvoy'], [95, 205, 296, 404]) == [{'ylupsys': {'rcavavqara': 95}}, {'wbfdey': {'xzoyvdmutrut': 205}}, {'gigzs': {'zyczxgoxqw': 296}}, {'gmsx': {'ixsbybtvvoy': 404}}]
    assert candidate(['wmtnynivi', 'canibbiel', 'vkacu', 'dxe'], ['nyipzjbyfmoi', 'fitfhs', 'vfizzhytol', 'gpzsdawsprrm'], [95, 195, 304, 404]) == [{'wmtnynivi': {'nyipzjbyfmoi': 95}}, {'canibbiel': {'fitfhs': 195}}, {'vkacu': {'vfizzhytol': 304}}, {'dxe': {'gpzsdawsprrm': 404}}]
    assert candidate(['hixuq', 'hcjlwudw', 'vmhsf', 'xkkpfl'], ['jnhsbobbrrq', 'ibfznxxwm', 'cqm', 'rur'], [97, 197, 305, 403]) == [{'hixuq': {'jnhsbobbrrq': 97}}, {'hcjlwudw': {'ibfznxxwm': 197}}, {'vmhsf': {'cqm': 305}}, {'xkkpfl': {'rur': 403}}]
    assert candidate(['ppgawdw', 'vkiutyg', 'aes', 'zljfzaql'], ['dbkp', 'sluqghdeob', 'zsyxrakxds', 'uybxflbqmbz'], [103, 203, 299, 396]) == [{'ppgawdw': {'dbkp': 103}}, {'vkiutyg': {'sluqghdeob': 203}}, {'aes': {'zsyxrakxds': 299}}, {'zljfzaql': {'uybxflbqmbz': 396}}]
    assert candidate(['qpoqbjzed', 'qavbngsxa', 'esbjreot', 'knlpmgzj'], ['wqyzd', 'oiijwdkf', 'kbovz', 'sqmjutsi'], [97, 199, 301, 403]) == [{'qpoqbjzed': {'wqyzd': 97}}, {'qavbngsxa': {'oiijwdkf': 199}}, {'esbjreot': {'kbovz': 301}}, {'knlpmgzj': {'sqmjutsi': 403}}]
    assert candidate(['bjikejvbz', 'wtlhoqvjz', 'zvvgq', 'hgkszoch'], ['sbilyli', 'wnduiw', 'xvqwvml', 'srwldg'], [100, 197, 303, 395]) == [{'bjikejvbz': {'sbilyli': 100}}, {'wtlhoqvjz': {'wnduiw': 197}}, {'zvvgq': {'xvqwvml': 303}}, {'hgkszoch': {'srwldg': 395}}]
    assert candidate(['rpiiwrhp', 'cmhg', 'vmaqu', 'jycs'], ['uajigbwmlwe', 'ovawdx', 'btkgfgbyo', 'kpsnohbjdzkt'], [103, 195, 297, 398]) == [{'rpiiwrhp': {'uajigbwmlwe': 103}}, {'cmhg': {'ovawdx': 195}}, {'vmaqu': {'btkgfgbyo': 297}}, {'jycs': {'kpsnohbjdzkt': 398}}]
    assert candidate(['hmkuvkot', 'kpkaei', 'kwu', 'rofeuntbc'], ['jeytvy', 'ctlkaitx', 'nnumx', 'ykngfsyzfxyn'], [103, 205, 305, 404]) == [{'hmkuvkot': {'jeytvy': 103}}, {'kpkaei': {'ctlkaitx': 205}}, {'kwu': {'nnumx': 305}}, {'rofeuntbc': {'ykngfsyzfxyn': 404}}]
    assert candidate(['qjpk', 'ucbg', 'qmt', 'jcn'], ['ibbnmrgaer', 'nljqica', 'gcjtaw', 'xrzgqdjpcfn'], [100, 197, 295, 402]) == [{'qjpk': {'ibbnmrgaer': 100}}, {'ucbg': {'nljqica': 197}}, {'qmt': {'gcjtaw': 295}}, {'jcn': {'xrzgqdjpcfn': 402}}]
    assert candidate(['gtmueyvf', 'gsj', 'vdghiyxo', 'iwil'], ['minkxowdpes', 'hnfkyqx', 'mitw', 'dlejvrplf'], [101, 197, 301, 403]) == [{'gtmueyvf': {'minkxowdpes': 101}}, {'gsj': {'hnfkyqx': 197}}, {'vdghiyxo': {'mitw': 301}}, {'iwil': {'dlejvrplf': 403}}]
    assert candidate(['nmro', 'hfl', 'fydrgllk', 'hnqhdu'], ['ccos', 'ayktzhdhfgo', 'qfcokyz', 'xgj'], [96, 199, 299, 404]) == [{'nmro': {'ccos': 96}}, {'hfl': {'ayktzhdhfgo': 199}}, {'fydrgllk': {'qfcokyz': 299}}, {'hnqhdu': {'xgj': 404}}]
    assert candidate(['bniptu', 'nkk', 'nwntc', 'teldo'], ['puplcjovu', 'olf', 'yiqnyrrai', 'cnphhnvwrblj'], [101, 205, 304, 401]) == [{'bniptu': {'puplcjovu': 101}}, {'nkk': {'olf': 205}}, {'nwntc': {'yiqnyrrai': 304}}, {'teldo': {'cnphhnvwrblj': 401}}]
    assert candidate(['nmkvxdibb', 'mkyoeheqf', 'bxhwz', 'igab'], ['uhvgxr', 'okkwwuauq', 'joktbet', 'yepoflvhr'], [105, 197, 300, 395]) == [{'nmkvxdibb': {'uhvgxr': 105}}, {'mkyoeheqf': {'okkwwuauq': 197}}, {'bxhwz': {'joktbet': 300}}, {'igab': {'yepoflvhr': 395}}]
    assert candidate(['mcw', 'dsrbsnji', 'sulez', 'kbcwpgik'], ['psy', 'bxsoovrtuhe', 'wpj', 'betpeuvsorm'], [100, 195, 303, 404]) == [{'mcw': {'psy': 100}}, {'dsrbsnji': {'bxsoovrtuhe': 195}}, {'sulez': {'wpj': 303}}, {'kbcwpgik': {'betpeuvsorm': 404}}]
    assert candidate(['gezb', 'qojnatc', 'exxktx', 'tnmpmtgkk'], ['yetmtyyldrl', 'lkeuohe', 'qhuficbvkkgo', 'kxoryapllcdv'], [104, 200, 296, 399]) == [{'gezb': {'yetmtyyldrl': 104}}, {'qojnatc': {'lkeuohe': 200}}, {'exxktx': {'qhuficbvkkgo': 296}}, {'tnmpmtgkk': {'kxoryapllcdv': 399}}]
    assert candidate(['tmyf', 'nke', 'wecv', 'rlmluthg'], ['mjhcvxz', 'yjfw', 'xxpywdy', 'xqfiezrti'], [103, 197, 304, 402]) == [{'tmyf': {'mjhcvxz': 103}}, {'nke': {'yjfw': 197}}, {'wecv': {'xxpywdy': 304}}, {'rlmluthg': {'xqfiezrti': 402}}]
    assert candidate(['ssozlp', 'eywceq', 'yfueecu', 'otrp'], ['bniiamehel', 'pocglsljsns', 'ohjdobq', 'dpqjemec'], [104, 199, 299, 399]) == [{'ssozlp': {'bniiamehel': 104}}, {'eywceq': {'pocglsljsns': 199}}, {'yfueecu': {'ohjdobq': 299}}, {'otrp': {'dpqjemec': 399}}]
    assert candidate(['mby', 'gsokscfv', 'coldyvovs', 'jnrsnpyc'], ['jjprobpafddb', 'fxzbquhs', 'nmmzauwfnxyu', 'rbefr'], [105, 197, 304, 395]) == [{'mby': {'jjprobpafddb': 105}}, {'gsokscfv': {'fxzbquhs': 197}}, {'coldyvovs': {'nmmzauwfnxyu': 304}}, {'jnrsnpyc': {'rbefr': 395}}]
    assert candidate(['snui', 'zxeymk', 'zbnu', 'rhlmx'], ['lgaeruehpuai', 'jlfkguq', 'ppacjoe', 'jzgtzd'], [105, 199, 303, 395]) == [{'snui': {'lgaeruehpuai': 105}}, {'zxeymk': {'jlfkguq': 199}}, {'zbnu': {'ppacjoe': 303}}, {'rhlmx': {'jzgtzd': 395}}]
    assert candidate(['ZZMDA', 'CTFNV', '88Q6', 'N7Z632'], ['vzkn', 'B', '=#WUVG?', 'ZADVC'], [10, 24, 29, 42]) == [{'ZZMDA': {'vzkn': 10}}, {'CTFNV': {'B': 24}}, {'88Q6': {'=#WUVG?': 29}}, {'N7Z632': {'ZADVC': 42}}]
    assert candidate(['LIT7O', 'N2G3', '3A46FL', '4DEI'], ['neg', 'S', '_<CX-', 'LGM'], [12, 17, 27, 36]) == [{'LIT7O': {'neg': 12}}, {'N2G3': {'S': 17}}, {'3A46FL': {'_<CX-': 27}}, {'4DEI': {'LGM': 36}}]
    assert candidate(['EBV', '3QTIS', '8FRGB', 'UCQ'], ['zcbggc', 'N', 'HHI/*L', 'WMB'], [15, 20, 35, 41]) == [{'EBV': {'zcbggc': 15}}, {'3QTIS': {'N': 20}}, {'8FRGB': {'HHI/*L': 35}}, {'UCQ': {'WMB': 41}}]
    assert candidate(['1OL5W', '5EY7GG', 'TNHPC', 'KT0TQW'], ['zinq', 'Z', '&T-!*', 'MWXHZAJTU'], [10, 23, 30, 41]) == [{'1OL5W': {'zinq': 10}}, {'5EY7GG': {'Z': 23}}, {'TNHPC': {'&T-!*': 30}}, {'KT0TQW': {'MWXHZAJTU': 41}}]
    assert candidate(['DDF6', 'ZOKBL', 'NP50B6', '98AG3'], ['qdcnoay', 'E', 'O%DXA~', 'BOCANZYIF'], [7, 22, 27, 35]) == [{'DDF6': {'qdcnoay': 7}}, {'ZOKBL': {'E': 22}}, {'NP50B6': {'O%DXA~': 27}}, {'98AG3': {'BOCANZYIF': 35}}]
    assert candidate(['K4T', '5Z62', 'M8WJ', '5KKU'], ['lwezmyx', 'H', 'WITO#F', 'UKF'], [7, 21, 33, 42]) == [{'K4T': {'lwezmyx': 7}}, {'5Z62': {'H': 21}}, {'M8WJ': {'WITO#F': 33}}, {'5KKU': {'UKF': 42}}]
    assert candidate(['4DU', 'TD4T', 'XBV95W', 'WU8BUA'], ['xakcuc', 'Y', ':TGR|Q', 'CWYS'], [14, 18, 29, 44]) == [{'4DU': {'xakcuc': 14}}, {'TD4T': {'Y': 18}}, {'XBV95W': {':TGR|Q': 29}}, {'WU8BUA': {'CWYS': 44}}]
    assert candidate(['T408', 'TRNEX', '0P4610', 'HYZAG'], ['eymotcusz', 'J', 'GR=?', 'YPYHHO'], [15, 24, 25, 35]) == [{'T408': {'eymotcusz': 15}}, {'TRNEX': {'J': 24}}, {'0P4610': {'GR=?': 25}}, {'HYZAG': {'YPYHHO': 35}}]
    assert candidate(['QBF', '8D2G', '9XR6B8', '12Q6'], ['zxl', 'G', 'PAL#<', 'NUFCQNP'], [6, 16, 25, 45]) == [{'QBF': {'zxl': 6}}, {'8D2G': {'G': 16}}, {'9XR6B8': {'PAL#<': 25}}, {'12Q6': {'NUFCQNP': 45}}]
    assert candidate(['6VNE', '0DTKBB', 'TAJ8', 'RM2XTY'], ['izmcnk', 'U', '=B?UMT', 'JDVXF'], [15, 20, 28, 43]) == [{'6VNE': {'izmcnk': 15}}, {'0DTKBB': {'U': 20}}, {'TAJ8': {'=B?UMT': 28}}, {'RM2XTY': {'JDVXF': 43}}]
    assert candidate(['NJD', 'JC1', 'JCCTBJ', 'KPS'], ['ebujt', 'U', 'WE@H!PI&', 'ASGQWVHKM'], [6, 25, 34, 38]) == [{'NJD': {'ebujt': 6}}, {'JC1': {'U': 25}}, {'JCCTBJ': {'WE@H!PI&': 34}}, {'KPS': {'ASGQWVHKM': 38}}]
    assert candidate(['THDE', '0U7B', 'ZQFPBO', 'FBR'], ['rgxu', 'X', 'OVL', 'VOLXNWI'], [14, 22, 26, 40]) == [{'THDE': {'rgxu': 14}}, {'0U7B': {'X': 22}}, {'ZQFPBO': {'OVL': 26}}, {'FBR': {'VOLXNWI': 40}}]
    assert candidate(['1VDC9', '0M4NS', '9OYE7', 'AQM8'], ['bswosct', 'I', 'YLYVSWW', 'KWMRDZHG'], [6, 17, 30, 39]) == [{'1VDC9': {'bswosct': 6}}, {'0M4NS': {'I': 17}}, {'9OYE7': {'YLYVSWW': 30}}, {'AQM8': {'KWMRDZHG': 39}}]
    assert candidate(['U8VPKX', 'PZNSL', 'I5TP8F', '907'], ['hqpgma', 'K', 'GLYR', 'XSVLK'], [12, 18, 26, 41]) == [{'U8VPKX': {'hqpgma': 12}}, {'PZNSL': {'K': 18}}, {'I5TP8F': {'GLYR': 26}}, {'907': {'XSVLK': 41}}]
    assert candidate(['MGMG', '49XW2', 'F30J', '9G67H'], ['ldgpzur', 'G', 'SE~', 'TOUOJ'], [6, 20, 29, 35]) == [{'MGMG': {'ldgpzur': 6}}, {'49XW2': {'G': 20}}, {'F30J': {'SE~': 29}}, {'9G67H': {'TOUOJ': 35}}]
    assert candidate(['E1E', '539VY', 'VRYN', 'IGL67'], ['uapy', 'E', '$GV:', 'NGRPOE'], [13, 19, 30, 39]) == [{'E1E': {'uapy': 13}}, {'539VY': {'E': 19}}, {'VRYN': {'$GV:': 30}}, {'IGL67': {'NGRPOE': 39}}]
    assert candidate(['02M8SA', 'LC7', '59WH9', 'NJDF'], ['zldq', 'R', 'I-X', 'GQE'], [7, 20, 25, 42]) == [{'02M8SA': {'zldq': 7}}, {'LC7': {'R': 20}}, {'59WH9': {'I-X': 25}}, {'NJDF': {'GQE': 42}}]
    assert candidate(['2EL3E', 'KZRZU', '4W0E', 'RMU'], ['uahyn', 'M', 'WR+!', 'OCVNBBX'], [13, 19, 27, 45]) == [{'2EL3E': {'uahyn': 13}}, {'KZRZU': {'M': 19}}, {'4W0E': {'WR+!': 27}}, {'RMU': {'OCVNBBX': 45}}]
    assert candidate(['CFV6', 'YX5AL', 'Z0VY', 'RFCFI'], ['qpa', 'D', 'T-S^V@X', 'QWBADZT'], [11, 23, 28, 40]) == [{'CFV6': {'qpa': 11}}, {'YX5AL': {'D': 23}}, {'Z0VY': {'T-S^V@X': 28}}, {'RFCFI': {'QWBADZT': 40}}]
    assert candidate(['IZ88', 'TDM', '5Y8FB', 'UGYR'], ['key', 'Q', 'W@PP', 'BTUUY'], [11, 20, 25, 38]) == [{'IZ88': {'key': 11}}, {'TDM': {'Q': 20}}, {'5Y8FB': {'W@PP': 25}}, {'UGYR': {'BTUUY': 38}}]
    assert candidate(['K0D5HV', 'XKJCF', 'GJ2', 'KZ6WWF'], ['gqtvsl', 'Q', 'S<SF', 'SOC'], [15, 16, 32, 37]) == [{'K0D5HV': {'gqtvsl': 15}}, {'XKJCF': {'Q': 16}}, {'GJ2': {'S<SF': 32}}, {'KZ6WWF': {'SOC': 37}}]
    assert candidate(['2NY4Z', 'C05GH', 'PKZ', 'Y57Z1'], ['lwni', 'X', 'A^DV+P|A<', 'TIZ'], [6, 25, 29, 41]) == [{'2NY4Z': {'lwni': 6}}, {'C05GH': {'X': 25}}, {'PKZ': {'A^DV+P|A<': 29}}, {'Y57Z1': {'TIZ': 41}}]
    assert candidate(['CI95OF', '3WUPPK', 'SWS', 'RQH'], ['gec', 'R', '*-IQ|/=', 'RKBEGABF'], [6, 23, 29, 37]) == [{'CI95OF': {'gec': 6}}, {'3WUPPK': {'R': 23}}, {'SWS': {'*-IQ|/=': 29}}, {'RQH': {'RKBEGABF': 37}}]
    assert candidate(['KYXXK', 'GN4V8', 'ERN4LL', 'IL4DD'], ['cevixoh', 'U', '&%XAI', 'PGMDACZW'], [11, 24, 35, 45]) == [{'KYXXK': {'cevixoh': 11}}, {'GN4V8': {'U': 24}}, {'ERN4LL': {'&%XAI': 35}}, {'IL4DD': {'PGMDACZW': 45}}]
    assert candidate(['N3Z', 'QMLFI2', '4M1', 'E6TY4X'], ['oakpn', 'L', 'T@RJS', 'ANJZBGX'], [7, 21, 32, 36]) == [{'N3Z': {'oakpn': 7}}, {'QMLFI2': {'L': 21}}, {'4M1': {'T@RJS': 32}}, {'E6TY4X': {'ANJZBGX': 36}}]
    assert candidate(['7R5U', 'DA9', 'YCU', '1UH3'], ['tgntp', 'A', 'R~*U', 'JLFUNGROP'], [13, 15, 33, 39]) == [{'7R5U': {'tgntp': 13}}, {'DA9': {'A': 15}}, {'YCU': {'R~*U': 33}}, {'1UH3': {'JLFUNGROP': 39}}]
    assert candidate(['OY8BH3', 'ONGAS', 'E1F6', 'ZI8'], ['vakyhzrg', 'Y', '#@CF:@@', 'QBV'], [7, 22, 25, 37]) == [{'OY8BH3': {'vakyhzrg': 7}}, {'ONGAS': {'Y': 22}}, {'E1F6': {'#@CF:@@': 25}}, {'ZI8': {'QBV': 37}}]
    assert candidate(['TS41F', '1HC', 'Q24CRE', 'C4PXU'], ['kqyhid', 'Q', '#DZRSZW', 'DYBHIRR'], [8, 20, 31, 39]) == [{'TS41F': {'kqyhid': 8}}, {'1HC': {'Q': 20}}, {'Q24CRE': {'#DZRSZW': 31}}, {'C4PXU': {'DYBHIRR': 39}}]
    assert candidate(['W2O', 'O0D412', 'VX5', 'FV0'], ['adcsj', 'Y', '~/GHQ', 'UVEWYRJK'], [14, 18, 26, 36]) == [{'W2O': {'adcsj': 14}}, {'O0D412': {'Y': 18}}, {'VX5': {'~/GHQ': 26}}, {'FV0': {'UVEWYRJK': 36}}]
    assert candidate(['JVPG7', 'SRHP6K', 'FRM', 'SGJK7U'], ['xiuor', 'F', 'A:NND=W', 'PZH'], [10, 18, 31, 38]) == [{'JVPG7': {'xiuor': 10}}, {'SRHP6K': {'F': 18}}, {'FRM': {'A:NND=W': 31}}, {'SGJK7U': {'PZH': 38}}]
    assert candidate(['P567WD', 'HH28', 'TD6', '2KH15'], ['spr', 'B', 'B$F?A:', 'OXUA'], [7, 18, 25, 40]) == [{'P567WD': {'spr': 7}}, {'HH28': {'B': 18}}, {'TD6': {'B$F?A:': 25}}, {'2KH15': {'OXUA': 40}}]
    assert candidate(['8GJX', 'NEXZ6', 'OMZ1W', 'GZ1'], ['sqf', 'B', 'N-D', 'SBROW'], [15, 19, 35, 44]) == [{'8GJX': {'sqf': 15}}, {'NEXZ6': {'B': 19}}, {'OMZ1W': {'N-D': 35}}, {'GZ1': {'SBROW': 44}}]
    assert candidate(['XON', '248', 'A11', 'W4NFH6'], ['dxamm', 'F', 'KJJ|VXD', 'VCGQ'], [8, 15, 28, 43]) == [{'XON': {'dxamm': 8}}, {'248': {'F': 15}}, {'A11': {'KJJ|VXD': 28}}, {'W4NFH6': {'VCGQ': 43}}]

if __name__ == '__main__':
    check(convert_list_dictionary)