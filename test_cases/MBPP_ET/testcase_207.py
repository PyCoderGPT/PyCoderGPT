from case_MBPP_207 import Find_Max


def check(candidate):
    assert candidate([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
    assert candidate([[1],[1,2],[1,2,3]]) == [1,2,3]
    assert candidate([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]
    assert candidate([['Q'], ['W', 'S'], ['A', 'N', 'N']]) == ['W', 'S']
    assert candidate([['T'], ['C', 'Z'], ['N', 'N', 'I']]) == ['T']
    assert candidate([['F'], ['G', 'C'], ['F', 'R', 'N']]) == ['G', 'C']
    assert candidate([['J'], ['I', 'H'], ['K', 'L', 'H']]) == ['K', 'L', 'H']
    assert candidate([['F'], ['U', 'X'], ['J', 'H', 'B']]) == ['U', 'X']
    assert candidate([['K'], ['D', 'A'], ['X', 'W', 'P']]) == ['X', 'W', 'P']
    assert candidate([['J'], ['T', 'L'], ['C', 'W', 'U']]) == ['T', 'L']
    assert candidate([['Y'], ['M', 'Y'], ['O', 'Y', 'R']]) == ['Y']
    assert candidate([['E'], ['S', 'X'], ['E', 'G', 'O']]) == ['S', 'X']
    assert candidate([['H'], ['S', 'I'], ['T', 'U', 'P']]) == ['T', 'U', 'P']
    assert candidate([['F'], ['J', 'N'], ['K', 'P', 'F']]) == ['K', 'P', 'F']
    assert candidate([['A'], ['A', 'S'], ['J', 'E', 'M']]) == ['J', 'E', 'M']
    assert candidate([['A'], ['L', 'X'], ['Y', 'G', 'C']]) == ['Y', 'G', 'C']
    assert candidate([['J'], ['X', 'R'], ['B', 'M', 'L']]) == ['X', 'R']
    assert candidate([['X'], ['W', 'Q'], ['L', 'C', 'N']]) == ['X']
    assert candidate([['A'], ['R', 'D'], ['T', 'E', 'S']]) == ['T', 'E', 'S']
    assert candidate([['B'], ['B', 'G'], ['R', 'C', 'N']]) == ['R', 'C', 'N']
    assert candidate([['V'], ['D', 'N'], ['C', 'L', 'B']]) == ['V']
    assert candidate([['K'], ['M', 'E'], ['Q', 'K', 'X']]) == ['Q', 'K', 'X']
    assert candidate([['M'], ['C', 'T'], ['T', 'C', 'H']]) == ['T', 'C', 'H']
    assert candidate([['W'], ['U', 'P'], ['D', 'I', 'J']]) == ['W']
    assert candidate([['T'], ['N', 'N'], ['E', 'K', 'R']]) == ['T']
    assert candidate([['C'], ['H', 'X'], ['U', 'O', 'N']]) == ['U', 'O', 'N']
    assert candidate([['G'], ['H', 'P'], ['U', 'Z', 'C']]) == ['U', 'Z', 'C']
    assert candidate([['Z'], ['B', 'S'], ['R', 'Y', 'Y']]) == ['Z']
    assert candidate([['L'], ['T', 'Z'], ['L', 'X', 'M']]) == ['T', 'Z']
    assert candidate([['S'], ['D', 'Y'], ['Y', 'O', 'I']]) == ['Y', 'O', 'I']
    assert candidate([['G'], ['E', 'H'], ['L', 'X', 'K']]) == ['L', 'X', 'K']
    assert candidate([['L'], ['L', 'O'], ['L', 'K', 'B']]) == ['L', 'O']
    assert candidate([['B'], ['G', 'O'], ['D', 'F', 'G']]) == ['G', 'O']
    assert candidate([['O'], ['L', 'N'], ['W', 'B', 'Q']]) == ['W', 'B', 'Q']
    assert candidate([['X'], ['I', 'T'], ['L', 'T', 'B']]) == ['X']
    assert candidate([['R'], ['X', 'B'], ['Y', 'J', 'I']]) == ['Y', 'J', 'I']
    assert candidate([[5], [1, 5], [4, 7, 7]]) == [5]
    assert candidate([[2], [5, 7], [6, 2, 8]]) == [6, 2, 8]
    assert candidate([[2], [6, 4], [4, 3, 8]]) == [6, 4]
    assert candidate([[5], [4, 6], [1, 6, 8]]) == [5]
    assert candidate([[5], [3, 6], [5, 5, 8]]) == [5, 5, 8]
    assert candidate([[4], [4, 5], [3, 2, 2]]) == [4, 5]
    assert candidate([[1], [1, 1], [1, 5, 2]]) == [1, 5, 2]
    assert candidate([[1], [1, 7], [2, 5, 7]]) == [2, 5, 7]
    assert candidate([[4], [1, 4], [5, 3, 3]]) == [5, 3, 3]
    assert candidate([[2], [3, 2], [2, 2, 7]]) == [3, 2]
    assert candidate([[5], [3, 5], [5, 5, 7]]) == [5, 5, 7]
    assert candidate([[6], [1, 1], [2, 6, 8]]) == [6]
    assert candidate([[3], [3, 1], [1, 3, 1]]) == [3, 1]
    assert candidate([[2], [6, 5], [4, 6, 5]]) == [6, 5]
    assert candidate([[5], [3, 6], [4, 6, 6]]) == [5]
    assert candidate([[1], [6, 6], [6, 3, 3]]) == [6, 6]
    assert candidate([[5], [6, 1], [3, 3, 6]]) == [6, 1]
    assert candidate([[2], [2, 7], [2, 3, 6]]) == [2, 7]
    assert candidate([[3], [2, 2], [5, 4, 3]]) == [5, 4, 3]
    assert candidate([[4], [2, 6], [3, 6, 7]]) == [4]
    assert candidate([[1], [4, 5], [2, 5, 1]]) == [4, 5]
    assert candidate([[6], [5, 7], [4, 4, 8]]) == [6]
    assert candidate([[5], [3, 7], [1, 5, 8]]) == [5]
    assert candidate([[2], [6, 3], [6, 1, 1]]) == [6, 3]
    assert candidate([[6], [2, 4], [2, 5, 2]]) == [6]
    assert candidate([[2], [6, 4], [2, 7, 3]]) == [6, 4]
    assert candidate([[2], [3, 6], [5, 6, 4]]) == [5, 6, 4]
    assert candidate([[1], [2, 4], [5, 1, 1]]) == [5, 1, 1]
    assert candidate([[6], [4, 6], [3, 6, 1]]) == [6]
    assert candidate([[2], [1, 6], [1, 6, 7]]) == [2]
    assert candidate([[4], [3, 3], [5, 4, 2]]) == [5, 4, 2]
    assert candidate([[1], [5, 2], [5, 1, 6]]) == [5, 2]
    assert candidate([[6], [3, 2], [2, 1, 1]]) == [6]
    assert candidate([[4, 5], [5, 4, 4], [2, 4, 7, 2]]) == [5, 4, 4]
    assert candidate([[1, 2], [1, 1, 5], [1, 8, 7, 1]]) == [1, 8, 7, 1]
    assert candidate([[2, 6], [3, 6, 8], [3, 2, 1, 3]]) == [3, 6, 8]
    assert candidate([[4, 6], [4, 2, 7], [1, 4, 6, 1]]) == [4, 6]
    assert candidate([[1, 6], [5, 4, 1], [4, 6, 8, 3]]) == [5, 4, 1]
    assert candidate([[1, 3], [6, 2, 5], [6, 3, 3, 4]]) == [6, 3, 3, 4]
    assert candidate([[6, 4], [2, 5, 6], [2, 4, 1, 2]]) == [6, 4]
    assert candidate([[3, 5], [3, 7, 4], [2, 6, 1, 5]]) == [3, 7, 4]
    assert candidate([[2, 2], [2, 1, 4], [6, 2, 8, 4]]) == [6, 2, 8, 4]
    assert candidate([[6, 4], [6, 1, 5], [2, 10, 8, 2]]) == [6, 4]
    assert candidate([[6, 2], [2, 7, 7], [3, 7, 11, 5]]) == [6, 2]
    assert candidate([[5, 6], [2, 7, 3], [4, 4, 8, 2]]) == [5, 6]
    assert candidate([[5, 3], [2, 3, 5], [2, 1, 9, 3]]) == [5, 3]
    assert candidate([[3, 4], [4, 1, 3], [5, 1, 9, 6]]) == [5, 1, 9, 6]
    assert candidate([[5, 6], [4, 6, 3], [4, 1, 4, 2]]) == [5, 6]
    assert candidate([[5, 5], [4, 7, 7], [5, 6, 1, 4]]) == [5, 6, 1, 4]
    assert candidate([[2, 6], [6, 4, 5], [3, 5, 10, 3]]) == [6, 4, 5]
    assert candidate([[2, 4], [1, 5, 2], [6, 2, 7, 3]]) == [6, 2, 7, 3]
    assert candidate([[3, 4], [1, 3, 2], [4, 9, 1, 3]]) == [4, 9, 1, 3]
    assert candidate([[4, 4], [2, 3, 3], [4, 6, 8, 5]]) == [4, 6, 8, 5]
    assert candidate([[2, 2], [5, 5, 2], [2, 7, 3, 2]]) == [5, 5, 2]
    assert candidate([[6, 1], [5, 4, 3], [6, 10, 1, 6]]) == [6, 10, 1, 6]
    assert candidate([[5, 4], [1, 6, 3], [6, 1, 11, 5]]) == [6, 1, 11, 5]
    assert candidate([[1, 6], [1, 6, 7], [2, 7, 3, 5]]) == [2, 7, 3, 5]
    assert candidate([[6, 3], [1, 7, 5], [3, 9, 11, 1]]) == [6, 3]
    assert candidate([[2, 2], [1, 6, 1], [1, 2, 7, 1]]) == [2, 2]
    assert candidate([[3, 5], [5, 6, 2], [3, 6, 4, 3]]) == [5, 6, 2]
    assert candidate([[6, 3], [4, 4, 7], [6, 8, 9, 2]]) == [6, 8, 9, 2]
    assert candidate([[6, 4], [1, 1, 5], [1, 5, 2, 3]]) == [6, 4]
    assert candidate([[1, 4], [5, 5, 5], [3, 4, 4, 2]]) == [5, 5, 5]
    assert candidate([[5, 2], [6, 6, 5], [5, 1, 11, 4]]) == [6, 6, 5]
    assert candidate([[1, 4], [5, 3, 2], [1, 4, 4, 2]]) == [5, 3, 2]
    assert candidate([[1, 6], [4, 3, 5], [5, 7, 4, 2]]) == [5, 7, 4, 2]

if __name__ == '__main__':
    check(Find_Max)