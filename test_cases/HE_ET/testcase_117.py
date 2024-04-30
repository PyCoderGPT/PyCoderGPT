from case_HE_117 import select_words


def check(candidate):
    assert candidate('eg aqk', 2) == ['aqk']
    assert candidate('eoDDPoNuKJnQIcLHcFK', 14) == ['eoDDPoNuKJnQIcLHcFK']
    assert candidate('syk', 6) == []
    assert candidate('gw', 9) == []
    assert candidate('ZpJhNYG', 7) == ['ZpJhNYG']
    assert candidate("Mary had a little lamb", 4) == ["little"], "First test error: " + str(candidate("Mary had a little lamb", 4))
    assert candidate('ILkvuFIrW jXOOGXgdSWtd', 10) == ['jXOOGXgdSWtd']
    assert candidate('uwnynnkeh', 7) == ['uwnynnkeh']
    assert candidate('zGMhBC', 6) == ['zGMhBC']
    assert candidate('kfohjsjunakqmmsx', 1) == []
    assert candidate('KbpFfWgXZoVjXV', 1) == []
    assert candidate('GeLxcZJyRwUsQKBQkanf', 2) == []
    assert candidate('kg', 1) == []
    assert candidate("simple white space", 2) == [], "Third test error: " + str(candidate("simple white space", 2))
    assert candidate('xrbpxpncgqufqkq', 6) == []
    assert candidate('sqgikswgssxsbwkl', 7) == []
    assert candidate('kumJjGm AFFO', 6) == ['kumJjGm']
    assert candidate('iJxMQLiIZ', 6) == ['iJxMQLiIZ']
    assert candidate('uwebicR RgZrAiEnPkq', 4) == ['uwebicR']
    assert candidate('bnXA AjPVh', 5) == []
    assert candidate('omnivbqgmavyqdgqssas', 6) == []
    assert candidate('fmjizkhknnihqioic', 4) == []
    assert candidate('lINKPOlFIImtg', 3) == []
    assert candidate('nPxmyTd', 7) == ['nPxmyTd']
    assert candidate('yCRgLVwagpjADSN MUkt', 3) == ['MUkt']
    assert candidate('mehochzpausf', 2) == []
    assert candidate('TcXKTNbOnjCJLzWhlNELbGPc', 22) == ['TcXKTNbOnjCJLzWhlNELbGPc']
    assert candidate('EGiDfM', 1) == []
    assert candidate('mc', 7) == []
    assert candidate('wzx', 5) == []
    assert candidate('hgwhtsvqihhm', 11) == ['hgwhtsvqihhm']
    assert candidate('xwkxcjffocow', 5) == []
    assert candidate('dl', 5) == []
    assert candidate('UIOcsXneOjxMkRLvRLSDTV', 4) == []
    assert candidate('ABIStgq', 5) == ['ABIStgq']
    assert candidate('nb', 2) == ['nb']
    assert candidate('ny', 2) == ['ny']
    assert candidate('HWCLBC', 6) == ['HWCLBC']
    assert candidate('uuh', 6) == []
    assert candidate('uoubngttn', 3) == []
    assert candidate('g', 5) == []
    assert candidate('ffqkhIIChADuzMQIrcFek', 15) == ['ffqkhIIChADuzMQIrcFek']
    assert candidate('CbxmADxVZtHArXzwNxnuvda', 19) == ['CbxmADxVZtHArXzwNxnuvda']
    assert candidate('aztxoxesjkzqebhrfzw', 3) == []
    assert candidate('sqdcPgSPeHfNdISspJa', 16) == ['sqdcPgSPeHfNdISspJa']
    assert candidate('zdXc AqKVMGYLrZMPSz', 4) == ['zdXc']
    assert candidate('tJzO PnCT', 3) == ['tJzO']
    assert candidate('jizrraatfiyetneqergnnbfn', 3) == []
    assert candidate('qhwubvrfmwy', 2) == []
    assert candidate('dzrmzilzoxn l', 9) == ['dzrmzilzoxn']
    assert candidate('ZZcAZzrjekxbP tPNuYXLnOLVv', 10) == ['tPNuYXLnOLVv']
    assert candidate('JtsHoq wxvsLQqBXkNpmCTzBWTX', 1) == []
    assert candidate('aecdOIhfIbEBTOfoKnT', 1) == []
    assert candidate('gLFCSPHHP', 9) == ['gLFCSPHHP']
    assert candidate('r s rhhipmt', 6) == ['rhhipmt']
    assert candidate('aDqyhePv', 6) == ['aDqyhePv']
    assert candidate('tTxmhPuW', 7) == ['tTxmhPuW']
    assert candidate('gkaioVYtEtMLxrVq JIIwPCZW', 6) == ['JIIwPCZW']
    assert candidate('aru', 5) == []
    assert candidate('ySRkkHkfcvgHqOGVfaDTTRf', 1) == []
    assert candidate('SNeiILCez', 4) == []
    assert candidate('xzzxdz lkmvrvizpz z', 6) == ['xzzxdz']
    assert candidate('ySmjGAg', 6) == ['ySmjGAg']
    assert candidate('bRJRZC', 3) == []
    assert candidate('u', 1) == []
    assert candidate('djucfuuizrjfvuzzo', 4) == []
    assert candidate('dvYLMt', 6) == ['dvYLMt']
    assert candidate('xqvooek icmfdiysshehnyqx', 7) == []
    assert candidate('zIdcqeCrTYiDGGjYFC', 15) == ['zIdcqeCrTYiDGGjYFC']
    assert candidate('yp', 6) == []
    assert candidate('v', 4) == []
    assert candidate("a b c d e f", 1) == ["b", "c", "d", "f"], "2nd edge test error: " + str(candidate("a b c d e f", 1))
    assert candidate('afrrguc', 5) == ['afrrguc']
    assert candidate('KBDaAtwgkSQhbMcvLn', 16) == ['KBDaAtwgkSQhbMcvLn']
    assert candidate('WvvnDCbdBejJOXxALMQUP', 17) == ['WvvnDCbdBejJOXxALMQUP']
    assert candidate('IXWOrAdrmmcWXqngDkiVFKXaAWf', 4) == []
    assert candidate('nh vu lcakrb', 1) == ['vu']
    assert candidate('QOBKeojoDQGT jIZmKXyPl', 8) == ['QOBKeojoDQGT', 'jIZmKXyPl']
    assert candidate("Uncle sam", 3) == ["Uncle"], "Fifth test error: " + str(candidate("Uncle sam", 3))


    # Check some edge cases that are easy to work out by hand.
    assert candidate('zE sivlrNrHFgwiokUjTMdndl', 5) == []
    assert candidate('svMzfBuoveQXEPPIVV', 13) == ['svMzfBuoveQXEPPIVV']
    assert candidate('MjRnAErHPguQC', 1) == []
    assert candidate('tmchxmttrgfdanq', 3) == []
    assert candidate('jezkeorvxnruwhhwzxm', 7) == []
    assert candidate('caurfxlpkygqxoknil', 4) == []
    assert candidate('RBAY  hmsXCkloLHYheRDQL', 3) == ['RBAY']
    assert candidate('prFfoYsafgMfGYYGjsiqTXwL', 21) == ['prFfoYsafgMfGYYGjsiqTXwL']
    assert candidate('NSjIbZV', 2) == []
    assert candidate('rPKhzIot', 6) == ['rPKhzIot']
    assert candidate('ASDVzOVVDEdj J', 1) == ['J']
    assert candidate('oKNamFuRSJcV', 9) == ['oKNamFuRSJcV']
    assert candidate(' siweqafqot', 5) == []
    assert candidate('xdQgsAHI', 5) == []
    assert candidate('epzbicjvjcbxmxgfityzzv', 5) == []
    assert candidate('GFNxLvGHJnNx', 12) == ['GFNxLvGHJnNx']
    assert candidate('hguHoJGaaNwX', 3) == []
    assert candidate('cnxdrucrydrcyol', 13) == ['cnxdrucrydrcyol']
    assert candidate('choounwx', 5) == ['choounwx']
    assert candidate('yue', 2) == []
    assert candidate('DDdrgPy', 4) == []
    assert candidate('c zsYpMPdmr', 9) == ['zsYpMPdmr']
    assert candidate("", 4) == [], "1st edge test error: " + str(candidate("", 4))
    assert candidate('pzBxlNfcXEsOQzL', 13) == ['pzBxlNfcXEsOQzL']
    assert candidate('pWqNDaO zJwlHsqqEYCdDEZtNiL', 3) == []
    assert candidate("Mary had a little lamb", 3) == ["Mary", "lamb"], "Second test error: " + str(candidate("Mary had a little lamb", 3))
    assert candidate('Reg MuZcF', 4) == ['MuZcF']
    assert candidate('lxQnxHVtrUGfoufkLPXu', 16) == ['lxQnxHVtrUGfoufkLPXu']
    assert candidate('sl', 6) == []
    assert candidate('IFKqNq ', 5) == ['IFKqNq']
    assert candidate('lfspeijyudniowk', 1) == []
    assert candidate('kogmgdnk', 7) == ['kogmgdnk']
    assert candidate('nnchatjackywoavfwfps', 5) == []
    assert candidate('d', 2) == []
    assert candidate('fjnjvfo aqgasitdiyalwv', 1) == []
    assert candidate('IGEmiHg ne YIhrNkjpGfOObqJ', 1) == ['ne']
    assert candidate("Hello world", 4) == ["world"], "Fourth test error: " + str(candidate("Hello world", 4))
    assert candidate('jopfxbbvlslmluypcdt', 3) == []
    assert candidate('AWrNREXAqD WePeTbIPTS', 4) == []
    assert candidate('OWzTDtbfTAEOBLuZPqFdnmnSG', 5) == []
    assert candidate('TQzrMVZMngInaglSfwvrbAh', 20) == ['TQzrMVZMngInaglSfwvrbAh']
    assert candidate('etdrxwybqi', 1) == []
    assert candidate('aVCSziOkLCLGizHcmC', 2) == []
    assert candidate('sYlP HUxjpHVfeWBNAvXo', 4) == ['sYlP']
    assert candidate('txXxge', 4) == []
    assert candidate('kcpieuVjAOaxdpB', 4) == []
    assert candidate('oh', 8) == []
    assert candidate('bgosvLxdWAWUtCxHgfPugDKQfel', 5) == []
    assert candidate('fT LxYLtzO', 6) == ['LxYLtzO']
    assert candidate('eywh qxreeexrrhyovpwl', 7) == []
    assert candidate('JfStfbdqmygzcqzJvvbivZfDbwg', 26) == ['JfStfbdqmygzcqzJvvbivZfDbwg']
    assert candidate('asfwxvbzdfsrymc', 3) == []
    assert candidate('nBmjWxiPV', 3) == []
    assert candidate('lDqgwtu rM tfTmeKEd', 2) == ['rM']

if __name__ == '__main__':
    check(select_words)