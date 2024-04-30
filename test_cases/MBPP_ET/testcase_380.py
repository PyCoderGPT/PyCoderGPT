from case_MBPP_380 import unique_sublists


def check(candidate):
    assert candidate([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
    assert candidate([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])=={('green', 'orange'): 2, ('black',): 1, ('white',): 1}
    assert candidate([[10, 20, 30, 40], [60, 70, 50, 50], [90, 100, 200]])=={(10, 20, 30, 40): 1, (60, 70, 50, 50): 1, (90, 100, 200): 1}
    assert candidate([[6, 4], [2, 11], [4, 5], [15, 12, 17], [10, 12], [5, 11]]) == {(6, 4): 1, (2, 11): 1, (4, 5): 1, (15, 12, 17): 1, (10, 12): 1, (5, 11): 1}
    assert candidate([[2, 8], [2, 2], [3, 1], [15, 19, 13], [5, 2], [14, 15]]) == {(2, 8): 1, (2, 2): 1, (3, 1): 1, (15, 19, 13): 1, (5, 2): 1, (14, 15): 1}
    assert candidate([[4, 2], [2, 6], [5, 8], [18, 18, 12], [1, 12], [5, 9]]) == {(4, 2): 1, (2, 6): 1, (5, 8): 1, (18, 18, 12): 1, (1, 12): 1, (5, 9): 1}
    assert candidate([[5, 4], [5, 4], [5, 4], [10, 11, 13], [1, 6], [9, 10]]) == {(5, 4): 3, (10, 11, 13): 1, (1, 6): 1, (9, 10): 1}
    assert candidate([[3, 1], [5, 7], [6, 4], [15, 17, 21], [4, 4], [10, 15]]) == {(3, 1): 1, (5, 7): 1, (6, 4): 1, (15, 17, 21): 1, (4, 4): 1, (10, 15): 1}
    assert candidate([[6, 4], [5, 4], [4, 5], [11, 14, 19], [4, 12], [5, 10]]) == {(6, 4): 1, (5, 4): 1, (4, 5): 1, (11, 14, 19): 1, (4, 12): 1, (5, 10): 1}
    assert candidate([[6, 6], [2, 11], [2, 7], [18, 15, 12], [8, 5], [9, 6]]) == {(6, 6): 1, (2, 11): 1, (2, 7): 1, (18, 15, 12): 1, (8, 5): 1, (9, 6): 1}
    assert candidate([[6, 5], [5, 12], [3, 3], [9, 12, 17], [8, 4], [7, 14]]) == {(6, 5): 1, (5, 12): 1, (3, 3): 1, (9, 12, 17): 1, (8, 4): 1, (7, 14): 1}
    assert candidate([[3, 2], [2, 3], [2, 3], [14, 17, 17], [9, 4], [9, 16]]) == {(3, 2): 1, (2, 3): 2, (14, 17, 17): 1, (9, 4): 1, (9, 16): 1}
    assert candidate([[5, 3], [7, 2], [5, 5], [17, 11, 18], [7, 2], [4, 8]]) == {(5, 3): 1, (7, 2): 2, (5, 5): 1, (17, 11, 18): 1, (4, 8): 1}
    assert candidate([[3, 3], [10, 8], [3, 8], [13, 18, 14], [2, 2], [9, 8]]) == {(3, 3): 1, (10, 8): 1, (3, 8): 1, (13, 18, 14): 1, (2, 2): 1, (9, 8): 1}
    assert candidate([[4, 5], [4, 12], [1, 1], [8, 10, 13], [5, 9], [13, 14]]) == {(4, 5): 1, (4, 12): 1, (1, 1): 1, (8, 10, 13): 1, (5, 9): 1, (13, 14): 1}
    assert candidate([[4, 7], [1, 10], [2, 1], [16, 12, 14], [8, 9], [12, 8]]) == {(4, 7): 1, (1, 10): 1, (2, 1): 1, (16, 12, 14): 1, (8, 9): 1, (12, 8): 1}
    assert candidate([[6, 4], [1, 4], [6, 7], [11, 14, 21], [6, 8], [7, 13]]) == {(6, 4): 1, (1, 4): 1, (6, 7): 1, (11, 14, 21): 1, (6, 8): 1, (7, 13): 1}
    assert candidate([[4, 3], [8, 12], [4, 7], [18, 11, 17], [1, 7], [13, 6]]) == {(4, 3): 1, (8, 12): 1, (4, 7): 1, (18, 11, 17): 1, (1, 7): 1, (13, 6): 1}
    assert candidate([[4, 4], [7, 9], [2, 2], [18, 18, 14], [2, 10], [10, 9]]) == {(4, 4): 1, (7, 9): 1, (2, 2): 1, (18, 18, 14): 1, (2, 10): 1, (10, 9): 1}
    assert candidate([[2, 3], [9, 5], [6, 1], [15, 13, 14], [5, 3], [8, 11]]) == {(2, 3): 1, (9, 5): 1, (6, 1): 1, (15, 13, 14): 1, (5, 3): 1, (8, 11): 1}
    assert candidate([[2, 8], [1, 7], [5, 4], [18, 15, 12], [6, 12], [11, 13]]) == {(2, 8): 1, (1, 7): 1, (5, 4): 1, (18, 15, 12): 1, (6, 12): 1, (11, 13): 1}
    assert candidate([[1, 6], [7, 8], [4, 5], [9, 11, 14], [10, 12], [7, 14]]) == {(1, 6): 1, (7, 8): 1, (4, 5): 1, (9, 11, 14): 1, (10, 12): 1, (7, 14): 1}
    assert candidate([[5, 4], [8, 2], [3, 1], [8, 11, 15], [1, 11], [9, 12]]) == {(5, 4): 1, (8, 2): 1, (3, 1): 1, (8, 11, 15): 1, (1, 11): 1, (9, 12): 1}
    assert candidate([[4, 1], [2, 11], [6, 3], [17, 10, 16], [4, 3], [7, 14]]) == {(4, 1): 1, (2, 11): 1, (6, 3): 1, (17, 10, 16): 1, (4, 3): 1, (7, 14): 1}
    assert candidate([[3, 3], [3, 2], [1, 4], [18, 19, 18], [2, 8], [10, 8]]) == {(3, 3): 1, (3, 2): 1, (1, 4): 1, (18, 19, 18): 1, (2, 8): 1, (10, 8): 1}
    assert candidate([[6, 2], [5, 4], [6, 1], [14, 13, 20], [8, 5], [11, 15]]) == {(6, 2): 1, (5, 4): 1, (6, 1): 1, (14, 13, 20): 1, (8, 5): 1, (11, 15): 1}
    assert candidate([[6, 2], [1, 9], [3, 5], [17, 18, 21], [9, 10], [10, 11]]) == {(6, 2): 1, (1, 9): 1, (3, 5): 1, (17, 18, 21): 1, (9, 10): 1, (10, 11): 1}
    assert candidate([[4, 5], [3, 5], [2, 1], [15, 16, 14], [10, 3], [12, 9]]) == {(4, 5): 1, (3, 5): 1, (2, 1): 1, (15, 16, 14): 1, (10, 3): 1, (12, 9): 1}
    assert candidate([[3, 3], [10, 9], [3, 4], [17, 15, 17], [10, 9], [11, 13]]) == {(3, 3): 1, (10, 9): 2, (3, 4): 1, (17, 15, 17): 1, (11, 13): 1}
    assert candidate([[4, 5], [3, 11], [1, 8], [16, 14, 21], [2, 4], [13, 15]]) == {(4, 5): 1, (3, 11): 1, (1, 8): 1, (16, 14, 21): 1, (2, 4): 1, (13, 15): 1}
    assert candidate([[3, 5], [10, 3], [1, 2], [14, 11, 12], [2, 6], [9, 14]]) == {(3, 5): 1, (10, 3): 1, (1, 2): 1, (14, 11, 12): 1, (2, 6): 1, (9, 14): 1}
    assert candidate([[4, 8], [2, 6], [1, 5], [18, 10, 16], [3, 6], [14, 13]]) == {(4, 8): 1, (2, 6): 1, (1, 5): 1, (18, 10, 16): 1, (3, 6): 1, (14, 13): 1}
    assert candidate([[6, 7], [8, 5], [3, 6], [13, 14, 20], [8, 10], [9, 6]]) == {(6, 7): 1, (8, 5): 1, (3, 6): 1, (13, 14, 20): 1, (8, 10): 1, (9, 6): 1}
    assert candidate([[5, 2], [3, 9], [4, 5], [10, 15, 19], [3, 10], [8, 10]]) == {(5, 2): 1, (3, 9): 1, (4, 5): 1, (10, 15, 19): 1, (3, 10): 1, (8, 10): 1}
    assert candidate([[5, 5], [2, 5], [5, 6], [13, 12, 19], [6, 10], [7, 7]]) == {(5, 5): 1, (2, 5): 1, (5, 6): 1, (13, 12, 19): 1, (6, 10): 1, (7, 7): 1}
    assert candidate([[3, 7], [7, 5], [3, 5], [13, 14, 17], [3, 9], [9, 14]]) == {(3, 7): 1, (7, 5): 1, (3, 5): 1, (13, 14, 17): 1, (3, 9): 1, (9, 14): 1}
    assert candidate([['qos', 'weglgp'], ['anzkfj'], ['fulnpx', 'pjsclykwrv'], ['qacpnttd']]) == {('qos', 'weglgp'): 1, ('anzkfj',): 1, ('fulnpx', 'pjsclykwrv'): 1, ('qacpnttd',): 1}
    assert candidate([['pkpupog', 'woch'], ['vzwih'], ['xcjxdh', 'hastmm'], ['gdo']]) == {('pkpupog', 'woch'): 1, ('vzwih',): 1, ('xcjxdh', 'hastmm'): 1, ('gdo',): 1}
    assert candidate([['waokcpxt', 'woahl'], ['qknjqpkdj'], ['zjx', 'phayebml'], ['ocbho']]) == {('waokcpxt', 'woahl'): 1, ('qknjqpkdj',): 1, ('zjx', 'phayebml'): 1, ('ocbho',): 1}
    assert candidate([['imcwn', 'qtltmeljtx'], ['nlrt'], ['ircxx', 'uuajrjjee'], ['xyonisdxy']]) == {('imcwn', 'qtltmeljtx'): 1, ('nlrt',): 1, ('ircxx', 'uuajrjjee'): 1, ('xyonisdxy',): 1}
    assert candidate([['iqcmyuset', 'boprecghg'], ['mmpseo'], ['demyyvik', 'iqxcmuxyp'], ['kopkhn']]) == {('iqcmyuset', 'boprecghg'): 1, ('mmpseo',): 1, ('demyyvik', 'iqxcmuxyp'): 1, ('kopkhn',): 1}
    assert candidate([['bfxio', 'uioqtpwzb'], ['lisksol'], ['tgeuduefr', 'dvqvucu'], ['phbe']]) == {('bfxio', 'uioqtpwzb'): 1, ('lisksol',): 1, ('tgeuduefr', 'dvqvucu'): 1, ('phbe',): 1}
    assert candidate([['hxjb', 'grffeehdhqzt'], ['eysidm'], ['liukvjaym', 'lkuliy'], ['oqe']]) == {('hxjb', 'grffeehdhqzt'): 1, ('eysidm',): 1, ('liukvjaym', 'lkuliy'): 1, ('oqe',): 1}
    assert candidate([['bwdfrcqg', 'wcfnciqgg'], ['gzase'], ['oqztzlcz', 'kggxtafdkn'], ['tqeloc']]) == {('bwdfrcqg', 'wcfnciqgg'): 1, ('gzase',): 1, ('oqztzlcz', 'kggxtafdkn'): 1, ('tqeloc',): 1}
    assert candidate([['imdytnu', 'hnofkwvyjw'], ['jec'], ['uzabvyuf', 'fcfdhqoeunbm'], ['lwv']]) == {('imdytnu', 'hnofkwvyjw'): 1, ('jec',): 1, ('uzabvyuf', 'fcfdhqoeunbm'): 1, ('lwv',): 1}
    assert candidate([['huz', 'lioufv'], ['gmyrrre'], ['qkmjtn', 'qascffkovcu'], ['xewzuuho']]) == {('huz', 'lioufv'): 1, ('gmyrrre',): 1, ('qkmjtn', 'qascffkovcu'): 1, ('xewzuuho',): 1}
    assert candidate([['yctpj', 'ded'], ['pkpe'], ['tja', 'gjut'], ['xte']]) == {('yctpj', 'ded'): 1, ('pkpe',): 1, ('tja', 'gjut'): 1, ('xte',): 1}
    assert candidate([['qsffleoma', 'lwb'], ['beeiueui'], ['snh', 'abavkz'], ['jvfkr']]) == {('qsffleoma', 'lwb'): 1, ('beeiueui',): 1, ('snh', 'abavkz'): 1, ('jvfkr',): 1}
    assert candidate([['jui', 'tea'], ['ejtgop'], ['vosjqtg', 'oytvh'], ['xxn']]) == {('jui', 'tea'): 1, ('ejtgop',): 1, ('vosjqtg', 'oytvh'): 1, ('xxn',): 1}
    assert candidate([['rvbf', 'rlbemmegrlc'], ['krrhfwmip'], ['ajpqspsyr', 'esymz'], ['iglofkan']]) == {('rvbf', 'rlbemmegrlc'): 1, ('krrhfwmip',): 1, ('ajpqspsyr', 'esymz'): 1, ('iglofkan',): 1}
    assert candidate([['iqrfvwraq', 'gsocfqqwgab'], ['ijtei'], ['nxcyfzyu', 'qkieacqwiu'], ['casqfrjxp']]) == {('iqrfvwraq', 'gsocfqqwgab'): 1, ('ijtei',): 1, ('nxcyfzyu', 'qkieacqwiu'): 1, ('casqfrjxp',): 1}
    assert candidate([['lkivlpwmd', 'koxefke'], ['zbd'], ['dshqkw', 'gbujxt'], ['ytw']]) == {('lkivlpwmd', 'koxefke'): 1, ('zbd',): 1, ('dshqkw', 'gbujxt'): 1, ('ytw',): 1}
    assert candidate([['vdt', 'jbgna'], ['llmzpaa'], ['luscpgu', 'ycvxmegrfy'], ['cgkqk']]) == {('vdt', 'jbgna'): 1, ('llmzpaa',): 1, ('luscpgu', 'ycvxmegrfy'): 1, ('cgkqk',): 1}
    assert candidate([['pas', 'xixcqulsudm'], ['rsqly'], ['xeg', 'sezvfnhtinq'], ['ubdrplq']]) == {('pas', 'xixcqulsudm'): 1, ('rsqly',): 1, ('xeg', 'sezvfnhtinq'): 1, ('ubdrplq',): 1}
    assert candidate([['qxtnrft', 'jczmixyjmhm'], ['dgs'], ['ladgw', 'xvbprjs'], ['vnpxuhm']]) == {('qxtnrft', 'jczmixyjmhm'): 1, ('dgs',): 1, ('ladgw', 'xvbprjs'): 1, ('vnpxuhm',): 1}
    assert candidate([['stgpbaxv', 'ctaem'], ['doowiwqf'], ['lzqgke', 'difrkvle'], ['gcvdj']]) == {('stgpbaxv', 'ctaem'): 1, ('doowiwqf',): 1, ('lzqgke', 'difrkvle'): 1, ('gcvdj',): 1}
    assert candidate([['tajdxzl', 'pyvhqnjcltoh'], ['rmnxvo'], ['rnibrtx', 'wuideq'], ['krloeram']]) == {('tajdxzl', 'pyvhqnjcltoh'): 1, ('rmnxvo',): 1, ('rnibrtx', 'wuideq'): 1, ('krloeram',): 1}
    assert candidate([['ladkwjel', 'kceiuvvg'], ['lqegw'], ['flbpfad', 'myeir'], ['vjvye']]) == {('ladkwjel', 'kceiuvvg'): 1, ('lqegw',): 1, ('flbpfad', 'myeir'): 1, ('vjvye',): 1}
    assert candidate([['rqszbakp', 'jryvuafhl'], ['ilmprw'], ['hdiiq', 'lsrckp'], ['bqwc']]) == {('rqszbakp', 'jryvuafhl'): 1, ('ilmprw',): 1, ('hdiiq', 'lsrckp'): 1, ('bqwc',): 1}
    assert candidate([['jcbjkm', 'fvtdxv'], ['pfyisbcua'], ['upqgahe', 'obnxraatrqob'], ['suofll']]) == {('jcbjkm', 'fvtdxv'): 1, ('pfyisbcua',): 1, ('upqgahe', 'obnxraatrqob'): 1, ('suofll',): 1}
    assert candidate([['akghbntii', 'uyxt'], ['pehykqo'], ['pslad', 'fiiwrpq'], ['gsvidhp']]) == {('akghbntii', 'uyxt'): 1, ('pehykqo',): 1, ('pslad', 'fiiwrpq'): 1, ('gsvidhp',): 1}
    assert candidate([['lcidqzjh', 'obviu'], ['byd'], ['qjwhphe', 'izy'], ['ybiatac']]) == {('lcidqzjh', 'obviu'): 1, ('byd',): 1, ('qjwhphe', 'izy'): 1, ('ybiatac',): 1}
    assert candidate([['sjewpr', 'zxxugflb'], ['pebu'], ['trscthd', 'aurnmv'], ['ipvxfslsc']]) == {('sjewpr', 'zxxugflb'): 1, ('pebu',): 1, ('trscthd', 'aurnmv'): 1, ('ipvxfslsc',): 1}
    assert candidate([['wgg', 'cpanz'], ['jqn'], ['nprib', 'urh'], ['ktbpggcal']]) == {('wgg', 'cpanz'): 1, ('jqn',): 1, ('nprib', 'urh'): 1, ('ktbpggcal',): 1}
    assert candidate([['werbhs', 'abbe'], ['jbj'], ['zqaymx', 'vydzs'], ['desmlt']]) == {('werbhs', 'abbe'): 1, ('jbj',): 1, ('zqaymx', 'vydzs'): 1, ('desmlt',): 1}
    assert candidate([['vvjmqnva', 'zxycdjen'], ['nwk'], ['jcmu', 'ohjamrd'], ['mvivn']]) == {('vvjmqnva', 'zxycdjen'): 1, ('nwk',): 1, ('jcmu', 'ohjamrd'): 1, ('mvivn',): 1}
    assert candidate([['jllgrdy', 'qwwkbaced'], ['ebdlefzfd'], ['ehn', 'gatdxkjiiocf'], ['pglji']]) == {('jllgrdy', 'qwwkbaced'): 1, ('ebdlefzfd',): 1, ('ehn', 'gatdxkjiiocf'): 1, ('pglji',): 1}
    assert candidate([['jjvbedgi', 'ftkqowshji'], ['kvuqc'], ['toacn', 'pfglwsuwby'], ['vdycqee']]) == {('jjvbedgi', 'ftkqowshji'): 1, ('kvuqc',): 1, ('toacn', 'pfglwsuwby'): 1, ('vdycqee',): 1}
    assert candidate([['odqodv', 'qswj'], ['pxkamtapg'], ['kqmo', 'jzvsvf'], ['kywwypo']]) == {('odqodv', 'qswj'): 1, ('pxkamtapg',): 1, ('kqmo', 'jzvsvf'): 1, ('kywwypo',): 1}
    assert candidate([[11, 21, 31, 36], [56, 72, 52, 54], [86, 96, 200]]) == {(11, 21, 31, 36): 1, (56, 72, 52, 54): 1, (86, 96, 200): 1}
    assert candidate([[14, 25, 29, 41], [61, 65, 50, 53], [88, 99, 204]]) == {(14, 25, 29, 41): 1, (61, 65, 50, 53): 1, (88, 99, 204): 1}
    assert candidate([[12, 22, 33, 35], [64, 65, 52, 54], [94, 101, 199]]) == {(12, 22, 33, 35): 1, (64, 65, 52, 54): 1, (94, 101, 199): 1}
    assert candidate([[5, 19, 34, 37], [56, 75, 45, 50], [88, 99, 205]]) == {(5, 19, 34, 37): 1, (56, 75, 45, 50): 1, (88, 99, 205): 1}
    assert candidate([[5, 22, 34, 35], [57, 70, 45, 45], [86, 105, 196]]) == {(5, 22, 34, 35): 1, (57, 70, 45, 45): 1, (86, 105, 196): 1}
    assert candidate([[13, 22, 33, 38], [58, 74, 49, 45], [87, 105, 198]]) == {(13, 22, 33, 38): 1, (58, 74, 49, 45): 1, (87, 105, 198): 1}
    assert candidate([[7, 25, 35, 44], [57, 71, 51, 52], [87, 104, 198]]) == {(7, 25, 35, 44): 1, (57, 71, 51, 52): 1, (87, 104, 198): 1}
    assert candidate([[13, 16, 30, 45], [65, 69, 52, 53], [86, 102, 198]]) == {(13, 16, 30, 45): 1, (65, 69, 52, 53): 1, (86, 102, 198): 1}
    assert candidate([[7, 21, 33, 44], [65, 68, 45, 55], [94, 100, 202]]) == {(7, 21, 33, 44): 1, (65, 68, 45, 55): 1, (94, 100, 202): 1}
    assert candidate([[11, 18, 35, 37], [60, 70, 50, 46], [89, 99, 198]]) == {(11, 18, 35, 37): 1, (60, 70, 50, 46): 1, (89, 99, 198): 1}
    assert candidate([[11, 18, 26, 35], [61, 65, 53, 55], [86, 95, 198]]) == {(11, 18, 26, 35): 1, (61, 65, 53, 55): 1, (86, 95, 198): 1}
    assert candidate([[10, 15, 34, 38], [65, 72, 55, 46], [95, 97, 204]]) == {(10, 15, 34, 38): 1, (65, 72, 55, 46): 1, (95, 97, 204): 1}
    assert candidate([[13, 16, 33, 44], [59, 72, 52, 49], [85, 101, 196]]) == {(13, 16, 33, 44): 1, (59, 72, 52, 49): 1, (85, 101, 196): 1}
    assert candidate([[15, 17, 32, 42], [60, 69, 46, 45], [94, 99, 204]]) == {(15, 17, 32, 42): 1, (60, 69, 46, 45): 1, (94, 99, 204): 1}
    assert candidate([[12, 16, 31, 39], [55, 65, 55, 51], [88, 95, 204]]) == {(12, 16, 31, 39): 1, (55, 65, 55, 51): 1, (88, 95, 204): 1}
    assert candidate([[15, 15, 25, 36], [56, 73, 53, 50], [93, 101, 205]]) == {(15, 15, 25, 36): 1, (56, 73, 53, 50): 1, (93, 101, 205): 1}
    assert candidate([[11, 20, 27, 42], [58, 71, 49, 49], [95, 101, 199]]) == {(11, 20, 27, 42): 1, (58, 71, 49, 49): 1, (95, 101, 199): 1}
    assert candidate([[6, 19, 35, 45], [65, 75, 47, 51], [93, 101, 205]]) == {(6, 19, 35, 45): 1, (65, 75, 47, 51): 1, (93, 101, 205): 1}
    assert candidate([[14, 20, 26, 44], [60, 67, 53, 47], [91, 100, 200]]) == {(14, 20, 26, 44): 1, (60, 67, 53, 47): 1, (91, 100, 200): 1}
    assert candidate([[12, 18, 26, 37], [63, 70, 51, 45], [88, 102, 200]]) == {(12, 18, 26, 37): 1, (63, 70, 51, 45): 1, (88, 102, 200): 1}
    assert candidate([[12, 24, 35, 40], [65, 71, 48, 46], [90, 95, 200]]) == {(12, 24, 35, 40): 1, (65, 71, 48, 46): 1, (90, 95, 200): 1}
    assert candidate([[13, 23, 26, 41], [55, 68, 47, 49], [91, 101, 204]]) == {(13, 23, 26, 41): 1, (55, 68, 47, 49): 1, (91, 101, 204): 1}
    assert candidate([[5, 23, 35, 40], [64, 72, 49, 50], [90, 97, 199]]) == {(5, 23, 35, 40): 1, (64, 72, 49, 50): 1, (90, 97, 199): 1}
    assert candidate([[15, 21, 33, 37], [62, 68, 53, 55], [89, 96, 199]]) == {(15, 21, 33, 37): 1, (62, 68, 53, 55): 1, (89, 96, 199): 1}
    assert candidate([[9, 22, 33, 45], [64, 73, 48, 52], [91, 103, 198]]) == {(9, 22, 33, 45): 1, (64, 73, 48, 52): 1, (91, 103, 198): 1}
    assert candidate([[8, 16, 27, 45], [61, 69, 52, 49], [85, 105, 202]]) == {(8, 16, 27, 45): 1, (61, 69, 52, 49): 1, (85, 105, 202): 1}
    assert candidate([[10, 15, 32, 42], [60, 75, 53, 46], [90, 105, 197]]) == {(10, 15, 32, 42): 1, (60, 75, 53, 46): 1, (90, 105, 197): 1}
    assert candidate([[15, 20, 32, 40], [58, 70, 49, 51], [88, 96, 204]]) == {(15, 20, 32, 40): 1, (58, 70, 49, 51): 1, (88, 96, 204): 1}
    assert candidate([[12, 18, 28, 45], [64, 65, 54, 45], [87, 99, 195]]) == {(12, 18, 28, 45): 1, (64, 65, 54, 45): 1, (87, 99, 195): 1}
    assert candidate([[10, 17, 28, 40], [65, 71, 49, 49], [92, 101, 201]]) == {(10, 17, 28, 40): 1, (65, 71, 49, 49): 1, (92, 101, 201): 1}
    assert candidate([[7, 22, 26, 43], [63, 74, 48, 53], [91, 103, 200]]) == {(7, 22, 26, 43): 1, (63, 74, 48, 53): 1, (91, 103, 200): 1}
    assert candidate([[13, 25, 26, 43], [65, 67, 46, 50], [89, 100, 204]]) == {(13, 25, 26, 43): 1, (65, 67, 46, 50): 1, (89, 100, 204): 1}
    assert candidate([[14, 17, 33, 41], [63, 70, 50, 47], [95, 99, 203]]) == {(14, 17, 33, 41): 1, (63, 70, 50, 47): 1, (95, 99, 203): 1}

if __name__ == '__main__':
    check(unique_sublists)