from case_MBPP_058 import sort_sublists


def check(candidate):
    assert candidate((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    assert candidate(([" red ","green" ],["blue "," black"],[" orange","brown"]))==[[' red ', 'green'], [' black', 'blue '], [' orange', 'brown']]
    assert candidate((["zilver","gold"], ["magnesium","aluminium"], ["steel", "bronze"]))==[['gold', 'zilver'],['aluminium', 'magnesium'], ['bronze', 'steel']]
    assert candidate((['tadzuejy', 'cvc'], ['xtc', 'jua'], ['pjfm', 'qppqjvj', 'wvql'])) == [['cvc', 'tadzuejy'], ['jua', 'xtc'], ['pjfm', 'qppqjvj', 'wvql']]
    assert candidate((['hcinfc', 'fikumvqpnqj'], ['cwdtk', 'fjziidgk'], ['min', 'tjxs', 'prvts'])) == [['fikumvqpnqj', 'hcinfc'], ['cwdtk', 'fjziidgk'], ['min', 'prvts', 'tjxs']]
    assert candidate((['nqr', 'chrfh'], ['vchinhz', 'pbuoaspw'], ['ltb', 'ikmk', 'wzkop'])) == [['chrfh', 'nqr'], ['pbuoaspw', 'vchinhz'], ['ikmk', 'ltb', 'wzkop']]
    assert candidate((['vzxzoqxy', 'cmcuyx'], ['ybduc', 'fctrplpef'], ['inpdm', 'yqqrm', 'jywqb'])) == [['cmcuyx', 'vzxzoqxy'], ['fctrplpef', 'ybduc'], ['inpdm', 'jywqb', 'yqqrm']]
    assert candidate((['jmvv', 'hwvjvrpifiaf'], ['hojuttbq', 'qpdo'], ['mrgph', 'zjsqurq', 'qvmgrefon'])) == [['hwvjvrpifiaf', 'jmvv'], ['hojuttbq', 'qpdo'], ['mrgph', 'qvmgrefon', 'zjsqurq']]
    assert candidate((['yqsm', 'rnr'], ['jromgl', 'uqnsoohg'], ['zaefqjcg', 'jyjktrz', 'ibtvmuz'])) == [['rnr', 'yqsm'], ['jromgl', 'uqnsoohg'], ['ibtvmuz', 'jyjktrz', 'zaefqjcg']]
    assert candidate((['lfgdkdfhe', 'jkm'], ['bnww', 'htggvd'], ['cbg', 'pby', 'esbuc'])) == [['jkm', 'lfgdkdfhe'], ['bnww', 'htggvd'], ['cbg', 'esbuc', 'pby']]
    assert candidate((['hecl', 'abxfuhogrpl'], ['nbrwu', 'hgkjjnuj'], ['butcpzm', 'aocihqh', 'hehzjvi'])) == [['abxfuhogrpl', 'hecl'], ['hgkjjnuj', 'nbrwu'], ['aocihqh', 'butcpzm', 'hehzjvi']]
    assert candidate((['twwuvfpi', 'oddmq'], ['emq', 'bupohwl'], ['kkkwjhoqr', 'eqctfqxor', 'muaqwzd'])) == [['oddmq', 'twwuvfpi'], ['bupohwl', 'emq'], ['eqctfqxor', 'kkkwjhoqr', 'muaqwzd']]
    assert candidate((['yyjpxpmhi', 'kivkmhrvohu'], ['ehi', 'fgxjtlt'], ['nsncppua', 'rvn', 'rygvqtfv'])) == [['kivkmhrvohu', 'yyjpxpmhi'], ['ehi', 'fgxjtlt'], ['nsncppua', 'rvn', 'rygvqtfv']]
    assert candidate((['cuatvcr', 'nusxurf'], ['buo', 'jji'], ['mrij', 'mjknvmmdr', 'cnkkpwwtdgbi'])) == [['cuatvcr', 'nusxurf'], ['buo', 'jji'], ['cnkkpwwtdgbi', 'mrij', 'mjknvmmdr']]
    assert candidate((['btwntrrcs', 'dfgitpmhx'], ['mzqf', 'hikxycjaa'], ['oloxiuss', 'wipsqwhte', 'atydhquvsuzt'])) == [['btwntrrcs', 'dfgitpmhx'], ['hikxycjaa', 'mzqf'], ['atydhquvsuzt', 'oloxiuss', 'wipsqwhte']]
    assert candidate((['swp', 'jfbybirv'], ['ngf', 'jfu'], ['tqf', 'hloaidcpn', 'wujhc'])) == [['jfbybirv', 'swp'], ['jfu', 'ngf'], ['hloaidcpn', 'tqf', 'wujhc']]
    assert candidate((['bmcpohhe', 'cevetycg'], ['ftpen', 'knulnnw'], ['rwjvfmsl', 'duzv', 'bcfllq'])) == [['bmcpohhe', 'cevetycg'], ['ftpen', 'knulnnw'], ['bcfllq', 'duzv', 'rwjvfmsl']]
    assert candidate((['mbl', 'gkih'], ['hiioihsrt', 'cwb'], ['aho', 'uytmltuuy', 'xgptqbk'])) == [['gkih', 'mbl'], ['cwb', 'hiioihsrt'], ['aho', 'uytmltuuy', 'xgptqbk']]
    assert candidate((['raadz', 'jvgggojuq'], ['svabwfrc', 'aco'], ['dngem', 'ukcruumor', 'ghoglpcxbe'])) == [['jvgggojuq', 'raadz'], ['aco', 'svabwfrc'], ['dngem', 'ghoglpcxbe', 'ukcruumor']]
    assert candidate((['varyzu', 'lxp'], ['okhm', 'crclk'], ['wnqyu', 'llmfpskjw', 'uhrkdg'])) == [['lxp', 'varyzu'], ['crclk', 'okhm'], ['llmfpskjw', 'uhrkdg', 'wnqyu']]
    assert candidate((['dwbz', 'vjhrehuggg'], ['nglbg', 'lconh'], ['ujxrmyou', 'ojhwit', 'rpzxtdpd'])) == [['dwbz', 'vjhrehuggg'], ['lconh', 'nglbg'], ['ojhwit', 'rpzxtdpd', 'ujxrmyou']]
    assert candidate((['zht', 'mlinuiup'], ['uybeyok', 'tczkehv'], ['gvs', 'yiyodim', 'usvmpuw'])) == [['mlinuiup', 'zht'], ['tczkehv', 'uybeyok'], ['gvs', 'usvmpuw', 'yiyodim']]
    assert candidate((['udfm', 'ahwewcxiajkq'], ['cbubwie', 'lach'], ['izvxf', 'gyv', 'qed'])) == [['ahwewcxiajkq', 'udfm'], ['cbubwie', 'lach'], ['gyv', 'izvxf', 'qed']]
    assert candidate((['rmapusfkp', 'xpz'], ['rhsfq', 'rdjayfe'], ['yygk', 'rjcmt', 'oplifyqubyku'])) == [['rmapusfkp', 'xpz'], ['rhsfq', 'rdjayfe'], ['oplifyqubyku', 'rjcmt', 'yygk']]
    assert candidate((['adrs', 'eajokwtf'], ['afaebu', 'ctec'], ['lgw', 'fmzsjyfg', 'taxvb'])) == [['adrs', 'eajokwtf'], ['afaebu', 'ctec'], ['fmzsjyfg', 'lgw', 'taxvb']]
    assert candidate((['rflmfm', 'eke'], ['aldqogoyv', 'goevn'], ['qlu', 'vpcuv', 'gdnyjxrqvfj'])) == [['eke', 'rflmfm'], ['aldqogoyv', 'goevn'], ['gdnyjxrqvfj', 'qlu', 'vpcuv']]
    assert candidate((['gmuwbiyki', 'fvqcqrjjfe'], ['euuk', 'idhfsmk'], ['gjptc', 'cnun', 'wfjgxat'])) == [['fvqcqrjjfe', 'gmuwbiyki'], ['euuk', 'idhfsmk'], ['cnun', 'gjptc', 'wfjgxat']]
    assert candidate((['autfig', 'lntkk'], ['ketctzuwy', 'ygkqrcat'], ['rolsnkg', 'syns', 'bbq'])) == [['autfig', 'lntkk'], ['ketctzuwy', 'ygkqrcat'], ['bbq', 'rolsnkg', 'syns']]
    assert candidate((['zki', 'tqu'], ['jisjcnhax', 'mzzofg'], ['vdjacleef', 'hac', 'tobwfyyqb'])) == [['tqu', 'zki'], ['jisjcnhax', 'mzzofg'], ['hac', 'tobwfyyqb', 'vdjacleef']]
    assert candidate((['agjd', 'kdhvog'], ['btck', 'uesneijlc'], ['aokaegi', 'qnxxghnoh', 'tqqoibpifud'])) == [['agjd', 'kdhvog'], ['btck', 'uesneijlc'], ['aokaegi', 'qnxxghnoh', 'tqqoibpifud']]
    assert candidate((['lgyl', 'jvowkka'], ['avflrwa', 'eeskl'], ['yiambhvf', 'nir', 'veuhllxfmf'])) == [['jvowkka', 'lgyl'], ['avflrwa', 'eeskl'], ['nir', 'veuhllxfmf', 'yiambhvf']]
    assert candidate((['cmj', 'fsrbx'], ['pfn', 'ethejkfi'], ['yeapen', 'vrtharoge', 'tnr'])) == [['cmj', 'fsrbx'], ['ethejkfi', 'pfn'], ['tnr', 'vrtharoge', 'yeapen']]
    assert candidate((['bfvbb', 'eroffmp'], ['naeyj', 'spz'], ['idakvegq', 'lzcqqtfye', 'yglrcxoga'])) == [['bfvbb', 'eroffmp'], ['naeyj', 'spz'], ['idakvegq', 'lzcqqtfye', 'yglrcxoga']]
    assert candidate((['hijr', 'buodfri'], ['qhapbfums', 'zaxlgzmpr'], ['nqq', 'ayspqekac', 'plkk'])) == [['buodfri', 'hijr'], ['qhapbfums', 'zaxlgzmpr'], ['ayspqekac', 'nqq', 'plkk']]
    assert candidate((['mrczxum', 'krnw'], ['gtjkihl', 'dcu'], ['wqoed', 'hajahxtmz', 'bqqzgd'])) == [['krnw', 'mrczxum'], ['dcu', 'gtjkihl'], ['bqqzgd', 'hajahxtmz', 'wqoed']]
    assert candidate((['vuapfgq', 'ctbovljd'], ['tjlkwwcp', 'uzuxjablg'], ['enwfog', 'ycelqo', 'tmlgzpmvrfe'])) == [['ctbovljd', 'vuapfgq'], ['tjlkwwcp', 'uzuxjablg'], ['enwfog', 'tmlgzpmvrfe', 'ycelqo']]
    assert candidate((['oej', 'ugk'], ['kqpmxjpx', 'qobhctp'], ['nbcsk bulo', 'gds'])) == [['oej', 'ugk'], ['kqpmxjpx', 'qobhctp'], ['gds', 'nbcsk bulo']]
    assert candidate((['joe r', 'ioy'], ['zuj', 'kgbnira'], ['tkm', 'wqwqw'])) == [['ioy', 'joe r'], ['kgbnira', 'zuj'], ['tkm', 'wqwqw']]
    assert candidate((['mzpdom', 'nuzw'], ['yhvk', 'uydkutbbfhr'], ['ceohqsudhz', 'tazdnk'])) == [['mzpdom', 'nuzw'], ['uydkutbbfhr', 'yhvk'], ['ceohqsudhz', 'tazdnk']]
    assert candidate((['s rfin', 'kogsrjlpa'], ['zoenga', 'tjla'], ['ldgeec', 'fmdykkp'])) == [['kogsrjlpa', 's rfin'], ['tjla', 'zoenga'], ['fmdykkp', 'ldgeec']]
    assert candidate((['cfb', 'expfwg'], ['fldvxryl', 'rasoocdeavv'], [' gjkhdbrln', 'lbkfawohf'])) == [['cfb', 'expfwg'], ['fldvxryl', 'rasoocdeavv'], [' gjkhdbrln', 'lbkfawohf']]
    assert candidate((['ysqz', 'xmynmkjc'], ['r m', 'nor'], ['udfeflccsq', 'gbjfc'])) == [['xmynmkjc', 'ysqz'], ['nor', 'r m'], ['gbjfc', 'udfeflccsq']]
    assert candidate((['jnue ', 'khwquoc'], ['qxehc', 'faxfvxw'], ['tsfox', 'dprfgcbr'])) == [['jnue ', 'khwquoc'], ['faxfvxw', 'qxehc'], ['dprfgcbr', 'tsfox']]
    assert candidate((['ewvyhbat', 'impmlmb'], ['nmwedqq', 'zbu'], ['df pmlg  ', 'ytlayxtwc'])) == [['ewvyhbat', 'impmlmb'], ['nmwedqq', 'zbu'], ['df pmlg  ', 'ytlayxtwc']]
    assert candidate((['fubhce', 'bpvlb'], ['fppta', 'a p shiu'], ['mhy', 'gktjplyat'])) == [['bpvlb', 'fubhce'], ['a p shiu', 'fppta'], ['gktjplyat', 'mhy']]
    assert candidate((['ztbbuep', 'dzbol'], ['ahqpmjqu', 'ovkscjngiwd'], ['mmu npfratwq', 'chxxb'])) == [['dzbol', 'ztbbuep'], ['ahqpmjqu', 'ovkscjngiwd'], ['chxxb', 'mmu npfratwq']]
    assert candidate((['zd hs', 'uaoroziky'], ['ygr', 'mtxevc'], ['eka', 'gkdi'])) == [['uaoroziky', 'zd hs'], ['mtxevc', 'ygr'], ['eka', 'gkdi']]
    assert candidate((['sjjhji', 'hemixqvxe'], ['pmei', 'gujmwbysjx'], ['sqaujkis ixx', 'gawudr'])) == [['hemixqvxe', 'sjjhji'], ['gujmwbysjx', 'pmei'], ['gawudr', 'sqaujkis ixx']]
    assert candidate((['jovstad', 'qup'], ['p  k', 'fxhjpplyrqh'], ['bs  fab', 'rgltqlir'])) == [['jovstad', 'qup'], ['fxhjpplyrqh', 'p  k'], ['bs  fab', 'rgltqlir']]
    assert candidate((['digtgaf', 'wwf'], ['sbysbpye', 'tzgppyns'], ['zvdewidcm', 'vhseebz'])) == [['digtgaf', 'wwf'], ['sbysbpye', 'tzgppyns'], ['vhseebz', 'zvdewidcm']]
    assert candidate((['sbmv x', 'hmbrg'], ['kgg', 'uzwn'], ['oygspadouv', 'kiu'])) == [['hmbrg', 'sbmv x'], ['kgg', 'uzwn'], ['kiu', 'oygspadouv']]
    assert candidate((['wgb', 'qyvy'], ['dff', 'jmykgms'], ['jhnohajix', 'fyy'])) == [['qyvy', 'wgb'], ['dff', 'jmykgms'], ['fyy', 'jhnohajix']]
    assert candidate((['oqwg r', 'guyt'], ['xliijvsb', 'tahzc'], ['osug', 'pljvenubj'])) == [['guyt', 'oqwg r'], ['tahzc', 'xliijvsb'], ['osug', 'pljvenubj']]
    assert candidate((['boiq', 'wdhuc'], ['vthkwvqo', 'fsaznamgvz'], ['kmo', 'ufsnzwn'])) == [['boiq', 'wdhuc'], ['fsaznamgvz', 'vthkwvqo'], ['kmo', 'ufsnzwn']]
    assert candidate((['afdgpdr', 'lxkgr'], ['cmykkhw', 'fuscphgdoon'], ['lhem odr', 'fchdza'])) == [['afdgpdr', 'lxkgr'], ['cmykkhw', 'fuscphgdoon'], ['fchdza', 'lhem odr']]
    assert candidate((['wcuw aqs', 'gpelnhiqx'], ['olghpbugm', 'put sxgp '], ['topuiaznfzux', 'sia'])) == [['gpelnhiqx', 'wcuw aqs'], ['olghpbugm', 'put sxgp '], ['sia', 'topuiaznfzux']]
    assert candidate((['pkrlov', 'yhv'], ['lezqkqdsd', 'rig'], ['znbraqj', 'zefyln'])) == [['pkrlov', 'yhv'], ['lezqkqdsd', 'rig'], ['znbraqj', 'zefyln']]
    assert candidate((['ymge', 'xabn'], ['reweycnx', 'koav rujjjb'], ['enmkxemfnypb', 'bpvd'])) == [['xabn', 'ymge'], ['koav rujjjb', 'reweycnx'], ['bpvd', 'enmkxemfnypb']]
    assert candidate((['vvdgocw', 'jjkht'], ['oxo', 'fuatpr'], ['l vxspgeiv', 'mblpieto'])) == [['jjkht', 'vvdgocw'], ['fuatpr', 'oxo'], ['l vxspgeiv', 'mblpieto']]
    assert candidate((['sfech', 'rtdzwnvsf'], ['eaqqclsn', 'gfkmm ar'], ['mkuwh', 'tgh'])) == [['rtdzwnvsf', 'sfech'], ['eaqqclsn', 'gfkmm ar'], ['mkuwh', 'tgh']]
    assert candidate((['kosego', 'ptqopuruu'], ['bqsjpp', 'qfhswskw uab'], ['iwdvpmqvaq', 'eflctx'])) == [['kosego', 'ptqopuruu'], ['bqsjpp', 'qfhswskw uab'], ['eflctx', 'iwdvpmqvaq']]
    assert candidate((['fprqrb', 'kpwmfao'], ['hql f', 'tfdwjuwkx'], ['vzxdtysqm', 'zlqbesbj'])) == [['fprqrb', 'kpwmfao'], ['hql f', 'tfdwjuwkx'], ['vzxdtysqm', 'zlqbesbj']]
    assert candidate((['scsao jxt', 'zmtefc'], ['hdvrjv', 'vxx z dxqb'], ['khvn dafwncv', 'nuifqr'])) == [['scsao jxt', 'zmtefc'], ['hdvrjv', 'vxx z dxqb'], ['khvn dafwncv', 'nuifqr']]
    assert candidate((['brk', 'hwn'], ['zsm vpy w', 'fvvssvxcjc'], ['v f ', 'yhyzjeb'])) == [['brk', 'hwn'], ['fvvssvxcjc', 'zsm vpy w'], ['v f ', 'yhyzjeb']]
    assert candidate((['mvsclsym', 'dmhqtcko'], ['nsqdoc', 'hrecn'], ['yk orvpn', 'uzzvy'])) == [['dmhqtcko', 'mvsclsym'], ['hrecn', 'nsqdoc'], ['uzzvy', 'yk orvpn']]
    assert candidate((['mwizhte', 'hnlztgsmn'], ['cilb', 'moi prrju '], ['chqknu ', 'naomauc'])) == [['hnlztgsmn', 'mwizhte'], ['cilb', 'moi prrju '], ['chqknu ', 'naomauc']]
    assert candidate((['pagqkamqn', 'zulazvl'], ['srsasx ', 'aavle c'], ['ujjejfrnpktd', 'racq'])) == [['pagqkamqn', 'zulazvl'], ['aavle c', 'srsasx '], ['racq', 'ujjejfrnpktd']]
    assert candidate((['twakki', 'xpelmbyvl'], ['pdm', 'gumfqtb'], ['d clcmb', 'dydrytxsx'])) == [['twakki', 'xpelmbyvl'], ['gumfqtb', 'pdm'], ['d clcmb', 'dydrytxsx']]
    assert candidate((['mv reur ', 'adc'], ['vumugdk ', 'tuochyxzajv'], ['htgf', 'kmwmw'])) == [['adc', 'mv reur '], ['tuochyxzajv', 'vumugdk '], ['htgf', 'kmwmw']]
    assert candidate((['qrhzvu', 'wyes'], ['wnyseewh', 'pcqwjj'], ['silwqds', 'jeaziykug'])) == [['qrhzvu', 'wyes'], ['pcqwjj', 'wnyseewh'], ['jeaziykug', 'silwqds']]
    assert candidate((['akhoybw', 'duqulyu'], ['pyshhdfvue', 'cbfrtjycojjp'], ['uiyaee', 'lyf'])) == [['akhoybw', 'duqulyu'], ['cbfrtjycojjp', 'pyshhdfvue'], ['lyf', 'uiyaee']]
    assert candidate((['zxzhloxw', 'bgqdbrnbk'], ['kinsjndljdxki', 'atxxqelxvtdr'], ['tfjgz', 'yjmkxat'])) == [['bgqdbrnbk', 'zxzhloxw'], ['atxxqelxvtdr', 'kinsjndljdxki'], ['tfjgz', 'yjmkxat']]
    assert candidate((['qatqhg', 'epc'], ['qdayxgdse', 'cbqugmmirmrinhe'], ['dae', 'ahnkbqrt'])) == [['epc', 'qatqhg'], ['cbqugmmirmrinhe', 'qdayxgdse'], ['ahnkbqrt', 'dae']]
    assert candidate((['tdfygssbdmxn', 'ekam'], ['kkouwlawn', 'xszbbt'], ['clyiu', 'kwqqjiqafkq'])) == [['ekam', 'tdfygssbdmxn'], ['kkouwlawn', 'xszbbt'], ['clyiu', 'kwqqjiqafkq']]
    assert candidate((['qwooakj', 'qmbxbe'], ['kzduqzkauislvg', 'zuuptwmn'], ['pac', 'qxxmxrzqdua'])) == [['qwooakj', 'qmbxbe'], ['kzduqzkauislvg', 'zuuptwmn'], ['pac', 'qxxmxrzqdua']]
    assert candidate((['mshroftykk', 'jcdiuziym'], ['odmcklnpulutti', 'atsozovzhjayrr'], ['jdvoagt', 'cwba'])) == [['jcdiuziym', 'mshroftykk'], ['atsozovzhjayrr', 'odmcklnpulutti'], ['cwba', 'jdvoagt']]
    assert candidate((['raq', 'cxofozq'], ['scvywvetrchijsm', 'zeemidbpnx'], ['zhqkl', 'njf'])) == [['cxofozq', 'raq'], ['scvywvetrchijsm', 'zeemidbpnx'], ['njf', 'zhqkl']]
    assert candidate((['lrbleaiegey', 'jddlzbw'], ['fbmquliyd', 'uqqaflzpewkgfev'], ['mxrpxrspv', 'vubkn'])) == [['jddlzbw', 'lrbleaiegey'], ['fbmquliyd', 'uqqaflzpewkgfev'], ['mxrpxrspv', 'vubkn']]
    assert candidate((['xoqmyiqaryuu', 'wev'], ['jympihwdbk', 'skzpwadokdbz'], ['ekf', 'oxxkolsfz'])) == [['wev', 'xoqmyiqaryuu'], ['jympihwdbk', 'skzpwadokdbz'], ['ekf', 'oxxkolsfz']]
    assert candidate((['mvok', 'xvjhomj'], ['skvwjwuuglyy', 'vlitqf'], ['hbhl', 'mrw'])) == [['mvok', 'xvjhomj'], ['skvwjwuuglyy', 'vlitqf'], ['hbhl', 'mrw']]
    assert candidate((['jqjvdpkwp', 'mvg'], ['ykenhcnfbk', 'qmaythsnzqnz'], ['tgy', 'lrzaogopwvu'])) == [['jqjvdpkwp', 'mvg'], ['qmaythsnzqnz', 'ykenhcnfbk'], ['lrzaogopwvu', 'tgy']]
    assert candidate((['qhkbfir', 'pmw'], ['bxfqmfjh', 'mvquqbhoqasi'], ['hbwrcr', 'xgmey'])) == [['pmw', 'qhkbfir'], ['bxfqmfjh', 'mvquqbhoqasi'], ['hbwrcr', 'xgmey']]
    assert candidate((['jyvvf', 'micfasjel'], ['qczzbhuvq', 'dhrvdpnaxecr'], ['ficnz', 'yanfrjhdb'])) == [['jyvvf', 'micfasjel'], ['dhrvdpnaxecr', 'qczzbhuvq'], ['ficnz', 'yanfrjhdb']]
    assert candidate((['tanhdootrye', 'vezkdsla'], ['zohmzdocmepxoi', 'zbznzvp'], ['mljlslw', 'fynzifaosr'])) == [['tanhdootrye', 'vezkdsla'], ['zohmzdocmepxoi', 'zbznzvp'], ['fynzifaosr', 'mljlslw']]
    assert candidate((['gov', 'teorwfq'], ['opeihxyyg', 'ghooza'], ['riuvuuxoi', 'rwnvd'])) == [['gov', 'teorwfq'], ['ghooza', 'opeihxyyg'], ['riuvuuxoi', 'rwnvd']]
    assert candidate((['tdbcbqpvzp', 'yonvvvuhc'], ['hjkagygdu', 'bwjlrghcjnn'], ['tnwsm', 'bqidtgfcj'])) == [['tdbcbqpvzp', 'yonvvvuhc'], ['bwjlrghcjnn', 'hjkagygdu'], ['bqidtgfcj', 'tnwsm']]
    assert candidate((['jnn', 'kyu'], ['ghuqiewdyv', 'vbgcsgh'], ['duublalqi', 'bgggrsfhlexw'])) == [['jnn', 'kyu'], ['ghuqiewdyv', 'vbgcsgh'], ['bgggrsfhlexw', 'duublalqi']]
    assert candidate((['xtonbptvb', 'ihpfoq'], ['swcsbkgbqoygy', 'gxjbwhor'], ['mxssj', 'jegvyktaan'])) == [['ihpfoq', 'xtonbptvb'], ['gxjbwhor', 'swcsbkgbqoygy'], ['jegvyktaan', 'mxssj']]
    assert candidate((['csiyyuex', 'yeepbd'], ['rsowmqxh', 'eefooczwqffzov'], ['caidfgw', 'usgy'])) == [['csiyyuex', 'yeepbd'], ['eefooczwqffzov', 'rsowmqxh'], ['caidfgw', 'usgy']]
    assert candidate((['uee', 'rnd'], ['ahwurxcynb', 'nuzodiuxuwzo'], ['iefy', 'wlroxnbngi'])) == [['rnd', 'uee'], ['ahwurxcynb', 'nuzodiuxuwzo'], ['iefy', 'wlroxnbngi']]
    assert candidate((['qcffdtlhvavk', 'ddxztvqbo'], ['ezwovpzzee', 'cdexdvgtaxbi'], ['omallqxva', 'zarsxnvyihol'])) == [['ddxztvqbo', 'qcffdtlhvavk'], ['cdexdvgtaxbi', 'ezwovpzzee'], ['omallqxva', 'zarsxnvyihol']]
    assert candidate((['elwfgxoo', 'ekr'], ['ywlftzatrjssyo', 'pckvxyxmfjrsty'], ['tdaqgcgvt', 'asbbnlza'])) == [['elwfgxoo', 'ekr'], ['pckvxyxmfjrsty', 'ywlftzatrjssyo'], ['asbbnlza', 'tdaqgcgvt']]
    assert candidate((['jasbhmvmvlv', 'aegx'], ['cklxxq', 'gnwnzflgbckm'], ['rtu', 'mqifuoew'])) == [['aegx', 'jasbhmvmvlv'], ['cklxxq', 'gnwnzflgbckm'], ['mqifuoew', 'rtu']]
    assert candidate((['snjszrko', 'mitiinwhl'], ['ueqidusdln', 'fwioxkcynaz'], ['cducg', 'pcjltfv'])) == [['mitiinwhl', 'snjszrko'], ['fwioxkcynaz', 'ueqidusdln'], ['cducg', 'pcjltfv']]
    assert candidate((['oicccjgtnhep', 'wre'], ['dznqlrhkow', 'kfaejrqmxu'], ['pkqboh', 'kqqn'])) == [['oicccjgtnhep', 'wre'], ['dznqlrhkow', 'kfaejrqmxu'], ['kqqn', 'pkqboh']]
    assert candidate((['nqc', 'bbzmsd'], ['yjskognf', 'unlmxtfdzkhbv'], ['mxjj', 'jvj'])) == [['bbzmsd', 'nqc'], ['unlmxtfdzkhbv', 'yjskognf'], ['jvj', 'mxjj']]
    assert candidate((['lsvverbz', 'ndgtb'], ['yljwnugqepxl', 'xxzmrrgk'], ['jcvko', 'jmfggzzlsxaw'])) == [['lsvverbz', 'ndgtb'], ['xxzmrrgk', 'yljwnugqepxl'], ['jcvko', 'jmfggzzlsxaw']]
    assert candidate((['maqseq', 'ldzspo'], ['trtsvup', 'ymkkbozflkzzd'], ['modpg', 'ibyh'])) == [['ldzspo', 'maqseq'], ['trtsvup', 'ymkkbozflkzzd'], ['ibyh', 'modpg']]
    assert candidate((['tocmwojsxsl', 'vpsjs'], ['rmsdclhj', 'keujqfxzumg'], ['rkkffmtil', 'zioafguy'])) == [['tocmwojsxsl', 'vpsjs'], ['keujqfxzumg', 'rmsdclhj'], ['rkkffmtil', 'zioafguy']]
    assert candidate((['csahocmu', 'csgzs'], ['ltvvrbgsid', 'bdidxc'], ['ogjxm', 'cihuubyyrjvy'])) == [['csahocmu', 'csgzs'], ['bdidxc', 'ltvvrbgsid'], ['cihuubyyrjvy', 'ogjxm']]
    assert candidate((['jsryehyiw', 'ceh'], ['gyzyougik', 'shsouxqsgrqkeid'], ['xkwtnh', 'myinfinaodx'])) == [['ceh', 'jsryehyiw'], ['gyzyougik', 'shsouxqsgrqkeid'], ['myinfinaodx', 'xkwtnh']]
    assert candidate((['ymftdirllh', 'upl'], ['xwlonosayioleas', 'lydwidzryamx'], ['oqqvep', 'ghzabuj'])) == [['upl', 'ymftdirllh'], ['lydwidzryamx', 'xwlonosayioleas'], ['ghzabuj', 'oqqvep']]

if __name__ == '__main__':
    check(sort_sublists)