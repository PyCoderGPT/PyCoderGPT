from case_MBPP_170 import dict_depth


def check(candidate):
    assert candidate({'a':1, 'b': {'c': {'d': {}}}})==4
    assert candidate({'a':1, 'b': {'c':'python'}})==2
    assert candidate({1: 'Sun', 2: {3: {4:'Mon'}}})==3
    assert candidate({'h': 1, 'i': {'d': {'m': {}}}}) == 4
    assert candidate({'h': 4, 'n': {'h': {'a': {}}}}) == 4
    assert candidate({'v': 4, 'a': {'m': {'i': {}}}}) == 4
    assert candidate({'a': 1, 'f': {'w': {'h': {}}}}) == 4
    assert candidate({'t': 6, 'q': {'l': {'m': {}}}}) == 4
    assert candidate({'b': 6, 'x': {'d': {'s': {}}}}) == 4
    assert candidate({'c': 3, 'l': {'o': {'e': {}}}}) == 4
    assert candidate({'e': 1, 'b': {'p': {'d': {}}}}) == 4
    assert candidate({'o': 2, 'p': {'a': {'e': {}}}}) == 4
    assert candidate({'q': {'g': {'v': {}}}}) == 4
    assert candidate({'q': 3, 'y': {'h': {'i': {}}}}) == 4
    assert candidate({'h': 2, 'o': {'j': {'w': {}}}}) == 4
    assert candidate({'w': 4, 'l': {'n': {'q': {}}}}) == 4
    assert candidate({'j': 4, 'n': {'j': {'d': {}}}}) == 4
    assert candidate({'m': 2, 's': {'m': {'k': {}}}}) == 4
    assert candidate({'f': 1, 'j': {'v': {'p': {}}}}) == 4
    assert candidate({'f': 2, 'u': {'x': {'f': {}}}}) == 4
    assert candidate({'u': 2, 'q': {'n': {'a': {}}}}) == 4
    assert candidate({'t': 1, 'h': {'z': {'p': {}}}}) == 4
    assert candidate({'q': 3, 'n': {'y': {'w': {}}}}) == 4
    assert candidate({'q': 2, 'p': {'q': {'k': {}}}}) == 4
    assert candidate({'e': 2, 'l': {'g': {'w': {}}}}) == 4
    assert candidate({'y': 4, 'r': {'u': {'b': {}}}}) == 4
    assert candidate({'z': 4, 'c': {'r': {'m': {}}}}) == 4
    assert candidate({'m': 6, 'g': {'g': {'k': {}}}}) == 4
    assert candidate({'e': 1, 'i': {'n': {'q': {}}}}) == 4
    assert candidate({'z': 2, 'p': {'s': {'n': {}}}}) == 4
    assert candidate({'d': 6, 'f': {'g': {'f': {}}}}) == 4
    assert candidate({'y': 6, 'n': {'w': {'y': {}}}}) == 4
    assert candidate({'a': 3, 'g': {'y': {'s': {}}}}) == 4
    assert candidate({'u': 4, 'f': {'a': {'y': {}}}}) == 4
    assert candidate({'p': 6, 'o': {'u': {'y': {}}}}) == 4
    assert candidate({'n': 3, 'l': {'d': {'p': {}}}}) == 4
    assert candidate({'q': 3, 'x': {'c': 'cgru'}}) == 2
    assert candidate({'f': 3, 'x': {'v': 'adw'}}) == 2
    assert candidate({'t': {'x': 'tmev'}}) == 2
    assert candidate({'k': 5, 'r': {'r': 'zjuqacuwpypo'}}) == 2
    assert candidate({'e': 3, 'c': {'r': 'yqdrqxi'}}) == 2
    assert candidate({'t': 5, 'q': {'n': 'svn'}}) == 2
    assert candidate({'y': {'z': 'zwuq'}}) == 2
    assert candidate({'g': 4, 'z': {'y': 'vbwkuvnm'}}) == 2
    assert candidate({'s': 3, 'x': {'j': 'fztjekk'}}) == 2
    assert candidate({'l': 2, 'x': {'z': 'cyqbtbq'}}) == 2
    assert candidate({'p': 2, 'c': {'u': 'bytnoprdrac'}}) == 2
    assert candidate({'w': 4, 'j': {'h': 'oekpbkujs'}}) == 2
    assert candidate({'y': 4, 'l': {'e': 'bocnr'}}) == 2
    assert candidate({'y': 4, 'i': {'r': 'ydsns'}}) == 2
    assert candidate({'c': 2, 'x': {'l': 'npjzmwbczca'}}) == 2
    assert candidate({'b': 5, 'w': {'c': 'dfgukexilm'}}) == 2
    assert candidate({'c': {'d': 'mtbx'}}) == 2
    assert candidate({'x': 3, 'g': {'a': 'zfuvu'}}) == 2
    assert candidate({'k': 1, 'h': {'j': 'zqalgwlcuxyx'}}) == 2
    assert candidate({'m': 3, 'z': {'g': 'shbwwqulp'}}) == 2
    assert candidate({'i': 4, 'u': {'j': 'ktrnondywdh'}}) == 2
    assert candidate({'y': 4, 'l': {'x': 'jgvvuq'}}) == 2
    assert candidate({'f': 5, 's': {'g': 'vhrfvvcqcknf'}}) == 2
    assert candidate({'z': 6, 'f': {'l': 'fjzbsjpgecw'}}) == 2
    assert candidate({'m': 1, 'h': {'p': 'ekqo'}}) == 2
    assert candidate({'i': 3, 'e': {'g': 'xloseextqnr'}}) == 2
    assert candidate({'i': 2, 'j': {'a': 'rihuosp'}}) == 2
    assert candidate({'x': 2, 'u': {'t': 'jdsmtco'}}) == 2
    assert candidate({'r': 3, 'd': {'z': 'zbsiepfwcagj'}}) == 2
    assert candidate({'g': 4, 'm': {'b': 'xasvdu'}}) == 2
    assert candidate({'t': 6, 'g': {'d': 'atvszy'}}) == 2
    assert candidate({'n': 6, 'f': {'s': 'vpgznazavxow'}}) == 2
    assert candidate({'x': 4, 'q': {'d': 'zuszjhfe'}}) == 2
    assert candidate({4: 'BFlZFvDfv', 1: {1: {4: 'ozU'}}}) == 3
    assert candidate({1: 'CSd', 5: {8: {5: 'klesvkv'}}}) == 3
    assert candidate({6: 'auMlicwu', 2: {5: {1: 'mBtm'}}}) == 3
    assert candidate({2: {7: {7: 'Xlfq'}}}) == 3
    assert candidate({3: 'Jpasq', 6: {6: {5: 'ihfkhx'}}}) == 3
    assert candidate({6: {7: {9: 'pCr'}}}) == 3
    assert candidate({1: 'mdEhRWemo', 7: {5: {7: 'OPSs'}}}) == 3
    assert candidate({1: 'omV', 4: {8: {3: 'CmOyctkXy'}}}) == 3
    assert candidate({5: 'dGOSEmjD', 1: {3: {8: 'pSPDlSS'}}}) == 3
    assert candidate({1: {3: {1: 'qAp'}}}) == 3
    assert candidate({4: 'SvCBEG', 6: {2: {1: 'nqdnpktyZ'}}}) == 3
    assert candidate({4: 'wQn', 6: {6: {2: 'eNlOxXPFm'}}}) == 3
    assert candidate({3: 'xKpOhcQ', 6: {3: {6: 'jeUDzxpSV'}}}) == 3
    assert candidate({5: {7: {2: 'TTOcfxc'}}}) == 3
    assert candidate({1: 'BLCZOmSnr', 4: {4: {5: 'TjYtXtFXq'}}}) == 3
    assert candidate({3: {6: {7: 'Ktuow'}}}) == 3
    assert candidate({2: 'qgMZavQg', 5: {8: {9: 'CFoUM'}}}) == 3
    assert candidate({6: {1: {4: 'rECiF'}}}) == 3
    assert candidate({3: 'jgbcR', 1: {8: {5: 'LSLeDhYC'}}}) == 3
    assert candidate({2: 'ELrGJ', 6: {8: {7: 'XoU'}}}) == 3
    assert candidate({5: 'UkDT', 6: {8: {9: 'mRuFMnTEV'}}}) == 3
    assert candidate({1: 'GKvoCA', 6: {3: {5: 'Dpy'}}}) == 3
    assert candidate({2: 'YNXLJgzEJ', 7: {4: {9: 'TRS'}}}) == 3
    assert candidate({2: 'NycjnF', 1: {1: {3: 'MoIm'}}}) == 3
    assert candidate({4: 'HcHV', 7: {7: {4: 'JWR'}}}) == 3
    assert candidate({3: {7: {2: 'TxQcdU'}}}) == 3
    assert candidate({4: {3: {6: 'Lpc'}}}) == 3
    assert candidate({5: 'ASRpdRrEK', 4: {2: {2: 'cTDMxM'}}}) == 3
    assert candidate({3: 'iiwzJ', 5: {7: {6: 'fQGqk'}}}) == 3
    assert candidate({1: 'JcdEppwy', 2: {1: {4: 'LUBzgeCnp'}}}) == 3
    assert candidate({1: 'StoVGm', 2: {5: {9: 'uCcLmc'}}}) == 3
    assert candidate({6: 'XlGSCVR', 1: {2: {4: 'rHORFRde'}}}) == 3
    assert candidate({3: 'BVHVlGdwP', 2: {6: {4: 'NItuDFc'}}}) == 3

if __name__ == '__main__':
    check(dict_depth)