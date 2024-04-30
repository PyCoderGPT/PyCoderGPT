from case_MBPP_397 import pack_consecutive_duplicates


def check(candidate):
    assert candidate([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
    assert candidate([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10])==[[10, 10], [15], [19], [18, 18], [17], [26, 26], [17], [18], [10]]
    assert candidate(['a', 'a', 'b', 'c', 'd', 'd'])==[['a', 'a'], ['b'], ['c'], ['d', 'd']]
    assert candidate([1, 4, 2, 4, 5, 8, 8, 1, 3, 1, 6, 9, 8, 14, 9, 4]) == [[1], [4], [2], [4], [5], [8, 8], [1], [3], [1], [6], [9], [8], [14], [9], [4]]
    assert candidate([4, 1, 2, 7, 8, 5, 7, 4, 2, 4, 7, 3, 13, 7, 3, 9]) == [[4], [1], [2], [7], [8], [5], [7], [4], [2], [4], [7], [3], [13], [7], [3], [9]]
    assert candidate([5, 5, 5, 3, 5, 3, 1, 1, 8, 5, 4, 2, 13, 4, 6, 4]) == [[5, 5, 5], [3], [5], [3], [1, 1], [8], [5], [4], [2], [13], [4], [6], [4]]
    assert candidate([2, 4, 2, 6, 1, 7, 6, 2, 8, 6, 1, 2, 11, 11, 9, 3]) == [[2], [4], [2], [6], [1], [7], [6], [2], [8], [6], [1], [2], [11, 11], [9], [3]]
    assert candidate([1, 1, 2, 5, 5, 2, 9, 5, 5, 10, 7, 11, 12, 14, 7, 3]) == [[1, 1], [2], [5, 5], [2], [9], [5, 5], [10], [7], [11], [12], [14], [7], [3]]
    assert candidate([3, 2, 4, 6, 5, 3, 1, 5, 9, 4, 10, 11, 10, 13, 2, 7]) == [[3], [2], [4], [6], [5], [3], [1], [5], [9], [4], [10], [11], [10], [13], [2], [7]]
    assert candidate([1, 2, 6, 6, 7, 5, 3, 8, 11, 11, 10, 8, 4, 13, 3, 8]) == [[1], [2], [6, 6], [7], [5], [3], [8], [11, 11], [10], [8], [4], [13], [3], [8]]
    assert candidate([4, 5, 5, 1, 5, 3, 6, 7, 5, 7, 3, 9, 9, 9, 5, 8]) == [[4], [5, 5], [1], [5], [3], [6], [7], [5], [7], [3], [9, 9, 9], [5], [8]]
    assert candidate([5, 4, 5, 1, 5, 4, 2, 1, 4, 8, 11, 6, 9, 10, 7, 9]) == [[5], [4], [5], [1], [5], [4], [2], [1], [4], [8], [11], [6], [9], [10], [7], [9]]
    assert candidate([4, 4, 5, 1, 6, 9, 3, 7, 10, 2, 7, 3, 5, 6, 6, 2]) == [[4, 4], [5], [1], [6], [9], [3], [7], [10], [2], [7], [3], [5], [6, 6], [2]]
    assert candidate([2, 5, 4, 4, 2, 1, 1, 8, 3, 9, 11, 5, 5, 5, 8, 7]) == [[2], [5], [4, 4], [2], [1, 1], [8], [3], [9], [11], [5, 5, 5], [8], [7]]
    assert candidate([2, 1, 5, 3, 3, 9, 3, 1, 1, 7, 9, 10, 4, 5, 8, 6]) == [[2], [1], [5], [3, 3], [9], [3], [1, 1], [7], [9], [10], [4], [5], [8], [6]]
    assert candidate([1, 3, 1, 5, 4, 4, 8, 9, 10, 1, 7, 3, 6, 14, 7, 8]) == [[1], [3], [1], [5], [4, 4], [8], [9], [10], [1], [7], [3], [6], [14], [7], [8]]
    assert candidate([4, 3, 2, 5, 4, 9, 9, 8, 8, 9, 5, 6, 4, 4, 8, 2]) == [[4], [3], [2], [5], [4], [9, 9], [8, 8], [9], [5], [6], [4, 4], [8], [2]]
    assert candidate([5, 4, 1, 5, 1, 2, 5, 4, 5, 1, 7, 9, 9, 7, 2, 3]) == [[5], [4], [1], [5], [1], [2], [5], [4], [5], [1], [7], [9, 9], [7], [2], [3]]
    assert candidate([2, 1, 4, 4, 1, 4, 5, 8, 6, 6, 7, 12, 8, 6, 3, 5]) == [[2], [1], [4, 4], [1], [4], [5], [8], [6, 6], [7], [12], [8], [6], [3], [5]]
    assert candidate([3, 5, 3, 5, 6, 3, 3, 1, 6, 2, 5, 8, 9, 5, 5, 5]) == [[3], [5], [3], [5], [6], [3, 3], [1], [6], [2], [5], [8], [9], [5, 5, 5]]
    assert candidate([3, 5, 6, 2, 2, 7, 8, 10, 9, 1, 1, 10, 8, 10, 4, 1]) == [[3], [5], [6], [2, 2], [7], [8], [10], [9], [1, 1], [10], [8], [10], [4], [1]]
    assert candidate([1, 5, 5, 5, 1, 1, 8, 1, 2, 5, 4, 7, 13, 9, 5, 3]) == [[1], [5, 5, 5], [1, 1], [8], [1], [2], [5], [4], [7], [13], [9], [5], [3]]
    assert candidate([1, 4, 5, 3, 2, 5, 5, 1, 8, 9, 10, 4, 5, 13, 4, 1]) == [[1], [4], [5], [3], [2], [5, 5], [1], [8], [9], [10], [4], [5], [13], [4], [1]]
    assert candidate([5, 1, 3, 3, 2, 3, 7, 9, 8, 4, 9, 6, 8, 10, 4, 8]) == [[5], [1], [3, 3], [2], [3], [7], [9], [8], [4], [9], [6], [8], [10], [4], [8]]
    assert candidate([3, 4, 2, 1, 5, 5, 7, 7, 6, 1, 3, 8, 6, 7, 2, 7]) == [[3], [4], [2], [1], [5, 5], [7, 7], [6], [1], [3], [8], [6], [7], [2], [7]]
    assert candidate([2, 4, 4, 4, 2, 7, 1, 9, 11, 11, 2, 6, 12, 9, 5, 5]) == [[2], [4, 4, 4], [2], [7], [1], [9], [11, 11], [2], [6], [12], [9], [5, 5]]
    assert candidate([4, 1, 2, 4, 6, 2, 3, 3, 2, 4, 10, 8, 6, 8, 2, 9]) == [[4], [1], [2], [4], [6], [2], [3, 3], [2], [4], [10], [8], [6], [8], [2], [9]]
    assert candidate([5, 2, 5, 5, 6, 8, 9, 7, 2, 4, 7, 2, 7, 12, 5, 9]) == [[5], [2], [5, 5], [6], [8], [9], [7], [2], [4], [7], [2], [7], [12], [5], [9]]
    assert candidate([4, 4, 3, 3, 4, 8, 9, 3, 4, 11, 3, 9, 9, 8, 7, 6]) == [[4, 4], [3, 3], [4], [8], [9], [3], [4], [11], [3], [9, 9], [8], [7], [6]]
    assert candidate([4, 5, 6, 7, 5, 8, 2, 10, 11, 8, 7, 12, 11, 13, 8, 4]) == [[4], [5], [6], [7], [5], [8], [2], [10], [11], [8], [7], [12], [11], [13], [8], [4]]
    assert candidate([2, 5, 4, 2, 6, 9, 6, 2, 4, 2, 4, 5, 3, 9, 3, 5]) == [[2], [5], [4], [2], [6], [9], [6], [2], [4], [2], [4], [5], [3], [9], [3], [5]]
    assert candidate([5, 2, 4, 6, 6, 7, 1, 1, 1, 10, 11, 9, 10, 5, 2, 1]) == [[5], [2], [4], [6, 6], [7], [1, 1, 1], [10], [11], [9], [10], [5], [2], [1]]
    assert candidate([4, 2, 4, 2, 8, 9, 2, 4, 6, 3, 4, 12, 5, 6, 6, 3]) == [[4], [2], [4], [2], [8], [9], [2], [4], [6], [3], [4], [12], [5], [6, 6], [3]]
    assert candidate([4, 3, 1, 4, 4, 4, 1, 8, 10, 6, 9, 5, 3, 6, 7, 7]) == [[4], [3], [1], [4, 4, 4], [1], [8], [10], [6], [9], [5], [3], [6], [7, 7]]
    assert candidate([2, 3, 4, 4, 3, 6, 8, 2, 2, 10, 8, 3, 10, 14, 8, 8]) == [[2], [3], [4, 4], [3], [6], [8], [2, 2], [10], [8], [3], [10], [14], [8, 8]]
    assert candidate([2, 2, 2, 6, 6, 4, 6, 3, 2, 1, 10, 3, 5, 8, 7, 4]) == [[2, 2, 2], [6, 6], [4], [6], [3], [2], [1], [10], [3], [5], [8], [7], [4]]
    assert candidate([14, 13, 13, 22, 15, 14, 13, 21, 22, 15, 14, 6]) == [[14], [13, 13], [22], [15], [14], [13], [21], [22], [15], [14], [6]]
    assert candidate([14, 8, 20, 14, 15, 18, 13, 26, 27, 17, 21, 13]) == [[14], [8], [20], [14], [15], [18], [13], [26], [27], [17], [21], [13]]
    assert candidate([15, 8, 14, 22, 22, 19, 18, 26, 23, 17, 13, 10]) == [[15], [8], [14], [22, 22], [19], [18], [26], [23], [17], [13], [10]]
    assert candidate([13, 13, 16, 24, 21, 20, 19, 26, 27, 12, 19, 7]) == [[13, 13], [16], [24], [21], [20], [19], [26], [27], [12], [19], [7]]
    assert candidate([10, 6, 13, 20, 18, 14, 12, 22, 21, 22, 14, 8]) == [[10], [6], [13], [20], [18], [14], [12], [22], [21], [22], [14], [8]]
    assert candidate([8, 8, 20, 16, 21, 22, 21, 22, 28, 13, 15, 15]) == [[8, 8], [20], [16], [21], [22], [21], [22], [28], [13], [15, 15]]
    assert candidate([6, 11, 12, 22, 19, 14, 21, 28, 26, 16, 13, 11]) == [[6], [11], [12], [22], [19], [14], [21], [28], [26], [16], [13], [11]]
    assert candidate([10, 15, 13, 22, 20, 18, 13, 28, 26, 16, 14, 11]) == [[10], [15], [13], [22], [20], [18], [13], [28], [26], [16], [14], [11]]
    assert candidate([11, 14, 16, 17, 22, 18, 14, 24, 27, 20, 19, 13]) == [[11], [14], [16], [17], [22], [18], [14], [24], [27], [20], [19], [13]]
    assert candidate([13, 5, 19, 21, 14, 21, 21, 26, 31, 16, 17, 10]) == [[13], [5], [19], [21], [14], [21, 21], [26], [31], [16], [17], [10]]
    assert candidate([8, 15, 12, 22, 14, 21, 18, 25, 29, 12, 20, 9]) == [[8], [15], [12], [22], [14], [21], [18], [25], [29], [12], [20], [9]]
    assert candidate([6, 13, 12, 15, 21, 18, 15, 28, 24, 22, 21, 11]) == [[6], [13], [12], [15], [21], [18], [15], [28], [24], [22], [21], [11]]
    assert candidate([14, 7, 15, 19, 22, 16, 20, 24, 31, 13, 22, 10]) == [[14], [7], [15], [19], [22], [16], [20], [24], [31], [13], [22], [10]]
    assert candidate([6, 14, 14, 15, 17, 23, 22, 30, 25, 21, 17, 11]) == [[6], [14, 14], [15], [17], [23], [22], [30], [25], [21], [17], [11]]
    assert candidate([5, 8, 11, 15, 19, 23, 12, 30, 21, 20, 22, 11]) == [[5], [8], [11], [15], [19], [23], [12], [30], [21], [20], [22], [11]]
    assert candidate([10, 10, 12, 22, 16, 19, 20, 30, 22, 12, 14, 12]) == [[10, 10], [12], [22], [16], [19], [20], [30], [22], [12], [14], [12]]
    assert candidate([13, 14, 15, 17, 13, 23, 17, 23, 31, 15, 17, 11]) == [[13], [14], [15], [17], [13], [23], [17], [23], [31], [15], [17], [11]]
    assert candidate([5, 15, 20, 14, 20, 20, 15, 26, 25, 15, 16, 11]) == [[5], [15], [20], [14], [20, 20], [15], [26], [25], [15], [16], [11]]
    assert candidate([7, 6, 19, 24, 17, 22, 17, 29, 29, 14, 21, 14]) == [[7], [6], [19], [24], [17], [22], [17], [29, 29], [14], [21], [14]]
    assert candidate([11, 5, 19, 21, 18, 18, 19, 31, 28, 17, 18, 12]) == [[11], [5], [19], [21], [18, 18], [19], [31], [28], [17], [18], [12]]
    assert candidate([12, 12, 14, 17, 21, 19, 22, 27, 26, 19, 19, 6]) == [[12, 12], [14], [17], [21], [19], [22], [27], [26], [19, 19], [6]]
    assert candidate([11, 6, 15, 14, 16, 21, 17, 22, 27, 16, 14, 7]) == [[11], [6], [15], [14], [16], [21], [17], [22], [27], [16], [14], [7]]
    assert candidate([11, 11, 18, 16, 14, 15, 15, 21, 27, 18, 16, 9]) == [[11, 11], [18], [16], [14], [15, 15], [21], [27], [18], [16], [9]]
    assert candidate([11, 5, 14, 15, 22, 20, 15, 31, 23, 15, 17, 15]) == [[11], [5], [14], [15], [22], [20], [15], [31], [23], [15], [17], [15]]
    assert candidate([13, 7, 11, 17, 19, 22, 19, 23, 26, 16, 19, 7]) == [[13], [7], [11], [17], [19], [22], [19], [23], [26], [16], [19], [7]]
    assert candidate([15, 15, 19, 17, 22, 14, 18, 28, 22, 18, 13, 13]) == [[15, 15], [19], [17], [22], [14], [18], [28], [22], [18], [13, 13]]
    assert candidate([15, 10, 12, 24, 19, 20, 19, 23, 29, 22, 20, 6]) == [[15], [10], [12], [24], [19], [20], [19], [23], [29], [22], [20], [6]]
    assert candidate([8, 13, 19, 21, 23, 13, 18, 22, 24, 22, 13, 8]) == [[8], [13], [19], [21], [23], [13], [18], [22], [24], [22], [13], [8]]
    assert candidate([10, 15, 16, 20, 19, 23, 13, 22, 23, 17, 20, 15]) == [[10], [15], [16], [20], [19], [23], [13], [22], [23], [17], [20], [15]]
    assert candidate([14, 15, 17, 16, 19, 22, 17, 31, 27, 16, 14, 15]) == [[14], [15], [17], [16], [19], [22], [17], [31], [27], [16], [14], [15]]
    assert candidate([14, 5, 10, 19, 18, 19, 22, 25, 29, 19, 14, 14]) == [[14], [5], [10], [19], [18], [19], [22], [25], [29], [19], [14, 14]]
    assert candidate([14, 9, 19, 21, 13, 22, 15, 30, 30, 19, 16, 6]) == [[14], [9], [19], [21], [13], [22], [15], [30, 30], [19], [16], [6]]
    assert candidate([10, 7, 17, 22, 23, 16, 15, 30, 21, 12, 23, 11]) == [[10], [7], [17], [22], [23], [16], [15], [30], [21], [12], [23], [11]]
    assert candidate(['o', 'q', 'b', 'l', 'a', 'x']) == [['o'], ['q'], ['b'], ['l'], ['a'], ['x']]
    assert candidate(['z', 'v', 'd', 'c', 'w', 'e']) == [['z'], ['v'], ['d'], ['c'], ['w'], ['e']]
    assert candidate(['j', 'u', 'o', 'm', 'y', 't']) == [['j'], ['u'], ['o'], ['m'], ['y'], ['t']]
    assert candidate(['q', 'v', 'z', 'd', 'l', 'i']) == [['q'], ['v'], ['z'], ['d'], ['l'], ['i']]
    assert candidate(['e', 't', 'q', 'y', 'x', 'j']) == [['e'], ['t'], ['q'], ['y'], ['x'], ['j']]
    assert candidate(['t', 'o', 'u', 'x', 'n', 'z']) == [['t'], ['o'], ['u'], ['x'], ['n'], ['z']]
    assert candidate(['x', 'd', 'n', 'o', 'l', 'z']) == [['x'], ['d'], ['n'], ['o'], ['l'], ['z']]
    assert candidate(['m', 'l', 'l', 'x', 'c', 'n']) == [['m'], ['l', 'l'], ['x'], ['c'], ['n']]
    assert candidate(['j', 'j', 'n', 'f', 'v', 'd']) == [['j', 'j'], ['n'], ['f'], ['v'], ['d']]
    assert candidate(['m', 'f', 'z', 'j', 'i', 'k']) == [['m'], ['f'], ['z'], ['j'], ['i'], ['k']]
    assert candidate(['f', 'z', 'u', 'k', 'z', 'v']) == [['f'], ['z'], ['u'], ['k'], ['z'], ['v']]
    assert candidate(['a', 'n', 'y', 'w', 'q', 'm']) == [['a'], ['n'], ['y'], ['w'], ['q'], ['m']]
    assert candidate(['y', 'o', 'r', 'o', 'r', 'u']) == [['y'], ['o'], ['r'], ['o'], ['r'], ['u']]
    assert candidate(['m', 'p', 't', 't', 'f', 'v']) == [['m'], ['p'], ['t', 't'], ['f'], ['v']]
    assert candidate(['n', 's', 'n', 'i', 'g', 'b']) == [['n'], ['s'], ['n'], ['i'], ['g'], ['b']]
    assert candidate(['l', 'l', 'v', 'v', 'x', 'r']) == [['l', 'l'], ['v', 'v'], ['x'], ['r']]
    assert candidate(['y', 'l', 'l', 'w', 'c', 'v']) == [['y'], ['l', 'l'], ['w'], ['c'], ['v']]
    assert candidate(['h', 't', 'z', 'k', 's', 'r']) == [['h'], ['t'], ['z'], ['k'], ['s'], ['r']]
    assert candidate(['v', 'g', 'c', 'k', 'w', 'l']) == [['v'], ['g'], ['c'], ['k'], ['w'], ['l']]
    assert candidate(['k', 'e', 'm', 'o', 'e', 'v']) == [['k'], ['e'], ['m'], ['o'], ['e'], ['v']]
    assert candidate(['f', 'h', 'j', 'q', 'n', 'g']) == [['f'], ['h'], ['j'], ['q'], ['n'], ['g']]
    assert candidate(['e', 'v', 'w', 'j', 'a', 'u']) == [['e'], ['v'], ['w'], ['j'], ['a'], ['u']]
    assert candidate(['p', 'm', 'x', 'o', 'i', 'a']) == [['p'], ['m'], ['x'], ['o'], ['i'], ['a']]
    assert candidate(['y', 'c', 'd', 'p', 'x', 'a']) == [['y'], ['c'], ['d'], ['p'], ['x'], ['a']]
    assert candidate(['q', 'p', 'v', 'j', 'k', 'q']) == [['q'], ['p'], ['v'], ['j'], ['k'], ['q']]
    assert candidate(['p', 'j', 'z', 't', 'g', 'q']) == [['p'], ['j'], ['z'], ['t'], ['g'], ['q']]
    assert candidate(['l', 'c', 'j', 'q', 'n', 'a']) == [['l'], ['c'], ['j'], ['q'], ['n'], ['a']]
    assert candidate(['d', 'w', 'r', 'g', 'h', 'y']) == [['d'], ['w'], ['r'], ['g'], ['h'], ['y']]
    assert candidate(['j', 'a', 'z', 'p', 'b', 'u']) == [['j'], ['a'], ['z'], ['p'], ['b'], ['u']]
    assert candidate(['j', 'e', 'l', 'u', 't', 'x']) == [['j'], ['e'], ['l'], ['u'], ['t'], ['x']]
    assert candidate(['c', 'g', 'z', 'f', 'g', 'a']) == [['c'], ['g'], ['z'], ['f'], ['g'], ['a']]
    assert candidate(['j', 'r', 's', 'f', 'g', 'u']) == [['j'], ['r'], ['s'], ['f'], ['g'], ['u']]
    assert candidate(['w', 'g', 'o', 'b', 'i', 'f']) == [['w'], ['g'], ['o'], ['b'], ['i'], ['f']]

if __name__ == '__main__':
    check(pack_consecutive_duplicates)