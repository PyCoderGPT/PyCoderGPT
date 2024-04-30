from case_MBPP_219 import common_element


def check(candidate):
    assert candidate([1,2,3,4,5], [5,6,7,8,9])==True
    assert candidate([1,2,3,4,5], [6,7,8,9])==None
    assert candidate(['a','b','c'], ['d','b','e'])==True
    assert candidate([2, 7, 1, 4, 2], [6, 10, 7, 5, 11]) == True
    assert candidate([3, 5, 7, 8, 6], [9, 7, 2, 6, 4]) == True
    assert candidate([2, 2, 7, 5, 7], [7, 10, 7, 13, 12]) == True
    assert candidate([1, 2, 7, 2, 5], [8, 11, 10, 4, 12]) == None
    assert candidate([1, 3, 3, 3, 3], [9, 1, 10, 12, 7]) == True
    assert candidate([2, 6, 6, 4, 2], [10, 2, 4, 11, 8]) == True
    assert candidate([5, 4, 3, 2, 1], [9, 3, 12, 11, 14]) == True
    assert candidate([5, 2, 8, 3, 4], [5, 8, 3, 8, 9]) == True
    assert candidate([4, 1, 7, 2, 6], [7, 6, 11, 10, 5]) == True
    assert candidate([1, 4, 1, 9, 9], [6, 9, 8, 6, 4]) == True
    assert candidate([6, 1, 2, 9, 1], [6, 7, 4, 13, 11]) == True
    assert candidate([5, 7, 7, 6, 2], [4, 3, 11, 3, 6]) == True
    assert candidate([2, 4, 6, 6, 3], [2, 4, 9, 9, 14]) == True
    assert candidate([1, 2, 7, 1, 5], [6, 6, 12, 8, 13]) == None
    assert candidate([2, 1, 3, 8, 9], [7, 10, 5, 7, 5]) == None
    assert candidate([5, 3, 4, 5, 1], [2, 8, 11, 10, 4]) == True
    assert candidate([5, 2, 7, 8, 7], [1, 2, 5, 4, 10]) == True
    assert candidate([4, 5, 3, 6, 6], [6, 7, 9, 9, 9]) == True
    assert candidate([1, 6, 8, 2, 10], [10, 4, 12, 5, 7]) == True
    assert candidate([6, 4, 5, 3, 6], [5, 2, 9, 11, 13]) == True
    assert candidate([5, 7, 7, 2, 1], [1, 8, 12, 6, 9]) == True
    assert candidate([2, 2, 8, 6, 8], [2, 1, 5, 6, 5]) == True
    assert candidate([5, 6, 6, 9, 10], [9, 8, 11, 4, 10]) == True
    assert candidate([3, 4, 3, 5, 8], [4, 7, 7, 5, 12]) == True
    assert candidate([4, 2, 3, 9, 3], [5, 7, 4, 3, 12]) == True
    assert candidate([5, 7, 8, 2, 7], [8, 11, 8, 3, 13]) == True
    assert candidate([5, 7, 6, 5, 3], [2, 1, 4, 12, 12]) == None
    assert candidate([2, 2, 3, 3, 1], [7, 9, 8, 4, 7]) == None
    assert candidate([1, 7, 7, 5, 8], [7, 1, 5, 3, 10]) == True
    assert candidate([4, 4, 8, 2, 4], [8, 3, 4, 10, 5]) == True
    assert candidate([5, 7, 6, 6, 3], [8, 9, 3, 5, 13]) == True
    assert candidate([4, 3, 6, 9, 1], [2, 9, 6, 5, 5]) == True
    assert candidate([6, 2, 3, 8, 5], [9, 2, 3, 6, 6]) == True
    assert candidate([5, 1, 8, 1, 5], [11, 12, 5, 4]) == True
    assert candidate([3, 2, 4, 6, 6], [5, 5, 5, 5]) == None
    assert candidate([4, 7, 1, 7, 6], [11, 12, 4, 7]) == True
    assert candidate([6, 6, 8, 4, 1], [5, 4, 3, 5]) == True
    assert candidate([1, 7, 6, 8, 4], [10, 6, 9, 11]) == True
    assert candidate([1, 1, 7, 2, 8], [5, 10, 13, 7]) == True
    assert candidate([6, 5, 4, 8, 8], [4, 3, 11, 6]) == True
    assert candidate([2, 2, 3, 1, 5], [9, 3, 3, 8]) == True
    assert candidate([4, 7, 2, 6, 3], [2, 6, 6, 4]) == True
    assert candidate([3, 3, 4, 7, 7], [7, 9, 6, 11]) == True
    assert candidate([6, 4, 2, 7, 2], [3, 8, 6, 4]) == True
    assert candidate([2, 3, 6, 3, 8], [9, 12, 7, 7]) == None
    assert candidate([5, 5, 4, 6, 8], [6, 4, 6, 4]) == True
    assert candidate([3, 6, 1, 2, 2], [10, 10, 4, 7]) == None
    assert candidate([5, 2, 4, 8, 8], [4, 2, 10, 10]) == True
    assert candidate([3, 1, 6, 1, 6], [2, 6, 12, 4]) == True
    assert candidate([5, 6, 2, 8, 10], [9, 10, 6, 7]) == True
    assert candidate([1, 2, 4, 7, 8], [11, 3, 6, 9]) == None
    assert candidate([4, 1, 4, 6, 2], [2, 10, 12, 6]) == True
    assert candidate([1, 6, 3, 3, 7], [2, 7, 12, 6]) == True
    assert candidate([4, 4, 6, 6, 8], [7, 3, 9, 7]) == None
    assert candidate([2, 6, 7, 1, 1], [5, 9, 5, 11]) == None
    assert candidate([5, 7, 1, 2, 2], [8, 9, 3, 8]) == None
    assert candidate([3, 4, 7, 2, 9], [8, 7, 10, 10]) == True
    assert candidate([4, 7, 2, 8, 1], [5, 7, 6, 10]) == True
    assert candidate([4, 3, 4, 1, 9], [3, 11, 4, 14]) == True
    assert candidate([3, 5, 3, 5, 1], [4, 10, 4, 5]) == True
    assert candidate([4, 4, 3, 8, 2], [8, 2, 11, 11]) == True
    assert candidate([1, 1, 5, 1, 8], [5, 12, 10, 13]) == True
    assert candidate([5, 3, 2, 8, 7], [3, 5, 5, 10]) == True
    assert candidate([3, 6, 5, 6, 8], [9, 3, 4, 12]) == True
    assert candidate([6, 2, 2, 4, 8], [10, 8, 11, 10]) == True
    assert candidate([3, 6, 8, 7, 10], [2, 3, 11, 7]) == True
    assert candidate(['g', 't', 'w'], ['a', 'l', 'j']) == None
    assert candidate(['f', 'k', 'a'], ['j', 'b', 'y']) == None
    assert candidate(['a', 'o', 's'], ['o', 'c', 'm']) == True
    assert candidate(['a', 'a', 'w'], ['z', 'l', 'x']) == None
    assert candidate(['o', 'b', 'g'], ['b', 's', 'p']) == True
    assert candidate(['r', 'f', 'l'], ['z', 'd', 'l']) == True
    assert candidate(['n', 'w', 'l'], ['l', 'h', 'e']) == True
    assert candidate(['i', 'm', 'o'], ['p', 'a', 'h']) == None
    assert candidate(['n', 'r', 'n'], ['g', 'q', 'g']) == None
    assert candidate(['m', 'i', 't'], ['e', 't', 'x']) == True
    assert candidate(['r', 's', 'g'], ['v', 'v', 'w']) == None
    assert candidate(['p', 'x', 's'], ['g', 'y', 'f']) == None
    assert candidate(['i', 'j', 's'], ['h', 'u', 'g']) == None
    assert candidate(['f', 'w', 'z'], ['i', 'o', 'f']) == True
    assert candidate(['r', 'g', 's'], ['p', 'v', 'f']) == None
    assert candidate(['p', 'x', 'p'], ['r', 'q', 's']) == None
    assert candidate(['b', 'e', 'm'], ['v', 'w', 'b']) == True
    assert candidate(['w', 'z', 'd'], ['q', 'h', 'i']) == None
    assert candidate(['j', 'e', 'u'], ['m', 'g', 'b']) == None
    assert candidate(['h', 'w', 'y'], ['a', 't', 'x']) == None
    assert candidate(['o', 'c', 'b'], ['v', 'i', 'q']) == None
    assert candidate(['p', 'x', 'h'], ['u', 'k', 'z']) == None
    assert candidate(['s', 'u', 'p'], ['x', 'q', 'y']) == None
    assert candidate(['n', 'n', 'j'], ['q', 'n', 's']) == True
    assert candidate(['r', 't', 't'], ['i', 'z', 'k']) == None
    assert candidate(['s', 'h', 'k'], ['g', 'c', 'q']) == None
    assert candidate(['t', 'f', 'f'], ['d', 'l', 'e']) == None
    assert candidate(['k', 'm', 'w'], ['t', 'z', 'r']) == None
    assert candidate(['d', 'g', 'i'], ['s', 'n', 'e']) == None
    assert candidate(['c', 'k', 'g'], ['y', 't', 'm']) == None
    assert candidate(['w', 'd', 'p'], ['s', 'c', 'v']) == None
    assert candidate(['y', 'c', 'v'], ['w', 'o', 'l']) == None
    assert candidate(['q', 'y', 'a'], ['x', 's', 's']) == None

if __name__ == '__main__':
    check(common_element)