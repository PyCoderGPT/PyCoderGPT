from case_MBPP_413 import return_sum


def check(candidate):
    assert candidate({'a': 100, 'b':200, 'c':300}) == 600
    assert candidate({'a': 25, 'b':18, 'c':45}) == 88
    assert candidate({'a': 36, 'b':39, 'c':49}) == 124
    assert candidate({'k': 101, 'f': 199, 'n': 302}) == 602
    assert candidate({'x': 97, 'i': 295}) == 392
    assert candidate({'q': 95, 'u': 198, 'k': 298}) == 591
    assert candidate({'d': 100, 'c': 200, 'y': 305}) == 605
    assert candidate({'c': 105, 'z': 301}) == 406
    assert candidate({'w': 99, 'm': 196, 'j': 295}) == 590
    assert candidate({'t': 104, 'k': 198, 'q': 303}) == 605
    assert candidate({'n': 98, 's': 203, 'r': 300}) == 601
    assert candidate({'u': 96, 'i': 201, 'h': 303}) == 600
    assert candidate({'d': 101, 'f': 197, 'q': 304}) == 602
    assert candidate({'u': 99, 'g': 200, 'j': 299}) == 598
    assert candidate({'j': 97, 'x': 197, 'd': 305}) == 599
    assert candidate({'b': 99, 'h': 204, 'z': 303}) == 606
    assert candidate({'p': 104, 'u': 198, 'k': 295}) == 597
    assert candidate({'p': 102, 'l': 201, 'h': 300}) == 603
    assert candidate({'r': 95, 'l': 204, 'j': 304}) == 603
    assert candidate({'o': 101, 's': 198, 'h': 297}) == 596
    assert candidate({'l': 96, 'b': 195, 'g': 303}) == 594
    assert candidate({'p': 97, 'r': 205, 'j': 303}) == 605
    assert candidate({'v': 104, 'd': 204, 'm': 295}) == 603
    assert candidate({'a': 105, 'm': 200, 'n': 297}) == 602
    assert candidate({'v': 103, 'q': 198, 'r': 298}) == 599
    assert candidate({'y': 99, 'w': 203, 'v': 295}) == 597
    assert candidate({'l': 102, 's': 205, 'r': 299}) == 606
    assert candidate({'d': 196, 'c': 296}) == 492
    assert candidate({'u': 97, 'g': 197, 'a': 298}) == 592
    assert candidate({'m': 96, 'u': 196, 'g': 300}) == 592
    assert candidate({'a': 105, 'n': 200, 's': 296}) == 601
    assert candidate({'w': 100, 'k': 296}) == 396
    assert candidate({'v': 97, 'x': 200, 's': 297}) == 594
    assert candidate({'u': 102, 't': 202, 'l': 296}) == 600
    assert candidate({'x': 103, 'f': 203, 'd': 299}) == 605
    assert candidate({'h': 98, 'x': 202, 't': 299}) == 599
    assert candidate({'j': 22, 'e': 17, 'b': 48}) == 87
    assert candidate({'x': 22, 'j': 19, 'u': 46}) == 87
    assert candidate({'k': 29, 'n': 14, 'y': 42}) == 85
    assert candidate({'y': 30, 'h': 17, 'k': 46}) == 93
    assert candidate({'t': 29, 'r': 15, 'e': 43}) == 87
    assert candidate({'l': 21, 'o': 20, 'p': 42}) == 83
    assert candidate({'j': 21, 'u': 16, 'd': 42}) == 79
    assert candidate({'g': 29, 'd': 15, 'c': 48}) == 92
    assert candidate({'n': 16, 's': 47}) == 63
    assert candidate({'p': 21, 'n': 16, 'd': 42}) == 79
    assert candidate({'u': 27, 'x': 15, 'z': 44}) == 86
    assert candidate({'x': 23, 'j': 18, 'm': 40}) == 81
    assert candidate({'y': 26, 'v': 14, 'a': 42}) == 82
    assert candidate({'u': 21, 'w': 23, 'k': 50}) == 94
    assert candidate({'b': 28, 'h': 23, 'e': 45}) == 96
    assert candidate({'i': 29, 'w': 49}) == 78
    assert candidate({'a': 27, 'y': 17, 'f': 50}) == 94
    assert candidate({'j': 29, 'u': 22, 'h': 50}) == 101
    assert candidate({'u': 21, 'r': 17, 'p': 40}) == 78
    assert candidate({'o': 25, 'q': 45}) == 70
    assert candidate({'j': 21, 'g': 15, 'b': 47}) == 83
    assert candidate({'j': 18, 'o': 46}) == 64
    assert candidate({'g': 25, 'p': 14, 'b': 47}) == 86
    assert candidate({'r': 28, 's': 14, 'l': 41}) == 83
    assert candidate({'u': 28, 'w': 21, 'z': 49}) == 98
    assert candidate({'a': 25, 'h': 21, 'v': 50}) == 96
    assert candidate({'o': 25, 'b': 18, 'h': 50}) == 93
    assert candidate({'u': 30, 'g': 21, 'm': 50}) == 101
    assert candidate({'g': 25, 'v': 14, 'n': 47}) == 86
    assert candidate({'n': 25, 'z': 18, 'e': 43}) == 86
    assert candidate({'g': 23, 'l': 22, 'y': 40}) == 85
    assert candidate({'i': 21, 'e': 19, 'c': 45}) == 85
    assert candidate({'o': 28, 'j': 22, 'y': 43}) == 93
    assert candidate({'g': 32, 'm': 34, 'b': 53}) == 119
    assert candidate({'q': 38, 's': 40, 'v': 45}) == 123
    assert candidate({'n': 35, 'e': 43, 'p': 51}) == 129
    assert candidate({'w': 31, 'n': 35, 'h': 44}) == 110
    assert candidate({'d': 35, 'a': 41, 'k': 54}) == 130
    assert candidate({'u': 38, 'o': 42, 'y': 46}) == 126
    assert candidate({'q': 37, 'a': 39, 'm': 48}) == 124
    assert candidate({'i': 38, 'g': 36, 'q': 51}) == 125
    assert candidate({'l': 37, 'g': 38, 'e': 54}) == 129
    assert candidate({'g': 34, 'b': 39, 'z': 53}) == 126
    assert candidate({'w': 31, 'z': 35, 'd': 44}) == 110
    assert candidate({'r': 32, 'o': 38, 'j': 46}) == 116
    assert candidate({'y': 31, 'v': 34, 'a': 45}) == 110
    assert candidate({'x': 35, 'd': 37, 's': 50}) == 122
    assert candidate({'b': 35, 'k': 41, 'f': 51}) == 127
    assert candidate({'x': 34, 'y': 39, 'z': 44}) == 117
    assert candidate({'p': 46, 'd': 44}) == 90
    assert candidate({'s': 34, 'o': 34, 'r': 47}) == 115
    assert candidate({'b': 37, 'd': 40, 'z': 47}) == 124
    assert candidate({'v': 34, 'q': 42, 'i': 49}) == 125
    assert candidate({'y': 35, 'j': 39, 'u': 47}) == 121
    assert candidate({'v': 41, 'j': 40, 'x': 49}) == 130
    assert candidate({'u': 35, 'h': 43, 'a': 50}) == 128
    assert candidate({'e': 39, 'c': 36, 'x': 54}) == 129
    assert candidate({'v': 31, 'u': 44, 'h': 50}) == 125
    assert candidate({'t': 39, 'c': 39, 'w': 50}) == 128
    assert candidate({'h': 43, 'd': 44}) == 87
    assert candidate({'l': 39, 'e': 39, 'w': 53}) == 131
    assert candidate({'o': 37, 'q': 35, 'k': 48}) == 120
    assert candidate({'i': 35, 'f': 37, 'y': 45}) == 117
    assert candidate({'c': 32, 'h': 38, 'i': 47}) == 117
    assert candidate({'u': 34, 'l': 44, 'z': 51}) == 129
    assert candidate({'p': 36, 't': 44, 'q': 52}) == 132

if __name__ == '__main__':
    check(return_sum)