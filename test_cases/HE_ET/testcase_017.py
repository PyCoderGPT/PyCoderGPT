from case_HE_017 import parse_music


def check(candidate):
    assert candidate(".| o .| o o o o| o| o| .| o o o .| .|") == [1, 4, 1, 4, 4, 4, 2, 2, 2, 1, 4, 4, 4, 1, 1]
    assert candidate(".| o o| o| o .| .| .| o .| o o| o| .| o| o o| o| .|") == [1, 4, 2, 2, 4, 1, 1, 1, 4, 1, 4, 2, 2, 1, 2, 4, 2, 2, 1]
    assert candidate("o| o o| .| .| .| .| o| o| .| o o| o| o| .| .| o|") == [2, 4, 2, 1, 1, 1, 1, 2, 2, 1, 4, 2, 2, 2, 1, 1, 2]
    assert candidate("o .| o .| o o o| o| o| o| o o .| o|") == [4, 1, 4, 1, 4, 4, 2, 2, 2, 2, 4, 4, 1, 2]
    assert candidate("o| o| o| o o o .| .| o o| o| o o| o o| o|") == [2, 2, 2, 4, 4, 4, 1, 1, 4, 2, 2, 4, 2, 4, 2, 2]
    assert candidate("o o| o .| o o| .| o| .| .| o o| o| o o| o| .|") == [4, 2, 4, 1, 4, 2, 1, 2, 1, 1, 4, 2, 2, 4, 2, 2, 1]
    assert candidate("o| .| .| o| o o o o o|") == [2, 1, 1, 2, 4, 4, 4, 4, 2]
    assert candidate("o o| o o o| .| o| o .|") == [4, 2, 4, 4, 2, 1, 2, 4, 1]
    assert candidate("o| o") == [2, 4]
    assert candidate("o o o| .| o| .| .| .| o| o o") == [4, 4, 2, 1, 2, 1, 1, 1, 2, 4, 4]
    assert candidate('o| o| .| .| o o o o') == [2, 2, 1, 1, 4, 4, 4, 4]
    assert candidate("o o o") == [4, 4, 4]
    assert candidate("o .| o| o| .| o .| o| .| o|") == [4, 1, 2, 2, 1, 4, 1, 2, 1, 2]
    assert candidate(".| .| o o| .| o .| o| o o| o o| o| .| o| o .|") == [1, 1, 4, 2, 1, 4, 1, 2, 4, 2, 4, 2, 2, 1, 2, 4, 1]
    assert candidate("o") == [4]
    assert candidate("o| .| o o| .| .| o .| o .| o .| .| o o .|") == [2, 1, 4, 2, 1, 1, 4, 1, 4, 1, 4, 1, 1, 4, 4, 1]
    assert candidate(".| o| .| o| o .| o| o| .| o| o| o| .| o|") == [1, 2, 1, 2, 4, 1, 2, 2, 1, 2, 2, 2, 1, 2]
    assert candidate(".| .|") == [1, 1]
    assert candidate(".| .| o .| o| o o| o o| o .| .| o o o .| o") == [1, 1, 4, 1, 2, 4, 2, 4, 2, 4, 1, 1, 4, 4, 4, 1, 4]
    assert candidate("o o .| o| o o o o o o| o o| .| o") == [4, 4, 1, 2, 4, 4, 4, 4, 4, 2, 4, 2, 1, 4]
    assert candidate(".| o o| .| .|") == [1, 4, 2, 1, 1]
    assert candidate(".| o o| o| .| o .| .| o") == [1, 4, 2, 2, 1, 4, 1, 1, 4]
    assert candidate("o| o o| .| .| o o o| .| o .| o| o") == [2, 4, 2, 1, 1, 4, 4, 2, 1, 4, 1, 2, 4]
    assert candidate("o| o o| o| .| .| .| .| o|") == [2, 4, 2, 2, 1, 1, 1, 1, 2]
    assert candidate("o|") == [2]
    assert candidate("o| o o o o o o .| o| o| o") == [2, 4, 4, 4, 4, 4, 4, 1, 2, 2, 4]
    assert candidate("o| o| o| o o o o o| .|") == [2, 2, 2, 4, 4, 4, 4, 2, 1]
    assert candidate('o| .| o| .| o o| o o|') == [2, 1, 2, 1, 4, 2, 4, 2]
    assert candidate("o| o| .| .| o| .| o| o o| .| o| o| o|") == [2, 2, 1, 1, 2, 1, 2, 4, 2, 1, 2, 2, 2]
    assert candidate("o| .| .| o .| o") == [2, 1, 1, 4, 1, 4]
    assert candidate("o o o .| o| o| o") == [4, 4, 4, 1, 2, 2, 4]
    assert candidate("o| .| o| .| o| o| o| .| o| .| o| o| o| o .| o o| o|") == [2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 4, 1, 4, 2, 2]
    assert candidate("o| o| o o| o| o o| o| .| .| o o .| .| o o o .|") == [2, 2, 4, 2, 2, 4, 2, 2, 1, 1, 4, 4, 1, 1, 4, 4, 4, 1]
    assert candidate(".| o| .| o o .| .| o o| o| o o| .| .| .|") == [1, 2, 1, 4, 4, 1, 1, 4, 2, 2, 4, 2, 1, 1, 1]
    assert candidate(".|") == [1]
    assert candidate("o| .| o| o| o| o| o .|") == [2, 1, 2, 2, 2, 2, 4, 1]
    assert candidate(".| .| o o .| o|") == [1, 1, 4, 4, 1, 2]
    assert candidate("o o o .| o o| o| o .| o o o .| o o| o o") == [4, 4, 4, 1, 4, 2, 2, 4, 1, 4, 4, 4, 1, 4, 2, 4, 4]
    assert candidate(".| o") == [1, 4]
    assert candidate("o| .| o| o| o| o| o| o| o| .| o| o| o .| o o| .| o o|") == [2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 4, 1, 4, 2, 1, 4, 2]
    assert candidate("o o o| o") == [4, 4, 2, 4]
    assert candidate("o| o .| o| o| o| o .| .| o| .| o| .|") == [2, 4, 1, 2, 2, 2, 4, 1, 1, 2, 1, 2, 1]
    assert candidate("o o o o| o| o o| o") == [4, 4, 4, 2, 2, 4, 2, 4]
    assert candidate("o| .| o| o o o| o o o| o .| .| .| o .|") == [2, 1, 2, 4, 4, 2, 4, 4, 2, 4, 1, 1, 1, 4, 1]
    assert candidate(".| .| o| o| o o o| o| o o| o o .| .| o o o") == [1, 1, 2, 2, 4, 4, 2, 2, 4, 2, 4, 4, 1, 1, 4, 4, 4]
    assert candidate(".| o| o .| o|") == [1, 2, 4, 1, 2]
    assert candidate("o| o .| o o| .|") == [2, 4, 1, 4, 2, 1]
    assert candidate(".| o .| o .| o| .| o .| o|") == [1, 4, 1, 4, 1, 2, 1, 4, 1, 2]
    assert candidate("o| o| o|") == [2, 2, 2]
    assert candidate(".| o| o .| .|") == [1, 2, 4, 1, 1]
    assert candidate("o| .| .| .| .|") == [2, 1, 1, 1, 1]
    assert candidate("o o| o o .| o| o|") == [4, 2, 4, 4, 1, 2, 2]
    assert candidate(".| o| o o .| .| .| o .| o| .| .| .| o| o| o o .| .|") == [1, 2, 4, 4, 1, 1, 1, 4, 1, 2, 1, 1, 1, 2, 2, 4, 4, 1, 1]
    assert candidate(".| .| o| o o o .| o|") == [1, 1, 2, 4, 4, 4, 1, 2]
    assert candidate("o| .| o| o| .| o| o| o .| .| .| o| o o| .| o .| .|") == [2, 1, 2, 2, 1, 2, 2, 4, 1, 1, 1, 2, 4, 2, 1, 4, 1, 1]
    assert candidate("o .| .| o .| o| .| o|") == [4, 1, 1, 4, 1, 2, 1, 2]
    assert candidate("o .| .|") == [4, 1, 1]
    assert candidate("o| .| o| o") == [2, 1, 2, 4]
    assert candidate(".| o .| o o| .| o o o|") == [1, 4, 1, 4, 2, 1, 4, 4, 2]
    assert candidate(".| .| o| .| .| o| o| .| o| o o| .| .| .|") == [1, 1, 2, 1, 1, 2, 2, 1, 2, 4, 2, 1, 1, 1]
    assert candidate(".| o| o|") == [1, 2, 2]
    assert candidate("o .| o o| .| o| .| o o| .| o") == [4, 1, 4, 2, 1, 2, 1, 4, 2, 1, 4]
    assert candidate("o o o| o| o| o| o| o| o|") == [4, 4, 2, 2, 2, 2, 2, 2, 2]
    assert candidate(".| o| o| o| o o| o| o| o| o o| .| o") == [1, 2, 2, 2, 4, 2, 2, 2, 2, 4, 2, 1, 4]
    assert candidate("o .|") == [4, 1]
    assert candidate(".| .| o .| o| .| o .| o| o o| o|") == [1, 1, 4, 1, 2, 1, 4, 1, 2, 4, 2, 2]
    assert candidate("o .| o o .| o o| o| o o .|") == [4, 1, 4, 4, 1, 4, 2, 2, 4, 4, 1]
    assert candidate("o| o .| .| o .| o o| .| o o| o| o") == [2, 4, 1, 1, 4, 1, 4, 2, 1, 4, 2, 2, 4]
    assert candidate("o o| .| .| o| .| .| .|") == [4, 2, 1, 1, 2, 1, 1, 1]
    assert candidate("o o| .| .|") == [4, 2, 1, 1]
    assert candidate(".| o| o o .| o|") == [1, 2, 4, 4, 1, 2]
    assert candidate('.| .| .| .|') == [1, 1, 1, 1]
    assert candidate(".| .| .| o| .| o| .| o o| o") == [1, 1, 1, 2, 1, 2, 1, 4, 2, 4]
    assert candidate("o| o| o| o .| o o| o|") == [2, 2, 2, 4, 1, 4, 2, 2]
    assert candidate(".| .| .| o .| .| o| o o .| o| o o .| o| o| .|") == [1, 1, 1, 4, 1, 1, 2, 4, 4, 1, 2, 4, 4, 1, 2, 2, 1]
    assert candidate(".| o| o") == [1, 2, 4]
    assert candidate("o| o| .| o .|") == [2, 2, 1, 4, 1]
    assert candidate(".| .| o o| .| o o .| o| o .| o o| .| o o| o o| o o") == [1, 1, 4, 2, 1, 4, 4, 1, 2, 4, 1, 4, 2, 1, 4, 2, 4, 2, 4, 4]
    assert candidate("o .| o|") == [4, 1, 2]
    assert candidate(".| o o| o") == [1, 4, 2, 4]
    assert candidate("o| .| o| .| o o o| .|") == [2, 1, 2, 1, 4, 4, 2, 1]
    assert candidate('o o o o') == [4, 4, 4, 4]
    assert candidate("o| .| o o| .| o .| o o .| o| .| o| o| .|") == [2, 1, 4, 2, 1, 4, 1, 4, 4, 1, 2, 1, 2, 2, 1]
    assert candidate(".| o| .| o| o| .| o .| o") == [1, 2, 1, 2, 2, 1, 4, 1, 4]
    assert candidate('') == []
    assert candidate(".| o o o .|") == [1, 4, 4, 4, 1]
    assert candidate(".| .| o| .| o|") == [1, 1, 2, 1, 2]
    assert candidate("o o o .| o|") == [4, 4, 4, 1, 2]
    assert candidate(".| .| o o| o| .| o .| .| o .| .| .| o|") == [1, 1, 4, 2, 2, 1, 4, 1, 1, 4, 1, 1, 1, 2]
    assert candidate("o o .|") == [4, 4, 1]
    assert candidate(".| o o o o o o o o| .| o o .| o o| o|") == [1, 4, 4, 4, 4, 4, 4, 4, 2, 1, 4, 4, 1, 4, 2, 2]
    assert candidate("o| o .| o|") == [2, 4, 1, 2]
    assert candidate(".| .| o o| o o o o o| .| .| o| .| .| o| .| o| .| o|") == [1, 1, 4, 2, 4, 4, 4, 4, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2]
    assert candidate("o o .| o| o o o o| .| o o o o| o .|") == [4, 4, 1, 2, 4, 4, 4, 2, 1, 4, 4, 4, 2, 4, 1]
    assert candidate("o o o o| o o|") == [4, 4, 4, 2, 4, 2]
    assert candidate("o .| o o| o o o o o| .| o o o| .|") == [4, 1, 4, 2, 4, 4, 4, 4, 2, 1, 4, 4, 2, 1]
    assert candidate(".| o| o o o| o o|") == [1, 2, 4, 4, 2, 4, 2]
    assert candidate("o o| o| .|") == [4, 2, 2, 1]
    assert candidate(".| o| o| .| o o| o o| o o .| o| o| o| o o .|") == [1, 2, 2, 1, 4, 2, 4, 2, 4, 4, 1, 2, 2, 2, 4, 4, 1]
    assert candidate(".| o| .| o .| o| o o .| o| o| o o .| o o .|") == [1, 2, 1, 4, 1, 2, 4, 4, 1, 2, 2, 4, 4, 1, 4, 4, 1]
    assert candidate(".| o| o o| o") == [1, 2, 4, 2, 4]
    assert candidate("o| o| o .| o| o o o| o o .|") == [2, 2, 4, 1, 2, 4, 4, 2, 4, 4, 1]
    assert candidate(".| o o| .| o o o o| o .| o") == [1, 4, 2, 1, 4, 4, 4, 2, 4, 1, 4]
    assert candidate(".| o| .| o .| o .| .| o .| o o o .| o o .| .|") == [1, 2, 1, 4, 1, 4, 1, 1, 4, 1, 4, 4, 4, 1, 4, 4, 1, 1]
    assert candidate("o .| o| o|") == [4, 1, 2, 2]
    assert candidate(".| o| o| .| o") == [1, 2, 2, 1, 4]
    assert candidate("o| o o| o") == [2, 4, 2, 4]
    assert candidate("o o o o o o| .| o| o .| o o|") == [4, 4, 4, 4, 4, 2, 1, 2, 4, 1, 4, 2]
    assert candidate(".| o| o o|") == [1, 2, 4, 2]
    assert candidate("o| o o|") == [2, 4, 2]
    assert candidate("o o|") == [4, 2]
    assert candidate("o .| .| o") == [4, 1, 1, 4]
    assert candidate(".| .| .| .| o| .| .| o o .| o| o .|") == [1, 1, 1, 1, 2, 1, 1, 4, 4, 1, 2, 4, 1]
    assert candidate("o o o o| o| .| o o| o o .| o .| o|") == [4, 4, 4, 2, 2, 1, 4, 2, 4, 4, 1, 4, 1, 2]
    assert candidate("o o| o| .| .| o| o|") == [4, 2, 2, 1, 1, 2, 2]
    assert candidate(".| o| .| .| .| o .| o| o| o o .| o") == [1, 2, 1, 1, 1, 4, 1, 2, 2, 4, 4, 1, 4]
    assert candidate("o o o .| o o| o| o o .| o| o| o| o") == [4, 4, 4, 1, 4, 2, 2, 4, 4, 1, 2, 2, 2, 4]
    assert candidate("o| .| o| o| .| o| .| o .| .| .| .| o o o| o") == [2, 1, 2, 2, 1, 2, 1, 4, 1, 1, 1, 1, 4, 4, 2, 4]
    assert candidate("o o| .| o| o .| o o| o| o o| o o") == [4, 2, 1, 2, 4, 1, 4, 2, 2, 4, 2, 4, 4]
    assert candidate("o| o .| .| o| .| o| o| o") == [2, 4, 1, 1, 2, 1, 2, 2, 4]
    assert candidate("o o o| o o o| o") == [4, 4, 2, 4, 4, 2, 4]
    assert candidate("o o o| .| o") == [4, 4, 2, 1, 4]
    assert candidate("o .| o| o .| .| .| o o| o") == [4, 1, 2, 4, 1, 1, 1, 4, 2, 4]
    assert candidate(".| o| .|") == [1, 2, 1]
    assert candidate("o| o|") == [2, 2]
    assert candidate(".| .| .| o| o| o o .| o o .| o") == [1, 1, 1, 2, 2, 4, 4, 1, 4, 4, 1, 4]
    assert candidate("o| o o .| o o| o| o o| o o .|") == [2, 4, 4, 1, 4, 2, 2, 4, 2, 4, 4, 1]
    assert candidate("o| o| .| o| .| o o o o| o o| o| .| o o o o|") == [2, 2, 1, 2, 1, 4, 4, 4, 2, 4, 2, 2, 1, 4, 4, 4, 2]
    assert candidate("o o .| o") == [4, 4, 1, 4]

if __name__ == '__main__':
    check(parse_music)