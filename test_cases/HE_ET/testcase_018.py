from case_HE_018 import how_many_times


def check(candidate):
    assert candidate('nvdmrufrqwdqnn', 'n') == 3
    assert candidate('qkbdoiyfy', 'k') == 1
    assert candidate('fmrlzbsunvxw', 'fm') == 1
    assert candidate('be', 'b') == 1
    assert candidate('zjisbzekeudl', 'zj') == 1
    assert candidate('anfovmji', 'a') == 1
    assert candidate('eeq', 'eq') == 1
    assert candidate('qboo', 'qb') == 1
    assert candidate('jzhmab vb', 'j') == 1
    assert candidate('pwu', 'w') == 1
    assert candidate('vrt', 'vr') == 1
    assert candidate('nujl', 'u') == 1
    assert candidate('otffpnivuj', 't') == 1
    assert candidate('xalqwccwlzx', 'a') == 1
    assert candidate('rbomgmes', 'rb') == 1
    assert candidate('u', 'u') == 1
    assert candidate('nszheeqkvhn', 'ns') == 1
    assert candidate('nk', 'k') == 1
    assert candidate('jrvzqqmmft', 'rv') == 1
    assert candidate('z', '') == 2
    assert candidate('nbhcp', 'bh') == 1
    assert candidate('ktxmngrvtzyagna', 'tx') == 1
    assert candidate('jslhdijlb', 'j') == 2
    assert candidate('sfz', 'fz') == 1
    assert candidate('cnsosehe', 'cn') == 1
    assert candidate('llfcwot', 'lf') == 1
    assert candidate('eqnkivb', 'e') == 1
    assert candidate('caicghhyug', 'ai') == 1
    assert candidate('iu', 'i') == 1
    assert candidate('ugkfkyg', 'ug') == 1
    assert candidate('je', 'e') == 1
    assert candidate('fhkoyhaus', 'h') == 2
    assert candidate('icfpyzle', 'c') == 1
    assert candidate('whizuczp', 'hi') == 1
    assert candidate('l', '') == 2
    assert candidate('tlt', 'l') == 1
    assert candidate('bb ', 'b') == 2
    assert candidate('vjxplzti', 'jx') == 1
    assert candidate('ivtarxrlxdy', 'vt') == 1
    assert candidate('xyxyxyx', 'x') == 4
    assert candidate('syolthqzdqe', 'sy') == 1
    assert candidate('t a', 't') == 1
    assert candidate('uocfpojadumagm', 'u') == 2
    assert candidate('ceakek', 'e') == 2
    assert candidate('uxw', 'u') == 1
    assert candidate('mhf', 'mh') == 1
    assert candidate('z', 'z') == 1
    assert candidate('lqzvrsvhs', 'q') == 1
    assert candidate('zfkihkvbqgxoyqa', 'z') == 1
    assert candidate('clzgocfvbuefacz', 'c') == 3
    assert candidate('bfnzwslcalkmsx', 'b') == 1
    assert candidate('gat', 'a') == 1
    assert candidate('qwalaa', 'qw') == 1
    assert candidate('john doe', 'john') == 1
    assert candidate('rcd', 'r') == 1
    assert candidate('azhzsokbfol', 'z') == 2
    assert candidate('gmjlmoi', 'mj') == 1
    assert candidate('aw', 'aw') == 1
    assert candidate('yhiofgbhza', 'hi') == 1
    assert candidate('k', 'k') == 1
    assert candidate('wfxkmyyktkkl', 'fx') == 1
    assert candidate('vrx', 'v') == 1
    assert candidate('uciilfjx', 'ci') == 1
    assert candidate('pvgwfhuopwremt', 'pv') == 1
    assert candidate('hrc', 'h') == 1
    assert candidate('aakzdpfjy', 'a') == 2
    assert candidate('unttpexxmrb', 'n') == 1
    assert candidate('ofbjvtsddgre', 'f') == 1
    assert candidate('kqd', 'q') == 1
    assert candidate('qwwg', 'q') == 1
    assert candidate('eyeamwnvphy', 'e') == 2
    assert candidate('mmegmdpv', 'm') == 3
    assert candidate('rmklhebu', 'r') == 1
    assert candidate(' dnddh', ' ') == 1
    assert candidate('aoi', 'oi') == 1
    assert candidate('yhk', 'h') == 1
    assert candidate('g', '') == 2
    assert candidate('hoviwyeolsvtwx', 'ho') == 1
    assert candidate('pdvxbxv', 'p') == 1
    assert candidate('vq', 'v') == 1
    assert candidate('ujhki', 'j') == 1
    assert candidate('stng', 'tn') == 1
    assert candidate('rpwwqfxiizm', 'p') == 1
    assert candidate('sidvztfhtd', 'si') == 1
    assert candidate('xugjvtx ', 'u') == 1
    assert candidate('hhuscpoywkov', 'hu') == 1
    assert candidate('jmgucrpprt', 'jm') == 1
    assert candidate('wnvgsxj', 'n') == 1
    assert candidate('jdvktqcenyil', 'j') == 1
    assert candidate('kxit', 'xi') == 1
    assert candidate('scab dszdeft', 's') == 2
    assert candidate('evjis', 'ev') == 1
    assert candidate('', 'x') == 0
    assert candidate('qcqg', 'qc') == 1
    assert candidate('rvzgt', 'vz') == 1
    assert candidate('cacacacac', 'cac') == 4
    assert candidate('kk', 'k') == 2
    assert candidate('tsqxytjiivrz', 'ts') == 1
    assert candidate('at', 't') == 1
    assert candidate('wkojkobxgk', 'k') == 3
    assert candidate('hmc', 'mc') == 1
    assert candidate('dn', 'n') == 1
    assert candidate('ucqgonvrjdrkq', 'uc') == 1
    assert candidate('srzn', 'r') == 1
    assert candidate('ijy', 'i') == 1
    assert candidate('x', '') == 2
    assert candidate(' ndohd', ' ') == 1
    assert candidate('avawcwvx', 'av') == 1
    assert candidate('vyemhdw', 'ye') == 1
    assert candidate('up', 'up') == 1
    assert candidate('yvg', 'vg') == 1
    assert candidate('nkwawgxmpgpdbmk', 'kw') == 1
    assert candidate('upvl', 'up') == 1
    assert candidate('nnkggonzeqndpfp', 'nk') == 1
    assert candidate('mof', 'm') == 1
    assert candidate('ke', 'ke') == 1
    assert candidate('spedonqop', 'sp') == 1
    assert candidate('aeapeggccxsumz', 'ea') == 1
    assert candidate('c', 'c') == 1
    assert candidate('mch', 'ch') == 1
    assert candidate('mk', 'k') == 1
    assert candidate('mkrn yvnza', 'k') == 1
    assert candidate('wqgmsdi', 'qg') == 1
    assert candidate('gykecbjj', 'g') == 1
    assert candidate('yiklalp', 'y') == 1
    assert candidate('ayz', 'yz') == 1
    assert candidate('vjvezdoknedfm', 'v') == 2
    assert candidate('qhlqxeamji', 'q') == 2
    assert candidate('gkfz', 'g') == 1
    assert candidate('skvkibi', 'kv') == 1
    assert candidate('zxcpshdh', 'zx') == 1
    assert candidate('xrawl', 'x') == 1

if __name__ == '__main__':
    check(how_many_times)