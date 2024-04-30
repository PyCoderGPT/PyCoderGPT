from case_MBPP_031 import is_samepatterns


def check(candidate):
    assert candidate(["red","green","green"], ["a", "b", "b"])==True 
    assert candidate(["red","green","greenn"], ["a","b","b"])==False 
    assert candidate(["red","green","greenn"], ["a","b"])==False 
    assert candidate(['sbor', 'evokzv', 'aynbsdo'], ['b', 'p', 'o']) == True
    assert candidate(['bahgcmlui', 'rebv', 'fevwt'], ['s', 'x', 'u']) == True
    assert candidate(['hzqv', 'ytwizljzq', 'zktdwece'], ['c', 'v', 'b']) == True
    assert candidate(['kahrqickx', 'tnfhrvhfv', 'ihcnmo'], ['v', 'n', 's']) == True
    assert candidate(['mojtynv', 'knt', 'xbo'], ['n', 'j', 'f']) == True
    assert candidate(['krxan', 'urezgmsp', 'fiu'], ['b', 'o', 'p']) == True
    assert candidate(['jrw', 'zdopbf', 'cqcbyovkw'], ['m', 'k', 'g']) == True
    assert candidate(['rvysae', 'sywc', 'mayzpvgs'], ['g', 'f', 'u']) == True
    assert candidate(['psh', 'nyyuxwefd', 'kricl'], ['u', 'p', 'q']) == True
    assert candidate(['ptrzl', 'rwombho', 'xqnwcr'], ['a', 'j', 'p']) == True
    assert candidate(['fotvzecub', 'hvxokbse', 'irfjm'], ['m', 'l', 'q']) == True
    assert candidate(['zjsdp', 'trsax', 'iypqsxz'], ['d', 'o', 'p']) == True
    assert candidate(['ieidqbqnc', 'lfztjjl', 'pithacm'], ['g', 'w', 'z']) == True
    assert candidate(['jvxqteix', 'wfha', 'ejfqn'], ['e', 'o', 'o']) == False
    assert candidate(['vdjpqukm', 'yhuidp', 'vehtddme'], ['d', 's', 'z']) == True
    assert candidate(['dtfxpbocq', 'vbgynhus', 'vlu'], ['i', 'o', 'h']) == True
    assert candidate(['avvto', 'qmqltxo', 'wucedojp'], ['l', 'z', 'e']) == True
    assert candidate(['xxcw', 'pca', 'ztzihwg'], ['b', 'u', 'y']) == True
    assert candidate(['ppn', 'vcar', 'zbxbmb'], ['f', 'm', 'o']) == True
    assert candidate(['qaweskj', 'cusgsmp', 'jwk'], ['j', 'j', 'a']) == False
    assert candidate(['jxslxx', 'yazmhkfnr', 'jxv'], ['b', 'g', 'i']) == True
    assert candidate(['ecvjxeghf', 'ohawcihgx', 'mitfe'], ['h', 'x', 's']) == True
    assert candidate(['laajks', 'skiormcl', 'eyjepkr'], ['h', 'n', 'u']) == True
    assert candidate(['maaaatf', 'vvuy', 'zdgjrwlnq'], ['g', 'h', 'c']) == True
    assert candidate(['wqyn', 'hxug', 'gcpziwzj'], ['e', 'r', 'g']) == True
    assert candidate(['lcgywd', 'kwsrzg', 'lzb'], ['v', 'z', 'q']) == True
    assert candidate(['iya', 'bxo', 'xflu'], ['g', 'a', 'u']) == True
    assert candidate(['iety', 'grvavh', 'vigisjn'], ['c', 'q', 'd']) == True
    assert candidate(['utdckwx', 'qmk', 'wisc'], ['d', 'e', 'g']) == True
    assert candidate(['orgmfhg', 'tube', 'miv'], ['e', 'g', 'd']) == True
    assert candidate(['jiqxyrwj', 'vpvceudsc', 'wnseqw'], ['w', 'j', 'y']) == True
    assert candidate(['mdlqk', 'dsom', 'pcqx'], ['r', 'a', 'g']) == True
    assert candidate(['ajiitu', 'nzow', 'wtt'], ['j', 'h', 'u']) == True
    assert candidate(['fqis', 'ksyb', 'udblilcup'], ['w', 'z', 'a']) == True
    assert candidate(['lmyu', 'lfd', 'yfoaqkeiwq'], ['i', 'z', 'g']) == True
    assert candidate(['pzqstxm', 'bdrnb', 'duqslzwg'], ['y', 'y', 'm']) == False
    assert candidate(['voqduh', 'ezgwcltu', 'bsg'], ['n', 't', 'w']) == True
    assert candidate(['mbjrurjn', 'evhnyqg', 'cdqhqhai'], ['n', 'f', 'c']) == True
    assert candidate(['jppud', 'qooiuzq', 'eawrzsnrgvq'], ['h', 'h', 'l']) == False
    assert candidate(['trjmz', 'egjo', 'fkla'], ['w', 'f', 'm']) == True
    assert candidate(['fpcb', 'drniykblq', 'ubhfuyxqc'], ['n', 'l', 'f']) == True
    assert candidate(['bautwv', 'elauko', 'qiik'], ['l', 'd', 'l']) == False
    assert candidate(['syhvw', 'jnbd', 'vdb'], ['w', 'f', 'z']) == True
    assert candidate(['aqktexpiw', 'huyf', 'ukkboiqns'], ['i', 'e', 'z']) == True
    assert candidate(['gkdd', 'qbmniz', 'lqu'], ['h', 'x', 'u']) == True
    assert candidate(['pdszily', 'bgvs', 'zitrnylovpv'], ['r', 'a', 'i']) == True
    assert candidate(['nehslooob', 'flifipa', 'ftdyroyrof'], ['t', 'r', 'e']) == True
    assert candidate(['cmsyeh', 'hquckxh', 'zeb'], ['i', 'n', 'x']) == True
    assert candidate(['yampiezdo', 'jmsghfn', 'hisdjcgvkgt'], ['v', 'x', 'y']) == True
    assert candidate(['aamqsx', 'cfsgooln', 'gvzztbwe'], ['n', 'y', 'e']) == True
    assert candidate(['wkobodmue', 'ndgi', 'zhqjyqco'], ['w', 'x', 'q']) == True
    assert candidate(['qsesgx', 'fxn', 'igegytqi'], ['r', 'w', 'm']) == True
    assert candidate(['hcjbpbk', 'unmzhxm', 'rozymmo'], ['o', 'e', 'q']) == True
    assert candidate(['cbwnj', 'lgc', 'nwziuku'], ['g', 'b', 'x']) == True
    assert candidate(['pqqff', 'ouzwb', 'hazocjwxqeq'], ['f', 's', 'u']) == True
    assert candidate(['zvnq', 'htcejmja', 'tckhgrmqdeq'], ['b', 't', 'h']) == True
    assert candidate(['usbziwrq', 'uezqnoyk', 'csn'], ['p', 'b', 'q']) == True
    assert candidate(['szx', 'mfuu', 'zgduvove'], ['o', 't', 'h']) == True
    assert candidate(['ilra', 'zyzyyqnnx', 'rpceox'], ['q', 'b', 'i']) == True
    assert candidate(['phtbld', 'xlspib', 'cfqszkws'], ['h', 'r', 'u']) == True
    assert candidate(['xkokxokts', 'bfzbyqg', 'zdcvznmkrmc'], ['o', 's', 'a']) == True
    assert candidate(['mlanxt', 'fewc', 'ezak'], ['p', 'v', 'c']) == True
    assert candidate(['iyk', 'kiauets', 'nzqot'], ['u', 'r', 'z']) == True
    assert candidate(['ecgcuq', 'iilsfdime', 'lcb'], ['n', 'f', 'x']) == True
    assert candidate(['eckwrkc', 'zrzn', 'fwdhzrag'], ['t', 'z', 'j']) == True
    assert candidate(['zhn', 'bdccr', 'vrcfbano'], ['o', 'k', 'z']) == True
    assert candidate(['qrnsgwpg', 'hgkdiahat', 'qbzkmckmt'], ['o', 'l']) == False
    assert candidate(['hbdob', 'pztejjm', 'zafk'], ['p', 'u']) == False
    assert candidate(['ifdi', 'uemvj', 'bbavmbadwvne'], ['k', 'x']) == False
    assert candidate(['rksdgi', 'clrzdtuz', 'qnpi'], ['s', 'g']) == False
    assert candidate(['hpfzhvwws', 'kbosltgj', 'wetdaolmxzmo'], ['y', 'k']) == False
    assert candidate(['rtu', 'xceq', 'vms'], ['j', 's']) == False
    assert candidate(['eiohtnq', 'esk', 'wql'], ['j', 'z']) == False
    assert candidate(['uamgftz', 'zajfs', 'fsybhkf'], ['z', 'a']) == False
    assert candidate(['zvnvltwc', 'hvqropji', 'zrgxigubver'], ['b', 'x']) == False
    assert candidate(['vkldyl', 'uyvnxmebx', 'dmhg'], ['k', 'v']) == False
    assert candidate(['mhd', 'gexuo', 'wwlxuroga'], ['b', 'v']) == False
    assert candidate(['bxia', 'ebge', 'jgqw'], ['c', 'a']) == False
    assert candidate(['rcxgxgel', 'alygjhu', 'xrccxqgqzc'], ['v', 'y']) == False
    assert candidate(['taj', 'lgscp', 'nvpsuqcjk'], ['k', 'v']) == False
    assert candidate(['nbityzvn', 'ncuq', 'wuvtlgczxwc'], ['f', 'e']) == False
    assert candidate(['novujswv', 'gclgdwrkx', 'csbkdouw'], ['n', 's']) == False
    assert candidate(['vacbpoml', 'jowwvdpoe', 'jwexfcouicu'], ['p', 'o']) == False
    assert candidate(['cjyo', 'nvyq', 'meesgnzjtppn'], ['d', 'x']) == False
    assert candidate(['qom', 'rjmtbnriw', 'mfzbqvcuh'], ['l', 'm']) == False
    assert candidate(['kusep', 'cvy', 'eqiolyh'], ['h', 'q']) == False
    assert candidate(['zpdoxms', 'piw', 'mqtcv'], ['o', 'o']) == False
    assert candidate(['xxq', 'kbewgvz', 'twyfes'], ['k', 'v']) == False
    assert candidate(['rns', 'kslkcaxq', 'vvuhuhplebb'], ['q', 'e']) == False
    assert candidate(['qverm', 'hzfucwr', 'uja'], ['f', 's']) == False
    assert candidate(['mpfz', 'mwrjtxfq', 'nemozilkya'], ['l', 'h']) == False
    assert candidate(['xsv', 'tsb', 'feoges'], ['b', 'z']) == False
    assert candidate(['favl', 'kqnsul', 'nrzkrc'], ['x', 'p']) == False
    assert candidate(['tpuiqmdec', 'bvje', 'euvrl'], ['c', 'u']) == False
    assert candidate(['tyxxzdf', 'zrv', 'qmkiithywszn'], ['v', 'o']) == False
    assert candidate(['vwownu', 'gogbwin', 'ylexycawfna'], ['u', 'c']) == False
    assert candidate(['jjrfwr', 'mkfqm', 'cjjezopwhmt'], ['o', 'h']) == False
    assert candidate(['ytkiiw', 'iobofumi', 'mfqubcqjit'], ['i', 'n']) == False
    assert candidate(['wsilq', 'oqojqqioh', 'njdxtqsw'], ['g', 'y']) == False

if __name__ == '__main__':
    check(is_samepatterns)