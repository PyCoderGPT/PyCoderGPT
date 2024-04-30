from case_MBPP_252 import drop_empty


def check(candidate):
    assert candidate({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
    assert candidate({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}
    assert candidate({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'}
    assert candidate({'2n25': 'LQNnMq', 'cv0': 'tuIsx', 'jjn': None}) == {'2n25': 'LQNnMq', 'cv0': 'tuIsx'}
    assert candidate({'yrr': 'JDOt', '9s9': 'QqHdahSf', 'z4nv': None}) == {'yrr': 'JDOt', '9s9': 'QqHdahSf'}
    assert candidate({'4z70d': 'hUiL', 'zeu7g': 'bQoEp', 'a2n': None}) == {'4z70d': 'hUiL', 'zeu7g': 'bQoEp'}
    assert candidate({'c9e3q': 'iWwLWv', 'aqnol': 'ojJFa', '9gv': None}) == {'c9e3q': 'iWwLWv', 'aqnol': 'ojJFa'}
    assert candidate({'7j1': 'glXWkYhcE', 'astt': 'jdNa', 's2c7': None}) == {'7j1': 'glXWkYhcE', 'astt': 'jdNa'}
    assert candidate({'oxx1': 'Qhqme', '0c7pj': 'iAzrK', 'yi7': None}) == {'oxx1': 'Qhqme', '0c7pj': 'iAzrK'}
    assert candidate({'gsq': 'cIErXgntJ', '8vtth9': 'GymDovPtR', '1i9h': None}) == {'gsq': 'cIErXgntJ', '8vtth9': 'GymDovPtR'}
    assert candidate({'siuy': 'LSGnZP', '31e0e': 'kzdIEJsYk', 'qfev': None}) == {'siuy': 'LSGnZP', '31e0e': 'kzdIEJsYk'}
    assert candidate({'qgmi14': 'LIftGMro', 'wsua': 'bEPe', '9afni': None}) == {'qgmi14': 'LIftGMro', 'wsua': 'bEPe'}
    assert candidate({'fd4': 'OOS', 'riby': 'bWH', 'd4rk': None}) == {'fd4': 'OOS', 'riby': 'bWH'}
    assert candidate({'v4erv': 'PpXmT', '45tx': 'VRelcsa', '8cm6u5': None}) == {'v4erv': 'PpXmT', '45tx': 'VRelcsa'}
    assert candidate({'h4ql': 'RPTkuk', 'cgpp': 'uxvlw', 's9b': None}) == {'h4ql': 'RPTkuk', 'cgpp': 'uxvlw'}
    assert candidate({'bkrwx': 'VzyaT', 'kmzunb': 'wios', 'pjbefn': None}) == {'bkrwx': 'VzyaT', 'kmzunb': 'wios'}
    assert candidate({'0u9ev': 'NfooAVKgn', 'gtvr': 'TKt', 'j59c': None}) == {'0u9ev': 'NfooAVKgn', 'gtvr': 'TKt'}
    assert candidate({'i6n7': 'YsFrTvQ', 'yct': 'nEw', 'kfz1l5': None}) == {'i6n7': 'YsFrTvQ', 'yct': 'nEw'}
    assert candidate({'t6m': 'yHe', '6hp': 'VMbKGWJY', '13m45': None}) == {'t6m': 'yHe', '6hp': 'VMbKGWJY'}
    assert candidate({'ptfsb': 'iCKUfVm', 'pzjy': 'WaG', 'pb3fjr': None}) == {'ptfsb': 'iCKUfVm', 'pzjy': 'WaG'}
    assert candidate({'shmve': 'tZZ', 'ywt': 'bNV', 'cl2i': None}) == {'shmve': 'tZZ', 'ywt': 'bNV'}
    assert candidate({'xpe3h1': 'GbRLHacO', 'n86b9f': 'wCvxWbmUV', 'nnd': None}) == {'xpe3h1': 'GbRLHacO', 'n86b9f': 'wCvxWbmUV'}
    assert candidate({'o6g53': 'VHxl', 'krga17': 'bBiAw', '3vr8fe': None}) == {'o6g53': 'VHxl', 'krga17': 'bBiAw'}
    assert candidate({'9f0no': 'iMvOp', 'z6gr10': 'oICk', 'ef8': None}) == {'9f0no': 'iMvOp', 'z6gr10': 'oICk'}
    assert candidate({'j3ddy': 'ysvmjMrX', 'phy4d': 'EcKcHg', 'il08': None}) == {'j3ddy': 'ysvmjMrX', 'phy4d': 'EcKcHg'}
    assert candidate({'cxwy': 'aXGVZ', 'gwk01': 'ElGXU', 'ualpd': None}) == {'cxwy': 'aXGVZ', 'gwk01': 'ElGXU'}
    assert candidate({'jtz4zt': 'blS', '9qh': 'CNyIhQz', '3m5wt': None}) == {'jtz4zt': 'blS', '9qh': 'CNyIhQz'}
    assert candidate({'6o4v6n': 'YcgWpAmyU', 'dyz': 'jFUXj', 'a71q': None}) == {'6o4v6n': 'YcgWpAmyU', 'dyz': 'jFUXj'}
    assert candidate({'08z': 'uXicoC', '1cpsfm': 'ZjG', 'jhkmtm': None}) == {'08z': 'uXicoC', '1cpsfm': 'ZjG'}
    assert candidate({'t0u': 'pDb', 'ib4rc': 'TvlHO', '1nqu': None}) == {'t0u': 'pDb', 'ib4rc': 'TvlHO'}
    assert candidate({'uc7hv': 'lWcBoQb', 'i0b9sc': 'pgMkLzDSn', 'idamk': None}) == {'uc7hv': 'lWcBoQb', 'i0b9sc': 'pgMkLzDSn'}
    assert candidate({'nbr': 'LNKnOBna', 'r9yz7': 'unPgGkP', '74mww': None}) == {'nbr': 'LNKnOBna', 'r9yz7': 'unPgGkP'}
    assert candidate({'x2djd': 'cYfP', 's8s9c': 'SXSR', 'tym': None}) == {'x2djd': 'cYfP', 's8s9c': 'SXSR'}
    assert candidate({'qztipz': 'dhU', 'n39': 'TGxsmkbl', 'jd8x': None}) == {'qztipz': 'dhU', 'n39': 'TGxsmkbl'}
    assert candidate({'01nv': 'bGyPFtjo', '39umq': 'FJgc', 'zp0z': None}) == {'01nv': 'bGyPFtjo', '39umq': 'FJgc'}
    assert candidate({'41rybs': 'gxnSVN', 'cys': 'SNYhRdY', 'uih': None}) == {'41rybs': 'gxnSVN', 'cys': 'SNYhRdY'}
    assert candidate({'cxi': 'iAgqMXfx', 'cqzl5d': None, 'zoy6ks': None}) == {'cxi': 'iAgqMXfx'}
    assert candidate({'6rh8d': 'vut', '2hmlmj': None, '9igsgz': None}) == {'6rh8d': 'vut'}
    assert candidate({'r1tn': 'fFWbsk', 't11sv': None, '5p55r': None}) == {'r1tn': 'fFWbsk'}
    assert candidate({'6osa6': 'NiTHuhCsw', 'zl7': None, 'nca8': None}) == {'6osa6': 'NiTHuhCsw'}
    assert candidate({'1k0td': 'PQahulE', '2n9': None, '90g8o': None}) == {'1k0td': 'PQahulE'}
    assert candidate({'206': 'sEWv', 'x0ju': None, 'lbpvd': None}) == {'206': 'sEWv'}
    assert candidate({'ef89f': 'YEtQYtcF', '3j24s': None, 'gl17': None}) == {'ef89f': 'YEtQYtcF'}
    assert candidate({'t96w': 'PopYERAfD', 'cfpd': None, 'j15': None}) == {'t96w': 'PopYERAfD'}
    assert candidate({'8s1y': 'ONRiOHD', 'ih4u': None, 'c0mt0': None}) == {'8s1y': 'ONRiOHD'}
    assert candidate({'z23': 'etkDGRC', '0rj': None, '93jcqf': None}) == {'z23': 'etkDGRC'}
    assert candidate({'t2hv6p': 'Ycl', 'mcvi6': None, 'ivwpj': None}) == {'t2hv6p': 'Ycl'}
    assert candidate({'wryxl3': 'hYQxweb', 'qbm17u': None, 'zhwpz': None}) == {'wryxl3': 'hYQxweb'}
    assert candidate({'wwd': 'qWqFGhg', 'aobqdc': None, '9r3lz7': None}) == {'wwd': 'qWqFGhg'}
    assert candidate({'lb3f': 'Kvl', 'kqlce': None, 'yc7jwn': None}) == {'lb3f': 'Kvl'}
    assert candidate({'2p3': 'CKH', '3oy': None, '4x1z': None}) == {'2p3': 'CKH'}
    assert candidate({'q7k': 'CHNPmQKkh', '5z9r': None, 'use3m': None}) == {'q7k': 'CHNPmQKkh'}
    assert candidate({'oq0lz': 'WTgorBmL', '63r1m': None, 'iye6': None}) == {'oq0lz': 'WTgorBmL'}
    assert candidate({'s63r5b': 'uXzndjX', '7469': None, 'grg4x': None}) == {'s63r5b': 'uXzndjX'}
    assert candidate({'tbiy1': 'KAFp', 'rmge4a': None, 'vmf76': None}) == {'tbiy1': 'KAFp'}
    assert candidate({'qqssfi': 'WHVm', 'r6t9l4': None, 'o4q': None}) == {'qqssfi': 'WHVm'}
    assert candidate({'hp81jf': 'JIrGnLY', 'e0o6e': None, 'iyy0y6': None}) == {'hp81jf': 'JIrGnLY'}
    assert candidate({'yrovnb': 'zKhe', 'd5d': None, 'l0k0j': None}) == {'yrovnb': 'zKhe'}
    assert candidate({'1nru': 'uJE', 'u1cf': None, 'nmjq': None}) == {'1nru': 'uJE'}
    assert candidate({'9bimzy': 'avS', '1np4v': None, 'mpud': None}) == {'9bimzy': 'avS'}
    assert candidate({'ig4icn': 'LzNPc', '30khs': None, 'u8amk': None}) == {'ig4icn': 'LzNPc'}
    assert candidate({'om88': 'onYtR', 'jvnidw': None, 'ao1xdy': None}) == {'om88': 'onYtR'}
    assert candidate({'p93lbe': 'CaNWCG', 'epxoh': None, 'ofbcp': None}) == {'p93lbe': 'CaNWCG'}
    assert candidate({'tvqzx': 'PMZ', 'byvjl5': None, 'x0xag': None}) == {'tvqzx': 'PMZ'}
    assert candidate({'u1k': 'ubWX', '25hoa': None, 'cjp': None}) == {'u1k': 'ubWX'}
    assert candidate({'c1f60': 'siXkmqar', 'yq2lwg': None, '73jcc': None}) == {'c1f60': 'siXkmqar'}
    assert candidate({'3bgx': 'FqzYzN', 'qb9p': None, 'zrgmn': None}) == {'3bgx': 'FqzYzN'}
    assert candidate({'kek3o': 'VYtV', 'y9yj4': None, '08lji8': None}) == {'kek3o': 'VYtV'}
    assert candidate({'8fmg': 'BPTHCATF', 'wta9': None, 'sduo': None}) == {'8fmg': 'BPTHCATF'}
    assert candidate({'sad0y': None, 'n95n1': 'vnajWWKOX', 'k5946c': None}) == {'n95n1': 'vnajWWKOX'}
    assert candidate({'gedw': None, '1req7': 'bxw', 'keyofg': None}) == {'1req7': 'bxw'}
    assert candidate({'jwy0w': None, 'gqmbc': 'WVRcgw', 'uroamn': None}) == {'gqmbc': 'WVRcgw'}
    assert candidate({'osxo': None, 'yoldus': 'MFScAGOiq', 'q4v': None}) == {'yoldus': 'MFScAGOiq'}
    assert candidate({'t6o': None, 'mj9rox': 'dui', 'qveow': None}) == {'mj9rox': 'dui'}
    assert candidate({'xy9v11': None, 'pvytm': 'tgGysF', 'dcdqj': None}) == {'pvytm': 'tgGysF'}
    assert candidate({'gyiuv': None, '1qxmu': 'FTXJtRusr', 'l2te': None}) == {'1qxmu': 'FTXJtRusr'}
    assert candidate({'2g0eb': None, '50jkr': 'JiZJ', '5qlbc': None}) == {'50jkr': 'JiZJ'}
    assert candidate({'q63t': None, 'xd6cua': 'WEVXvHPT', 'k95': None}) == {'xd6cua': 'WEVXvHPT'}
    assert candidate({'owu': None, '0qf': 'WaB', '1d531f': None}) == {'0qf': 'WaB'}
    assert candidate({'1x8qz': None, '3auq': 'QNiPzGmbq', 'z0kbh': None}) == {'3auq': 'QNiPzGmbq'}
    assert candidate({'bc5yu': None, 'q5no0': 'pxGGD', '7l088s': None}) == {'q5no0': 'pxGGD'}
    assert candidate({'h79ab': None, '45u06': 'YDHM', 'c8cc': None}) == {'45u06': 'YDHM'}
    assert candidate({'7wut': None, '7bol': 'wTKeV', '6qk': None}) == {'7bol': 'wTKeV'}
    assert candidate({'15p84': None, 'y65w': 'NRb', 'c5udt0': None}) == {'y65w': 'NRb'}
    assert candidate({'160': None, '0wmmf': 'HHoHPoLR', 'hpdb5': None}) == {'0wmmf': 'HHoHPoLR'}
    assert candidate({'iioyl6': None, 'nylj2': 'wStBGEV', 'z43gs': None}) == {'nylj2': 'wStBGEV'}
    assert candidate({'cp2j': None, '2zr0r': 'LfuNU', 'uihk8': None}) == {'2zr0r': 'LfuNU'}
    assert candidate({'2xek': None, 'n4glv': 'Gtwq', 'yl3': None}) == {'n4glv': 'Gtwq'}
    assert candidate({'61z2': None, 'yman8': 'bICs', '9twvb': None}) == {'yman8': 'bICs'}
    assert candidate({'7rv': None, 'ulz': 'ZSSV', 'm1gt': None}) == {'ulz': 'ZSSV'}
    assert candidate({'da5lm': None, 'kv3': 'EpmGcS', 'x3m9': None}) == {'kv3': 'EpmGcS'}
    assert candidate({'i3e': None, '8db': 'KPVyhNUiX', 'i6idq': None}) == {'8db': 'KPVyhNUiX'}
    assert candidate({'e4x2d': None, 'ox99xb': 'oQZfGCr', 'bxkd5': None}) == {'ox99xb': 'oQZfGCr'}
    assert candidate({'7wmm': None, 'xyyw3': 'cFcfRzUIJ', '7kfsn': None}) == {'xyyw3': 'cFcfRzUIJ'}
    assert candidate({'fgxl6m': None, 'd63': 'PAxRIEGoK', 'y99': None}) == {'d63': 'PAxRIEGoK'}
    assert candidate({'29lh2': None, 'kjqwa3': 'nLgf', 'k8d': None}) == {'kjqwa3': 'nLgf'}
    assert candidate({'iev': None, 'l5mpkv': 'TSXgO', '7kt': None}) == {'l5mpkv': 'TSXgO'}
    assert candidate({'2bq': None, '1i87': 'FzaRyoI', '9ktw': None}) == {'1i87': 'FzaRyoI'}
    assert candidate({'ycvr': None, 'por4js': 'ywIukY', '2oz8m': None}) == {'por4js': 'ywIukY'}
    assert candidate({'7zvv': None, 'bbk2b': 'nKapd', 'am3wm': None}) == {'bbk2b': 'nKapd'}
    assert candidate({'ac7f': None, 'pnswq': 'dvqtDq', 'ct6': None}) == {'pnswq': 'dvqtDq'}
    assert candidate({'qks3': None, '10kmil': 'qcJwPG', '53r1': None}) == {'10kmil': 'qcJwPG'}

if __name__ == '__main__':
    check(drop_empty)