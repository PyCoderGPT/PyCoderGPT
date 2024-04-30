from case_MBPP_316 import merge


def check(candidate):
    assert candidate([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
    assert candidate([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]
    assert candidate([['x', 'y','z' ], ['a', 'b','c'], ['m', 'n','o']]) == [['x', 'a', 'm'], ['y', 'b', 'n'],['z', 'c','o']]
    assert candidate([['d', 'g'], ['u', 'l'], ['y', 'a']]) == [['d', 'u', 'y'], ['g', 'l', 'a']]
    assert candidate([['h', 'q'], ['w', 'p'], ['s', 'x']]) == [['h', 'w', 's'], ['q', 'p', 'x']]
    assert candidate([['w', 'r'], ['k', 't'], ['p', 'i']]) == [['w', 'k', 'p'], ['r', 't', 'i']]
    assert candidate([['f', 'h'], ['y', 'e'], ['y', 'c']]) == [['f', 'y', 'y'], ['h', 'e', 'c']]
    assert candidate([['q', 'm'], ['b', 't'], ['j', 'x']]) == [['q', 'b', 'j'], ['m', 't', 'x']]
    assert candidate([['e', 'w'], ['x', 'c'], ['x', 'o']]) == [['e', 'x', 'x'], ['w', 'c', 'o']]
    assert candidate([['a', 'u'], ['s', 'k'], ['m', 'd']]) == [['a', 's', 'm'], ['u', 'k', 'd']]
    assert candidate([['k', 's'], ['s', 'g'], ['i', 'n']]) == [['k', 's', 'i'], ['s', 'g', 'n']]
    assert candidate([['x', 'w'], ['v', 'y'], ['u', 'e']]) == [['x', 'v', 'u'], ['w', 'y', 'e']]
    assert candidate([['b', 'd'], ['u', 'l'], ['c', 'd']]) == [['b', 'u', 'c'], ['d', 'l', 'd']]
    assert candidate([['n', 'l'], ['r', 'n'], ['p', 'm']]) == [['n', 'r', 'p'], ['l', 'n', 'm']]
    assert candidate([['r', 'b'], ['r', 'c'], ['w', 'p']]) == [['r', 'r', 'w'], ['b', 'c', 'p']]
    assert candidate([['h', 'o'], ['f', 'y'], ['s', 'u']]) == [['h', 'f', 's'], ['o', 'y', 'u']]
    assert candidate([['q', 'r'], ['f', 'i'], ['h', 'f']]) == [['q', 'f', 'h'], ['r', 'i', 'f']]
    assert candidate([['d', 'v'], ['w', 'z'], ['l', 'e']]) == [['d', 'w', 'l'], ['v', 'z', 'e']]
    assert candidate([['a', 'w'], ['p', 'm'], ['z', 'c']]) == [['a', 'p', 'z'], ['w', 'm', 'c']]
    assert candidate([['h', 'n'], ['d', 'o'], ['o', 'h']]) == [['h', 'd', 'o'], ['n', 'o', 'h']]
    assert candidate([['l', 'x'], ['k', 'g'], ['d', 'v']]) == [['l', 'k', 'd'], ['x', 'g', 'v']]
    assert candidate([['e', 'r'], ['j', 'm'], ['t', 'j']]) == [['e', 'j', 't'], ['r', 'm', 'j']]
    assert candidate([['i', 'd'], ['e', 'j'], ['p', 'a']]) == [['i', 'e', 'p'], ['d', 'j', 'a']]
    assert candidate([['c', 'j'], ['v', 'l'], ['k', 'u']]) == [['c', 'v', 'k'], ['j', 'l', 'u']]
    assert candidate([['k', 't'], ['z', 'h'], ['g', 'a']]) == [['k', 'z', 'g'], ['t', 'h', 'a']]
    assert candidate([['p', 'r'], ['b', 'm'], ['a', 'a']]) == [['p', 'b', 'a'], ['r', 'm', 'a']]
    assert candidate([['e', 'h'], ['t', 'l'], ['z', 'm']]) == [['e', 't', 'z'], ['h', 'l', 'm']]
    assert candidate([['j', 'u'], ['e', 'y'], ['c', 'z']]) == [['j', 'e', 'c'], ['u', 'y', 'z']]
    assert candidate([['u', 'm'], ['t', 'f'], ['a', 'v']]) == [['u', 't', 'a'], ['m', 'f', 'v']]
    assert candidate([['x', 'u'], ['l', 'v'], ['v', 'i']]) == [['x', 'l', 'v'], ['u', 'v', 'i']]
    assert candidate([['f', 'z'], ['h', 'i'], ['x', 'h']]) == [['f', 'h', 'x'], ['z', 'i', 'h']]
    assert candidate([['m', 'q'], ['a', 'o'], ['y', 't']]) == [['m', 'a', 'y'], ['q', 'o', 't']]
    assert candidate([['d', 'a'], ['m', 'c'], ['t', 'f']]) == [['d', 'm', 't'], ['a', 'c', 'f']]
    assert candidate([['l', 'x'], ['v', 'u'], ['p', 'l']]) == [['l', 'v', 'p'], ['x', 'u', 'l']]
    assert candidate([['b', 'v'], ['n', 's'], ['b', 'j']]) == [['b', 'n', 'b'], ['v', 's', 'j']]
    assert candidate([['n', 'w'], ['v', 'v'], ['s', 'a']]) == [['n', 'v', 's'], ['w', 'v', 'a']]
    assert candidate([[2, 5], [6, 7], [8, 6], [10, 11]]) == [[2, 6, 8, 10], [5, 7, 6, 11]]
    assert candidate([[1, 6], [1, 6], [9, 1], [9, 4]]) == [[1, 1, 9, 9], [6, 6, 1, 4]]
    assert candidate([[4, 6], [5, 9], [4, 11], [7, 13]]) == [[4, 5, 4, 7], [6, 9, 11, 13]]
    assert candidate([[1, 4], [3, 9], [9, 8], [10, 6]]) == [[1, 3, 9, 10], [4, 9, 8, 6]]
    assert candidate([[5, 1], [6, 8], [7, 1], [12, 3]]) == [[5, 6, 7, 12], [1, 8, 1, 3]]
    assert candidate([[1, 1], [3, 2], [9, 8], [2, 4]]) == [[1, 3, 9, 2], [1, 2, 8, 4]]
    assert candidate([[6, 3], [5, 3], [9, 7], [5, 12]]) == [[6, 5, 9, 5], [3, 3, 7, 12]]
    assert candidate([[3, 2], [2, 5], [1, 8], [3, 9]]) == [[3, 2, 1, 3], [2, 5, 8, 9]]
    assert candidate([[5, 6], [2, 7], [2, 5], [3, 4]]) == [[5, 2, 2, 3], [6, 7, 5, 4]]
    assert candidate([[4, 6], [6, 5], [3, 10], [11, 10]]) == [[4, 6, 3, 11], [6, 5, 10, 10]]
    assert candidate([[4, 7], [4, 3], [5, 9], [7, 8]]) == [[4, 4, 5, 7], [7, 3, 9, 8]]
    assert candidate([[6, 3], [2, 6], [10, 2], [3, 12]]) == [[6, 2, 10, 3], [3, 6, 2, 12]]
    assert candidate([[4, 7], [4, 9], [7, 4], [9, 11]]) == [[4, 4, 7, 9], [7, 9, 4, 11]]
    assert candidate([[3, 5], [1, 5], [3, 9], [7, 3]]) == [[3, 1, 3, 7], [5, 5, 9, 3]]
    assert candidate([[2, 4], [8, 8], [2, 10], [10, 8]]) == [[2, 8, 2, 10], [4, 8, 10, 8]]
    assert candidate([[3, 1], [5, 6], [1, 11], [10, 3]]) == [[3, 5, 1, 10], [1, 6, 11, 3]]
    assert candidate([[2, 4], [6, 8], [6, 6], [4, 9]]) == [[2, 6, 6, 4], [4, 8, 6, 9]]
    assert candidate([[2, 4], [7, 2], [2, 7], [8, 10]]) == [[2, 7, 2, 8], [4, 2, 7, 10]]
    assert candidate([[6, 7], [1, 3], [9, 9], [5, 6]]) == [[6, 1, 9, 5], [7, 3, 9, 6]]
    assert candidate([[5, 2], [1, 5], [6, 5], [8, 8]]) == [[5, 1, 6, 8], [2, 5, 5, 8]]
    assert candidate([[1, 4], [8, 8], [1, 3], [9, 10]]) == [[1, 8, 1, 9], [4, 8, 3, 10]]
    assert candidate([[6, 2], [1, 5], [5, 9], [12, 4]]) == [[6, 1, 5, 12], [2, 5, 9, 4]]
    assert candidate([[3, 7], [1, 2], [8, 11], [12, 9]]) == [[3, 1, 8, 12], [7, 2, 11, 9]]
    assert candidate([[2, 1], [7, 3], [1, 9], [11, 13]]) == [[2, 7, 1, 11], [1, 3, 9, 13]]
    assert candidate([[6, 2], [1, 1], [2, 4], [10, 10]]) == [[6, 1, 2, 10], [2, 1, 4, 10]]
    assert candidate([[5, 2], [3, 5], [2, 1], [7, 6]]) == [[5, 3, 2, 7], [2, 5, 1, 6]]
    assert candidate([[1, 6], [5, 7], [8, 8], [3, 8]]) == [[1, 5, 8, 3], [6, 7, 8, 8]]
    assert candidate([[4, 6], [5, 3], [5, 1], [7, 4]]) == [[4, 5, 5, 7], [6, 3, 1, 4]]
    assert candidate([[4, 3], [8, 5], [6, 6], [9, 5]]) == [[4, 8, 6, 9], [3, 5, 6, 5]]
    assert candidate([[5, 2], [8, 1], [5, 10], [9, 3]]) == [[5, 8, 5, 9], [2, 1, 10, 3]]
    assert candidate([[2, 5], [7, 6], [9, 11], [9, 6]]) == [[2, 7, 9, 9], [5, 6, 11, 6]]
    assert candidate([[3, 7], [5, 4], [5, 10], [11, 8]]) == [[3, 5, 5, 11], [7, 4, 10, 8]]
    assert candidate([[3, 2], [8, 6], [2, 11], [2, 3]]) == [[3, 8, 2, 2], [2, 6, 11, 3]]
    assert candidate([['q', 'u', 's'], ['d', 'e', 'o'], ['b', 'z', 'i']]) == [['q', 'd', 'b'], ['u', 'e', 'z'], ['s', 'o', 'i']]
    assert candidate([['n', 'd', 'z'], ['n', 'x', 'e'], ['d', 'p', 'l']]) == [['n', 'n', 'd'], ['d', 'x', 'p'], ['z', 'e', 'l']]
    assert candidate([['v', 'b', 'e'], ['j', 'h', 'd'], ['j', 'h', 'f']]) == [['v', 'j', 'j'], ['b', 'h', 'h'], ['e', 'd', 'f']]
    assert candidate([['o', 'a', 'l'], ['e', 'x', 'y'], ['u', 'v', 'i']]) == [['o', 'e', 'u'], ['a', 'x', 'v'], ['l', 'y', 'i']]
    assert candidate([['g', 'w', 'u'], ['t', 'b', 'y'], ['z', 'p', 'm']]) == [['g', 't', 'z'], ['w', 'b', 'p'], ['u', 'y', 'm']]
    assert candidate([['c', 'x', 'j'], ['q', 's', 'x'], ['i', 'e', 't']]) == [['c', 'q', 'i'], ['x', 's', 'e'], ['j', 'x', 't']]
    assert candidate([['u', 't', 'q'], ['l', 'a', 's'], ['m', 'a', 'd']]) == [['u', 'l', 'm'], ['t', 'a', 'a'], ['q', 's', 'd']]
    assert candidate([['b', 'y', 'v'], ['g', 'w', 'k'], ['u', 'h', 'a']]) == [['b', 'g', 'u'], ['y', 'w', 'h'], ['v', 'k', 'a']]
    assert candidate([['g', 'd', 'q'], ['h', 'h', 'w'], ['m', 'a', 'j']]) == [['g', 'h', 'm'], ['d', 'h', 'a'], ['q', 'w', 'j']]
    assert candidate([['r', 't', 'q'], ['o', 'h', 'o'], ['q', 'y', 'c']]) == [['r', 'o', 'q'], ['t', 'h', 'y'], ['q', 'o', 'c']]
    assert candidate([['t', 'u', 'g'], ['o', 'e', 'o'], ['a', 'a', 'z']]) == [['t', 'o', 'a'], ['u', 'e', 'a'], ['g', 'o', 'z']]
    assert candidate([['q', 'd', 'e'], ['p', 'v', 'v'], ['x', 't', 'd']]) == [['q', 'p', 'x'], ['d', 'v', 't'], ['e', 'v', 'd']]
    assert candidate([['f', 'k', 'f'], ['m', 'x', 'j'], ['h', 'd', 'u']]) == [['f', 'm', 'h'], ['k', 'x', 'd'], ['f', 'j', 'u']]
    assert candidate([['x', 'f', 'f'], ['l', 'p', 'y'], ['h', 'f', 'v']]) == [['x', 'l', 'h'], ['f', 'p', 'f'], ['f', 'y', 'v']]
    assert candidate([['o', 'q', 'g'], ['y', 'e', 'x'], ['c', 'q', 'o']]) == [['o', 'y', 'c'], ['q', 'e', 'q'], ['g', 'x', 'o']]
    assert candidate([['t', 'a', 'e'], ['i', 'a', 'e'], ['o', 'y', 'w']]) == [['t', 'i', 'o'], ['a', 'a', 'y'], ['e', 'e', 'w']]
    assert candidate([['b', 'n', 'r'], ['y', 'h', 'g'], ['g', 'j', 'n']]) == [['b', 'y', 'g'], ['n', 'h', 'j'], ['r', 'g', 'n']]
    assert candidate([['p', 'a', 'f'], ['f', 'g', 'j'], ['w', 'z', 'm']]) == [['p', 'f', 'w'], ['a', 'g', 'z'], ['f', 'j', 'm']]
    assert candidate([['s', 'b', 'l'], ['z', 'g', 'b'], ['w', 'w', 'v']]) == [['s', 'z', 'w'], ['b', 'g', 'w'], ['l', 'b', 'v']]
    assert candidate([['n', 'q', 'x'], ['r', 'd', 'y'], ['k', 'n', 'y']]) == [['n', 'r', 'k'], ['q', 'd', 'n'], ['x', 'y', 'y']]
    assert candidate([['q', 'q', 'o'], ['l', 'o', 'x'], ['q', 'f', 'y']]) == [['q', 'l', 'q'], ['q', 'o', 'f'], ['o', 'x', 'y']]
    assert candidate([['w', 'm', 'n'], ['t', 'b', 'z'], ['q', 'e', 'u']]) == [['w', 't', 'q'], ['m', 'b', 'e'], ['n', 'z', 'u']]
    assert candidate([['a', 'i', 'w'], ['m', 'm', 'x'], ['d', 'x', 't']]) == [['a', 'm', 'd'], ['i', 'm', 'x'], ['w', 'x', 't']]
    assert candidate([['v', 'o', 'o'], ['k', 'u', 'a'], ['s', 't', 'h']]) == [['v', 'k', 's'], ['o', 'u', 't'], ['o', 'a', 'h']]
    assert candidate([['b', 'm', 'y'], ['e', 'm', 'r'], ['h', 'a', 'a']]) == [['b', 'e', 'h'], ['m', 'm', 'a'], ['y', 'r', 'a']]
    assert candidate([['m', 'w', 'r'], ['p', 'z', 'u'], ['f', 'l', 'c']]) == [['m', 'p', 'f'], ['w', 'z', 'l'], ['r', 'u', 'c']]
    assert candidate([['f', 'w', 'w'], ['g', 'b', 'q'], ['n', 'k', 'n']]) == [['f', 'g', 'n'], ['w', 'b', 'k'], ['w', 'q', 'n']]
    assert candidate([['z', 'n', 'q'], ['k', 'j', 'r'], ['u', 'g', 'j']]) == [['z', 'k', 'u'], ['n', 'j', 'g'], ['q', 'r', 'j']]
    assert candidate([['b', 'o', 't'], ['g', 'h', 'n'], ['t', 'i', 'f']]) == [['b', 'g', 't'], ['o', 'h', 'i'], ['t', 'n', 'f']]
    assert candidate([['p', 'p', 'c'], ['a', 'q', 'c'], ['g', 'k', 't']]) == [['p', 'a', 'g'], ['p', 'q', 'k'], ['c', 'c', 't']]
    assert candidate([['a', 'm', 'e'], ['s', 'q', 'p'], ['b', 'm', 'z']]) == [['a', 's', 'b'], ['m', 'q', 'm'], ['e', 'p', 'z']]
    assert candidate([['i', 'l', 'p'], ['w', 'i', 'q'], ['f', 'g', 'n']]) == [['i', 'w', 'f'], ['l', 'i', 'g'], ['p', 'q', 'n']]
    assert candidate([['t', 'd', 'j'], ['a', 'y', 'i'], ['k', 'c', 'q']]) == [['t', 'a', 'k'], ['d', 'y', 'c'], ['j', 'i', 'q']]

if __name__ == '__main__':
    check(merge)