from case_MBPP_379 import count_reverse_pairs


def check(candidate):
    assert candidate(["julia", "best", "tseb", "for", "ailuj"])== '2'
    assert candidate(["geeks", "best", "for", "skeeg"]) == '1'
    assert candidate(["makes", "best", "sekam", "for", "rof"]) == '2' 
    assert candidate(['hvcvuxtz', 'rlclafl', 'sobsr', 'ifdykvux', 'xzzcx']) == 0
    assert candidate(['pku', 'tnhejei', 'exokgcanm', 'mqu', 'auy']) == 0
    assert candidate(['ycneybfvy', 'gimxkwzor', 'apc', 'kepuoih', 'jzbpclhfp']) == 0
    assert candidate(['ita', 'vaavdipp', 'rjav', 'doblw', 'lefany']) == 0
    assert candidate(['zer', 'rakhfttmh', 'jzdkokdrl', 'iappfzei', 'chjetstp']) == 0
    assert candidate(['vkhgl', 'xfkmajchh', 'khelent', 'aafqsjwn', 'fjkyw']) == 0
    assert candidate(['ejiflmd', 'fsabdv', 'dfcpq', 'lnh', 'cic']) == 1
    assert candidate(['ejk', 'dztcl', 'gtkjhpat', 'lioe', 'todmz']) == 0
    assert candidate(['gkj', 'hdy', 'npkcmyxek', 'qzyrhfk', 'qrfd']) == 0
    assert candidate(['atgzdhz', 'opjna', 'nfzxpmopu', 'dhuu', 'nhck']) == 0
    assert candidate(['kiyhuszrl', 'uwxw', 'sejczivb', 'gzjlush', 'zxd']) == 0
    assert candidate(['kej', 'wnvxad', 'vsezm', 'cqtpvm', 'ctglaudm']) == 0
    assert candidate(['tikbpajl', 'yeueb', 'hdwgh', 'iasl', 'lbl']) == 1
    assert candidate(['fdhon', 'iqmobjmo', 'arzsd', 'zwblzvnug', 'mpoxhn']) == 0
    assert candidate(['tnyzo', 'ruerw', 'cifuuv', 'iuhq', 'elrj']) == 0
    assert candidate(['hxsmswmh', 'uxnnhe', 'jgg', 'kzxxfn', 'ihonuzw']) == 0
    assert candidate(['njmlpn', 'nbgjtrdt', 'iqirnus', 'hxfqm', 'jahyncu']) == 0
    assert candidate(['sxqsrqj', 'vhrkqtvel', 'viuujpx', 'zjp', 'edc']) == 0
    assert candidate(['rnhb', 'rzrg', 'owqoycta', 'uwssfhap', 'jzjchditw']) == 0
    assert candidate(['yceytl', 'nhhmqzo', 'uxme', 'diqfwf', 'byiwwx']) == 0
    assert candidate(['daxcdrw', 'psiodlmj', 'etwbzv', 'ceyidi', 'znrka']) == 0
    assert candidate(['bfgno', 'yjkxpi', 'atpqg', 'zphosoetq', 'ecwkvmyt']) == 0
    assert candidate(['jozhw', 'llxg', 'jui', 'kcshg', 'sjurjy']) == 0
    assert candidate(['omoy', 'gglkbg', 'rvpk', 'mut', 'zgiovsx']) == 0
    assert candidate(['ffvmtpa', 'qcqra', 'lgmdtbg', 'qss', 'rsshgy']) == 0
    assert candidate(['ksypxq', 'cofgincg', 'jpnyqc', 'iwi', 'pdene']) == 1
    assert candidate(['gpnob', 'mlq', 'uhr', 'oybmir', 'men']) == 0
    assert candidate(['gdzzlw', 'ddapngqq', 'lskdgizhp', 'ksvlym', 'rcjj']) == 0
    assert candidate(['gebwzpa', 'lfnumc', 'edhwha', 'uceqkndw', 'zayyyftyd']) == 0
    assert candidate(['zxdif', 'fyhckoy', 'loihtp', 'hpoo', 'qogyfwgno']) == 0
    assert candidate(['qlm', 'zgrhdeh', 'khvrycrm', 'ryrhkay', 'thgsp']) == 0
    assert candidate(['snvru', 'susrlht', 'fukirlot', 'telsuu', 'fayyk']) == 0
    assert candidate(['vztqpyc', 'rywbtqxj', 'xnldrdw', 'fuoyoelud', 'zjopfx']) == 0
    assert candidate(['cdkfi', 'mhfqirde', 'ydypgzcj', 'uzowam']) == 0
    assert candidate(['abpd', 'ssmfodjpv', 'amxbkj', 'yvivyoptr']) == 0
    assert candidate(['rwqv', 'qnmaos', 'gwrjzwdou', 'azoziecn']) == 0
    assert candidate(['yym', 'pzi', 'usdsacq', 'ybygitxza']) == 0
    assert candidate(['ckrmb', 'ksw', 'jcsrz', 'pyw']) == 0
    assert candidate(['juhivbnw', 'dqllnxyj', 'bhueosk', 'tqkpfoih']) == 0
    assert candidate(['oraw', 'frz', 'uthsgh', 'vrwgiom']) == 0
    assert candidate(['ilolj', 'ikar', 'kxzilado', 'mdzeby']) == 0
    assert candidate(['vidoufes', 'lqdibdc', 'pvi', 'zru']) == 0
    assert candidate(['ogjxvjfwa', 'jdvvltwkd', 'xtphz', 'glludhn']) == 0
    assert candidate(['xstu', 'pulnz', 'gsad', 'ngitj']) == 0
    assert candidate(['bfx', 'dzjfj', 'npvnsll', 'lhxv']) == 0
    assert candidate(['dngwc', 'woipfkd', 'zadwjj', 'tagjc']) == 0
    assert candidate(['yaljjy', 'heacpbyk', 'zbo', 'olf']) == 0
    assert candidate(['zzm', 'rixp', 'qkidll', 'khiwt']) == 0
    assert candidate(['qmvsyt', 'vvabg', 'wpgknb', 'dsrvajdkj']) == 0
    assert candidate(['pdcmpwui', 'tlxw', 'qxrvd', 'oetwki']) == 0
    assert candidate(['knbewt', 'hjlbkgg', 'fqlezta', 'fygt']) == 0
    assert candidate(['gupydsebu', 'rqe', 'xxht', 'dxnygp']) == 0
    assert candidate(['cfyw', 'mpccyw', 'ofupjfix', 'dfczjfw']) == 0
    assert candidate(['szlzcxpn', 'drxzi', 'xrri', 'ootdh']) == 0
    assert candidate(['pmpojez', 'qkxd', 'tbrepmi', 'xblw']) == 0
    assert candidate(['iwpdrjja', 'ugtg', 'fsec', 'qdd']) == 0
    assert candidate(['qevtgwmfx', 'llgta', 'ztfqaq', 'sntggnh']) == 0
    assert candidate(['fxikcmx', 'lqqzdde', 'wlbuonv', 'zugequfuu']) == 0
    assert candidate(['vbax', 'kmdeapc', 'wafg', 'accno']) == 0
    assert candidate(['qmyktr', 'wdlqp', 'ivovwf', 'wfgtxmv']) == 0
    assert candidate(['ykklq', 'imfysg', 'qreton', 'mgnv']) == 0
    assert candidate(['cdt', 'terskyqzt', 'gxogqkj', 'gxexc']) == 0
    assert candidate(['zbz', 'sejrzx', 'bhwrpfqz', 'mot']) == 1
    assert candidate(['gmdkddueu', 'sfra', 'lrhaaro', 'iwwcg']) == 0
    assert candidate(['hhrva', 'tbx', 'anhusysn', 'wmk']) == 0
    assert candidate(['fnodylbn', 'pgzwztbe', 'rpqqi', 'qgvhci']) == 0
    assert candidate(['afvglnwh', 'fdsyyz', 'oikfosgcm', 'obo', 'mpe']) == 1
    assert candidate(['fywkjwj', 'sce', 'acud', 'yxlszf', 'xvly']) == 0
    assert candidate(['gkuead', 'odfvmactw', 'pwasslri', 'ufj', 'obetll']) == 0
    assert candidate(['oekt', 'unxlevb', 'zld', 'blso', 'zcjmehbz']) == 0
    assert candidate(['ehm', 'ckdt', 'cfuh', 'uzdvhkdvy', 'dylf']) == 0
    assert candidate(['ijlkjea', 'sfehmmp', 'wnt', 'yql', 'anlljja']) == 0
    assert candidate(['gmmuhz', 'ruxnmzbna', 'syoxpirgc', 'daioyxmw', 'ucrmasj']) == 0
    assert candidate(['dmglfy', 'dzhrpo', 'mvaeohbzh', 'amoccyr', 'woxdamuyb']) == 0
    assert candidate(['jyhn', 'wzza', 'ejjxyk', 'pfjzxhvy', 'xdgzemwd']) == 0
    assert candidate(['iuemlm', 'xwgca', 'uwz', 'zxj', 'aabhu']) == 0
    assert candidate(['vjrm', 'ograbmi', 'rnvbbnvtv', 'gidopi', 'ycqxvqiz']) == 0
    assert candidate(['mqit', 'inrhwa', 'ziagiosq', 'vcq', 'vdic']) == 0
    assert candidate(['zznhlsxng', 'wbcvbnu', 'qioj', 'iuslukst', 'uwmcjdity']) == 0
    assert candidate(['iptmvajf', 'zxu', 'adcjo', 'ygkwsogvx', 'aewhbpa']) == 0
    assert candidate(['muhb', 'dmjzwfz', 'swne', 'ikhrimwgy', 'crhj']) == 0
    assert candidate(['usi', 'qstof', 'iquduhc', 'knmrn', 'qlqc']) == 0
    assert candidate(['ueuasbbop', 'xbogfbqlq', 'pzin', 'zxzrrivft', 'lnx']) == 0
    assert candidate(['zaru', 'xjzergzoa', 'hgtfsrf', 'vfgs', 'tas']) == 0
    assert candidate(['mqyapc', 'zuyuwmwe', 'eoxw', 'wornijm', 'ikwjag']) == 0
    assert candidate(['axc', 'tiubrh', 'yozvgej', 'kyftx', 'wcagu']) == 0
    assert candidate(['uknxkswqc', 'qyggrvbe', 'xxepfg', 'wyxbjuihw', 'iusg']) == 0
    assert candidate(['hdhqmr', 'ernpsuhbb', 'emmrlw', 'ixbldut', 'sfwrcl']) == 0
    assert candidate(['zlb', 'otiyypr', 'fugv', 'sfocqgl', 'usuwgqean']) == 0
    assert candidate(['rcroijtd', 'nzarymdnu', 'xzsuxethg', 'qfyqfs', 'qjlwbgm']) == 0
    assert candidate(['ymk', 'nigk', 'vqanj', 'mcubrsbub', 'jhldwo']) == 0
    assert candidate(['xtquup', 'gnsmmgw', 'jjtmxrez', 'awxsizx', 'zpbevisyy']) == 0
    assert candidate(['bkgck', 'qsto', 'sdoljc', 'tvaqj', 'oslgdr']) == 0
    assert candidate(['gonljhlx', 'bqua', 'lhkxynhq', 'hyztxlsq', 'viowi']) == 0
    assert candidate(['vftzeu', 'uzqydpf', 'rzgbty', 'orqquuvpn', 'getwbvw']) == 0
    assert candidate(['wuloaey', 'buesbt', 'onvhtio', 'odt', 'ldk']) == 0
    assert candidate(['kongjqx', 'fhmdu', 'zcymainum', 'bxif', 'yrvgjv']) == 0
    assert candidate(['trvfp', 'isyyjv', 'mwpa', 'xvtphpycj', 'eal']) == 0
    assert candidate(['cdqmkicau', 'yzaxkrezr', 'chmbzl', 'bvez', 'xogpifgj']) == 0

if __name__ == '__main__':
    check(count_reverse_pairs)