from case_MBPP_398 import unique_sublists


def check(candidate):
    assert candidate([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
    assert candidate([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])=={('green', 'orange'): 2, ('black',): 1, ('white',): 1}
    assert candidate([[1, 2], [3, 4], [4, 5], [6, 7]])=={(1, 2): 1, (3, 4): 1, (4, 5): 1, (6, 7): 1}
    assert candidate([[3, 5], [2, 2], [4, 3], [14, 20, 21], [3, 8], [12, 13]]) == {(3, 5): 1, (2, 2): 1, (4, 3): 1, (14, 20, 21): 1, (3, 8): 1, (12, 13): 1}
    assert candidate([[2, 2], [6, 10], [6, 5], [18, 12, 22], [10, 8], [6, 12]]) == {(2, 2): 1, (6, 10): 1, (6, 5): 1, (18, 12, 22): 1, (10, 8): 1, (6, 12): 1}
    assert candidate([[1, 8], [1, 8], [3, 3], [11, 11, 21], [1, 11], [10, 13]]) == {(1, 8): 2, (3, 3): 1, (11, 11, 21): 1, (1, 11): 1, (10, 13): 1}
    assert candidate([[2, 8], [9, 2], [2, 7], [12, 10, 15], [8, 11], [7, 9]]) == {(2, 8): 1, (9, 2): 1, (2, 7): 1, (12, 10, 15): 1, (8, 11): 1, (7, 9): 1}
    assert candidate([[5, 3], [8, 7], [6, 8], [15, 19, 17], [3, 7], [4, 9]]) == {(5, 3): 1, (8, 7): 1, (6, 8): 1, (15, 19, 17): 1, (3, 7): 1, (4, 9): 1}
    assert candidate([[4, 1], [8, 11], [5, 5], [16, 10, 20], [3, 5], [4, 8]]) == {(4, 1): 1, (8, 11): 1, (5, 5): 1, (16, 10, 20): 1, (3, 5): 1, (4, 8): 1}
    assert candidate([[4, 8], [8, 6], [3, 1], [16, 20, 21], [9, 11], [12, 16]]) == {(4, 8): 1, (8, 6): 1, (3, 1): 1, (16, 20, 21): 1, (9, 11): 1, (12, 16): 1}
    assert candidate([[6, 7], [2, 3], [1, 5], [9, 20, 18], [5, 6], [8, 13]]) == {(6, 7): 1, (2, 3): 1, (1, 5): 1, (9, 20, 18): 1, (5, 6): 1, (8, 13): 1}
    assert candidate([[1, 4], [5, 2], [3, 3], [9, 19, 16], [3, 2], [13, 6]]) == {(1, 4): 1, (5, 2): 1, (3, 3): 1, (9, 19, 16): 1, (3, 2): 1, (13, 6): 1}
    assert candidate([[5, 2], [1, 2], [3, 5], [9, 20, 16], [5, 9], [6, 15]]) == {(5, 2): 1, (1, 2): 1, (3, 5): 1, (9, 20, 16): 1, (5, 9): 1, (6, 15): 1}
    assert candidate([[5, 3], [2, 8], [5, 5], [14, 16, 20], [6, 9], [7, 6]]) == {(5, 3): 1, (2, 8): 1, (5, 5): 1, (14, 16, 20): 1, (6, 9): 1, (7, 6): 1}
    assert candidate([[3, 3], [2, 12], [4, 7], [18, 19, 18], [4, 12], [13, 14]]) == {(3, 3): 1, (2, 12): 1, (4, 7): 1, (18, 19, 18): 1, (4, 12): 1, (13, 14): 1}
    assert candidate([[4, 1], [4, 6], [5, 2], [17, 20, 17], [8, 12], [5, 6]]) == {(4, 1): 1, (4, 6): 1, (5, 2): 1, (17, 20, 17): 1, (8, 12): 1, (5, 6): 1}
    assert candidate([[2, 4], [7, 7], [4, 8], [14, 14, 14], [2, 2], [4, 15]]) == {(2, 4): 1, (7, 7): 1, (4, 8): 1, (14, 14, 14): 1, (2, 2): 1, (4, 15): 1}
    assert candidate([[2, 7], [9, 7], [1, 7], [14, 12, 19], [9, 9], [9, 12]]) == {(2, 7): 1, (9, 7): 1, (1, 7): 1, (14, 12, 19): 1, (9, 9): 1, (9, 12): 1}
    assert candidate([[2, 4], [5, 12], [4, 6], [16, 20, 19], [9, 8], [11, 15]]) == {(2, 4): 1, (5, 12): 1, (4, 6): 1, (16, 20, 19): 1, (9, 8): 1, (11, 15): 1}
    assert candidate([[6, 5], [5, 7], [2, 4], [18, 14, 16], [2, 7], [12, 10]]) == {(6, 5): 1, (5, 7): 1, (2, 4): 1, (18, 14, 16): 1, (2, 7): 1, (12, 10): 1}
    assert candidate([[6, 5], [1, 6], [3, 5], [14, 12, 16], [10, 11], [6, 6]]) == {(6, 5): 1, (1, 6): 1, (3, 5): 1, (14, 12, 16): 1, (10, 11): 1, (6, 6): 1}
    assert candidate([[3, 1], [9, 9], [1, 6], [8, 10, 17], [6, 2], [14, 11]]) == {(3, 1): 1, (9, 9): 1, (1, 6): 1, (8, 10, 17): 1, (6, 2): 1, (14, 11): 1}
    assert candidate([[2, 2], [7, 6], [2, 5], [10, 14, 22], [5, 10], [14, 12]]) == {(2, 2): 1, (7, 6): 1, (2, 5): 1, (10, 14, 22): 1, (5, 10): 1, (14, 12): 1}
    assert candidate([[3, 4], [10, 6], [5, 2], [12, 19, 22], [6, 7], [6, 8]]) == {(3, 4): 1, (10, 6): 1, (5, 2): 1, (12, 19, 22): 1, (6, 7): 1, (6, 8): 1}
    assert candidate([[5, 8], [8, 4], [3, 4], [13, 17, 21], [5, 10], [8, 6]]) == {(5, 8): 1, (8, 4): 1, (3, 4): 1, (13, 17, 21): 1, (5, 10): 1, (8, 6): 1}
    assert candidate([[5, 8], [9, 12], [2, 7], [17, 16, 14], [3, 7], [4, 7]]) == {(5, 8): 1, (9, 12): 1, (2, 7): 1, (17, 16, 14): 1, (3, 7): 1, (4, 7): 1}
    assert candidate([[3, 1], [1, 8], [6, 8], [12, 16, 20], [1, 12], [8, 9]]) == {(3, 1): 1, (1, 8): 1, (6, 8): 1, (12, 16, 20): 1, (1, 12): 1, (8, 9): 1}
    assert candidate([[5, 2], [1, 6], [5, 3], [18, 19, 21], [7, 4], [12, 8]]) == {(5, 2): 1, (1, 6): 1, (5, 3): 1, (18, 19, 21): 1, (7, 4): 1, (12, 8): 1}
    assert candidate([[2, 8], [6, 2], [4, 4], [14, 17, 17], [6, 7], [5, 14]]) == {(2, 8): 1, (6, 2): 1, (4, 4): 1, (14, 17, 17): 1, (6, 7): 1, (5, 14): 1}
    assert candidate([[3, 8], [2, 7], [4, 4], [10, 15, 12], [8, 7], [8, 13]]) == {(3, 8): 1, (2, 7): 1, (4, 4): 1, (10, 15, 12): 1, (8, 7): 1, (8, 13): 1}
    assert candidate([[5, 7], [6, 7], [1, 4], [15, 16, 22], [10, 11], [4, 12]]) == {(5, 7): 1, (6, 7): 1, (1, 4): 1, (15, 16, 22): 1, (10, 11): 1, (4, 12): 1}
    assert candidate([[6, 8], [4, 6], [1, 2], [18, 13, 20], [6, 4], [6, 15]]) == {(6, 8): 1, (4, 6): 1, (1, 2): 1, (18, 13, 20): 1, (6, 4): 1, (6, 15): 1}
    assert candidate([[3, 1], [6, 11], [5, 5], [10, 11, 19], [6, 2], [14, 13]]) == {(3, 1): 1, (6, 11): 1, (5, 5): 1, (10, 11, 19): 1, (6, 2): 1, (14, 13): 1}
    assert candidate([[3, 4], [1, 11], [4, 1], [15, 13, 19], [3, 3], [6, 9]]) == {(3, 4): 1, (1, 11): 1, (4, 1): 1, (15, 13, 19): 1, (3, 3): 1, (6, 9): 1}
    assert candidate([[1, 4], [3, 12], [1, 6], [11, 15, 12], [8, 7], [9, 6]]) == {(1, 4): 1, (3, 12): 1, (1, 6): 1, (11, 15, 12): 1, (8, 7): 1, (9, 6): 1}
    assert candidate([[6, 2], [4, 12], [6, 8], [10, 10, 15], [6, 2], [10, 14]]) == {(6, 2): 2, (4, 12): 1, (6, 8): 1, (10, 10, 15): 1, (10, 14): 1}
    assert candidate([['whkqetdu', 'lmqlnaxvefj'], ['lyid'], ['uyvdx', 'bzgmgoxz'], ['tugj']]) == {('whkqetdu', 'lmqlnaxvefj'): 1, ('lyid',): 1, ('uyvdx', 'bzgmgoxz'): 1, ('tugj',): 1}
    assert candidate([['yvqf', 'avcduc'], ['vuxu'], ['fism', 'umfjlkg'], ['zvfyq']]) == {('yvqf', 'avcduc'): 1, ('vuxu',): 1, ('fism', 'umfjlkg'): 1, ('zvfyq',): 1}
    assert candidate([['lixrcqawo', 'qtgpmhnsnytb'], ['wmzztqn'], ['qxmbs', 'ijiuynujn'], ['jevd']]) == {('lixrcqawo', 'qtgpmhnsnytb'): 1, ('wmzztqn',): 1, ('qxmbs', 'ijiuynujn'): 1, ('jevd',): 1}
    assert candidate([['pla', 'wzgkdiz'], ['iwhtwkpfa'], ['xop', 'nlvttyn'], ['knfxsbish']]) == {('pla', 'wzgkdiz'): 1, ('iwhtwkpfa',): 1, ('xop', 'nlvttyn'): 1, ('knfxsbish',): 1}
    assert candidate([['nrcixtzkm', 'jzvbcr'], ['stxxk'], ['ijo', 'vnxdexuespy'], ['wybwq']]) == {('nrcixtzkm', 'jzvbcr'): 1, ('stxxk',): 1, ('ijo', 'vnxdexuespy'): 1, ('wybwq',): 1}
    assert candidate([['klg', 'wixnpu'], ['lpm'], ['ebhcqlrde', 'nhjo'], ['npmyi']]) == {('klg', 'wixnpu'): 1, ('lpm',): 1, ('ebhcqlrde', 'nhjo'): 1, ('npmyi',): 1}
    assert candidate([['jbf', 'psemfbv'], ['ppzxh'], ['gimnnuyov', 'rmyijyvmnidb'], ['borlmpwbv']]) == {('jbf', 'psemfbv'): 1, ('ppzxh',): 1, ('gimnnuyov', 'rmyijyvmnidb'): 1, ('borlmpwbv',): 1}
    assert candidate([['hkwp', 'fonatzvdhepa'], ['aewv'], ['csmyghws', 'xvqoenivi'], ['vyoioej']]) == {('hkwp', 'fonatzvdhepa'): 1, ('aewv',): 1, ('csmyghws', 'xvqoenivi'): 1, ('vyoioej',): 1}
    assert candidate([['nic', 'flu'], ['sgm'], ['jjnxkwpe', 'csuqn'], ['nakkrdoo']]) == {('nic', 'flu'): 1, ('sgm',): 1, ('jjnxkwpe', 'csuqn'): 1, ('nakkrdoo',): 1}
    assert candidate([['eve', 'sdbv'], ['jjkz'], ['hby', 'gwhloxgls'], ['eovp']]) == {('eve', 'sdbv'): 1, ('jjkz',): 1, ('hby', 'gwhloxgls'): 1, ('eovp',): 1}
    assert candidate([['phnnzvgbw', 'xix'], ['axqqpd'], ['boix', 'jfpo'], ['dilm']]) == {('phnnzvgbw', 'xix'): 1, ('axqqpd',): 1, ('boix', 'jfpo'): 1, ('dilm',): 1}
    assert candidate([['afbt', 'ciaqijtxinnv'], ['ozwdake'], ['wuctv', 'wfzlvc'], ['wkiqssgk']]) == {('afbt', 'ciaqijtxinnv'): 1, ('ozwdake',): 1, ('wuctv', 'wfzlvc'): 1, ('wkiqssgk',): 1}
    assert candidate([['fvgfnfqm', 'xunpvficzzc'], ['ghhr'], ['yuk', 'ruydpovwjxce'], ['kcyu']]) == {('fvgfnfqm', 'xunpvficzzc'): 1, ('ghhr',): 1, ('yuk', 'ruydpovwjxce'): 1, ('kcyu',): 1}
    assert candidate([['mlujyy', 'bbxhnzodcu'], ['zhhzxezbx'], ['soh', 'swadtocbq'], ['qlf']]) == {('mlujyy', 'bbxhnzodcu'): 1, ('zhhzxezbx',): 1, ('soh', 'swadtocbq'): 1, ('qlf',): 1}
    assert candidate([['chyrmxd', 'qstmd'], ['detm'], ['fgfg', 'pteduzagqj'], ['xnlmtyts']]) == {('chyrmxd', 'qstmd'): 1, ('detm',): 1, ('fgfg', 'pteduzagqj'): 1, ('xnlmtyts',): 1}
    assert candidate([['qcfnaykhq', 'ifumq'], ['trp'], ['iwo', 'moylylks'], ['amlxkbl']]) == {('qcfnaykhq', 'ifumq'): 1, ('trp',): 1, ('iwo', 'moylylks'): 1, ('amlxkbl',): 1}
    assert candidate([['zkahjws', 'iaimoelvw'], ['qkqtkb'], ['vmrpexoxw', 'rnyh'], ['mjgfq']]) == {('zkahjws', 'iaimoelvw'): 1, ('qkqtkb',): 1, ('vmrpexoxw', 'rnyh'): 1, ('mjgfq',): 1}
    assert candidate([['jetzk', 'ykpfpgv'], ['yxqouoavn'], ['jtdm', 'ysqmumacdycn'], ['wzp']]) == {('jetzk', 'ykpfpgv'): 1, ('yxqouoavn',): 1, ('jtdm', 'ysqmumacdycn'): 1, ('wzp',): 1}
    assert candidate([['wdgenplks', 'lqdn'], ['tsmlrfelx'], ['nvsp', 'qkpuueoen'], ['vhslmdqv']]) == {('wdgenplks', 'lqdn'): 1, ('tsmlrfelx',): 1, ('nvsp', 'qkpuueoen'): 1, ('vhslmdqv',): 1}
    assert candidate([['najytso', 'siwtuoglb'], ['lhvpapcpv'], ['xpnuqbso', 'mlgzdci'], ['ufik']]) == {('najytso', 'siwtuoglb'): 1, ('lhvpapcpv',): 1, ('xpnuqbso', 'mlgzdci'): 1, ('ufik',): 1}
    assert candidate([['gwreye', 'amifhlyszwez'], ['cyoqp'], ['rmrljg', 'ilihr'], ['wwfxtuzq']]) == {('gwreye', 'amifhlyszwez'): 1, ('cyoqp',): 1, ('rmrljg', 'ilihr'): 1, ('wwfxtuzq',): 1}
    assert candidate([['scyklu', 'cbishqzxh'], ['wmszg'], ['qnlfgie', 'hjcisf'], ['nikyz']]) == {('scyklu', 'cbishqzxh'): 1, ('wmszg',): 1, ('qnlfgie', 'hjcisf'): 1, ('nikyz',): 1}
    assert candidate([['ryxbjl', 'nduwwedor'], ['jqc'], ['dsozewns', 'vcip'], ['hpckjb']]) == {('ryxbjl', 'nduwwedor'): 1, ('jqc',): 1, ('dsozewns', 'vcip'): 1, ('hpckjb',): 1}
    assert candidate([['uvcl', 'msvjz'], ['vlevihg'], ['zgzkvtl', 'qmi'], ['mix']]) == {('uvcl', 'msvjz'): 1, ('vlevihg',): 1, ('zgzkvtl', 'qmi'): 1, ('mix',): 1}
    assert candidate([['pqetunau', 'vkmfevcaaie'], ['mnqopqbn'], ['oprvjh', 'lkiwrni'], ['zsyad']]) == {('pqetunau', 'vkmfevcaaie'): 1, ('mnqopqbn',): 1, ('oprvjh', 'lkiwrni'): 1, ('zsyad',): 1}
    assert candidate([['khlwvu', 'iwkyz'], ['fhsejcjgt'], ['uzsystip', 'ozgn'], ['zjnhhyn']]) == {('khlwvu', 'iwkyz'): 1, ('fhsejcjgt',): 1, ('uzsystip', 'ozgn'): 1, ('zjnhhyn',): 1}
    assert candidate([['rbeiumbv', 'wzuehkttjg'], ['hhhjvac'], ['xyy', 'hnrramgt'], ['wljwvjkc']]) == {('rbeiumbv', 'wzuehkttjg'): 1, ('hhhjvac',): 1, ('xyy', 'hnrramgt'): 1, ('wljwvjkc',): 1}
    assert candidate([['ibaascy', 'slsplgipehic'], ['ubfuvrcp'], ['lltvvhns', 'iaojo'], ['sfr']]) == {('ibaascy', 'slsplgipehic'): 1, ('ubfuvrcp',): 1, ('lltvvhns', 'iaojo'): 1, ('sfr',): 1}
    assert candidate([['vciagot', 'yileycb'], ['npsouv'], ['cash', 'kwitbhgitknm'], ['ohcd']]) == {('vciagot', 'yileycb'): 1, ('npsouv',): 1, ('cash', 'kwitbhgitknm'): 1, ('ohcd',): 1}
    assert candidate([['aaevqctls', 'rxrnfbiyvob'], ['zqxpj'], ['idvenw', 'vxkyyxuurbr'], ['jcubc']]) == {('aaevqctls', 'rxrnfbiyvob'): 1, ('zqxpj',): 1, ('idvenw', 'vxkyyxuurbr'): 1, ('jcubc',): 1}
    assert candidate([['mcvbzd', 'cfrouazdrg'], ['pblaxnwlw'], ['hqvmp', 'gbxolpgmatg'], ['rwtuns']]) == {('mcvbzd', 'cfrouazdrg'): 1, ('pblaxnwlw',): 1, ('hqvmp', 'gbxolpgmatg'): 1, ('rwtuns',): 1}
    assert candidate([['lzujhyjl', 'mgglqw'], ['yplnzky'], ['cftqdm', 'ttrjjoxglhh'], ['fhyg']]) == {('lzujhyjl', 'mgglqw'): 1, ('yplnzky',): 1, ('cftqdm', 'ttrjjoxglhh'): 1, ('fhyg',): 1}
    assert candidate([['hymbqwozb', 'oimn'], ['xjtwml'], ['qqmrnujhc', 'oizcztnhpgzt'], ['smzlzrwp']]) == {('hymbqwozb', 'oimn'): 1, ('xjtwml',): 1, ('qqmrnujhc', 'oizcztnhpgzt'): 1, ('smzlzrwp',): 1}
    assert candidate([[4, 7], [8, 2], [3, 9], [5, 2]]) == {(4, 7): 1, (8, 2): 1, (3, 9): 1, (5, 2): 1}
    assert candidate([[6, 7], [6, 3], [2, 5], [10, 10]]) == {(6, 7): 1, (6, 3): 1, (2, 5): 1, (10, 10): 1}
    assert candidate([[1, 5], [7, 7], [7, 9], [10, 12]]) == {(1, 5): 1, (7, 7): 1, (7, 9): 1, (10, 12): 1}
    assert candidate([[6, 4], [2, 1], [4, 9], [1, 7]]) == {(6, 4): 1, (2, 1): 1, (4, 9): 1, (1, 7): 1}
    assert candidate([[3, 3], [6, 1], [1, 4], [7, 10]]) == {(3, 3): 1, (6, 1): 1, (1, 4): 1, (7, 10): 1}
    assert candidate([[6, 7], [5, 6], [6, 9], [1, 10]]) == {(6, 7): 1, (5, 6): 1, (6, 9): 1, (1, 10): 1}
    assert candidate([[4, 2], [7, 5], [6, 2], [10, 9]]) == {(4, 2): 1, (7, 5): 1, (6, 2): 1, (10, 9): 1}
    assert candidate([[1, 5], [4, 1], [3, 4], [7, 4]]) == {(1, 5): 1, (4, 1): 1, (3, 4): 1, (7, 4): 1}
    assert candidate([[4, 5], [6, 7], [4, 10], [10, 8]]) == {(4, 5): 1, (6, 7): 1, (4, 10): 1, (10, 8): 1}
    assert candidate([[3, 1], [7, 4], [9, 1], [9, 12]]) == {(3, 1): 1, (7, 4): 1, (9, 1): 1, (9, 12): 1}
    assert candidate([[6, 1], [2, 1], [1, 8], [11, 3]]) == {(6, 1): 1, (2, 1): 1, (1, 8): 1, (11, 3): 1}
    assert candidate([[6, 5], [3, 9], [7, 6], [5, 9]]) == {(6, 5): 1, (3, 9): 1, (7, 6): 1, (5, 9): 1}
    assert candidate([[1, 3], [2, 3], [8, 4], [1, 9]]) == {(1, 3): 1, (2, 3): 1, (8, 4): 1, (1, 9): 1}
    assert candidate([[4, 4], [3, 4], [8, 1], [7, 12]]) == {(4, 4): 1, (3, 4): 1, (8, 1): 1, (7, 12): 1}
    assert candidate([[2, 2], [7, 3], [9, 8], [1, 2]]) == {(2, 2): 1, (7, 3): 1, (9, 8): 1, (1, 2): 1}
    assert candidate([[6, 3], [7, 3], [3, 9], [7, 6]]) == {(6, 3): 1, (7, 3): 1, (3, 9): 1, (7, 6): 1}
    assert candidate([[1, 2], [4, 8], [5, 4], [2, 8]]) == {(1, 2): 1, (4, 8): 1, (5, 4): 1, (2, 8): 1}
    assert candidate([[5, 7], [6, 9], [4, 1], [10, 7]]) == {(5, 7): 1, (6, 9): 1, (4, 1): 1, (10, 7): 1}
    assert candidate([[6, 1], [1, 5], [8, 5], [4, 7]]) == {(6, 1): 1, (1, 5): 1, (8, 5): 1, (4, 7): 1}
    assert candidate([[5, 1], [3, 8], [9, 8], [2, 12]]) == {(5, 1): 1, (3, 8): 1, (9, 8): 1, (2, 12): 1}
    assert candidate([[4, 1], [2, 5], [3, 6], [3, 9]]) == {(4, 1): 1, (2, 5): 1, (3, 6): 1, (3, 9): 1}
    assert candidate([[1, 2], [3, 5], [7, 6], [8, 8]]) == {(1, 2): 1, (3, 5): 1, (7, 6): 1, (8, 8): 1}
    assert candidate([[2, 4], [4, 9], [1, 8], [1, 10]]) == {(2, 4): 1, (4, 9): 1, (1, 8): 1, (1, 10): 1}
    assert candidate([[6, 7], [8, 5], [3, 2], [9, 5]]) == {(6, 7): 1, (8, 5): 1, (3, 2): 1, (9, 5): 1}
    assert candidate([[2, 3], [4, 8], [1, 9], [1, 4]]) == {(2, 3): 1, (4, 8): 1, (1, 9): 1, (1, 4): 1}
    assert candidate([[4, 6], [5, 1], [1, 1], [2, 9]]) == {(4, 6): 1, (5, 1): 1, (1, 1): 1, (2, 9): 1}
    assert candidate([[5, 1], [6, 2], [7, 8], [9, 10]]) == {(5, 1): 1, (6, 2): 1, (7, 8): 1, (9, 10): 1}
    assert candidate([[2, 4], [1, 2], [3, 1], [3, 3]]) == {(2, 4): 1, (1, 2): 1, (3, 1): 1, (3, 3): 1}
    assert candidate([[1, 6], [8, 8], [7, 10], [7, 2]]) == {(1, 6): 1, (8, 8): 1, (7, 10): 1, (7, 2): 1}
    assert candidate([[4, 2], [2, 7], [8, 4], [11, 4]]) == {(4, 2): 1, (2, 7): 1, (8, 4): 1, (11, 4): 1}
    assert candidate([[3, 2], [8, 4], [3, 7], [3, 2]]) == {(3, 2): 2, (8, 4): 1, (3, 7): 1}
    assert candidate([[6, 7], [3, 6], [6, 4], [9, 2]]) == {(6, 7): 1, (3, 6): 1, (6, 4): 1, (9, 2): 1}
    assert candidate([[5, 7], [7, 1], [7, 10], [8, 11]]) == {(5, 7): 1, (7, 1): 1, (7, 10): 1, (8, 11): 1}

if __name__ == '__main__':
    check(unique_sublists)