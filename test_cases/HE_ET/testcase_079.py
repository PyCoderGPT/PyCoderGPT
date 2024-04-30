from case_HE_079 import decimal_to_binary


def check(candidate):
    assert candidate(103) == "db1100111db"
    assert candidate(107) == 'db1101011db'
    assert candidate(4) == 'db100db'
    assert candidate(108) == 'db1101100db'
    assert candidate(99) == 'db1100011db'
    assert candidate(27) == 'db11011db'
    assert candidate(0) == "db0db"
    assert candidate(29) == 'db11101db'
    assert candidate(15) == "db1111db"
    assert candidate(100) == 'db1100100db'
    assert candidate(103) == 'db1100111db'
    assert candidate(32) == 'db100000db'
    assert candidate(3) == 'db11db'
    assert candidate(104) == 'db1101000db'
    assert candidate(32) == "db100000db"
    assert candidate(30) == 'db11110db'
    assert candidate(35) == 'db100011db'
    assert candidate(31) == 'db11111db'
    assert candidate(37) == 'db100101db'
    assert candidate(36) == 'db100100db'
    assert candidate(28) == 'db11100db'
    assert candidate(5) == 'db101db'
    assert candidate(102) == 'db1100110db'
    assert candidate(98) == 'db1100010db'
    assert candidate(101) == 'db1100101db'
    assert candidate(33) == 'db100001db'
    assert candidate(2) == 'db10db'
    assert candidate(34) == 'db100010db'
    assert candidate(106) == 'db1101010db'
    assert candidate(1) == 'db1db'

if __name__ == '__main__':
    check(decimal_to_binary)