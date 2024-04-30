from case_MBPP_195 import check_tuplex


def check(candidate):
    assert candidate(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
    assert candidate(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'5')==False
    assert candidate(("w", 3, "r", "e", "s", "o", "u", "r", "c","e"),3)==True
    assert candidate(('y', 2, 'f', 'e', 'h', 'y', 'e', 'o', 'v', 'r'), 'p') == False
    assert candidate(('p', 6, 'a', 'i', 't', 'q', 'e', 'g', 'r', 'z'), 'f') == False
    assert candidate(('d', 8, 'y', 'z', 'r', 'j', 'h', 'q', 'y', 'n'), 's') == False
    assert candidate(('h', 7, 'a', 'i', 'w', 'o', 'v', 'q', 'a', 'a'), 'e') == False
    assert candidate(('q', 2, 'a', 'y', 'y', 'b', 't', 'q', 'c', 'l'), 'n') == False
    assert candidate(('r', 4, 'e', 'v', 'q', 'k', 'y', 'r', 'a', 'c'), 'o') == False
    assert candidate(('b', 6, 'q', 'h', 'f', 'x', 'n', 'p', 'k', 'x'), 'k') == True
    assert candidate(('l', 5, 'x', 'k', 'd', 'v', 'd', 'b', 'd', 'f'), 'w') == False
    assert candidate(('r', 6, 'm', 'h', 'h', 'y', 'r', 'c', 'u', 'h'), 'y') == True
    assert candidate(('u', 3, 'f', 'g', 'p', 'a', 'c', 'q', 'b', 'm'), 'i') == False
    assert candidate(('j', 1, 'z', 'h', 'b', 'y', 'e', 'p', 'r', 'e'), 'x') == False
    assert candidate(('f', 6, 'c', 'w', 'y', 'r', 'x', 'm', 'h', 'j'), 'd') == False
    assert candidate(('f', 1, 'z', 'w', 'l', 'a', 'q', 'n', 'l', 'b'), 'h') == False
    assert candidate(('r', 3, 'l', 'i', 'n', 'k', 'd', 'i', 'k', 'c'), 't') == False
    assert candidate(('l', 8, 'z', 'i', 'w', 'w', 'o', 'f', 'c', 'w'), 'f') == True
    assert candidate(('i', 6, 'u', 'z', 'a', 'p', 'y', 'i', 'e', 'f'), 'w') == False
    assert candidate(('u', 2, 'f', 'f', 'x', 'i', 'k', 'k', 'i', 't'), 'o') == False
    assert candidate(('r', 4, 'u', 'i', 's', 'm', 'a', 'o', 'k', 'w'), 'm') == True
    assert candidate(('n', 8, 'w', 'u', 'v', 't', 'n', 'x', 'q', 'a'), 'l') == False
    assert candidate(('a', 3, 'd', 'd', 'z', 'b', 'k', 'i', 'n', 'b'), 'v') == False
    assert candidate(('v', 8, 't', 's', 'z', 'c', 'j', 'f', 'j', 'o'), 'y') == False
    assert candidate(('c', 6, 'f', 'f', 'y', 'p', 'j', 'v', 'b', 'k'), 'e') == False
    assert candidate(('w', 6, 'b', 'x', 'y', 'q', 'v', 'o', 'i', 's'), 'c') == False
    assert candidate(('y', 3, 'g', 'u', 'l', 'e', 't', 'z', 'a', 'g'), 'j') == False
    assert candidate(('i', 5, 'y', 'h', 'o', 'x', 'j', 'i', 'j', 'n'), 't') == False
    assert candidate(('x', 7, 'g', 'p', 'c', 't', 'f', 'o', 'j', 'f'), 'z') == False
    assert candidate(('u', 3, 'd', 't', 'm', 'k', 'm', 'm', 'u', 'd'), 'h') == False
    assert candidate(('x', 5, 'n', 'x', 'b', 's', 'h', 'a', 'p', 's'), 'z') == False
    assert candidate(('t', 8, 'c', 'a', 'm', 'i', 'o', 'h', 'a', 'c'), 'g') == False
    assert candidate(('o', 4, 'r', 'u', 'v', 'z', 'g', 'b', 'e', 'e'), 'j') == False
    assert candidate(('q', 5, 'z', 'o', 'f', 'v', 'd', 'c', 'p', 's'), 'n') == False
    assert candidate(('j', 7, 'u', 'g', 'r', 'r', 't', 'c', 'k', 'l'), 'j') == True
    assert candidate(('z', 6, 'j', 'r', 'n', 'c', 'v', 'j', 'k', 'h'), 'b') == False
    assert candidate(('e', 5, 'x', 'b', 'l', 'q', 'q', 'w', 'u', 'f'), '0') == False
    assert candidate(('p', 5, 'j', 'v', 'f', 's', 'x', 'v', 'q', 'n'), '7') == False
    assert candidate(('j', 7, 'c', 'f', 'p', 'p', 'i', 'b', 'l', 'i'), '8') == False
    assert candidate(('j', 2, 'a', 't', 'o', 't', 'k', 'e', 'g', 'z'), '0') == False
    assert candidate(('y', 4, 'w', 'c', 'c', 'r', 'b', 'x', 'i', 'x'), '8') == False
    assert candidate(('c', 2, 'u', 'o', 'z', 'e', 'i', 'l', 'x', 'd'), '2') == False
    assert candidate(('s', 1, 'd', 's', 'r', 'j', 't', 'n', 'k', 'n'), '6') == False
    assert candidate(('w', 8, 'u', 'q', 't', 'c', 'z', 'l', 'd', 's'), '9') == False
    assert candidate(('s', 1, 'b', 'u', 'y', 'c', 'z', 't', 'u', 't'), '8') == False
    assert candidate(('p', 8, 'k', 'm', 'm', 'g', 'h', 'j', 't', 'm'), '8') == False
    assert candidate(('s', 5, 'w', 'x', 'w', 'k', 'l', 'h', 'g', 'k'), '1') == False
    assert candidate(('c', 4, 'i', 'd', 'o', 's', 'p', 'm', 'r', 'c'), '8') == False
    assert candidate(('s', 1, 'l', 's', 'u', 'j', 'q', 't', 'w', 'f'), '8') == False
    assert candidate(('n', 2, 'f', 'n', 'j', 'y', 'c', 'n', 'm', 'h'), '5') == False
    assert candidate(('q', 3, 'c', 'n', 'o', 'e', 'o', 'x', 'w', 'm'), '0') == False
    assert candidate(('p', 6, 'z', 'b', 'r', 'n', 'b', 'q', 'u', 'n'), '7') == False
    assert candidate(('a', 1, 'w', 'w', 'k', 's', 'j', 'h', 'm', 'm'), '6') == False
    assert candidate(('f', 2, 'd', 'c', 'v', 'g', 'q', 'k', 'm', 'w'), '5') == False
    assert candidate(('u', 5, 'l', 'k', 'p', 'y', 'u', 'y', 'u', 'b'), '2') == False
    assert candidate(('o', 4, 's', 'e', 't', 'b', 'f', 'c', 'n', 'b'), '2') == False
    assert candidate(('h', 6, 'm', 'v', 'c', 'j', 'q', 'i', 'k', 'j'), '0') == False
    assert candidate(('e', 3, 'f', 's', 'u', 'v', 'g', 'q', 'a', 'n'), '3') == False
    assert candidate(('b', 8, 'h', 'g', 'm', 'e', 'v', 't', 'o', 'g'), '5') == False
    assert candidate(('p', 5, 'v', 'e', 'c', 'b', 't', 'm', 'r', 'b'), '3') == False
    assert candidate(('l', 8, 'f', 'g', 'j', 'i', 'f', 'i', 'h', 'g'), '5') == False
    assert candidate(('e', 3, 'y', 't', 'x', 'b', 'y', 's', 'o', 'j'), '3') == False
    assert candidate(('j', 7, 'n', 'u', 'e', 'z', 'm', 'y', 'm', 'z'), '7') == False
    assert candidate(('h', 2, 'w', 'x', 'z', 'f', 'p', 'g', 'm', 'r'), '9') == False
    assert candidate(('j', 3, 'v', 'j', 'l', 'l', 'u', 'f', 'd', 'o'), '5') == False
    assert candidate(('b', 2, 'b', 'q', 'n', 't', 'a', 'k', 'u', 'u'), '7') == False
    assert candidate(('r', 2, 'w', 'q', 's', 'k', 'p', 'r', 'f', 'u'), '6') == False
    assert candidate(('p', 8, 'o', 'k', 't', 't', 'w', 'b', 'i', 'a'), '5') == False
    assert candidate(('z', 1, 'y', 'o', 'e', 'm', 'k', 'j', 'o', 'i'), '2') == False
    assert candidate(('y', 3, 'p', 'x', 'i', 'f', 'y', 'x', 'm', 'n'), 7) == False
    assert candidate(('s', 7, 'e', 'x', 'y', 'z', 'i', 'o', 'g', 'p'), 6) == False
    assert candidate(('u', 8, 'q', 'q', 'm', 'g', 'q', 'y', 'b', 'm'), 8) == True
    assert candidate(('l', 1, 's', 'n', 'e', 'h', 'o', 'f', 'n', 'u'), 5) == False
    assert candidate(('o', 8, 'b', 'h', 's', 'l', 'w', 'o', 'd', 'c'), 8) == True
    assert candidate(('q', 7, 'c', 'k', 'c', 't', 's', 'y', 'j', 'p'), 2) == False
    assert candidate(('k', 5, 'k', 'v', 'p', 'u', 'p', 'g', 'g', 'o'), 7) == False
    assert candidate(('i', 2, 'r', 'r', 'y', 'u', 's', 'o', 't', 'v'), 8) == False
    assert candidate(('i', 7, 'w', 'h', 'v', 'm', 'e', 'f', 'e', 'o'), 3) == False
    assert candidate(('x', 3, 'y', 'b', 'f', 'g', 'b', 'g', 'q', 'k'), 2) == False
    assert candidate(('o', 6, 'k', 'u', 's', 'r', 'q', 'p', 'j', 't'), 4) == False
    assert candidate(('a', 4, 'u', 'n', 'm', 'y', 'a', 'v', 'r', 'e'), 1) == False
    assert candidate(('m', 2, 'y', 'u', 'r', 'y', 'w', 'i', 'j', 'x'), 8) == False
    assert candidate(('q', 8, 'h', 'n', 'v', 't', 'w', 'q', 'j', 'f'), 2) == False
    assert candidate(('f', 5, 'p', 'v', 'i', 'n', 'l', 'q', 'o', 'd'), 6) == False
    assert candidate(('t', 3, 's', 'l', 'i', 'j', 't', 'h', 'd', 'z'), 7) == False
    assert candidate(('q', 3, 'p', 'n', 'r', 'u', 'v', 'm', 'o', 'g'), 2) == False
    assert candidate(('z', 5, 'c', 's', 'g', 'a', 't', 'k', 'n', 'p'), 7) == False
    assert candidate(('w', 1, 'f', 'g', 's', 'o', 's', 'g', 't', 'v'), 6) == False
    assert candidate(('l', 3, 'l', 'h', 'x', 'd', 'w', 't', 'p', 'o'), 1) == False
    assert candidate(('r', 7, 'k', 'r', 't', 'g', 'q', 'b', 'f', 'k'), 3) == False
    assert candidate(('g', 1, 't', 'i', 'l', 'w', 'o', 'x', 'j', 'm'), 4) == False
    assert candidate(('a', 4, 'x', 'u', 'm', 'r', 'x', 'y', 'b', 's'), 2) == False
    assert candidate(('c', 7, 'b', 't', 'v', 'b', 'h', 'v', 'u', 'm'), 4) == False
    assert candidate(('w', 5, 'z', 'z', 'j', 'y', 'i', 'p', 'f', 'm'), 5) == True
    assert candidate(('j', 4, 'y', 'v', 'h', 'k', 'j', 'f', 'f', 'q'), 3) == False
    assert candidate(('x', 1, 'z', 'a', 'm', 'c', 'z', 'f', 'h', 't'), 8) == False
    assert candidate(('s', 1, 'f', 'l', 'v', 'x', 'a', 'w', 'n', 'y'), 8) == False
    assert candidate(('h', 5, 'm', 'm', 'q', 'z', 'z', 'v', 'z', 'h'), 3) == False
    assert candidate(('o', 1, 'n', 'f', 'l', 'n', 'o', 'k', 'u', 'n'), 6) == False
    assert candidate(('k', 8, 'b', 'u', 's', 'q', 'f', 'g', 'k', 'k'), 6) == False
    assert candidate(('u', 7, 'c', 'b', 't', 'y', 'c', 'm', 'q', 'e'), 2) == False
    assert candidate(('b', 6, 'e', 'x', 'b', 'h', 'v', 'g', 't', 'l'), 7) == False

if __name__ == '__main__':
    check(check_tuplex)