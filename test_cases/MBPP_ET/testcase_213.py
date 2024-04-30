from case_MBPP_213 import count_element_in_list


def check(candidate):
    assert candidate([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
    assert candidate([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'A')==3
    assert candidate([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'E')==1
    assert candidate([[6, 8], [4, 2], [5, 10], [3, 17, 5]], 3) == 1
    assert candidate([[2, 1], [1, 4], [4, 11], [2, 14, 12]], 6) == 0
    assert candidate([[3, 6], [7, 4], [5, 15], [4, 18, 4]], 3) == 1
    assert candidate([[2, 6], [9, 2], [6, 11], [1, 19, 6]], 1) == 1
    assert candidate([[1, 4], [4, 3], [1, 16], [6, 15, 9]], 6) == 1
    assert candidate([[4, 2], [7, 7], [1, 7], [6, 18, 5]], 1) == 1
    assert candidate([[2, 3], [9, 10], [2, 6], [3, 12, 12]], 4) == 0
    assert candidate([[4, 4], [4, 11], [4, 14], [6, 19, 4]], 3) == 0
    assert candidate([[3, 6], [4, 2], [4, 13], [4, 13, 12]], 2) == 1
    assert candidate([[5, 1], [2, 8], [2, 10], [5, 12, 6]], 3) == 0
    assert candidate([[1, 7], [2, 10], [6, 13], [2, 16, 8]], 4) == 0
    assert candidate([[5, 4], [1, 12], [3, 16], [3, 18, 6]], 2) == 0
    assert candidate([[5, 4], [5, 8], [1, 14], [3, 20, 10]], 3) == 1
    assert candidate([[3, 4], [5, 7], [1, 14], [5, 20, 11]], 5) == 2
    assert candidate([[3, 6], [6, 2], [6, 15], [1, 11, 3]], 4) == 0
    assert candidate([[2, 7], [3, 7], [1, 16], [3, 10, 3]], 6) == 0
    assert candidate([[1, 5], [4, 11], [4, 12], [5, 16, 6]], 1) == 1
    assert candidate([[6, 5], [4, 7], [3, 12], [2, 10, 3]], 6) == 1
    assert candidate([[2, 3], [5, 11], [6, 13], [6, 13, 12]], 4) == 0
    assert candidate([[6, 6], [3, 3], [2, 13], [5, 16, 8]], 5) == 1
    assert candidate([[1, 6], [7, 12], [5, 16], [5, 14, 4]], 1) == 1
    assert candidate([[6, 8], [9, 6], [1, 9], [2, 10, 2]], 4) == 0
    assert candidate([[5, 2], [7, 2], [5, 15], [4, 10, 7]], 4) == 1
    assert candidate([[4, 1], [6, 5], [4, 15], [1, 20, 2]], 5) == 1
    assert candidate([[1, 1], [7, 7], [4, 7], [2, 15, 6]], 5) == 0
    assert candidate([[3, 8], [10, 6], [3, 15], [2, 19, 6]], 6) == 2
    assert candidate([[5, 5], [3, 11], [3, 15], [3, 10, 8]], 5) == 1
    assert candidate([[5, 3], [9, 6], [6, 9], [1, 16, 2]], 3) == 1
    assert candidate([[4, 8], [6, 12], [4, 12], [6, 16, 2]], 2) == 1
    assert candidate([[3, 1], [2, 10], [1, 11], [4, 15, 9]], 6) == 0
    assert candidate([[4, 1], [4, 7], [1, 6], [4, 20, 4]], 6) == 1
    assert candidate([[2, 2], [5, 2], [4, 13], [6, 15, 6]], 5) == 1
    assert candidate([[1, 5], [6, 3], [4, 6], [4, 17, 12]], 6) == 2
    assert candidate([['S', 'M'], ['Z', 'Y'], ['M', 'W', 'U'], ['V', 'Y', 'W']], 'R') == 0
    assert candidate([['P', 'I'], ['I', 'F'], ['E', 'O', 'X'], ['D', 'B', 'T']], 'E') == 1
    assert candidate([['Y', 'F'], ['A', 'L'], ['Y', 'T', 'V'], ['U', 'D', 'C']], 'Z') == 0
    assert candidate([['J', 'Z'], ['L', 'H'], ['D', 'Q', 'I'], ['X', 'P', 'O']], 'X') == 1
    assert candidate([['D', 'O'], ['F', 'S'], ['V', 'F', 'U'], ['S', 'H', 'U']], 'J') == 0
    assert candidate([['S', 'M'], ['X', 'X'], ['E', 'P', 'Q'], ['P', 'K', 'W']], 'G') == 0
    assert candidate([['M', 'A'], ['F', 'V'], ['Y', 'F', 'E'], ['B', 'A', 'H']], 'G') == 0
    assert candidate([['R', 'S'], ['C', 'Z'], ['X', 'J', 'V'], ['V', 'H', 'N']], 'C') == 1
    assert candidate([['S', 'J'], ['Y', 'Y'], ['D', 'D', 'M'], ['M', 'P', 'R']], 'V') == 0
    assert candidate([['C', 'T'], ['U', 'J'], ['E', 'Z', 'S'], ['D', 'E', 'K']], 'X') == 0
    assert candidate([['J', 'G'], ['L', 'G'], ['F', 'U', 'C'], ['H', 'I', 'Z']], 'E') == 0
    assert candidate([['A', 'B'], ['K', 'H'], ['Z', 'A', 'P'], ['A', 'U', 'L']], 'L') == 1
    assert candidate([['R', 'X'], ['K', 'D'], ['I', 'W', 'R'], ['Z', 'X', 'W']], 'K') == 1
    assert candidate([['N', 'N'], ['J', 'Q'], ['N', 'K', 'T'], ['H', 'G', 'L']], 'R') == 0
    assert candidate([['Z', 'L'], ['H', 'C'], ['J', 'T', 'S'], ['N', 'Z', 'N']], 'E') == 0
    assert candidate([['F', 'Z'], ['B', 'E'], ['E', 'A', 'Y'], ['H', 'L', 'K']], 'M') == 0
    assert candidate([['G', 'L'], ['C', 'O'], ['Y', 'M', 'K'], ['V', 'C', 'Y']], 'H') == 0
    assert candidate([['U', 'X'], ['D', 'W'], ['P', 'G', 'M'], ['F', 'P', 'W']], 'P') == 2
    assert candidate([['Y', 'Y'], ['A', 'S'], ['K', 'T', 'S'], ['Y', 'B', 'N']], 'H') == 0
    assert candidate([['Q', 'Q'], ['G', 'U'], ['W', 'G', 'B'], ['C', 'E', 'K']], 'W') == 1
    assert candidate([['G', 'A'], ['R', 'I'], ['C', 'I', 'F'], ['Q', 'G', 'Q']], 'S') == 0
    assert candidate([['V', 'Z'], ['F', 'G'], ['O', 'T', 'Z'], ['P', 'E', 'D']], 'S') == 0
    assert candidate([['V', 'T'], ['C', 'C'], ['N', 'Z', 'T'], ['U', 'Z', 'X']], 'R') == 0
    assert candidate([['X', 'L'], ['D', 'D'], ['L', 'G', 'X'], ['T', 'S', 'P']], 'N') == 0
    assert candidate([['L', 'G'], ['N', 'U'], ['C', 'E', 'R'], ['N', 'B', 'O']], 'U') == 1
    assert candidate([['N', 'S'], ['P', 'G'], ['X', 'Z', 'O'], ['J', 'T', 'U']], 'L') == 0
    assert candidate([['X', 'K'], ['M', 'M'], ['H', 'I', 'F'], ['A', 'Q', 'L']], 'J') == 0
    assert candidate([['T', 'Q'], ['I', 'E'], ['Z', 'X', 'W'], ['J', 'X', 'S']], 'R') == 0
    assert candidate([['M', 'O'], ['W', 'N'], ['U', 'V', 'D'], ['E', 'H', 'A']], 'Y') == 0
    assert candidate([['X', 'O'], ['N', 'K'], ['Y', 'G', 'C'], ['D', 'Z', 'N']], 'R') == 0
    assert candidate([['C', 'I'], ['J', 'C'], ['J', 'I', 'K'], ['D', 'F', 'L']], 'B') == 0
    assert candidate([['T', 'P'], ['W', 'R'], ['P', 'E', 'K'], ['G', 'G', 'S']], 'P') == 2
    assert candidate([['R', 'B'], ['E', 'J'], ['A', 'U', 'H'], ['M', 'B', 'D']], 'M') == 1
    assert candidate([['S', 'M'], ['N', 'S'], ['Z', 'D', 'E'], ['E', 'C', 'C']], 'V') == 0
    assert candidate([['I', 'Q'], ['D', 'B'], ['C', 'C', 'F'], ['D', 'W', 'G']], 'F') == 1
    assert candidate([['P', 'S'], ['J', 'T'], ['Q', 'B', 'I'], ['L', 'R', 'K']], 'T') == 1
    assert candidate([['C', 'C'], ['V', 'E'], ['C', 'V', 'A'], ['Y', 'A', 'A']], 'K') == 0
    assert candidate([['V', 'N'], ['Z', 'R'], ['S', 'Y', 'D'], ['Q', 'H', 'Y']], 'P') == 0
    assert candidate([['P', 'B'], ['G', 'I'], ['E', 'L', 'U'], ['X', 'H', 'X']], 'K') == 0
    assert candidate([['K', 'L'], ['H', 'Y'], ['U', 'T', 'R'], ['H', 'S', 'H']], 'Z') == 0
    assert candidate([['P', 'G'], ['H', 'X'], ['N', 'Z', 'J'], ['P', 'V', 'R']], 'A') == 0
    assert candidate([['E', 'Q'], ['R', 'V'], ['T', 'F', 'F'], ['M', 'P', 'L']], 'D') == 0
    assert candidate([['X', 'R'], ['P', 'Q'], ['N', 'Q', 'C'], ['L', 'J', 'O']], 'T') == 0
    assert candidate([['B', 'I'], ['O', 'N'], ['R', 'U', 'I'], ['U', 'Z', 'Z']], 'Y') == 0
    assert candidate([['C', 'Z'], ['Z', 'V'], ['Y', 'L', 'E'], ['O', 'E', 'S']], 'C') == 1
    assert candidate([['S', 'T'], ['P', 'H'], ['P', 'U', 'B'], ['L', 'E', 'Z']], 'T') == 1
    assert candidate([['Z', 'Q'], ['R', 'I'], ['T', 'L', 'X'], ['B', 'W', 'N']], 'A') == 0
    assert candidate([['P', 'R'], ['H', 'B'], ['K', 'X', 'J'], ['W', 'Z', 'U']], 'U') == 1
    assert candidate([['P', 'J'], ['G', 'Q'], ['T', 'P', 'Q'], ['N', 'E', 'Z']], 'T') == 1
    assert candidate([['Y', 'O'], ['J', 'I'], ['D', 'W', 'Z'], ['Z', 'Y', 'H']], 'L') == 0
    assert candidate([['O', 'W'], ['Q', 'V'], ['C', 'Z', 'V'], ['V', 'V', 'V']], 'J') == 0
    assert candidate([['K', 'D'], ['W', 'O'], ['V', 'R', 'M'], ['P', 'Q', 'H']], 'K') == 1
    assert candidate([['C', 'E'], ['D', 'K'], ['W', 'I', 'Y'], ['W', 'L', 'D']], 'C') == 1
    assert candidate([['T', 'P'], ['F', 'O'], ['A', 'D', 'Z'], ['H', 'W', 'X']], 'O') == 1
    assert candidate([['Q', 'A'], ['J', 'O'], ['P', 'Y', 'P'], ['H', 'Z', 'N']], 'U') == 0
    assert candidate([['F', 'Q'], ['S', 'L'], ['P', 'L', 'Z'], ['F', 'Y', 'P']], 'Z') == 1
    assert candidate([['A', 'D'], ['D', 'C'], ['H', 'D', 'H'], ['B', 'T', 'E']], 'Y') == 0
    assert candidate([['M', 'W'], ['M', 'S'], ['L', 'O', 'C'], ['X', 'X', 'M']], 'E') == 0
    assert candidate([['Q', 'A'], ['H', 'C'], ['X', 'V', 'J'], ['M', 'J', 'B']], 'P') == 0
    assert candidate([['M', 'A'], ['F', 'T'], ['C', 'E', 'G'], ['P', 'O', 'C']], 'C') == 2
    assert candidate([['F', 'F'], ['O', 'I'], ['S', 'F', 'M'], ['Y', 'R', 'F']], 'D') == 0
    assert candidate([['O', 'U'], ['K', 'R'], ['Z', 'O', 'A'], ['A', 'M', 'O']], 'H') == 0
    assert candidate([['Q', 'R'], ['U', 'N'], ['V', 'N', 'E'], ['L', 'Y', 'A']], 'S') == 0
    assert candidate([['Z', 'K'], ['M', 'T'], ['T', 'G', 'X'], ['Y', 'L', 'N']], 'Z') == 1
    assert candidate([['A', 'P'], ['J', 'P'], ['P', 'D', 'O'], ['K', 'C', 'R']], 'Q') == 0
    assert candidate([['Y', 'Y'], ['Z', 'P'], ['T', 'C', 'C'], ['Z', 'G', 'A']], 'T') == 1

if __name__ == '__main__':
    check(count_element_in_list)