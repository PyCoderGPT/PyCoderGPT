from case_MBPP_164 import max_val


def check(candidate):
    assert candidate(['Python', 3, 2, 4, 5, 'version'])==5
    assert candidate(['Python', 15, 20, 25])==25
    assert candidate(['Python', 30, 20, 40, 50, 'version'])==50
    assert candidate(['UHl', 1, 2, 8, 4, 'kwlksrdf']) == 8
    assert candidate(['FakkAzq', 8, 3, 1, 5, 'hwpylqf']) == 8
    assert candidate(['RFWzQwBbr', 5, 7, 8, 3, 'hbycc']) == 8
    assert candidate(['BVpduSMZGh', 2, 3, 7, 1, 'vhpremob']) == 7
    assert candidate(['uzpYhYJ', 6, 7, 8, 2, 'tytl']) == 8
    assert candidate(['SkZzNsdg', 8, 7, 7, 9, 'shkehkv']) == 9
    assert candidate(['QlBHC', 2, 4, 4, 7, 'ewsk']) == 7
    assert candidate(['mzsYnOe', 3, 1, 3, 2, 'jykjvlyuem']) == 3
    assert candidate(['vOWfHr', 5, 6, 6, 7, 'ilr']) == 7
    assert candidate(['TNhxxpSc', 3, 3, 9, 4, 'nlwohzww']) == 9
    assert candidate(['IUP', 8, 4, 8, 6, 'chv']) == 8
    assert candidate(['dyRoCbMN', 2, 7, 9, 6, 'nwyhwvtuza']) == 9
    assert candidate(['qmPHVsqvj', 5, 1, 1, 9, 'iks']) == 9
    assert candidate(['yxHRU', 5, 3, 9, 8, 'hlegopyfgys']) == 9
    assert candidate(['sTg', 1, 6, 2, 4, 'frtkxhris']) == 6
    assert candidate(['cuoAgfmG', 4, 3, 6, 6, 'iooprjettet']) == 6
    assert candidate(['CqxrCJ', 1, 2, 6, 1, 'lnemcvynvbg']) == 6
    assert candidate(['ozugudjtM', 7, 4, 8, 10, 'vle']) == 10
    assert candidate(['fmDshRLT', 2, 2, 6, 4, 'pvhhww']) == 6
    assert candidate(['ACXAORHev', 3, 7, 3, 2, 'fhob']) == 7
    assert candidate(['yrTcb', 7, 7, 4, 3, 'nbmrfe']) == 7
    assert candidate(['rNJrEkjs', 6, 4, 2, 6, 'ojvtmn']) == 6
    assert candidate(['cDDHoh', 4, 1, 8, 1, 'hprlc']) == 8
    assert candidate(['LBLb', 3, 1, 2, 3, 'pabxsft']) == 3
    assert candidate(['BbCM', 1, 6, 2, 5, 'hwjjjdaee']) == 6
    assert candidate(['CRIyVrQaP', 5, 2, 5, 7, 'mcjl']) == 7
    assert candidate(['lasOvOY', 6, 4, 3, 7, 'yanaunvf']) == 7
    assert candidate(['zJZEpSS', 5, 5, 1, 3, 'jxfyxiubwq']) == 5
    assert candidate(['tHw', 3, 2, 5, 3, 'aafzjz']) == 5
    assert candidate(['OMmNk', 1, 4, 1, 4, 'dpdkupohpah']) == 4
    assert candidate(['CubHZX', 1, 5, 7, 8, 'rigcoeajroh']) == 8
    assert candidate(['oSsMW', 1, 4, 9, 9, 'wufgfiajeswa']) == 9
    assert candidate(['yhXi', 1, 4, 4, 10, 'rnjioqfuzamn']) == 10
    assert candidate(['tIUcbsoUBNn', 17, 25, 29]) == 29
    assert candidate(['hgARn', 11, 17, 21]) == 21
    assert candidate(['Byxw', 12, 24, 23]) == 24
    assert candidate(['JIdU', 19, 25, 29]) == 29
    assert candidate(['xwI', 10, 23, 29]) == 29
    assert candidate(['iVHgkWnKtg', 20, 20, 26]) == 26
    assert candidate(['qhKpu', 17, 19, 30]) == 30
    assert candidate(['JyN', 13, 20, 29]) == 29
    assert candidate(['GYRp', 14, 25, 29]) == 29
    assert candidate(['HBlDvAICE', 16, 16, 22]) == 22
    assert candidate(['seE', 14, 19, 22]) == 22
    assert candidate(['faUY', 16, 23, 30]) == 30
    assert candidate(['XiSW', 12, 15, 22]) == 22
    assert candidate(['YgYCLpEsTH', 13, 17, 24]) == 24
    assert candidate(['pMPqY', 11, 23, 24]) == 24
    assert candidate(['FXFNMZW', 16, 25, 23]) == 25
    assert candidate(['ggSThCaFSv', 14, 18, 21]) == 21
    assert candidate(['jAKAHEM', 16, 18, 28]) == 28
    assert candidate(['bmuNbouvZA', 19, 23, 21]) == 23
    assert candidate(['fAGhMlINl', 12, 15, 20]) == 20
    assert candidate(['OunIvskwA', 19, 20, 28]) == 28
    assert candidate(['tqfpaZP', 15, 25, 25]) == 25
    assert candidate(['AqzZJyK', 11, 17, 20]) == 20
    assert candidate(['oJiOCuXJqfE', 18, 25, 26]) == 26
    assert candidate(['DyudAhEQz', 10, 18, 20]) == 20
    assert candidate(['bPHvcBsHho', 20, 18, 25]) == 25
    assert candidate(['NSKMT', 19, 23, 23]) == 23
    assert candidate(['qCiXxZDwsymA', 16, 25, 30]) == 30
    assert candidate(['ckrOIWEMUE', 13, 18, 27]) == 27
    assert candidate(['aHEH', 20, 19, 29]) == 29
    assert candidate(['uFmdi', 11, 25, 20]) == 25
    assert candidate(['GXS', 19, 24, 21]) == 24
    assert candidate(['CbjmshEbS', 20, 18, 27]) == 27
    assert candidate(['QBeXGFCFWE', 27, 15, 45, 55, 'xzlgirz']) == 55
    assert candidate(['llcMbkNzSW', 32, 20, 37, 49, 'ddzpwgtp']) == 49
    assert candidate(['DTeHrszw', 31, 20, 39, 50, 'bksdcnzirn']) == 50
    assert candidate(['UlAdwSTUEhy', 34, 15, 42, 51, 'wajewzpnrt']) == 51
    assert candidate(['DuvKLdbnNeiA', 33, 20, 37, 55, 'jwfnrfcwjpjo']) == 55
    assert candidate(['umAvjcMCcq', 35, 16, 39, 49, 'xfhxlfu']) == 49
    assert candidate(['vwQjUWLD', 34, 22, 38, 51, 'aoxpsr']) == 51
    assert candidate(['FcZKqLGSiR', 28, 21, 43, 45, 'atktceh']) == 45
    assert candidate(['nAHlhcrS', 35, 17, 41, 53, 'fnoetfbogr']) == 53
    assert candidate(['QAzBKVvnDs', 32, 17, 36, 53, 'wjdvxcl']) == 53
    assert candidate(['MmjoE', 28, 15, 39, 53, 'csgdolo']) == 53
    assert candidate(['odNxQL', 34, 23, 40, 48, 'umwrkyoctu']) == 48
    assert candidate(['cBEsnJL', 35, 20, 44, 51, 'weunhadfz']) == 51
    assert candidate(['AbfAxymrg', 34, 17, 36, 53, 'plzhay']) == 53
    assert candidate(['NNZY', 26, 22, 45, 51, 'oeo']) == 51
    assert candidate(['yyosG', 25, 21, 36, 51, 'rknhctix']) == 51
    assert candidate(['pCoxJkhsZrlj', 30, 21, 36, 55, 'yeb']) == 55
    assert candidate(['gXeZltnwwsJd', 34, 25, 38, 52, 'zbiml']) == 52
    assert candidate(['ScvNcxeljW', 32, 17, 39, 53, 'hnqfbnskgir']) == 53
    assert candidate(['YMKonclVM', 31, 25, 39, 50, 'krgjk']) == 50
    assert candidate(['kTCaaC', 29, 24, 35, 54, 'tabjmrrzkys']) == 54
    assert candidate(['RllwtviqzZ', 31, 24, 42, 51, 'btfljhn']) == 51
    assert candidate(['EuHWJBf', 30, 18, 37, 48, 'apwv']) == 48
    assert candidate(['UEtKxJJ', 29, 24, 36, 46, 'wtitxtevah']) == 46
    assert candidate(['clpAaAbyehbO', 30, 16, 39, 55, 'kymiuwlwsrp']) == 55
    assert candidate(['KcSskxXx', 33, 21, 42, 50, 'wzmcroorljns']) == 50
    assert candidate(['IAjeiGy', 35, 16, 42, 46, 'yjxukbmx']) == 46
    assert candidate(['zDkREPWyF', 27, 22, 36, 46, 'hwiayrxzhrcd']) == 46
    assert candidate(['UpyEsjJFRSl', 30, 17, 39, 49, 'blo']) == 49
    assert candidate(['QPHZ', 28, 24, 41, 46, 'zloenxoskj']) == 46
    assert candidate(['lXpzVktZQ', 25, 16, 44, 46, 'qpluyq']) == 46
    assert candidate(['wwfqwmjswzB', 27, 22, 43, 51, 'vbokpy']) == 51
    assert candidate(['WUfrP', 28, 15, 39, 49, 'sge']) == 49

if __name__ == '__main__':
    check(max_val)