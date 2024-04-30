from case_MBPP_234 import count_Occurrence


def check(candidate):
    assert candidate(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
    assert candidate((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6
    assert candidate((1,2,3,4,5,6),[1,2]) == 2
    assert candidate(('y', 'k', 'a', 'b', 'd'), ['l', 'l']) == 0
    assert candidate(('y', 'm', 'e', 'b', 'l'), ['f', 'n']) == 0
    assert candidate(('o', 'f', 'j', 'm', 'm'), ['y', 'e']) == 0
    assert candidate(('u', 'q', 'h', 'f', 'r'), ['m', 'c']) == 0
    assert candidate(('v', 'g', 'r', 'f', 'y'), ['r', 'g']) == 2
    assert candidate(('a', 'w', 'l', 'o', 'b'), ['g', 's']) == 0
    assert candidate(('u', 'p', 'g', 'q', 'a'), ['k', 'w']) == 0
    assert candidate(('q', 'w', 'o', 'b', 'u'), ['b', 'm']) == 1
    assert candidate(('o', 'h', 'q', 'n', 'v'), ['y', 'l']) == 0
    assert candidate(('p', 'f', 'e', 'l', 'v'), ['v', 'g']) == 1
    assert candidate(('j', 'u', 'c', 'u', 'r'), ['f', 't']) == 0
    assert candidate(('h', 'q', 'w', 'r', 'z'), ['b', 'l']) == 0
    assert candidate(('m', 'u', 'a', 'z', 's'), ['g', 's']) == 1
    assert candidate(('x', 'v', 'x', 't', 'l'), ['g', 'o']) == 0
    assert candidate(('z', 'o', 's', 'v', 'g'), ['u', 'k']) == 0
    assert candidate(('p', 'w', 'm', 'f', 'b'), ['w', 'f']) == 2
    assert candidate(('w', 'u', 'e', 'd', 'v'), ['x', 'o']) == 0
    assert candidate(('c', 'k', 'y', 'k', 'v'), ['n', 'f']) == 0
    assert candidate(('t', 'l', 'h', 'l', 'i'), ['n', 'o']) == 0
    assert candidate(('y', 'a', 'd', 'a', 'z'), ['y', 'w']) == 1
    assert candidate(('f', 't', 'q', 'm', 'x'), ['f', 'l']) == 1
    assert candidate(('n', 'c', 'v', 'h', 'r'), ['u', 'a']) == 0
    assert candidate(('p', 'c', 'k', 'f', 'i'), ['p', 'r']) == 1
    assert candidate(('p', 'i', 'g', 't', 'q'), ['e', 'k']) == 0
    assert candidate(('f', 'c', 'p', 'q', 'r'), ['g', 'a']) == 0
    assert candidate(('m', 's', 'i', 'o', 'x'), ['z', 'e']) == 0
    assert candidate(('y', 'q', 'w', 'q', 'm'), ['y', 'v']) == 1
    assert candidate(('y', 'r', 'l', 'k', 'c'), ['a', 'p']) == 0
    assert candidate(('f', 'y', 's', 'c', 'x'), ['n', 'z']) == 0
    assert candidate(('j', 'u', 'n', 'b', 'u'), ['t', 'a']) == 0
    assert candidate(('x', 'x', 'f', 'a', 'l'), ['r', 'j']) == 0
    assert candidate(('d', 'g', 'w', 'i', 'e'), ['h', 'e']) == 1
    assert candidate(('s', 't', 'h', 'c', 'm'), ['r', 'p']) == 0
    assert candidate((1, 5, 1, 1, 3, 9, 5, 2, 4), [1, 1, 2]) == 4
    assert candidate((4, 5, 7, 3, 4, 9, 8, 5, 4), [3, 9, 11]) == 2
    assert candidate((3, 4, 3, 2, 3, 6, 6, 4, 6), [4, 1, 4]) == 2
    assert candidate((1, 4, 1, 4, 9, 10, 4, 1, 9), [3, 1, 2]) == 3
    assert candidate((4, 5, 8, 2, 2, 6, 5, 2, 1), [1, 2, 5]) == 6
    assert candidate((6, 6, 7, 3, 1, 6, 6, 4, 9), [3, 4, 5]) == 2
    assert candidate((4, 2, 6, 6, 8, 2, 7, 5, 6), [1, 7, 6]) == 4
    assert candidate((5, 7, 5, 4, 5, 11, 8, 2, 5), [5, 9, 9]) == 4
    assert candidate((1, 3, 3, 4, 5, 3, 11, 1, 8), [2, 5, 8]) == 2
    assert candidate((1, 6, 3, 2, 9, 7, 4, 4, 9), [5, 3, 8]) == 1
    assert candidate((2, 6, 5, 5, 8, 3, 12, 6, 3), [2, 5, 10]) == 3
    assert candidate((5, 5, 7, 3, 9, 11, 3, 4, 5), [4, 1, 2]) == 1
    assert candidate((6, 5, 6, 2, 3, 3, 8, 3, 7), [4, 5, 9]) == 1
    assert candidate((2, 5, 7, 1, 2, 7, 10, 2, 4), [4, 8, 4]) == 1
    assert candidate((2, 7, 3, 5, 2, 11, 5, 2, 5), [6, 3, 6]) == 1
    assert candidate((1, 7, 2, 4, 1, 1, 3, 3, 3), [5, 1, 7]) == 4
    assert candidate((4, 3, 6, 6, 5, 5, 11, 2, 2), [3, 8, 6]) == 3
    assert candidate((6, 4, 7, 5, 6, 6, 12, 1, 4), [6, 7, 6]) == 4
    assert candidate((5, 6, 7, 1, 4, 5, 5, 6, 7), [2, 6, 7]) == 4
    assert candidate((5, 3, 3, 4, 5, 4, 3, 6, 2), [1, 3, 4]) == 5
    assert candidate((2, 2, 5, 6, 6, 8, 9, 5, 4), [3, 9, 8]) == 2
    assert candidate((4, 6, 3, 1, 9, 3, 3, 5, 9), [4, 9, 10]) == 3
    assert candidate((4, 7, 3, 4, 4, 6, 5, 2, 2), [6, 2, 4]) == 6
    assert candidate((6, 4, 5, 3, 5, 6, 7, 6, 8), [6, 3, 5]) == 6
    assert candidate((5, 5, 3, 6, 5, 8, 9, 2, 2), [2, 1, 9]) == 3
    assert candidate((3, 1, 4, 2, 7, 3, 4, 4, 9), [5, 5, 4]) == 3
    assert candidate((5, 7, 8, 1, 4, 10, 2, 5, 5), [5, 8, 11]) == 4
    assert candidate((5, 6, 5, 1, 9, 11, 10, 6, 7), [6, 5, 7]) == 5
    assert candidate((3, 3, 6, 1, 9, 1, 4, 3, 5), [5, 1, 4]) == 4
    assert candidate((5, 2, 6, 4, 8, 6, 8, 6, 3), [1, 1, 12]) == 0
    assert candidate((6, 2, 5, 3, 8, 8, 6, 4, 2), [6, 7, 3]) == 3
    assert candidate((5, 2, 7, 5, 9, 10, 6, 2, 9), [6, 4, 3]) == 1
    assert candidate((4, 6, 7, 2, 3, 2, 2, 6, 4), [4, 5, 4]) == 2
    assert candidate((1, 4, 2, 5, 3, 7), [3, 3]) == 1
    assert candidate((2, 4, 8, 2, 6, 2), [3, 5]) == 0
    assert candidate((4, 7, 3, 9, 10, 5), [3, 3]) == 1
    assert candidate((3, 3, 2, 8, 6, 7), [1, 3]) == 2
    assert candidate((3, 3, 1, 7, 7, 4), [6, 6]) == 0
    assert candidate((4, 3, 3, 7, 6, 5), [3, 4]) == 3
    assert candidate((1, 1, 7, 7, 9, 9), [2, 5]) == 0
    assert candidate((6, 7, 2, 2, 4, 11), [1, 7]) == 1
    assert candidate((4, 5, 6, 3, 5, 4), [2, 3]) == 1
    assert candidate((6, 6, 2, 9, 10, 3), [4, 1]) == 0
    assert candidate((4, 3, 3, 2, 4, 6), [4, 6]) == 3
    assert candidate((4, 7, 2, 9, 5, 7), [3, 6]) == 0
    assert candidate((1, 6, 1, 3, 1, 2), [3, 5]) == 1
    assert candidate((5, 4, 7, 7, 3, 10), [4, 2]) == 1
    assert candidate((3, 2, 1, 4, 3, 6), [6, 6]) == 1
    assert candidate((2, 2, 7, 3, 5, 8), [5, 1]) == 1
    assert candidate((2, 2, 7, 4, 9, 10), [6, 6]) == 0
    assert candidate((6, 2, 1, 3, 7, 10), [5, 2]) == 1
    assert candidate((3, 7, 8, 8, 10, 4), [5, 6]) == 0
    assert candidate((5, 7, 2, 4, 6, 6), [5, 4]) == 2
    assert candidate((3, 6, 3, 2, 7, 6), [3, 3]) == 2
    assert candidate((5, 3, 1, 5, 1, 10), [2, 3]) == 1
    assert candidate((1, 6, 2, 5, 4, 3), [2, 1]) == 2
    assert candidate((6, 4, 5, 8, 1, 5), [4, 3]) == 1
    assert candidate((4, 1, 1, 5, 9, 6), [4, 5]) == 2
    assert candidate((4, 3, 8, 3, 8, 8), [3, 4]) == 3
    assert candidate((2, 7, 3, 9, 2, 3), [1, 5]) == 0
    assert candidate((4, 5, 6, 4, 9, 2), [4, 5]) == 3
    assert candidate((3, 4, 3, 5, 5, 10), [4, 1]) == 1
    assert candidate((5, 3, 7, 3, 1, 3), [1, 7]) == 2
    assert candidate((2, 6, 3, 9, 1, 5), [4, 3]) == 1
    assert candidate((3, 5, 7, 1, 1, 6), [1, 4]) == 2
    assert candidate((3, 7, 6, 3, 4, 4), [3, 6]) == 3

if __name__ == '__main__':
    check(count_Occurrence)