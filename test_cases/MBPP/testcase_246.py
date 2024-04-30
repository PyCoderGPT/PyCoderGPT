from case_MBPP_246 import remove_uppercase


def check(candidate):
    assert candidate('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    assert candidate('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
    assert candidate('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'

if __name__ == '__main__':
    check(remove_uppercase)