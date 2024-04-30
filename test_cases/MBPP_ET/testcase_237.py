from case_MBPP_237 import extract_string


def check(candidate):
    assert candidate(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
    assert candidate(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
    assert candidate(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']
    assert candidate(['jKZxOlbTaCu', 'zidnr', 'xltfgdxamss', 'smtiqxdjc', 'mgtwbidx'], 10) == []
    assert candidate(['Zhe', 'izedzf', 'ovwmfog', 'qsoizovqmp', 'ldrggernh'], 12) == []
    assert candidate(['BApRsE', 'gqofblu', 'obikzivdtqfgyua', 'ekuizhhfbzgj', 'ehgisf'], 9) == []
    assert candidate(['jNGUkWdPB', 'avmpxwx', 'yshaiwxgetv', 'xpuoyfeyiss', 'ezghlnx'], 3) == []
    assert candidate(['dlpzCg', 'nnkxwjvcj', 'uckxhf', 'org', 'ngeiwjld'], 9) == ['nnkxwjvcj']
    assert candidate(['qiLnBlBVj', 'aqfmgu', 'ogfajlf', 'nkpjspnrglch', 'onrbz'], 13) == []
    assert candidate(['EXe', 'rvorn', 'tdmsbycpjsqf', 'tpycx', 'ekxvplpan'], 5) == ['rvorn', 'tpycx']
    assert candidate(['wlRv', 'jlakv', 'rcaholmfvpcr', 'yqyk', 'hnizdsxozl'], 3) == []
    assert candidate(['IxdWseMF', 'hxcmql', 'umjmrklebwoo', 'lzxlgcf', 'fnivue'], 11) == []
    assert candidate(['iHGsQqvLWN', 'yjp', 'jgwnkuveyqxvwtk', 'vamwzd', 'srubdizrzf'], 4) == []
    assert candidate(['NqOFuIkkLvfy', 'ppqws', 'xiphudcfbbjepny', 'aarbeuq', 'gstx'], 12) == ['NqOFuIkkLvfy']
    assert candidate(['njVBD', 'zkglez', 'etwmrmolooxmx', 'yoismcx', 'uejkcgiizjdm'], 11) == []
    assert candidate(['TuKjvortMDW', 'mykzhqsi', 'kedodjdilijtczg', 'fhmhkqihbgq', 'dkv'], 3) == ['dkv']
    assert candidate(['cfAjjBcyAZ', 'npqki', 'qcaxrrzmkpynti', 'ickyesvysq', 'hfwbnabmrhnu'], 11) == []
    assert candidate(['uilztUqcfYT', 'dcykggdb', 'zyxuhhkfpxu', 'ohonoifypmim', 'jkuhtm'], 6) == ['jkuhtm']
    assert candidate(['xRyIDvJIkLAL', 'dgtfbavd', 'qjzxkfp', 'itudjtqnwa', 'koop'], 7) == ['qjzxkfp']
    assert candidate(['UTIaeel', 'fwidoza', 'kqodrsniaucvrw', 'bzwvhqzdxmu', 'pcgyemagtz'], 8) == []
    assert candidate(['hBHPytxSSPZD', 'xpn', 'fraakn', 'wlgcplz', 'kcf'], 8) == []
    assert candidate(['cTNkh', 'qcyluhgvt', 'adaovka', 'gcqlvlu', 'qbu'], 4) == []
    assert candidate(['puoQ', 'hpg', 'dwgsvnijfcxsac', 'jgwtzbnbok', 'onhhojymv'], 5) == []
    assert candidate(['qFRztkZpcXZQ', 'jzu', 'ytptnt', 'dzkegjhb', 'xgka'], 3) == ['jzu']
    assert candidate(['ZpnDIzn', 'yrv', 'jeuzpwufhmpjdd', 'vtebtv', 'bxj'], 4) == []
    assert candidate(['uPmaLpDnHDY', 'yccg', 'yfsthyrcjlepqx', 'trm', 'usiiat'], 11) == ['uPmaLpDnHDY']
    assert candidate(['yJoWsqXW', 'fpjlbg', 'dztsakosic', 'yuvjqanlxhmx', 'nxjnmosfyb'], 12) == ['yuvjqanlxhmx']
    assert candidate(['uhnhSKLTHv', 'xxcqj', 'lgqmhnyimzmnx', 'uqtheqbvmt', 'vofocpbodgrj'], 10) == ['uhnhSKLTHv', 'uqtheqbvmt']
    assert candidate(['sbdnssDPvP', 'spx', 'gmbegpimvqfg', 'szaaxcpbi', 'ytiupavt'], 5) == []
    assert candidate(['WANM', 'rdjbp', 'lecfmv', 'bshpflmlhmu', 'qtl'], 12) == []
    assert candidate(['IkT', 'aka', 'ccixezbmy', 'jyokaqmodc', 'dzlkcqwskxpd'], 11) == []
    assert candidate(['fRuUWlOFAaa', 'dbl', 'zsisxpmhlzbhns', 'moao', 'rohvglzgfj'], 7) == []
    assert candidate(['NsU', 'wxrox', 'zniqnpguf', 'tdudqqqynk', 'asqjfqbx'], 5) == ['wxrox']
    assert candidate(['ZLudB', 'nuky', 'nynnor', 'glt', 'asegimcqbi'], 5) == ['ZLudB']
    assert candidate(['jGJERDGVKYi', 'bkrstpsh', 'fwhysjwnvwqdnec', 'axhnclpuq', 'usjxvfmb'], 7) == []
    assert candidate(['NNXY', 'vjwxzvj', 'aczciavhppbwcc', 'fgktlykw', 'jdqva'], 9) == []
    assert candidate(['oGcmYUri', 'okxyz', 'qmbhowtfpqza', 'atgwvceh', 'tmji'], 2) == []
    assert candidate(['ORulboIGPk', 'nqpachx', 'ifopccvpslnarb', 'rybhhlyb', 'lmbqgslrbtss'], 8) == ['rybhhlyb']
    assert candidate(['DMAGPTjNl', 'bawiyko', 'ktasnut', 'jykrjrem', 'ftzdocnr'], 1) == []
    assert candidate(['RjjNLI', 'kwnmigrvg', 'vktqhugw', 'ptjt', 'vixoimmdtf'], 10) == ['vixoimmdtf']
    assert candidate(['HOLaaJtY', 'vhowitgg', 'jgpbpjmr', 'gjtszex', 'jvlojhwystev'], 5) == []
    assert candidate(['lFaS', 'acfencxp', 'yehlorakttvx', 'fdhgagzepi', 'xypgmb'], 6) == ['xypgmb']
    assert candidate(['eFrN', 'lad', 'ohabvssqo', 'pqucnc', 'kbd'], 1) == []
    assert candidate(['pdh', 'bzpdbquby', 'obijxkxyggvuplg', 'fqwtrycrlykp', 'bsejeldtfyx'], 4) == []
    assert candidate(['mXlWvciwAss', 'krq', 'hdnspxvczv', 'gclwusih', 'kxdngh'], 8) == ['gclwusih']
    assert candidate(['VwTnATgEQ', 'kvaps', 'aappnineaqihdur', 'sbcur', 'kieiypucajbh'], 4) == []
    assert candidate(['eHG', 'kwplmaur', 'nntcsofm', 'kijhbcmaod', 'tlyig'], 5) == ['tlyig']
    assert candidate(['uhHIh', 'mwyjvyuid', 'ixrvfhdc', 'oroolrhw', 'dgsvq'], 9) == ['mwyjvyuid']
    assert candidate(['CnKkr', 'xnfmwjthj', 'abjwmem', 'pczh', 'onmjfs'], 2) == []
    assert candidate(['eVBNi', 'zyz', 'ogrildsjfpevn', 'lslyorggn', 'unqvawyz'], 4) == []
    assert candidate(['llwsMBCqN', 'vwdh', 'ccabxbhtfvscg', 'bflsrutzs', 'hszmgzudedn'], 10) == []
    assert candidate(['FfEx', 'bodzqjn', 'wxwouraulxh', 'roy', 'slsnypjspyw'], 5) == []
    assert candidate(['WehfmOw', 'tbduqrcmn', 'lzjmrvxzvcpmku', 'xerbwpk', 'aka'], 1) == []
    assert candidate(['arFJSEi', 'ajuxxh', 'jcbulfhzdljftca', 'jbkqkjzoi', 'pdcpbp'], 6) == ['ajuxxh', 'pdcpbp']
    assert candidate(['yaXZCHRpL', 'szdsugfte', 'zsxbsjdl', 'efgmhlkpyq', 'cuckfgasiu'], 6) == []
    assert candidate(['TykKJEXmfsCu', 'bndi', 'vwavjd', 'mbkwy', 'ivtembvxnxx'], 1) == []
    assert candidate(['Yapm', 'isrlw', 'krujpqxalbfnc', 'aeqr', 'jerboootja'], 4) == ['Yapm', 'aeqr']
    assert candidate(['kmdQxSk', 'gywfg', 'znhbvbrsnapwfn', 'phhyui', 'trw'], 1) == []
    assert candidate(['lQz', 'irvtzrg', 'ehwoss', 'zvpqa', 'asvy'], 11) == []
    assert candidate(['lkUQsj', 'xjhfwgrp', 'hlfcmp', 'qur', 'qhgjx'], 2) == []
    assert candidate(['jlIvP', 'hdojcyh', 'jeoagmoa', 'lbpvdwentuch', 'dcnqo'], 8) == ['jeoagmoa']
    assert candidate(['cTwyLkLvRoj', 'ykjtxbr', 'lqvjtx', 'yecbleuj', 'wnqxghdb'], 7) == ['ykjtxbr']
    assert candidate(['hccEwgC', 'yjd', 'uokzwcczpvsb', 'bmvhgx', 'svrn'], 8) == []
    assert candidate(['tpOa', 'dvq', 'lrpuecccgluizma', 'iftaa', 'fkjihu'], 1) == []
    assert candidate(['KwnZ', 'eksebeodh', 'imodlc', 'cjhrj', 'mdyl'], 10) == []
    assert candidate(['JvhxG', 'sjgsj', 'sxnqqqnili', 'vuy', 'mlwsvyfrphc'], 10) == ['sxnqqqnili']
    assert candidate(['QdhSmsLAubVU', 'xbzqhulx', 'acbusubjn', 'mkfynjoz', 'atrmdmupltad'], 8) == ['xbzqhulx', 'mkfynjoz']
    assert candidate(['CFwdBijf', 'kxa', 'fbjigawanb', 'llmefz', 'ecgyjxis'], 5) == []
    assert candidate(['tQRJyzpFM', 'hwcz', 'geqtutltlxclil', 'kqeq', 'hkzxmnhvl'], 11) == []
    assert candidate(['fRtPMnFd', 'lzezfaako', 'svxwfxhviowej', 'binvjageuybm', 'wljmkfwxu'], 7) == []
    assert candidate(['QtklXVEQ', 'sacklcoq', 'smtmlthfiggeez', 'luao', 'ssmg'], 12) == []
    assert candidate(['deRs', 'ypy', 'khxcxlsyhupvr', 'hrhojwmvzni', 'mkhijhwhrqsh'], 11) == ['hrhojwmvzni']
    assert candidate(['tjDdGemi', 'zapfi', 'qkugnxqldrvg', 'gmoisdvdipbj', 'kgkrtucybilr'], 6) == []
    assert candidate(['FPRXokkiErxM', 'zbxvjcuy', 'gylahjlnsfkam', 'vics', 'uqucacmltwy'], 8) == ['zbxvjcuy']
    assert candidate(['pDBwDagBZz', 'itkxwqwxj', 'jufssdmqu', 'totoaqcocf', 'xae'], 11) == []
    assert candidate(['TtAKb', 'iscr', 'ookgzgmsdffim', 'ltnpjnzfheb', 'nyysgpfsaw'], 9) == []
    assert candidate(['zOBfcS', 'edquwnacz', 'mqdrbqk', 'nfta', 'oyj'], 11) == []
    assert candidate(['gKHJi', 'kbujwgh', 'rpjyedpkg', 'vhxou', 'ugzmlp'], 14) == []
    assert candidate(['msMrNGiA', 'vigojgqu', 'xtunpubkjxy', 'nafguzepvwk', 'iqpwig'], 10) == []
    assert candidate(['QOMl', 'buebmomjw', 'puvytkdimonvwqs', 'qjwemc', 'zncgi'], 10) == []
    assert candidate(['OzZPPlug', 'eufydot', 'jwtnas', 'lwesfhjnl', 'rolj'], 12) == []
    assert candidate(['HpEgWRuGZ', 'atfcuqi', 'uobifsuhulkv', 'nfbiigw', 'mybnvveeky'], 4) == []
    assert candidate(['zNpPqeHKTkRB', 'vjexpy', 'wijkiitcrpmnpue', 'xzqlmwaybow', 'jfgrdquowzj'], 4) == []
    assert candidate(['CNEuyxKYgY', 'tjbgflieo', 'ztvzcg', 'bcn', 'apa'], 7) == []
    assert candidate(['bkqRrG', 'mrc', 'zqpcdchvwc', 'eobojonbo', 'irglaue'], 6) == ['bkqRrG']
    assert candidate(['yKZHIbqUcOf', 'vbap', 'temtsdkvmfyg', 'vgholm', 'nxwoi'], 7) == []
    assert candidate(['OSqDpECc', 'grkaor', 'dcoxnpueknq', 'vsxautphmnva', 'rgbe'], 4) == ['rgbe']
    assert candidate(['mIL', 'eytiuuru', 'ptzhwvxaydbedh', 'odolwiqs', 'anpdogtsmhme'], 10) == []
    assert candidate(['uIkcyo', 'wwbgeb', 'xalrsw', 'juroqql', 'oxgohi'], 5) == []
    assert candidate(['hCAkU', 'zajv', 'umevtcvsbemxgc', 'jeshwtrlp', 'coydeatcexx'], 5) == ['hCAkU']
    assert candidate(['QiusjluDm', 'ixzuyi', 'afosdjxofjrgw', 'eoesfb', 'cnigxqut'], 8) == ['cnigxqut']
    assert candidate(['cDaTdqPRiIJO', 'ytyzqtm', 'qbduwkn', 'bpfoeymufcx', 'secwkqsv'], 12) == ['cDaTdqPRiIJO']
    assert candidate(['OtUxgXLi', 'alcta', 'fpzycv', 'smzlsvido', 'sfndgj'], 9) == ['smzlsvido']
    assert candidate(['CXyvrbK', 'pkcadm', 'zugxlqlajsktm', 'jffbzxek', 'olyjh'], 7) == ['CXyvrbK']
    assert candidate(['hAXrI', 'lgpwinx', 'fmbosrqdourfu', 'irnrvikoztpy', 'xxell'], 7) == ['lgpwinx']
    assert candidate(['XUKRrkUPdle', 'qdqu', 'ggcdbhho', 'pnkegk', 'kbkwatjzkwf'], 11) == ['XUKRrkUPdle', 'kbkwatjzkwf']
    assert candidate(['wodZDBBP', 'urpypeilp', 'acabxqj', 'qaasiyjgl', 'ligawovb'], 8) == ['wodZDBBP', 'ligawovb']
    assert candidate(['RGYEVnw', 'necptvhl', 'aorjemubsk', 'unpkc', 'zydxygap'], 10) == ['aorjemubsk']
    assert candidate(['TMXzNPgP', 'slldo', 'ntuphclibkh', 'osqwqb', 'moi'], 4) == []
    assert candidate(['EoZ', 'qyfypovk', 'ourfcn', 'jwz', 'llqxtppzt'], 14) == []
    assert candidate(['RIawmwjQdirR', 'pnhet', 'mywjfndfwl', 'nym', 'idsgtty'], 8) == []
    assert candidate(['Eip', 'qgccnc', 'ujgeifgzrsxmuvw', 'fism', 'ifnn'], 13) == []

if __name__ == '__main__':
    check(extract_string)