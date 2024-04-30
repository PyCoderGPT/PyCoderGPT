from case_MBPP_138 import list_split


def check(candidate):
    assert candidate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']] 
    assert candidate([1,2,3,4,5,6,7,8,9,10,11,12,13,14],3)==[[1,4,7,10,13], [2,5,8,11,14], [3,6,9,12]] 
    assert candidate(['python','java','C','C++','DBMS','SQL'],2)==[['python', 'C', 'DBMS'], ['java', 'C++', 'SQL']] 
    assert candidate(['j', 'q', 'l', 'd', 'n', 'j', 'm', 'j', 'b', 'w', 'v', 'u', 'q', 'z'], 6) == [['j', 'm', 'q'], ['q', 'j', 'z'], ['l', 'b'], ['d', 'w'], ['n', 'v'], ['j', 'u']]
    assert candidate(['j', 's', 'n', 'f', 's', 'q', 'f', 'v', 'k', 'd', 'q', 'm', 'c', 'q'], 2) == [['j', 'n', 's', 'f', 'k', 'q', 'c'], ['s', 'f', 'q', 'v', 'd', 'm', 'q']]
    assert candidate(['h', 'k', 't', 'a', 'b', 'p', 'h', 's', 'y', 'm', 'x', 'f', 'u', 'f'], 4) == [['h', 'b', 'y', 'u'], ['k', 'p', 'm', 'f'], ['t', 'h', 'x'], ['a', 's', 'f']]
    assert candidate(['x', 'j', 'w', 'x', 'b', 'x', 'w', 'm', 'b', 'b', 'y', 'p', 'g', 'o'], 6) == [['x', 'w', 'g'], ['j', 'm', 'o'], ['w', 'b'], ['x', 'b'], ['b', 'y'], ['x', 'p']]
    assert candidate(['u', 'j', 'm', 'i', 'h', 't', 'q', 'c', 'w', 'e', 'y', 'o', 'o', 'e'], 2) == [['u', 'm', 'h', 'q', 'w', 'y', 'o'], ['j', 'i', 't', 'c', 'e', 'o', 'e']]
    assert candidate(['s', 'z', 'j', 'y', 'c', 'p', 'i', 'd', 'l', 'v', 'o', 'k', 'y', 'a'], 3) == [['s', 'y', 'i', 'v', 'y'], ['z', 'c', 'd', 'o', 'a'], ['j', 'p', 'l', 'k']]
    assert candidate(['p', 'o', 'u', 'd', 'r', 'w', 'b', 'u', 'j', 't', 'a', 'v', 'c', 'b'], 8) == [['p', 'j'], ['o', 't'], ['u', 'a'], ['d', 'v'], ['r', 'c'], ['w', 'b'], ['b'], ['u']]
    assert candidate(['v', 'e', 'z', 'w', 'u', 'h', 'j', 'o', 'f', 'n', 't', 'p', 'u', 'k'], 6) == [['v', 'j', 'u'], ['e', 'o', 'k'], ['z', 'f'], ['w', 'n'], ['u', 't'], ['h', 'p']]
    assert candidate(['d', 'l', 'p', 'v', 'j', 'k', 'v', 'p', 'b', 'f', 'i', 'w', 'b', 'r'], 5) == [['d', 'k', 'i'], ['l', 'v', 'w'], ['p', 'p', 'b'], ['v', 'b', 'r'], ['j', 'f']]
    assert candidate(['k', 'u', 'c', 't', 'n', 'd', 'y', 'e', 'n', 'b', 'f', 'z', 'k', 'm'], 5) == [['k', 'd', 'f'], ['u', 'y', 'z'], ['c', 'e', 'k'], ['t', 'n', 'm'], ['n', 'b']]
    assert candidate(['b', 'm', 'f', 'p', 'p', 'v', 'p', 'n', 'v', 'h', 'g', 'h', 'h', 'l'], 7) == [['b', 'n'], ['m', 'v'], ['f', 'h'], ['p', 'g'], ['p', 'h'], ['v', 'h'], ['p', 'l']]
    assert candidate(['w', 'j', 'm', 'h', 'y', 'c', 'k', 'e', 'v', 's', 'f', 'q', 'l', 'p'], 8) == [['w', 'v'], ['j', 's'], ['m', 'f'], ['h', 'q'], ['y', 'l'], ['c', 'p'], ['k'], ['e']]
    assert candidate(['v', 'g', 'm', 'i', 'v', 'u', 'b', 'i', 'b', 'c', 'j', 'j', 's', 'z'], 5) == [['v', 'u', 'j'], ['g', 'b', 'j'], ['m', 'i', 's'], ['i', 'b', 'z'], ['v', 'c']]
    assert candidate(['z', 'm', 'x', 'r', 'i', 't', 'p', 'o', 'u', 'n', 'a', 'j', 'e', 'i'], 2) == [['z', 'x', 'i', 'p', 'u', 'a', 'e'], ['m', 'r', 't', 'o', 'n', 'j', 'i']]
    assert candidate(['q', 'p', 'l', 't', 'i', 'd', 'k', 'x', 'n', 'j', 'g', 'i', 'k', 'l'], 8) == [['q', 'n'], ['p', 'j'], ['l', 'g'], ['t', 'i'], ['i', 'k'], ['d', 'l'], ['k'], ['x']]
    assert candidate(['g', 'j', 'q', 'y', 's', 'g', 'l', 'x', 't', 't', 'c', 's', 'm', 'h'], 8) == [['g', 't'], ['j', 't'], ['q', 'c'], ['y', 's'], ['s', 'm'], ['g', 'h'], ['l'], ['x']]
    assert candidate(['d', 'i', 'b', 's', 'b', 'g', 'g', 'i', 'l', 'd', 'm', 'y', 'x', 'z'], 5) == [['d', 'g', 'm'], ['i', 'g', 'y'], ['b', 'i', 'x'], ['s', 'l', 'z'], ['b', 'd']]
    assert candidate(['p', 'l', 's', 'w', 'l', 'p', 'f', 'd', 'w', 'i', 'j', 'l', 'h', 'n'], 3) == [['p', 'w', 'f', 'i', 'h'], ['l', 'l', 'd', 'j', 'n'], ['s', 'p', 'w', 'l']]
    assert candidate(['m', 'n', 'b', 'b', 'k', 'g', 'u', 'n', 'q', 'q', 'd', 't', 'y', 'a'], 3) == [['m', 'b', 'u', 'q', 'y'], ['n', 'k', 'n', 'd', 'a'], ['b', 'g', 'q', 't']]
    assert candidate(['c', 'p', 'e', 't', 'q', 'o', 'o', 'i', 'p', 'x', 'r', 'y', 'y', 'j'], 2) == [['c', 'e', 'q', 'o', 'p', 'r', 'y'], ['p', 't', 'o', 'i', 'x', 'y', 'j']]
    assert candidate(['j', 'r', 'o', 'f', 'f', 'u', 'x', 't', 'p', 'o', 'c', 'f', 'x', 'f'], 8) == [['j', 'p'], ['r', 'o'], ['o', 'c'], ['f', 'f'], ['f', 'x'], ['u', 'f'], ['x'], ['t']]
    assert candidate(['b', 'j', 'a', 'u', 'q', 'c', 't', 'd', 'h', 'a', 'x', 'r', 'x', 'o'], 8) == [['b', 'h'], ['j', 'a'], ['a', 'x'], ['u', 'r'], ['q', 'x'], ['c', 'o'], ['t'], ['d']]
    assert candidate(['n', 'r', 'r', 'j', 'e', 't', 'f', 's', 'x', 'x', 'y', 'b', 'e', 'z'], 6) == [['n', 'f', 'e'], ['r', 's', 'z'], ['r', 'x'], ['j', 'x'], ['e', 'y'], ['t', 'b']]
    assert candidate(['b', 'w', 'u', 'r', 'f', 'h', 't', 'o', 'f', 'm', 'k', 'g', 'l', 'f'], 6) == [['b', 't', 'l'], ['w', 'o', 'f'], ['u', 'f'], ['r', 'm'], ['f', 'k'], ['h', 'g']]
    assert candidate(['y', 'j', 'o', 'd', 'f', 'x', 'n', 'p', 'd', 'a', 'a', 's', 'l', 't'], 2) == [['y', 'o', 'f', 'n', 'd', 'a', 'l'], ['j', 'd', 'x', 'p', 'a', 's', 't']]
    assert candidate(['f', 'v', 'h', 'k', 'c', 'x', 'r', 'l', 'z', 'x', 'j', 'r', 'f', 'l'], 5) == [['f', 'x', 'j'], ['v', 'r', 'r'], ['h', 'l', 'f'], ['k', 'z', 'l'], ['c', 'x']]
    assert candidate(['b', 'j', 'd', 'm', 'v', 't', 'g', 'o', 'q', 'd', 'l', 'p', 'b', 'w'], 5) == [['b', 't', 'l'], ['j', 'g', 'p'], ['d', 'o', 'b'], ['m', 'q', 'w'], ['v', 'd']]
    assert candidate(['y', 'y', 'i', 'q', 'x', 'w', 'r', 'o', 'i', 't', 'd', 't', 'k', 'f'], 6) == [['y', 'r', 'k'], ['y', 'o', 'f'], ['i', 'i'], ['q', 't'], ['x', 'd'], ['w', 't']]
    assert candidate(['q', 'j', 'i', 'c', 'u', 'v', 'd', 'l', 'v', 'r', 'k', 'k', 'u', 'c'], 1) == [['q', 'j', 'i', 'c', 'u', 'v', 'd', 'l', 'v', 'r', 'k', 'k', 'u', 'c']]
    assert candidate(['p', 't', 'c', 'h', 'b', 'y', 'n', 'z', 'k', 'p', 'z', 'f', 'w', 'z'], 6) == [['p', 'n', 'w'], ['t', 'z', 'z'], ['c', 'k'], ['h', 'p'], ['b', 'z'], ['y', 'f']]
    assert candidate(['h', 'n', 'a', 'p', 'n', 't', 'z', 'u', 'j', 'n', 'z', 'w', 'a', 'h'], 5) == [['h', 't', 'z'], ['n', 'z', 'w'], ['a', 'u', 'a'], ['p', 'j', 'h'], ['n', 'n']]
    assert candidate(['h', 'g', 'h', 'v', 'j', 'm', 'f', 'y', 'y', 'a', 'r', 'z', 'h', 'c'], 1) == [['h', 'g', 'h', 'v', 'j', 'm', 'f', 'y', 'y', 'a', 'r', 'z', 'h', 'c']]
    assert candidate(['p', 'b', 'e', 't', 'q', 'y', 'f', 'o', 'r', 'i', 'r', 'b', 's', 'r'], 4) == [['p', 'q', 'r', 's'], ['b', 'y', 'i', 'r'], ['e', 'f', 'r'], ['t', 'o', 'b']]
    assert candidate([1, 7, 6, 6, 6, 7, 2, 13, 14, 8, 7, 15, 11, 13], 8) == [[1, 14], [7, 8], [6, 7], [6, 15], [6, 11], [7, 13], [2], [13]]
    assert candidate([2, 1, 6, 6, 3, 2, 10, 5, 6, 8, 8, 14, 15, 18], 4) == [[2, 3, 6, 15], [1, 2, 8, 18], [6, 10, 8], [6, 5, 14]]
    assert candidate([3, 2, 3, 6, 4, 11, 9, 8, 13, 9, 7, 10, 10, 9], 6) == [[3, 9, 10], [2, 8, 9], [3, 13], [6, 9], [4, 7], [11, 10]]
    assert candidate([6, 3, 7, 9, 3, 5, 8, 4, 10, 12, 12, 15, 14, 13], 4) == [[6, 3, 10, 14], [3, 5, 12, 13], [7, 8, 12], [9, 4, 15]]
    assert candidate([1, 5, 4, 5, 7, 3, 8, 8, 12, 9, 15, 9, 18, 15], 4) == [[1, 7, 12, 18], [5, 3, 9, 15], [4, 8, 15], [5, 8, 9]]
    assert candidate([4, 6, 4, 5, 9, 2, 4, 4, 12, 15, 10, 15, 16, 13], 1) == [[4, 6, 4, 5, 9, 2, 4, 4, 12, 15, 10, 15, 16, 13]]
    assert candidate([4, 5, 5, 1, 3, 9, 5, 12, 14, 13, 13, 12, 12, 16], 1) == [[4, 5, 5, 1, 3, 9, 5, 12, 14, 13, 13, 12, 12, 16]]
    assert candidate([5, 2, 2, 4, 7, 11, 3, 3, 12, 5, 13, 14, 16, 16], 3) == [[5, 4, 3, 5, 16], [2, 7, 3, 13, 16], [2, 11, 12, 14]]
    assert candidate([3, 4, 8, 6, 10, 8, 8, 8, 10, 13, 7, 17, 17, 16], 4) == [[3, 10, 10, 17], [4, 8, 13, 16], [8, 8, 7], [6, 8, 17]]
    assert candidate([1, 7, 5, 4, 2, 3, 11, 10, 6, 11, 14, 11, 8, 12], 4) == [[1, 2, 6, 8], [7, 3, 11, 12], [5, 11, 14], [4, 10, 11]]
    assert candidate([2, 1, 4, 8, 6, 1, 3, 6, 11, 15, 8, 7, 8, 10], 4) == [[2, 6, 11, 8], [1, 1, 15, 10], [4, 3, 8], [8, 6, 7]]
    assert candidate([1, 5, 8, 4, 3, 5, 9, 3, 6, 12, 8, 13, 12, 9], 8) == [[1, 6], [5, 12], [8, 8], [4, 13], [3, 12], [5, 9], [9], [3]]
    assert candidate([6, 6, 8, 5, 2, 7, 8, 13, 14, 10, 6, 9, 14, 14], 5) == [[6, 7, 6], [6, 8, 9], [8, 13, 14], [5, 14, 14], [2, 10]]
    assert candidate([3, 4, 8, 9, 6, 11, 6, 9, 6, 12, 6, 17, 18, 17], 3) == [[3, 9, 6, 12, 18], [4, 6, 9, 6, 17], [8, 11, 6, 17]]
    assert candidate([4, 5, 4, 9, 10, 6, 12, 4, 10, 9, 16, 13, 17, 10], 8) == [[4, 10], [5, 9], [4, 16], [9, 13], [10, 17], [6, 10], [12], [4]]
    assert candidate([1, 5, 5, 3, 6, 10, 3, 10, 12, 15, 12, 10, 14, 16], 2) == [[1, 5, 6, 3, 12, 12, 14], [5, 3, 10, 10, 15, 10, 16]]
    assert candidate([5, 5, 8, 7, 3, 5, 9, 9, 5, 5, 9, 12, 11, 16], 3) == [[5, 7, 9, 5, 11], [5, 3, 9, 9, 16], [8, 5, 5, 12]]
    assert candidate([6, 3, 8, 2, 6, 3, 5, 7, 5, 6, 13, 17, 14, 17], 3) == [[6, 2, 5, 6, 14], [3, 6, 7, 13, 17], [8, 3, 5, 17]]
    assert candidate([5, 4, 6, 6, 8, 3, 4, 12, 6, 15, 12, 11, 9, 17], 2) == [[5, 6, 8, 4, 6, 12, 9], [4, 6, 3, 12, 15, 11, 17]]
    assert candidate([3, 1, 3, 9, 5, 6, 6, 4, 11, 11, 10, 14, 10, 17], 7) == [[3, 4], [1, 11], [3, 11], [9, 10], [5, 14], [6, 10], [6, 17]]
    assert candidate([4, 3, 1, 3, 7, 10, 10, 5, 5, 11, 11, 14, 17, 9], 4) == [[4, 7, 5, 17], [3, 10, 11, 9], [1, 10, 11], [3, 5, 14]]
    assert candidate([2, 3, 8, 9, 4, 9, 11, 12, 11, 15, 13, 10, 11, 17], 7) == [[2, 12], [3, 11], [8, 15], [9, 13], [4, 10], [9, 11], [11, 17]]
    assert candidate([2, 5, 3, 1, 5, 8, 3, 7, 10, 5, 14, 15, 14, 11], 4) == [[2, 5, 10, 14], [5, 8, 5, 11], [3, 3, 14], [1, 7, 15]]
    assert candidate([5, 7, 6, 6, 9, 9, 4, 10, 4, 11, 12, 15, 9, 11], 6) == [[5, 4, 9], [7, 10, 11], [6, 4], [6, 11], [9, 12], [9, 15]]
    assert candidate([5, 2, 7, 6, 5, 6, 5, 6, 5, 6, 13, 17, 12, 16], 7) == [[5, 6], [2, 5], [7, 6], [6, 13], [5, 17], [6, 12], [5, 16]]
    assert candidate([5, 2, 4, 4, 1, 10, 3, 13, 11, 8, 12, 14, 9, 13], 3) == [[5, 4, 3, 8, 9], [2, 1, 13, 12, 13], [4, 10, 11, 14]]
    assert candidate([1, 4, 7, 2, 7, 8, 12, 4, 12, 5, 12, 9, 9, 16], 7) == [[1, 4], [4, 12], [7, 5], [2, 12], [7, 9], [8, 9], [12, 16]]
    assert candidate([4, 5, 7, 5, 6, 7, 9, 6, 8, 11, 6, 15, 15, 18], 6) == [[4, 9, 15], [5, 6, 18], [7, 8], [5, 11], [6, 6], [7, 15]]
    assert candidate([6, 1, 1, 9, 8, 11, 10, 5, 10, 7, 7, 9, 13, 9], 3) == [[6, 9, 10, 7, 13], [1, 8, 5, 7, 9], [1, 11, 10, 9]]
    assert candidate([3, 5, 8, 1, 7, 3, 7, 13, 10, 15, 9, 12, 12, 14], 5) == [[3, 3, 9], [5, 7, 12], [8, 13, 12], [1, 10, 14], [7, 15]]
    assert candidate([5, 5, 4, 8, 9, 9, 8, 5, 7, 13, 6, 8, 17, 19], 3) == [[5, 8, 8, 13, 17], [5, 9, 5, 6, 19], [4, 9, 7, 8]]
    assert candidate([2, 4, 6, 5, 4, 5, 5, 13, 7, 7, 9, 16, 16, 10], 7) == [[2, 13], [4, 7], [6, 7], [5, 9], [4, 16], [5, 16], [5, 10]]
    assert candidate([3, 5, 5, 1, 5, 8, 5, 12, 14, 7, 10, 15, 12, 15], 4) == [[3, 5, 14, 12], [5, 8, 7, 15], [5, 5, 10], [1, 12, 15]]
    assert candidate(['mldawzqafgqy', 'hjxingcz', 'F', 'O<@YV>', 'WUOU', 'ASTU'], 2) == [['mldawzqafgqy', 'F', 'WUOU'], ['hjxingcz', 'O<@YV>', 'ASTU']]
    assert candidate(['jxwlgjrckp', 'ygn', 'W', 'TOSJ/JB~', 'TAM', 'ZPYWLK'], 4) == [['jxwlgjrckp', 'TAM'], ['ygn', 'ZPYWLK'], ['W'], ['TOSJ/JB~']]
    assert candidate(['zzczoyjvne', 'uyy', 'B', '*>C>', 'KETDI', 'PFDYPK'], 6) == [['zzczoyjvne'], ['uyy'], ['B'], ['*>C>'], ['KETDI'], ['PFDYPK']]
    assert candidate(['pflcapycprf', 'foz', 'P', '-$%PNP:', 'KKI', 'LJUQIH'], 5) == [['pflcapycprf', 'LJUQIH'], ['foz'], ['P'], ['-$%PNP:'], ['KKI']]
    assert candidate(['aqzshftajzav', 'sqlmrk', 'U', 'OO!KZTC', 'WRBM', 'ZGT'], 4) == [['aqzshftajzav', 'WRBM'], ['sqlmrk', 'ZGT'], ['U'], ['OO!KZTC']]
    assert candidate(['xnepknc', 'yvpjhfky', 'D', 'XCHE', 'VKH', 'VYY'], 1) == [['xnepknc', 'yvpjhfky', 'D', 'XCHE', 'VKH', 'VYY']]
    assert candidate(['rlbvnzwbbwg', 'yvd', 'B', 'HF<HC', 'PMRELUQ', 'UKEAHLH'], 4) == [['rlbvnzwbbwg', 'PMRELUQ'], ['yvd', 'UKEAHLH'], ['B'], ['HF<HC']]
    assert candidate(['wom', 'odh', 'M', '_ZVM', 'ONNGKAO', 'FGOHBQPK'], 7) == [['wom'], ['odh'], ['M'], ['_ZVM'], ['ONNGKAO'], ['FGOHBQPK'], []]
    assert candidate(['hcujy', 'ftu', 'T', '<LL>KJ', 'UGDLK', 'VEC'], 7) == [['hcujy'], ['ftu'], ['T'], ['<LL>KJ'], ['UGDLK'], ['VEC'], []]
    assert candidate(['rrhhrpcssoql', 'rqfjytod', 'I', 'YA&$R', 'NYV', 'LHVZWFPJA'], 3) == [['rrhhrpcssoql', 'YA&$R'], ['rqfjytod', 'NYV'], ['I', 'LHVZWFPJA']]
    assert candidate(['vgeciikehj', 'vsxucvfb', 'H', '>UA', 'AJFSSVKI', 'JZP'], 2) == [['vgeciikehj', 'H', 'AJFSSVKI'], ['vsxucvfb', '>UA', 'JZP']]
    assert candidate(['tpimgzkzrc', 'ytm', 'Y', 'B-+-SHJ', 'PKUN', 'GQBHT'], 5) == [['tpimgzkzrc', 'GQBHT'], ['ytm'], ['Y'], ['B-+-SHJ'], ['PKUN']]
    assert candidate(['zjdsfcnfs', 'pfnuxdal', 'I', '#S>^', 'CFFWC', 'AJGBG'], 2) == [['zjdsfcnfs', 'I', 'CFFWC'], ['pfnuxdal', '#S>^', 'AJGBG']]
    assert candidate(['huyb', 'wgvyu', 'E', 'L&P', 'YEDISE', 'RUJEDJ'], 3) == [['huyb', 'L&P'], ['wgvyu', 'YEDISE'], ['E', 'RUJEDJ']]
    assert candidate(['kuk', 'tactevqo', 'L', '>RU=E', 'DBIU', 'BRZ'], 6) == [['kuk'], ['tactevqo'], ['L'], ['>RU=E'], ['DBIU'], ['BRZ']]
    assert candidate(['qxqkppyenhqc', 'kackpnmg', 'U', '^<LZ/', 'PAH', 'IXWHEGL'], 3) == [['qxqkppyenhqc', '^<LZ/'], ['kackpnmg', 'PAH'], ['U', 'IXWHEGL']]
    assert candidate(['cgk', 'uzmezww', 'P', 'UFUZNT', 'WOEPJ', 'YHEXMO'], 7) == [['cgk'], ['uzmezww'], ['P'], ['UFUZNT'], ['WOEPJ'], ['YHEXMO'], []]
    assert candidate(['sckskgqqom', 'orbqe', 'J', 'J<+&', 'XEVBTEX', 'JTR'], 2) == [['sckskgqqom', 'J', 'XEVBTEX'], ['orbqe', 'J<+&', 'JTR']]
    assert candidate(['nkndpuyc', 'ufjv', 'D', '_/QNG>-', 'SZACNRA', 'VCSB'], 1) == [['nkndpuyc', 'ufjv', 'D', '_/QNG>-', 'SZACNRA', 'VCSB']]
    assert candidate(['eiqi', 'bpvkpkm', 'U', 'P*:D|JDEE', 'FLFEQADYF', 'SKI'], 5) == [['eiqi', 'SKI'], ['bpvkpkm'], ['U'], ['P*:D|JDEE'], ['FLFEQADYF']]
    assert candidate(['uqfbqo', 'ygyykebkp', 'G', 'D_JL/', 'BBHWSSTWN', 'KSLTRM'], 3) == [['uqfbqo', 'D_JL/'], ['ygyykebkp', 'BBHWSSTWN'], ['G', 'KSLTRM']]
    assert candidate(['ptkalnuif', 'frhje', 'E', 'JCSF<:B', 'YLHFRIVGN', 'FKM'], 2) == [['ptkalnuif', 'E', 'YLHFRIVGN'], ['frhje', 'JCSF<:B', 'FKM']]
    assert candidate(['fthdke', 'vczvnb', 'Y', 'V-H^N', 'OIQB', 'QOLQYGUY'], 3) == [['fthdke', 'V-H^N'], ['vczvnb', 'OIQB'], ['Y', 'QOLQYGUY']]
    assert candidate(['ccjtgkfqti', 'xqu', 'O', 'O<@D_W', 'TEHKWQPO', 'NVRTJ'], 2) == [['ccjtgkfqti', 'O', 'TEHKWQPO'], ['xqu', 'O<@D_W', 'NVRTJ']]
    assert candidate(['kjqifx', 'gnztfgx', 'C', '<%ZWTVI', 'QHV', 'WVAXRVY'], 3) == [['kjqifx', '<%ZWTVI'], ['gnztfgx', 'QHV'], ['C', 'WVAXRVY']]
    assert candidate(['mkrzv', 'okll', 'S', 'GXU^IH=Z', 'MAERAVIBB', 'CNTHT'], 1) == [['mkrzv', 'okll', 'S', 'GXU^IH=Z', 'MAERAVIBB', 'CNTHT']]
    assert candidate(['ykqmukk', 'sproluv', 'V', 'V=R@RY$/P', 'GKDNPCP', 'IIIJSOS'], 4) == [['ykqmukk', 'GKDNPCP'], ['sproluv', 'IIIJSOS'], ['V'], ['V=R@RY$/P']]
    assert candidate(['wmly', 'pgwkis', 'U', 'D>_JRTN%', 'KDLJL', 'SOAG'], 1) == [['wmly', 'pgwkis', 'U', 'D>_JRTN%', 'KDLJL', 'SOAG']]
    assert candidate(['glnxgopgguih', 'kzm', 'B', 'M>L', 'JAWI', 'HCRHSEGZK'], 4) == [['glnxgopgguih', 'JAWI'], ['kzm', 'HCRHSEGZK'], ['B'], ['M>L']]
    assert candidate(['lwxugh', 'yhaycqrm', 'U', 'VK:', 'IRU', 'NFTDBDIBN'], 4) == [['lwxugh', 'IRU'], ['yhaycqrm', 'NFTDBDIBN'], ['U'], ['VK:']]
    assert candidate(['mjtqyin', 'xzeiwcy', 'I', '*~$~', 'YJUUHQ', 'BJOQ'], 7) == [['mjtqyin'], ['xzeiwcy'], ['I'], ['*~$~'], ['YJUUHQ'], ['BJOQ'], []]
    assert candidate(['cjxznkyts', 'tdqih', 'X', '!J+L*', 'OIR', 'THFQX'], 1) == [['cjxznkyts', 'tdqih', 'X', '!J+L*', 'OIR', 'THFQX']]
    assert candidate(['vabqxvvhbbk', 'wxd', 'C', '&JVU', 'HIABYZ', 'BBLSXUFRY'], 1) == [['vabqxvvhbbk', 'wxd', 'C', '&JVU', 'HIABYZ', 'BBLSXUFRY']]

if __name__ == '__main__':
    check(list_split)