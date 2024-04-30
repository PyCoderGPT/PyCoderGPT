from case_HE_098 import count_upper


def check(candidate):
    assert candidate("aBEdEI") == 2
    assert candidate("aBIOEf") == 2
    assert candidate("aEcdefg") == 0
    assert candidate("dBOE") == 1
    assert candidate("IEEU") == 2
    assert candidate("AEEE") == 2
    assert candidate("aBEdEf") == 2
    assert candidate("") == 0
    assert candidate('abcdefg') == 0
    assert candidate("aOcdOfg") == 1
    assert candidate("UBCdUf") == 2
    assert candidate('U')  == 1
    assert candidate("ABCdEf") == 2
    assert candidate('') == 0
    assert candidate("IbcdeAg") == 1
    assert candidate("UBUE") == 2
    assert candidate("Ebcdefg") == 1
    assert candidate("dUBE") == 0
    assert candidate("EOEE") == 2
    assert candidate("OBCdEA") == 2
    assert candidate("I") == 1
    assert candidate("OBCdEf") == 2
    assert candidate("EIEE") == 2
    assert candidate("dBBU") == 0
    assert candidate("dEOE") == 1
    assert candidate("O") == 1
    assert candidate("AEAE") == 2
    assert candidate("EEEE") == 2
    assert candidate("aBCdEf") == 1
    assert candidate("abUdOfg") == 2
    assert candidate('aBCdEf')  == 1
    assert candidate("aBAUEf") == 2
    assert candidate("EBIdUU") == 3
    assert candidate("abcdeAg") == 0
    assert candidate("ABIE") == 2
    assert candidate("abOdefg") == 1
    assert candidate("aBUAEf") == 2
    assert candidate("aBIdIf") == 2
    assert candidate("abcdUfg") == 1
    assert candidate("IBBE") == 1
    assert candidate("dBBE") == 0
    assert candidate("B") == 0
    assert candidate("A") == 1
    assert candidate("IICdEf") == 2
    assert candidate('EEEE') == 2

    # Check some edge cases that are easy to work out by hand.
    assert candidate("AbcdefA") == 2
    assert candidate("abIdUfg") == 2
    assert candidate("aUCdEf") == 1
    assert candidate("abcdefg") == 0
    assert candidate("UBBE") == 1
    assert candidate("U") == 1
    assert candidate("dBIE") == 1
    assert candidate('dBBE') == 0
    assert candidate("abcUefU") == 1
    assert candidate("abcdefU") == 1
    assert candidate("EUEE") == 2
    assert candidate("E") == 1
    assert candidate("EBCdEf") == 2
    assert candidate('B')  == 0
    assert candidate("abOUAfg") == 2

if __name__ == '__main__':
    check(count_upper)